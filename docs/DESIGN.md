# Design

## Problem analysis

Recall that, the score of a slide transition from s1 to s2 is given by:

`min( | s1 \ s1 |, | s1 & s2 |, | s2 \ s1 | )`

Notice, we use s1 to denote interchangeably the slide and the set of tags 
in that slide.

### Observations

Given two slides s1 and s2, whose cardinality of the tag set is N.

The worst case is when the set are the same. 

```

|s1 / s2|     |s1 & s2|     |s2 / s1|

    0             N             0

```

The best case is when we have (assume N even for simplicity):

```

|s1 / s2|     |s1 & s2|     |s2 / s1|

   N/2           N/2           N/2

```

Now assume we remove an element _e_ from s2.

- if _e_ was in s1:

```

|s1 / s2|     |s1 & s2|     |s2 / s1|

 N/2 + 1       N/2 - 1         N/2

```
- if _e_ was not in s2:

```

|s1 / s2|     |s1 & s2|     |s2 / s1|

   N/2           N/2         N/2 - 1

```

In both cases, the score decreases.

## Solutions

TODO
