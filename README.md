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

Then query for the part-of-speech of all heads of words with the lemma καθώς:

```
query = Q(lemma="καθώς", head=Q(pos=Var("pos")))

for result, count in sorted(d.count(query).items()):
    print("καθώς with a {pos} head".format(**dict(result)), count)
```

This outputs:

```
καθώς with a A- head 9
καθώς with a D- head 2
καθώς with a N- head 14
καθώς with a RD head 1
καθώς with a RP head 8
καθώς with a V- head 148
```

See `tests.py` for more examples.
