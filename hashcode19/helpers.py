# -*- coding: utf-8 -*-
import sys
from collections import defaultdict

import logging
from enum import Enum
from typing import List, Set

logger = logging.getLogger(__name__)


class PictureType(Enum):
    H = "H"
    V = "V"


class Picture(object):

    def __init__(self, id_: int, type_: PictureType, tags: Set[str]):
        self.id_ = id_
        self.type_ = type_
        self.tags = tags

    def __hash__(self):
        return self.id_

    @property
    def type(self) -> PictureType:
        return self.type_


class Slide(object):

    def __init__(self, pictures: List[Picture]):
        assert len(pictures) == 1 and pictures[0].type_ == PictureType.H or \
               (len(pictures) == 2 and pictures[0].type_ == PictureType.V and pictures[1].type_ == PictureType.V)
        self.pictures = pictures

    def is_horiziontal(self) -> bool:
        return len(self.pictures) == 1

    @property
    def tags(self) -> Set[str]:
        return set(t for p in self.pictures for t in p.tags)


class Input(object):

    def __init__(self, N, pictures: List[Picture]):
        self.N = N
        self.pictures = pictures
        self._build_indexes()

    def _build_indexes(self):
        self._id_to_pic = dict(enumerate(self.pictures))
        self.type_to_pics = {PictureType.H: [], PictureType.V: []}
        self.numtag_to_pics = defaultdict(lambda: [])
        for i, p in enumerate(self.pictures):
            self.type_to_pics[p.type_].append(p)
            self.numtag_to_pics[len(p.tags)].append(p)

    @classmethod
    def read(cls, filename=None):
        """Returns an Input instance. If filename is None, read from stdin."""
        if filename is None:
            lines = sys.stdin
        else:
            lines = iter(open(filename).readlines())

        line = next(lines)
        N = int(line.strip())

        pictures = []
        for id_ in range(N):
            tokens = next(lines).strip().split(" ")

            picture_type = PictureType(tokens[0])
            tags = set(tokens[2:])

            picture = Picture(id_, picture_type, tags)
            pictures.append(picture)

        assert len(pictures) == N
        logger.debug("Parsed input: {} pictures.".format(N))
        return Input(N, pictures)


class Output(object):

    def __init__(self, slides: List[Slide]):
        self.slides = slides

    def write(self, filename=None) -> None:
        if filename is not None:
            file = open(filename, "w")
        else:
            file = None
        logger.debug("Printing to {}...".format("stdout" if file is None else filename))
        print(len(self.slides), file=file)
        for s in self.slides:
            if len(s.pictures) == 1:
                print("{}".format(s.pictures[0].id_), file=file)
            else:
                print("{} {}".format(s.pictures[0].id_, s.pictures[1].id_), file=file)

    @classmethod
    def read(cls, in_file=None, solution_file=None):
        i = Input.read(in_file)

        if solution_file is None:
            lines = sys.stdin
        else:
            lines = iter(open(solution_file).readlines())

        line = next(lines)
        N = int(line.strip())

        slideshow = []
        for id_ in range(N):
            tokens = map(int, next(lines).strip().split(" "))
            pictures = [i._id_to_pic[idx] for idx in tokens]
            slideshow.append(Slide(pictures))

        return Output(slideshow)


def score_tag_transition(tags1: Set[str], tags2: Set[str]):
    common = len(tags1.intersection(tags2))
    s1_minus_s2 = len(tags1.difference(tags2))
    s2_minus_s1 = len(tags2.difference(tags1))
    return min(common, s1_minus_s2, s2_minus_s1)


def score_transition(s1: Slide, s2: Slide) -> int:
    return score_tag_transition(s1.tags, s2.tags)


def score(output: Output) -> int:
    result = 0
    for i in range(len(output.slides) - 1):
        s1 = output.slides[i]
        s2 = output.slides[i+1]
        result += score_transition(s1, s2)

    return result
