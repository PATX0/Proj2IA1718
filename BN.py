# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 15:51:49 2018

@author: mlopes
"""

import numpy as np

# 		  B	  E     A	  J	   M
#gra = [ [], [], [0,1], [2], [2] ]
class Node():
	def __init__(self, prob, parents = []): #prob = [pFalse, pTrue]
		self.parents = parents
		self.prob = prob


	def computeProb(self, evid): #evid = evidencia |info atual sobre cada uma das variaveis(0:false 1:true)
		"""precisa da evid dos parents e devolve [prob_node = false, prob_node = true]"""
		if self.parents == []: #se nao tem parents
			return [1-self.prob[0], self.prob[0]]

		if len(self.parents) == 1: #se apenas tiver 1 parent apresenta apenas prob_node = true
			if evid[self.parents[0]] == 0:
				return [self.prob[0]]
			if evid[self.parents[0]] == 1:
				return [self.prob[1]]

		else: #caso com mais de 1 parent
			for i in range(0, len(self.parents)): #para cada parent
				for j in [0, 1]: # 2 probs dentro de cada parent
					if evid[self.parents[i]] == 0 and evid[self.parents[i+1]] == 0: # False, False
						print('0		0\n')
						return [1-self.prob[evid[self.parents[i]]][evid[self.parents[j]]],
							self.prob[evid[self.parents[i]]][evid[self.parents[j]]]]
					if evid[self.parents[i]] == 0 and evid[self.parents[j]] == 1: # False, True !nao funciona este!
						print('0		1\n')
						return [1-self.prob[evid[self.parents[i]]][evid[self.parents[j]]],
							self.prob[evid[self.parents[i]]][evid[self.parents[j]]]]
					if evid[self.parents[i]] == 1 and evid[self.parents[j]] == 0: # True, False
						print('1		0\n')
						return [1-self.prob[evid[self.parents[i]]][evid[self.parents[j]]],
							self.prob[evid[self.parents[i]]][evid[self.parents[j]]]]
					if evid[self.parents[0]] == 1 and evid[self.parents[1]] == 1: # True, True
						print('1		1\n')
						return [1-self.prob[evid[self.parents[i]]][evid[self.parents[j]]],
							self.prob[evid[self.parents[i]]][evid[self.parents[j]]]]

class BN():
	def __init__(self, gra, prob):
		pass

	def computePostProb(self, evid):
		pass
		return 0

	def computeJointProb(self, evid):
		pass

		return 0


		# else: #caso com mais de 1 parent
		# 	for i in range(0, len(self.parents)):
		# 		for j in range(0, len(self.parents)):
		# 			if evid[self.parents[i]] == 0 and evid[self.parents[j]] == 0: # False, False
		# 				pass
		# 			if evid[self.parents[i]] == 0 and evid[self.parents[j]] == 1: # False, True
		# 				pass
		# 			if evid[self.parents[i]] == 1 and evid[self.parents[j]] == 0: # True, False
		# 				pass
		# 			if evid[self.parents[0]] == 1 and evid[self.parents[1]] == 1: # True, True
		# 				pass
