import re

from mrjob.job import MRJob
from mrjob.protocol import TextProtocol

WORD_RE = re.compile(r"\w+")

class MRLongestWord(MRJob):
    OUTPUT_PROTOCOL = TextProtocol

    def mapper(self, _, line):
        for word in WORD_RE.findall(line):
            yield None, (word, len(word))

    def combiner(self, _, wordlens):
        word = max(wordlens, key=lambda x: x[1])
        yield None, (word[0], word[1])

    def reducer(self, _, wordlens):
        word = max(wordlens, key=lambda x: x[1])
        yield word[0], str(word[1])


if __name__ == "__main__":
    MRLongestWord.run()
