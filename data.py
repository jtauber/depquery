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
