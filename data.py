from collections import defaultdict


class Data:

    def __init__(self):
        self.words = {}
        self.lemma_index = defaultdict(set)

    def load(self, filename):
        with open(filename) as f:
            for line in f:
                (
                    word_id, verse_id, paragraph_id, sentence_id, pos, parse,
                    crit_text, text, word, norm, lemma, rel, head
                ) = line.strip().split()

                if head == "None":
                    head = None

                self.words[word_id] = dict(
                    verse_id=verse_id,
                    paragraph_id=paragraph_id,
                    sentence_id=sentence_id,
                    pos=pos,
                    parse=parse,
                    crit_text=crit_text,
                    text=text,
                    word=word,
                    norm=norm,
                    lemma=lemma,
                    rel=rel,
                    head=head,
                )

                self.lemma_index[lemma].add(word_id)

    def test_word(self, query_object, word_id):
        result = {}
        match = True
        for kwarg, value in query_object.kwargs.items():
            if isinstance(value, str):
                if value != self.words.get(word_id, {}).get(kwarg):
                    match = False
                    break
            elif isinstance(value, Var):
                result.update({
                    value.label: self.words.get(word_id, {}).get(kwarg)})
            elif isinstance(value, Q):
                sub_result = self.test_word(value, self.words[word_id][kwarg])
                if sub_result is None:
                    match = False
                    break
                else:
                    result.update(sub_result)
            else:
                raise ValueError("{} of unknown type".format(value))
        if match:
            return result

    def query(self, query_object):
        # optimize for root query involving lemma
        if "lemma" in query_object.kwargs:
            domain = self.lemma_index[query_object.kwargs["lemma"]]
        else:
            domain = self.words

        for word_id in domain:
            result = self.test_word(query_object, word_id)
            if result is not None:
                yield result

    def count(self, query_object):
        results = defaultdict(int)

        for result in self.query(query_object):
            results[tuple(sorted(result.items()))] += 1

        return results


class Q:
    def __init__(self, **kwargs):
        self.kwargs = kwargs


class Var:
    def __init__(self, label):
        self.label = label
