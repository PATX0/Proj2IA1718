# Grupo 56 - Tiago Soares 78658; Goncalo Correia 83897;
# Projecto 2 IA 18-19
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 15:51:49 2018

@author: mlopes
"""
import sys
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
						return [1-self.prob[evid[self.parents[i]]][evid[self.parents[j]]],
							self.prob[evid[self.parents[i]]][evid[self.parents[j]]]]
					if evid[self.parents[i]] == 0 and evid[self.parents[j]] == 1: # False, True !nao funciona este!
						return [1-self.prob[evid[self.parents[i]]][evid[self.parents[j]]],
							self.prob[evid[self.parents[i]]][evid[self.parents[j]]]]
					if evid[self.parents[i]] == 1 and evid[self.parents[j]] == 0: # True, False
						return [1-self.prob[evid[self.parents[i]]][evid[self.parents[j]]],
							self.prob[evid[self.parents[i]]][evid[self.parents[j]]]]
					if evid[self.parents[0]] == 1 and evid[self.parents[1]] == 1: # True, True
						return [1-self.prob[evid[self.parents[i]]][evid[self.parents[j]]],
							self.prob[evid[self.parents[i]]][evid[self.parents[j]]]]



class BN():
	def __init__(self, gra, prob): #prob = lista de nodes
		self.gra = gra
		self.prob = prob

	def computePostProb(self, evid):
		pass
		return 0

	def computeJointProb(self, evid):
		jp = 1
		p = Node([0], [])
		for node in self.prob:
			p = node.computeProb(evid)
			jp = jp * float((1-p[0]))
		return jp


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
# gra = [[],[],[0,1],[2],[2]]
# ev = (1,1,1,1,1)
#
# p1 = Node( np.array([.001]), gra[0] )                   # burglary
# print( "p1 false %.4e p1 true %.4e" % (p1.computeProb(ev)[0] , p1.computeProb(ev)[1]))
#
# p2 = Node( np.array([.002]), gra[1] )                   # earthquake
#
# p3 = Node( np.array([[.001,.29],[.94,.95]]), gra[2] )   # alarm
# print( "p1 = 1, p2 = 1, p3 false %.4e p3 true %.4e" % (p3.computeProb(ev)[0] , p3.computeProb(ev)[1]))
#
# p4 = Node( np.array([.05,.9]), gra[3] )                 # johncalls
#
# p5 = Node( np.array([.01,.7]), gra[4] )                 # marycalls
# prob = [p1,p2,p3,p4,p5]
#
# gra = [[],[],[0,1],[2],[2]]
# bn = BN(gra, prob)
