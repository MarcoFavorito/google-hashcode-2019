# -*- coding: utf-8 -*-
import copy

import logging
import random

from hashcode19.helpers import Input, Output, PictureType, Slide, score_transition, score_tag_transition

logger = logging.getLogger(__name__)


def main(i: Input) -> Output:
    """The same of the naive algorithm, but instead use smart packing of vertical pictures.
    That is, do not pack before, but during the greedy search in the current window."""
    slideshow = []

    horizontal_pics = i.type_to_pics[PictureType.H]
    vertical_pics = i.type_to_pics[PictureType.V]

    pictures = copy.deepcopy(i.pictures)
    random.shuffle(pictures)

    if len(horizontal_pics) > 0:
        cur_pic = horizontal_pics[0]
        cur_slide = Slide([cur_pic])
        pictures.remove(cur_pic)
    else:
        v1, v2 = random.sample(vertical_pics, 2)
        cur_slide = Slide([v1, v2])
        pictures.remove(v1)
        pictures.remove(v2)

    slideshow.append(cur_slide)

    while len(pictures) > 0:
        best_pic = None
        if len(pictures) % 1000 == 0:
            logger.debug("Pictures remaining: {}".format(len(pictures)))
        best_max = -1
        best_idx = -1
        # first loop iterating over a window to find the best next
        for i in range(min(1000, len(pictures))):
            p = pictures[i]
            cur_score = score_tag_transition(cur_slide.tags, p.tags)
            if cur_score > best_max:
                best_max = cur_score
                best_pic = p
                best_idx = i

        # if the best found is vertical, find another vertical to make the pair.
        if best_pic.type_ == PictureType.V:
            best_second_max = -1
            best_second_pic = -1
            best_second_idx = -1
            for i in range(min(1000, len(pictures))):
                p = pictures[i]
                if p == best_pic or p.type_ == PictureType.H: continue
                cur_score = score_tag_transition(cur_slide.tags, set.union(best_pic.tags, p.tags))
                if cur_score > best_second_max:
                    best_second_max = cur_score
                    best_second_pic = p
                    best_second_idx = i

            # if a second vertical picture is found,
            # we can create a slide with these two vertical pics.
            if best_second_pic != -1:
                best_slide = Slide([best_pic, best_second_pic])

                # remove both pics from the list
                if best_idx <= best_second_idx:
                    pictures.pop(best_second_idx)
                    pictures.pop(best_idx)
                else:
                    pictures.pop(best_idx)
                    pictures.pop(best_second_idx)

            # if for whatever reason no way to find another vertical image, then skip it.
            else:
                pictures.pop(best_idx)
                continue

        else:
            best_slide = Slide([best_pic])
            pictures.pop(best_idx)

        slideshow.append(best_slide)
        cur_slide = best_slide
    return Output(slideshow)

