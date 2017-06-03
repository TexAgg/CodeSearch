# http://bit.ly/2pVLFGL
from collections import Counter
import re
import json
import urllib
from decimal import *

# http://stackoverflow.com/a/475041/5415895
class Classifier():

	def __init__(self):
		self.data = {}
		# Number of inputs for a language.
		self.totals = Counter()
		self.word_totals = Counter()

	# http://stackoverflow.com/q/735975/5415895
	@staticmethod
	def words(code):
		return re.split("[^a-zA-Z]", code)
	
	def dump_training(self):
		with open("out/training.json", 'w') as outfile:
			outdata = {"data": self.data, "totals": self.totals, "word_totals": self.word_totals}
			json.dump(outdata, outfile)

	def train(self, code, lang):
		self.totals[lang] += 1
		if lang not in self.data:
			self.data[lang] = Counter()
		for word in Classifier.words(code):
			#re.sub(r'\W+', '', word)
			if word is not "":
				self.data[lang][word] += 1
				self.word_totals[word] += 1
		#self.dump_training()
		
	# http://bit.ly/2qxHQdt
	def classify(self, code):
		res = {}
		ws = Classifier.words(code)
		for lang, counts in self.data.iteritems():
			p = []
			for w in ws:
				plw = 1
				if self.data[lang][w] > 0:
					# Calculate plw.
					pwl = Decimal(self.data[lang][w]) / Decimal(len(list(self.data[lang].elements())))
					pl = Decimal(1) / len(self.totals.keys())
					
					# Problem here?
					not_lang_word = Decimal(Decimal(self.word_totals[w] - self.data[lang][w]) / Decimal(len(list(self.word_totals.elements()))))
					# Probability of not l.
					p_l = 1 - pl
					plw = pwl * pl / (pwl * pl + Decimal(p_l*not_lang_word))
					# Problem occurs before here!
					p.append(plw)
				# Else rare word: http://bit.ly/2r1tROu
				else:
					continue
			m = 1
			mp = 1
			for pj in p:
				m *= pj
				mp *= 1-pj
			res[lang] = float(m / (m + mp))
		return res

if __name__ == "__main__":
	c = Classifier()

	# python
	c.train(open("code_finder.py", 'r').read(), 'python')
	c.train(urllib.urlopen("https://raw.githubusercontent.com/schollz/howmanypeoplearearound/9e12f0b2996c0b98460c51aca14da1d744c7bded/howmanypeoplearearound/analysis.py").read(), "python")
	c.train(urllib.urlopen("https://raw.githubusercontent.com/TexAgg/cc-mrjob/64c17fb7e0b67fa9634e9672bf689d688d06c3c1/mrcc.py").read(), "python")

	# csharp
	c.train(open("../CodeSearch/Global.asax.cs", 'r').read(), 'csharp')
	c.train(urllib.urlopen("https://raw.githubusercontent.com/thedillonb/CodeHub/master/CodeHub.Core/AkavacheSqliteLinkerOverride.cs").read(), 'csharp')
	c.train(urllib.urlopen('https://raw.githubusercontent.com/thedillonb/CodeHub/96b44b931330a51eac0d039290eaa330cc81dd1e/CodeHub.Core/Factories/LoginFactory.cs').read(), "csharp")

	# cpp
	c.train(urllib.urlopen("https://raw.githubusercontent.com/tensorflow/tensorflow/b07791f6e9b306937eb58f7bb6c3300cd26583af/third_party/eigen3/unsupported/Eigen/CXX11/src/NeuralNetworks/Activations.h").read(), "cpp")
	c.train(urllib.urlopen("https://raw.githubusercontent.com/tensorflow/tensorflow/73115538fc37dd8967b8531e04a7a1d42f6bada4/tensorflow/stream_executor/cuda/cuda_diagnostics.cc").read(), "cpp")
	c.train(urllib.urlopen("https://raw.githubusercontent.com/aguinet/wannakey/c7a902c36b8d5c6bffe11cfbdec7b4b68cf7ed1f/search_primes/search_primes/search_primes.cpp").read(),"cpp")

	c.dump_training()


	########
	# TEST #
	########

	print c.classify(urllib.urlopen("https://raw.githubusercontent.com/jkleiber/Snake/e05cd53eaac9dd7c5f9ed93cf16f09113e947ca3/Cobra.py").read())