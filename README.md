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

results = defaultdict(int)

for result in d.query(query):
    results[tuple(sorted(result.items()))] += 1

for result, count in results.items():
    print("καθώς with a {pos} head".format(**dict(result)), count)
```

outputs:

```
καθώς with a RD head 1
καθώς with a A- head 9
καθώς with a V- head 148
καθώς with a D- head 2
καθώς with a N- head 14
καθώς with a RP head 8
```
