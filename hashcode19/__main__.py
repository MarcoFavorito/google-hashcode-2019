#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import inspect
import logging
import os
import importlib
import re

from hashcode19.helpers import Input, Output

logger = logging.getLogger(__name__)

PACKAGE_DIRECTORY = os.path.dirname(inspect.getfile(inspect.currentframe()))
ALGORITHMS = [s.replace(".py", "") for s in os.listdir(PACKAGE_DIRECTORY + "/sol") if re.match("[^_].+.py", s)]

parser = argparse.ArgumentParser("hashcode19", description="CLI util for Google Hash Code 2019. "
                                                           "It assumes the input provided in stdin.")

parser.add_argument("--alg", required=True, choices=ALGORITHMS, help="The algorithm to use for computing the solution.")

args = parser.parse_args()
solution = importlib.import_module('hashcode19.sol.{}'.format(args.alg))


def main():
    logger.debug("Chosen algorithm: {}".format(args.alg))
    input_ = Input.parse_from_stdin()  # type: Input
    output = solution.main(input_)  # type: Output
    output.to_stdout()


if __name__ == '__main__':
    main()
