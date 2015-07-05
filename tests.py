#!/usr/bin/env python3

from data import Data, Q, Var

d = Data()
d.load("supermorphgnt.txt")


assert len(list(d.query(Q(lemma="καθώς")))) == 182

assert d.count(
    Q(lemma="καθώς", rel=Var("rel"))
) == {
    (("rel", "conj"),): 182
}

assert d.count(
    Q(lemma="καθώς", rel=Var("rel"), pos=Var("pos"))
) == {
    (("pos", "C-"), ("rel", "conj")): 182
}

assert d.count(
    Q(lemma="καθώς", pos="C-")
) == {
    (): 182
}

assert d.count(
    Q(lemma="καθώς", pos="D-")
) == {
}

assert d.count(
    Q(pos="N-")
) == {
    (): 28237
}

assert d.count(
    Q(lemma="καθώς", rel=Var("rel"), head=Q(pos="V-"))
) == {
    (("rel", "conj"),): 148
}

assert d.count(
    Q(lemma="καθώς", rel=Var("rel"), head=Q(pos=Var("h_pos")))
) == {
    (("h_pos", "A-"), ("rel", "conj")): 9,
    (("h_pos", "RP"), ("rel", "conj")): 8,
    (("h_pos", "N-"), ("rel", "conj")): 14,
    (("h_pos", "V-"), ("rel", "conj")): 148,
    (("h_pos", "D-"), ("rel", "conj")): 2,
    (("h_pos", "RD"), ("rel", "conj")): 1,
}

assert d.count(
    Q(
        lemma="καθώς",
        rel=Var(1),
        head=Q(
            pos=Var(2),
            rel=Var(3),
            head=Q(pos=Var(4))
        )
    )
) == {
    ((1, 'conj'), (2, 'RP'), (3, 'CL'), (4, 'A-')): 2,
    ((1, 'conj'), (2, 'A-'), (3, 'CL'), (4, 'V-')): 4,
    ((1, 'conj'), (2, 'V-'), (3, 'CL'), (4, 'N-')): 12,
    ((1, 'conj'), (2, 'N-'), (3, 'CL'), (4, 'RP')): 1,
    ((1, 'conj'), (2, 'V-'), (3, 'CL'), (4, 'D-')): 2,
    ((1, 'conj'), (2, 'RD'), (3, 'CL'), (4, 'N-')): 1,
    ((1, 'conj'), (2, 'V-'), (3, 'ADV'), (4, 'V-')): 3,
    ((1, 'conj'), (2, 'V-'), (3, 'CL'), (4, 'RP')): 2,
    ((1, 'conj'), (2, 'V-'), (3, 'CL'), (4, 'V-')): 113,
    ((1, 'conj'), (2, 'D-'), (3, 'CL'), (4, None)): 1,
    ((1, 'conj'), (2, 'N-'), (3, 'CL'), (4, 'V-')): 8,
    ((1, 'conj'), (2, 'A-'), (3, 'CL'), (4, 'A-')): 3,
    ((1, 'conj'), (2, 'N-'), (3, 'CL'), (4, 'D-')): 1,
    ((1, 'conj'), (2, 'N-'), (3, 'CL'), (4, 'N-')): 3,
    ((1, 'conj'), (2, 'A-'), (3, 'CL'), (4, 'N-')): 1,
    ((1, 'conj'), (2, 'V-'), (3, 'CL'), (4, 'RD')): 1,
    ((1, 'conj'), (2, 'N-'), (3, 'ADV'), (4, 'V-')): 1,
    ((1, 'conj'), (2, 'V-'), (3, 'CL'), (4, None)): 10,
    ((1, 'conj'), (2, 'RP'), (3, 'CL'), (4, 'V-')): 4,
    ((1, 'conj'), (2, 'D-'), (3, 'CL'), (4, 'N-')): 1,
    ((1, 'conj'), (2, 'RP'), (3, 'CL'), (4, 'N-')): 2,
    ((1, 'conj'), (2, 'A-'), (3, 'CL'), (4, None)): 1,
    ((1, 'conj'), (2, 'V-'), (3, 'CL'), (4, 'A-')): 5,
}
