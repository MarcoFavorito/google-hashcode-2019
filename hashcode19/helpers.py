# -*- coding: utf-8 -*-


class Input(object):
    def __init__(self, **kwargs):
        pass

    @classmethod
    def parse_from_stdin(cls):
        """Returns an Input instance"""
        pass


class Output(object):

    @classmethod
    def to_stdout(cls) -> None:
        pass
