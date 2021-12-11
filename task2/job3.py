import re

from mrjob.job import MRJob
from mrjob.protocol import TextProtocol
from mrjob.step import MRStep

WORD_RE = re.compile(r"[A-Za-z]+")

class MRMostFrequentWord(MRJob):
    OUTPUT_PROTOCOL = TextProtocol

    def steps(self):
        return [MRStep(mapper=self.mapper, combiner=self.combiner, reducer=self.reducer), MRStep(reducer=self.frequency_reducer)]

    def mapper(self, _, line):
        for word in WORD_RE.findall(line):
            yield word.lower(), 1

    def combiner(self, word, counter):
        yield word, sum(counter)

    def reducer(self, word, counter):
        yield None, (word, sum(counter))

    def frequency_reducer(self, _, frequencies):
        word = max(frequencies, key=lambda x: x[1])
        yield word[0], str(word[1])


if __name__ == "__main__":
    MRMostFrequentWord.run()
