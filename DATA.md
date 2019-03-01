## Data analysis

Some info about the data:

### #pics, #H and #V

    head -n 1 a_example.in  # total number of pic 
    cat a_example.in | tail -n +2  | cut -d' ' -f1 | sort | uniq -c  # pic per type
    
    
```    
|   | #pics | #horiz | #vert |
|---|-------|--------|-------|
| a |     4 |      2 |     2 |
| b | 80000 |  80000 |     0 |
| c |  1000 |    500 |   500 |
| d | 90000 |  30000 | 60000 |
| e | 80000 |      0 | 80000 |
```

### #distinct tags 

    cat a_example.in | tail -n +2 | cut -d' ' -f3- |  tr " " "\n" | sort -u | wc -l


```
|   | #tags  |
|---|--------|
| a |      4 |
| b | 840000 |
| c |   2166 |
| d |    220 |
| e |    500 |
```


 

### #pics by #tags

    cat a_example.in | cut -d' ' -f2 | tail -n +2 | sort | uniq -c | sed -e "s/^ *//" | awk '{print $2 " " $1}' | sort -n -k 1

Here the list for every file a,b,c,d,e:

    2 3   9  4002   4   2   1    1    8    6    
    3 1  12 11840   5  90   2  241    9  358  
         15 17922   6 102   3 5503   10 4066
         18 18045   7 118   4 5660   11 4055
         21 13506   8  88   5 5845   12 4074
         24  7993   9 109   6 5737   13 4191
         27  4006  10  91   7 5988   14 4246
         30  1738  11  99   8 6066   15 4128
         33   664  12 109   9 6236   16 4158
         36   193  13 100  10 6298   17 4171
         39    69  14  92  11 6297   18 4150
         42    15          12 6553   19 4039
         45     6          13 6645   20 4146
         51     1          14 6445   21 4171
                           15 6146   22 4140
                           16 5114   23 4183
                           17 3466   24 4226
                           18 1446   25 4223
                           19  313   26 4091
                                     27 4035
                                     28 3422
                                     29 1721
      
      