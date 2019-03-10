# -*- coding: utf-8 -*-
import itertools
from collections import defaultdict

import logging
from typing import Dict, Set

from hashcode19.helpers import Input, Output, score_tag_transition, Slide, PictureType

logger = logging.getLogger(__name__)


def build_graph(inp: Input) -> Dict[int, Set[int]]:
    logger.debug("Build graph...")
    graph = defaultdict(lambda: [])  # type: Dict[int, Set[int]]

    ids = list(inp.id_to_pic.keys())
    for i in range(len(ids)):
        if i % 1000 == 0:
            logger.debug(i)
        ip1 = i
        p1 = inp.id_to_pic[ip1]
        graph[p1] = set.union(*map(lambda tag: inp.tag_to_pics[tag], p1.tags))

    logger.debug("Graph built. Done!")
    return graph


def main(inp: Input) -> Output:
    """Model the problem as a TSP. Do not compute the graph explicitly (too large), or try to approximate it."""

    # TODO generalize by including vertical pictures.
    nodes = set(filter(lambda x: inp.id_to_pic[x].type_ == PictureType.H, inp.id_to_pic))

    # add a dummy node, "-1", that will be the start node. the distance between any node and the start node is 0.
    start = -1
    distance_function = lambda x, y: score_tag_transition(inp.id_to_pic[x].tags, inp.id_to_pic[y].tags) if x != start and y != start else 0

    C = {}

    for i in nodes:
        C[(i, frozenset())] = distance_function(i, start)

    logger.debug("N={}".format(len(nodes)))
    for k in range(1, len(nodes)):
        combs = list(itertools.combinations(nodes, k))
        logger.debug("k={} #combs={}".format(k, len(combs)))
        for c in combs:
            cur_set = frozenset(c)
            cur_nodes = nodes.difference(cur_set)
            for i in cur_nodes:
                C[(i, cur_set)] = min([distance_function(i, prev) + C[prev, frozenset(c).difference({prev})] for prev in c])

    # reconstruct the path
    previous_nodes = set(nodes)
    path = [(start, )]
    current_node = start
    while len(previous_nodes) != 0:
        current_node = min(previous_nodes,
                           key=lambda x: distance_function(current_node, x) + C[(x, frozenset(previous_nodes).difference({x}))])
        previous_nodes.remove(current_node)
        path.append((current_node, ))

    path.append((start, ))

    slideshow = [Slide([inp.id_to_pic[pic_id] for pic_id in pic_ids]) for pic_ids in path[1:-1]]

    return Output(slideshow)
