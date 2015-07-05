from collections import defaultdict


class Data:

    def __init__(self):
        self.words = {}
        self.lemma_index = defaultdict(set)

    def load(self, filename):
        for line in open(filename):
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
                if value != self.words[word_id][kwarg]:
                    match = False
                    break
            elif isinstance(value, Var):
                result.update({value.label: self.words[word_id][kwarg]})
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


class Q:
    def __init__(self, **kwargs):
        self.kwargs = kwargs


class Var:
    def __init__(self, label):
        self.label = label
