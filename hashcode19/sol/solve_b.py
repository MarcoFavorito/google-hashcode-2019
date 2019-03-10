# -*- coding: utf-8 -*-
import itertools

import copy

import logging
import random

from hashcode19.helpers import Input, Output, PictureType, Slide, score_transition, score_tag_transition, Picture

logger = logging.getLogger(__name__)


def main(inp: Input) -> Output:
    """Optimized solution for Problem B.
    Many assumptions:
    - only horizontal pictures
    - only a small number of tag occurrence (for dataset B it was 2, that is at most a tag appear twice).
    """
    slideshow = []

    used_pics = set()
    free_pics = set(inp.id_to_pic)

    cur_pic = random.sample(inp.pictures, 1)[0]
    cur_slide = Slide([cur_pic])
    best_slide = None
    used_pics.add(cur_pic.id_)
    free_pics.remove(cur_pic.id_)
    slideshow.append(cur_slide)

    while len(used_pics) < len(inp.pictures):
        choose_randomly = True
        best_max = -1
        for p_id in itertools.chain(*[inp.tag_to_pics[t] for t in cur_slide.tags]):
            if p_id in used_pics: continue
            cur_score = score_tag_transition(cur_slide.tags, inp.id_to_pic[p_id].tags)
            if cur_score > best_max:
                best_max = cur_score
                best_slide = Slide([inp.id_to_pic[p_id]])
                choose_randomly = False

        if choose_randomly:
            # no way to find the next best (every one else already used.)
            random_pic_id = random.sample(free_pics, 1)[0]
            random_pic = inp.id_to_pic[random_pic_id]  # type: Picture
            best_slide = Slide([random_pic])

        slideshow.append(best_slide)
        used_pics.add(best_slide.pictures[0].id_)
        free_pics.remove(best_slide.pictures[0].id_)
        cur_slide = best_slide

    return Output(slideshow)

