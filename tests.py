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
    results[tuple(sorted(result.items()))] += 1

assert results == {(("rel", "conj"),): 182}


query = Q(lemma="καθώς", rel=Var("rel"), pos=Var("pos"))

results = defaultdict(int)

for result in d.query(query):
    results[tuple(sorted(result.items()))] += 1

assert results == {(("pos", "C-"), ("rel", "conj")): 182}


query = Q(lemma="καθώς", pos="C-")

results = defaultdict(int)

for result in d.query(query):
    results[tuple(sorted(result.items()))] += 1

assert results == {(): 182}


query = Q(lemma="καθώς", pos="D-")

results = defaultdict(int)

for result in d.query(query):
    results[tuple(sorted(result.items()))] += 1

assert results == {}


query = Q(pos="N-")

results = defaultdict(int)

for result in d.query(query):
    results[tuple(sorted(result.items()))] += 1

assert results == {(): 28237}


query = Q(lemma="καθώς", rel=Var("rel"), head=Q(pos="V-"))

results = defaultdict(int)

for result in d.query(query):
    results[tuple(sorted(result.items()))] += 1

assert results == {(("rel", "conj"),): 148}


query = Q(lemma="καθώς", rel=Var("rel"), head=Q(pos=Var("head_pos")))

results = defaultdict(int)

for result in d.query(query):
    results[tuple(sorted(result.items()))] += 1

assert results == {
    (("head_pos", "A-"), ("rel", "conj")): 9,
    (("head_pos", "RP"), ("rel", "conj")): 8,
    (("head_pos", "N-"), ("rel", "conj")): 14,
    (("head_pos", "V-"), ("rel", "conj")): 148,
    (("head_pos", "D-"), ("rel", "conj")): 2,
    (("head_pos", "RD"), ("rel", "conj")): 1,
}
