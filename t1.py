
import numpy as np

# 		  B	  E     A	  J	   M
#gra = [ [], [], [0,1], [2], [2] ]
class Node():
	def __init__(self, prob, parents = []): #prob = [pFalse, pTrue]
		self.parents = parents
		self.prob = prob


	def computeProb(self, evid): #evid = evidencia |info atual sobre cada uma das variaveis(0:false 1:true)
		"""precisa da evid dos parents e devolve [prob_node = false, prob_node = true]"""
		x=[]
		if self.parents == []: #se nao tem parents
			return [1-self.prob[0], self.prob[0]]

		if len(self.parents) == 1: #se apenas tiver 1 parent apresenta apenas prob_node = true
			if evid[self.parents[0]] == 0:
				return [self.prob[0]]
			if evid[self.parents[0]] == 1:
				return [self.prob[1]]
		else:
			for i in range(0, len(self.parents)): #mete evids em x
				x = x + [evid[self.parents[i]]]
			print(x)

			for i in range(0, len(self.parents)-1): #para cada parent
					if x[i] == 0 and x[i+1] == 0: # False, False
						print('0		0\n')
						return [1-self.prob[x[i]][i+1], self.prob[x[i]][i+1]]
					if x[i] == 0 and x[i+1] == 1: # False, True !nao funciona este!
						print('0		1\n')
						return [1-self.prob[x[i]][i+1], self.prob[x[i]][i+1]]
					if  x[i] == 1 and x[i+1] == 0: # True, False
						print('1		0\n')
						return [1-self.prob[x[i]][i+1], self.prob[x[i]][i+1]]
					if  x[i] == 1 and x[i+1] == 1: # True, True
						print('1		1\n')
						return [1-self.prob[x[i]][i+1], self.prob[x[i]][i+1]]
