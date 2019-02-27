# -*- coding: utf-8 -*-
import sys

import logging
import pprint
from typing import List, Tuple

logger = logging.getLogger(__name__)


class Input(object):

    def __init__(self, R, C, L, H, pizza: List[List[str]]):
        self.R = R
        self.C = C
        self.L = L
        self.H = H
        self.pizza = pizza

    @classmethod
    def parse_from_stdin(cls):
        """Returns an Input instance"""

        line = next(sys.stdin)
        R, C, L, H = map(int, line.strip().split(" "))

        pizza = [list(next(sys.stdin)) for r in range(R)]

        logger.debug("{}, {}, {}, {}".format(R, C, L, H))
        logger.debug("Pizza: {}".format(pprint.pformat(pizza)))

        return Input(R, C, L, H, pizza)


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

