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
        assert len(pictures) == 1 and pictures[0].type_ == PictureType.H\
               or len(pictures) == 2 and pictures[0].type_ == PictureType.V and pictures[1].type_ == PictureType.V
        self.pictures = pictures

    def is_horiziontal(self) -> bool:
        return len(self.pictures) == 1

    @property
    def tags(self):
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

    def __init__(self, N: int, slides: List[Slide]):
        self.N = N
        self.slides = slides
        assert len(slides) == N

    def to_stdout(self) -> None:
        print(self.N)
        for s in self.slides:
            if len(s.pictures) == 1:
                print("{}".format(s.pictures[0].id_))
            else:
                print("{} {}".format(s.pictures[0].id_, s.pictures[1].id_))


def score_transition(s1: Slide, s2: Slide) -> int:
    common = s1.pictures
    return 0


def score(output: Output) -> int:
    # for s in output.slides

    return 0
