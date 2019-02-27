#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import inspect
import os

from hashcode19.helpers import Input

PACKAGE_DIRECTORY = os.path.dirname(inspect.getfile(inspect.currentframe()))
ALGORITHMS = [s.replace(".py", "") for s in os.listdir(PACKAGE_DIRECTORY + "/sol") if s != "__init__.py"]

parser = argparse.ArgumentParser("hashcode19", description="CLI util for Google Hash Code 2019. "
                                                           "It assumes the input provided in stdin.")

parser.add_argument("--alg", required=True, choices=ALGORITHMS, help="The algorithm to use for computing the solution.")


def main():
    parser.parse_args()

    input_ = Input.parse_from_stdin()


if __name__ == '__main__':
    main()
