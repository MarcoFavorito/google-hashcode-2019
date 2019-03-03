# Design

## Problem analysis

Recall that, the score of a slide transition from s1 to s2 is given by:

`min( | s1 \ s1 |, | s1 & s2 |, | s2 \ s1 | )`

Notice, we use s1 to denote interchangeably the slide and the set of tags 
in that slide. Also, we denote with `//` integer division (`/` and then floor).

The main questions to answer are:

- given the current slide, how to find the best next slide
- how to pack vertical pictures in a good way.


### Observations

Given two slides s1 and s2, whose cardinality of the tag set is N.

#### Worst case

The worst case is when:
 
- the sets of tags are the same. 

```

|s1 / s2|     |s1 & s2|     |s2 / s1|

    0             N             0

```

- the sets of tags are completely different (empty intersection):

```

|s1 / s2|     |s1 & s2|     |s2 / s1|

    N             0             M

```

#### Best case

The best case is when we have (assume N even for simplicity):

```

|s1 / s2|     |s1 & s2|     |s2 / s1|

   N/2           N/2           N/2

```

That is, every tag contributes in the same way to the score.

Now assume we remove an element _e_ from s2.

- if _e_ was in s1, the score decreases:

```

|s1 / s2|     |s1 & s2|     |s2 / s1|

 N/2 + 1       N/2 - 1         N/2

```
- if _e_ was not in s2, the score decreases:

```

|s1 / s2|     |s1 & s2|     |s2 / s1|

   N/2           N/2         N/2 - 1

```

In both cases, the score decreases (only if from the best case).

If instead we add an element _e_ to s2:

- if _e_ is also in s1, the score decreases:

```

|s1 / s2|     |s1 & s2|     |s2 / s1|

 N/2 - 1       N/2 + 1         N/2

```
- if _e_ is not in s1, the score is the same:

```

|s1 / s2|     |s1 & s2|     |s2 / s1|

   N/2           N/2         N/2 + 1

```

In one case, the score decreases, in the other one the score remains the same. 
Remember that we are talking about local variations from the best case.

---

Given a slide s1, how to choose the next slide?

- no completely disjoint nor a subset of s1
- given `|s1|=N` and `|s2|=M`:
    - if `N > M`: the score is in the range `[0, M//2]`
    - if `N = M`: the score is in the range `[0, N//2]`
    - if `N < M`: the score is in the range `[0, N//2]`
    
    in other words, the score is in the range `[0, min(N, M)//2]`
    
    Which implies that, in order to maximize the range, from the slide s1 
    we should look at slides with a greater or equal 
    number of tags, that is `N <= M`.
    
    Nevertheless, this **does not imply** that we improve the score if `N <= M`.

## Summary

- s1 == s2 | s1 & s2 == {} -> worst case

## Solutions

TODO
