import math, collections

class CustomLanguageModel:

  def __init__(self, corpus):
    """Initialize your data structures in the constructor."""
    # TODO your code here
    self.unigramCounts = collections.defaultdict(lambda:0)
    self.bigramCounts = collections.defaultdict(lambda:0)
    self.trigramCounts = collections.defaultdict(lambda:0)
    self.total = 0
    self.train(corpus)

  def train(self, corpus):
    """ Takes a corpus and trains your language model. 
        Compute any counts or other corpus statistics in this function.
    """  
    # TODO your code here
    for sentence in corpus.corpus:
	token1 = '@NaN'
	token2 = '<s>'
	token3 = '@NaN'
	self.unigramCounts[token2] = self.unigramCounts[token2] + 1
	self.total += 1
	for datum in sentence.data:
	    token3 = datum.word
	    self.total += 1
	    self.bigramCounts[(token2,token3)] = self.bigramCounts[(token2,token3)] + 1
	    self.unigramCounts[token3] = self.unigramCounts[token3] + 1
	    if token1 != '@NaN':
		self.trigramCounts[(token1,token2,token3)] = self.trigramCounts[(token1,token2,token3)] + 1
	    # move everyone up
	    token1 = token2
	    token2 = token3
	
	# end of sentence
	token1 = token2
	token2 = token3
	token3 = '</s>'	
	self.total += 1
	self.bigramCounts[(token2,token3)] = self.bigramCounts[(token2,token3)] + 1
	self.unigramCounts[token3] = self.unigramCounts[token3] + 1
	self.trigramCounts[(token1,token2,token3)] = self.trigramCounts[(token1,token2,token3)] + 1
    # pass

  def score(self, sentence):
    """ Takes a list of strings as argument and returns the log-probability of the 
        sentence using your language model. Use whatever data you computed in train() here.
    """
    # TODO your code here
    score = 0.0
    token1 = '@NaN'
    token2 = '<s>'
    token3 = '@NaN'
    count1 = self.unigramCounts[token2]
    for word in sentence:
	token3 = word
	count3 = self.trigramCounts[(token1,token2,token3)]
	count2 = self.bigramCounts[(token2,token3)]
	if count3 > 0: #trigram exists
	    score += math.log(count3)
	    score -= math.log(self.bigramCounts[(token1,token2)])
	elif count2 > 0: # no trigram, but bigram exists
	    # score += math.log(0.4) + math.log(self.bigramCounts[(token2,token3)]+1)
	    score += math.log(0.4) + math.log(count2)
	   #  score -= math.log(self.unigramCounts[token2]+len(self.unigramCounts))
	    score -= math.log(self.unigramCounts[token2])
	else: # no trigram or bigram
	    score += math.log(0.4) + math.log(self.unigramCounts[token3]+1)
	    score -= math.log(self.total + (len(self.unigramCounts)))
	# move everyone up
	token1 = token2
	token2 = token3

    # end of sentence case
    token1 = token2
    token2 = token3
    token3 = '</s>'	
    
    count1 = self.unigramCounts[token3]
    count3 = self.trigramCounts[(token1,token2,token3)]
    count2 = self.bigramCounts[(token2,token3)]
    if count3 > 0: #trigram exists
	score += math.log(count3)
	score -= math.log(self.bigramCounts[(token2,token3)])
    elif count2 > 0: # no trigram, but bigram exists
	# score += math.log(0.4) + math.log(self.bigramCounts[(token2,token3)]+1)
	score += math.log(0.4) + math.log(count2)
	#  score -= math.log(self.unigramCounts[token2]+len(self.unigramCounts))
	score -= math.log(self.unigramCounts[token2])
    else: # no trigram or bigram
	score += math.log(0.4) + math.log(count1+1)
	score -= math.log(self.total + (len(self.unigramCounts)))
    return score
