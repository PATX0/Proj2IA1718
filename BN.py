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
		self.evid = 1


	def computeProb(self, evid): #evid = evidencia |info atual sobre cada uma das variaveis(0:false 1:true)
		"""precisa da evid dos parents e devolve [prob_node = false, prob_node = true]"""
		if self.parents == []: #se nao tem parents
			return [1-self.prob[0], self.prob[0]]

		if len(self.parents) == 1: #se apenas tiver 1 parent apresenta apenas prob_node = true
			if evid[self.parents[0]] == 0:
				return [self.prob[0]]
			if evid[self.parents[0]] == 1:
				return [self.prob[1]]

		else: #caso com mais de 1 parent , evid = (x,x,x,x,x) !!!!FORCED!!!! ---> caso com +2 pais ?????
			a = evid[self.parents[0]] # evid do no do 1 pai
			b = evid[self.parents[1]]
			return [1-self.prob[a][b], self.prob[a][b]]

class BN():
	def __init__(self, gra, prob): #prob = lista de nodes
		self.gra = gra
		self.prob = prob

	def computePostProb(self, evid):
		pp = 0
		aux = []
		evidNode(self.prob, evid)
		for node in self.prob:
			if node.evid == 0:
				pass
			elif node.evid == 1:
				pass
			elif node.evid == []:
				pass
			elif node.evid == -1:
				pass
		return 0 #P(X|e) | X  = var a posteriori , e = evid

	def computeJointProb(self, evid):
	""" ex: P(j,m,a,b,e) = P(j|a)*P(m|a)*P(a|b,e)*P(b)*P(e)
	prob do joao e da maria ligarem sabendo que o alarme tocou devido a um burglary e um earthquake"""
		jp = 1
		ni = 0
		for node in self.prob:
			node.evid = evid[ni] #atribui evid a cada no' respectivo
			p = node.computeProb(evid)
			print(p)
			if len(p)>1: #caso onde nao tem parents ou tem +1 parent
				if node.evid == 1:#case true queremos p[1 ]= prob de no ser true
					jp = jp * float(p[1])
				elif node.evid == 0:#case false queremos p[0 ]= prob de no ser false
					jp = jp * float(p[0])
			else: #so tem um parent , so tem [prob = true]
				jp = jp * float(p[0])

			ni = ni+1

		return jp

def evidNode(lst, ev):
	ni=0
	for node in lst:
		node.evid = ev[ni]
		ni = ni + 1
		print(node.evid)


def sumProbs(): #test function
	gra = [[],[],[0,1],[2],[2]]
	p1 = Node(np.array([.001]), gra[0])
	p2 = Node(np.array([.002]), gra[1]) # earthquake
	p3 = Node(np.array([[.001,.29],[.94,.95]]), gra[2])
	p4 = Node(np.array([.05,.9]), gra[3]) # johncalls
	p5 = Node(np.array([.01,.7]), gra[4])
	prob = [p1,p2,p3,p4,p5] # marycalls
	gra = [[],[],[0,1],[2],[2]]
	bn = BN(gra, prob)
	jp = []
	for e1 in [0,1]:
		for e2 in [0,1]:
			for e3 in [0,1]:
				for e4 in [0,1]:
					for e5 in [0,1]:
						jp.append(bn.computeJointProb((e1, e2, e3, e4, e5)))
	print(sum(jp))


def jProb(): #test function computeJointProb
	gra = [[],[],[0,1],[2],[2]]
	p1 = Node(np.array([.001]), gra[0])
	p2 = Node(np.array([.002]), gra[1]) # earthquake
	p3 = Node(np.array([[.001,.29],[.94,.95]]), gra[2])
	p4 = Node(np.array([.05,.9]), gra[3]) # johncalls
	p5 = Node(np.array([.01,.7]), gra[4])
	prob = [p1,p2,p3,p4,p5] # marycalls
	gra = [[],[],[0,1],[2],[2]]
	bn = BN(gra, prob)
	jp = []
	x3 = bn.computeJointProb((1,1,1,1,1))
	x2 = bn.computeJointProb((1,0,1,1,1))
	x1 = bn.computeJointProb((0,1,1,1,1))
	x = bn.computeJointProb((0,0,1,1,1))
	y3 = bn.computeJointProb((1,1,0,1,1))
	y2 = bn.computeJointProb((1,0,0,1,1))
	y1 = bn.computeJointProb((0,1,0,1,1))
	y = bn.computeJointProb((0,0,0,1,1))
	print(x)
	print(x1)
	print(x2)
	print(x3)
	print(y)
	print(y1)
	print(y2)
	print(y3)
			#
			# else: #caso com mais de 1 parent
			# 	for i in range(0, len(self.parents)): #para cada parent
			# 		for j in [0, 1]: # 2 probs dentro de cada parent
			# 			if evid[self.parents[i]] == 0 and evid[self.parents[i+1]] == 0: # False, False
			# 				return [1-self.prob[evid[self.parents[i]]][evid[self.parents[j]]],
			# 					self.prob[evid[self.parents[i]]][evid[self.parents[j]]]]
			# 			if evid[self.parents[i]] == 0 and evid[self.parents[j]] == 1: # False, True
			# 				return [1-self.prob[evid[self.parents[i]]][evid[self.parents[j]]],
			# 					self.prob[evid[self.parents[i]]][evid[self.parents[j]]]]
			# 			if evid[self.parents[i]] == 1 and evid[self.parents[j]] == 0: # True, False
			# 				return [1-self.prob[evid[self.parents[i]]][evid[self.parents[j]]],
			# 					self.prob[evid[self.parents[i]]][evid[self.parents[j]]]]
			# 			if evid[self.parents[0]] == 1 and evid[self.parents[1]] == 1: # True, True
			# 				return [1-self.prob[evid[self.parents[i]]][evid[self.parents[j]]],
			# 					self.prob[evid[self.parents[i]]][evid[self.parents[j]]]]
			# aux = []
			# l = len(self.parents)
			# for i in range(0, l): #para cada parent
