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

    def __init__(self, type_: PictureType, tags: Set[str]):
        self.type_ = type_
        self.tags = tags


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
        for _ in range(N):
            tokens = next(sys.stdin).strip().split(" ")

            picture_type = PictureType(tokens[0])
            tags = set(tokens[2:])

            picture = Picture(picture_type, tags)
            pictures.append(picture)

        assert len(pictures) == N
        return Input(N, pictures)


class Output(object):

    class Slice(object):

        def __init__(self, begin: Tuple[int, int], end: Tuple[int, int]):
            self.begin = begin
            self.end = end

    def __init__(self, N: int, slices: List[Slice]):
        self.N = N
        self.slices = slices
        assert len(slices) == N

    def to_stdout(self) -> None:
        print(self.N)
        for s in self.slices:
            print("{} {} {} {}".format(s.begin[0], s.begin[1], s.end[0], s.end[1]))

