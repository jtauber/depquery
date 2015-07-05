# depquery

Simple Python-based query language for the "super" MorphGNT with dependency
analysis.


## Example

Load the data:

```
from collections import defaultdict

from data import Data, Q, Var

d = Data()
d.load("supermorphgnt.txt")
```

Now query "what are the possible relationships of a noun to a verb head?":

```
for result, count in d.count(
    Q(pos="N-", rel=Var("rel"), head=Q(pos="V-"))
).items():
    print(result, count)
```

This outputs:

```
(('rel', 'O'),) 4618
(('rel', 'ADV'),) 6390
(('rel', 'np'),) 33
(('rel', 'CL'),) 1426
(('rel', 'S'),) 4311
(('rel', 'P'),) 2
(('rel', 'pp'),) 8
(('rel', 'IO'),) 478
(('rel', 'O2'),) 134
```

See `tests.py` for more examples.


## To Do

* logical connectives
* substring predicates
* ability for subqueries to walk back down dependency tree
