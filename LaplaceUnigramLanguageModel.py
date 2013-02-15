import math, collections

class LaplaceUnigramLanguageModel:

  def __init__(self, corpus):
    """Initialize your data structures in the constructor."""
    # TODO your code here
    self.laplaceUnigramCounts = collections.defaultdict(lambda:0)
    self.total = 0
    self.train(corpus)

  def train(self, corpus):
    """ Takes a corpus and trains your language model. 
        Compute any counts or other corpus statistics in this function.
    """  
    # TODO your code here
    for sentence in corpus.corpus:
	for datum in sentence.data:
	    token = datum.word
	    self.laplaceUnigramCounts[token] = self.laplaceUnigramCounts[token] + 1
	    self.total += 1

    # pass

  def score(self, sentence):
    """ Takes a list of strings as argument and returns the log-probability of the 
        sentence using your language model. Use whatever data you computed in train() here.
    """
    # TODO your code here
    score = 0.0
    for token in sentence:
	count = self.laplaceUnigramCounts[token]
	if count > 0:
	    score += math.log(count+1)
	    score -= math.log(self.total + len(self.laplaceUnigramCounts))
	else:
	    score -= math.log(self.total + len(self.laplaceUnigramCounts))

    return score
