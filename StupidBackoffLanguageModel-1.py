import math, collections
from LaplaceUnigramLanguageModel import LaplaceUnigramLanguageModel
from LaplaceBigramLanguageModel import LaplaceBigramLanguageModel

class StupidBackoffLanguageModel:

  def __init__(self, corpus):
    """Initialize your data structures in the constructor."""
    # TODO your code here
    self.laplaceUnigramLM = LaplaceUnigramLanguageModel(corpus)
    self.laplaceBigramLM = LaplaceBigramLanguageModel(corpus)

    self.train(corpus)

  def train(self, corpus):
    """ Takes a corpus and trains your language model. 
        Compute any counts or other corpus statistics in this function.
    """  
    # TODO your code here
    self.laplaceUnigramLM = LaplaceUnigramLanguageModel.train(self.laplaceUnigramLM,corpus)
    self.laplaceBigramLM = LaplaceBigramLanguageModel.train(self.laplaceBigramLM,corpus)
    # for sentence in corpus.corpus:
	# for datum in sentence.data:
	    

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
	count = self.laplaceBigramLM.laplaceBigramCounts[(token1,token2)]


    return 0.0
