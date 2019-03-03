# -*- coding: utf-8 -*-

import logging

from hashcode19.helpers import Input, Output

logger = logging.getLogger(__name__)


# def build_graph(inp: Input) -> Dict[int, Set[int]]:
#     logger.debug("Build graph...")
#     graph = defaultdict(lambda: [])  # type: Dict[int, Set[int]]
#
#     ids = list(inp.id_to_pic.keys())
#     for i in range(len(ids)):
#         if i % 1000 == 0:
#             logger.debug(i)
#         ip1 = i
#         p1 = inp.id_to_pic[ip1]
#         graph[p1] = set.union(*map(lambda tag: inp.tag_to_pics[tag], p1.tags))
#
#     logger.debug("Graph built. Done!")
#     return graph

def main(i: Input) -> Output:
    """Model the problem as a TSP. Do not compute the graph explicitly (too large), or try to approximate it."""
    slideshow = []

    return Output(slideshow)
