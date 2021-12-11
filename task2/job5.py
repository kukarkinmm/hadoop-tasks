import re

from mrjob.job import MRJob
from mrjob.protocol import TextProtocol
from mrjob.step import MRStep

WORD_RE = re.compile(r"\b[А-Яа-я]{2}\.")


class MRAbbreviation(MRJob):
    OUTPUT_PROTOCOL = TextProtocol
    
    def steps(self):
        return [
            MRStep(mapper=self.mapper, combiner=self.combiner, reducer=self.reducer),
            MRStep(reducer=self.filter)
        ]

    def mapper(self, _, line):
        for word in WORD_RE.findall(line):
            yield word.lower(), 1

    def combiner(self, word, counter):
        yield word, sum(counter)

    def reducer(self, word, counter):
        yield None, (word, sum(counter))

    def filter(self, _, stats):
        stats_list = list(stats)
        max_counter = max(stats_list, key=lambda v: v[1])
        for word, counter in stats_list:
            if float(counter / max_counter[1]) >= 0.2:
                yield word, None


if __name__ == "__main__":
    MRAbbreviation.run()
