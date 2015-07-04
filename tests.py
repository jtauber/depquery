#!/usr/bin/env python3

from collections import defaultdict

from data import Data, Q, Var

d = Data()
d.load("supermorphgnt.txt")


query = Q(lemma="καθώς")

assert len(list(d.query(query))) == 182


query = Q(lemma="καθώς", rel=Var("rel"))

results = defaultdict(int)

for result in d.query(query):
    results[tuple(result.items())] += 1

assert results == {(("rel", "conj"),): 182}
