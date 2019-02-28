# -*- coding: utf-8 -*-
import random

from hashcode19.helpers import Input, Output, Slide


def main(i: Input) -> Output:
    """Pick every picture at random, make a slide, and make a sequence."""
    random.shuffle(i.pictures)
    return Output([Slide([p for p in i.pictures])])
