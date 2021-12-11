import re

from mrjob.job import MRJob
from mrjob.protocol import TextProtocol

WORD_RE = re.compile(r"\w+")


class MRAvgWordLen(MRJob):
    OUTPUT_PROTOCOL = TextProtocol

    def mapper(self, _, line):
        for word in WORD_RE.findall(line):
            yield len(word), 1

    def combiner(self, wordlen, counter):
        count = sum(counter)
        yield None, (wordlen * count, count)

    def reducer(self, _, stats):
        lens, counters = zip(*stats)
        yield None, str(sum(lens) / sum(counters))


if __name__ == "__main__":
    MRAvgWordLen.run()
