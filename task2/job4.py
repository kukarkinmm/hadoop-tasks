import re

from mrjob.job import MRJob
from mrjob.protocol import TextProtocol

WORD_RE = re.compile(r"\w+")


class MRUpperCounter(MRJob):
    OUTPUT_PROTOCOL = TextProtocol

    def mapper(self, _, line):
        for word in WORD_RE.findall(line):
            is_upper = word.istitle()
            yield word.lower(), (1, int(is_upper))

    def combiner(self, word, stats):
        yield word, [sum(el) for el in zip(*stats)]

    def reducer(self, word, stats):
        counter, upper_counter = (sum(el) for el in zip(*stats))
        if counter > 10 and upper_counter > int(counter / 2):
            yield word, None


if __name__ == "__main__":
    MRUpperCounter.run()
