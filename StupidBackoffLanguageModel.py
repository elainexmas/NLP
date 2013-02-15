import math, collections

class StupidBackoffLanguageModel:

  def __init__(self, corpus):
    """Initialize your data structures in the constructor."""
    # TODO your code here
    self.unigramCounts = collections.defaultdict(lambda:0)
    self.bigramCounts = collections.defaultdict(lambda:0)
    self.total = 0
    self.train(corpus)

  def train(self, corpus):
    """ Takes a corpus and trains your language model. 
        Compute any counts or other corpus statistics in this function.
    """  
    # TODO your code here
    for sentence in corpus.corpus:
	token1 = '<s>'
	self.unigramCounts[token1] = self.unigramCounts[token1] + 1
	self.total += 1
	token2 = ''
	for datum in sentence.data:
	    token2 = datum.word
	    self.total += 1
	    self.bigramCounts[(token1,token2)] = self.bigramCounts[(token1,token2)]+1
	    self.unigramCounts[token2] = self.unigramCounts[token2] + 1
	    token1 = datum.word
	token2 = '</s>'
	self.total += 1
	self.bigramCounts[(token1,token2)] = self.bigramCounts[(token1,token2)]+1
	self.unigramCounts[token2] = self.unigramCounts[token2] + 1
    # pass


  def score(self, sentence):
    """ Takes a list of strings as argument and returns the log-probability of the 
        sentence using your language model. Use whatever data you computed in train() here.
    """
    # TODO your code here
    score = 0.0
    token1 = '<s>'
    token2 = ''
    for word in sentence:
	token2 = word
	count = self.bigramCounts[(token1,token2)]
	if count > 0:
	    score += math.log(count)
	    score -= math.log(self.unigramCounts[token1])
	else:
	    score += math.log(0.4) + math.log(self.unigramCounts[token2]+1)
	    score -= math.log(self.total + (len(self.unigramCounts)))
	token1 = word
    token2 = '</s>'
    count = self.bigramCounts[(token1,token2)]
    if count > 0:
	score += math.log(count)
	score -= math.log(self.unigramCounts[token1])
    else:
	score += math.log(0.4) + math.log(self.unigramCounts[token2]+1)
	score -= math.log(self.total + (len(self.unigramCounts)))


    return score
