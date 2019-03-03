# -*- coding: utf-8 -*-

import logging

from hashcode19.helpers import Input, Output, PictureType, Slide, score_transition

logger = logging.getLogger(__name__)


def main(i: Input) -> Output:
    """Sort by number of tags, then trivially pack vertical pictures.
    Choose the best next slide in 1000 other slides."""
    slideshow = []
    slides = [Slide([h]) for h in i.type_to_pics[PictureType.H]]
    vp = i.type_to_pics[PictureType.V]
    slides = slides + [Slide([vp[i], vp[i+1]]) for i in range(0, len(vp)//2, 2)]

    slides = sorted(slides, key=lambda x: len(x.tags), reverse=False)

    cur_slide, slides = slides[0], slides[1:]
    best_slide = None
    slideshow.append(cur_slide)
    while len(slides) > 0:
        if len(slides) % 1000 == 0:
            logger.debug("Slides remaining: {}".format(len(slides)))
        best_max = -1
        best_idx = -1
        for i, s in enumerate(slides[:1000]):
            cur_score = score_transition(cur_slide, s)
            if cur_score > best_max:
                best_max = cur_score
                best_slide = s
                best_idx = i

        slideshow.append(best_slide)
        slides.pop(best_idx)
        cur_slide = best_slide

    return Output(slideshow)

