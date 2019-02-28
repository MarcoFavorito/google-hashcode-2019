# -*- coding: utf-8 -*-
import sys

import logging
import pprint
from enum import Enum
from typing import List, Tuple, Set

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


class Slide(object):

    def __init__(self, pictures: List[Picture]):
        assert len(pictures) == 1 or len(pictures) == 2 and pictures[0].type_ == PictureType.V and pictures[1].type_ == PictureType.V
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

    @classmethod
    def parse_from_stdin(cls):
        """Returns an Input instance"""

        line = next(sys.stdin)
        N = int(line.strip())

        pictures = []
        for id_ in range(N):
            tokens = next(sys.stdin).strip().split(" ")

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

    def to_stdout(self) -> None:
        logger.debug("Printing to stdout...")
        print(len(self.slides))
        for s in self.slides:
            if len(s.pictures) == 1:
                print("{}".format(s.pictures[0].id_))
            else:
                print("{} {}".format(s.pictures[0].id_, s.pictures[1].id_))


def score_transition(s1: Slide, s2: Slide) -> int:
    common = len(s1.tags.intersection(s2.tags))
    s1_minus_s2 = len(s1.tags.difference(s2.tags))
    s2_minus_s1 = len(s2.tags.difference(s1.tags))
    return min(common, s1_minus_s2, s2_minus_s1)


def score(output: Output) -> int:
    result = 0
    for i in range(len(output.slides) - 1):
        s1 = output.slides[i]
        s2 = output.slides[i+1]
        result += score_transition(s1, s2)

    return result
