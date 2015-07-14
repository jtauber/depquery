# depquery

Simple Python-based query language for the "super" MorphGNT with dependency
analysis.


## Queries

A query is just a `Q` object with name/value pairs. The names correspond to
fields in the data and the values are either:

* literal matches (e.g. `pos="N-"`)
* variables that are to be filled in during the query (e.g. `rel=Var("rel")`)
* subqueries that are to be done by following head link and applying the
  subquery to the head word (e.g. `head=Q(pos="V-")`)

So for example:

    Q(pos="N-", rel=Var("rel"), head=Q(pos="V-"))

asks the question: "what are the possible `rel` values when `pos` is `N-` and
the `pos` of the `head` is `V-`?". In other words "what are the possible
relationships of a noun to a verb head?"

Once you have a query object like this, you can either run
`data.query(query_object)` to get an iterator over the results (a dictionary
of variables you've selected with `Var`) or `data.count(query_object)` to get
a dictionary mapping results to a count of how many times that result was seen.


## Full Usage Example

Load the data:

```
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

* rewrite test to not need `supermorphgnt.txt`
* logical connectives
* substring predicates
* ability for subqueries to walk back down dependency tree
