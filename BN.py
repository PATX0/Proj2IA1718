# Grupo 56 - Tiago Soares 78658; Goncalo Correia 83897;
# Projecto 2 IA 18-19
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 15:51:49 2018

@author: mlopes
"""
import sys
import numpy as np
import itertools as it

# 		  B	  E     A	  J	   M
#gra = [ [], [], [0,1], [2], [2] ]
class Node():
	def __init__(self, prob, parents = []): #prob = [pFalse, pTrue]
		self.parents = parents
		self.prob = prob
		self.evid = 0


	def computeProb(self, evid): #evid = evidencia |info atual sobre cada uma das variaveis(0:false 1:true)
		"""precisa da evid dos parents e devolve [prob_node = false, prob_node = true]"""
		p = 0
		if self.parents == []: #se nao tem parents
			return [1-self.prob[0], self.prob[0]]

		if len(self.parents) == 1: #se apenas tiver 1 parent apresenta apenas prob_node = true
			if evid[self.parents[0]] == 0:
				return [self.prob[0]]
			if evid[self.parents[0]] == 1:
				return [self.prob[1]]

		else: #caso com mais de 1 parent , evid = (x,x,x,x,x) !!!!FORCED!!!! ---> caso com +2 pais ?????
			for i in range(0, len(self.parents)):
				pai = self.parents[i]
				e = evid[pai]
				if e == 0:
					p = self.prob[e][0]
				elif e == 1:
					p = self.prob[e][1]

				#p = self.prob[pai][e]
			return [(1-p), p]
class BN():
	def __init__(self, gra, prob): #prob = lista de nodes
		self.gra = gra
		self.prob = prob

	def computePostProb(self, evid): #(-1, [], [], 1, 1)
		"""P(X | e) = a | P(X, e) = a * SOMATORIO(P(X, e, y))
	X = var a-posteriori y = vars desconhecidas, e  = vars conhecidas
	Soma de JointProbabilities(evid das desconhecidas 0 e 1)"""
		pp = 0
		jp = 0
		ppRet = 0
		lst_idx = processaEvid(evid)
		lst_evs = possEvid(lst_idx, evid)
		for evs in lst_evs:
			jp = jp + self.computeJointProb(evs)

		return jp #P(X|e) | X  = var a posteriori , e = evid

	def computeJointProb(self, evid):
		""" ex: P(j,m,a,b,e) = P(j|a)*P(m|a)*P(a|b,e)*P(b)*P(e)
	prob do joao e da maria ligarem sabendo que o alarme tocou devido a um burglary e um earthquake"""
		jp = 1
		ni = 0
		evidNode(self.prob, evid) #atribui evid aos nos
		for node in self.prob:
			p = node.computeProb(evid)
			if len(p)>1: #caso onde nao tem parents ou tem +1 parent
				if node.evid == 1:#case true queremos p[1 ]= prob de no ser true
					jp = jp * float(p[1])
				elif node.evid == 0:#case false queremos p[0 ]= prob de no ser false
					jp = jp * float(p[0])
			else: #so tem um parent , so tem [prob = true]
				if node.evid == 1:
					jp = jp * float(p[0])
				elif node.evid == 0:
					jp = jp * float(1-p[0])


		return jp

def evidNode(lst, ev): #atribui evid a cada no' respectivo
	ni=0
	for node in lst:
		node.evid = ev[ni]
		ni = ni + 1

def processaEvid(evid): #retorna lista de indices das vars desconhecidas
	lst = []
	for i in range(0, len(evid)):
		if evid[i] == []:
			lst.append(i)
	return lst

def possEvid(lstEv, ev): #retorna lista de evs possiveis
	lstPoss = []
	newEv = [];	newEv1 = []; newEv2 = []; newEv3 = []
	newEv4 = []; newEv5 = []; newEv6 = []; newEv7 = []
	for i in range(0, len(ev)): #create list with evs to manipulate
		if ev[i] == -1:
			newEv.append(1); newEv1.append(1)
			newEv2.append(1); newEv3.append(1)
			newEv4.append(0); newEv5.append(0)
			newEv6.append(0); newEv7.append(0)
		else:
			newEv.append(ev[i]); newEv1.append(ev[i])
			newEv2.append(ev[i]); newEv3.append(ev[i])
			newEv4.append(ev[i]); newEv5.append(ev[i])
			newEv6.append(ev[i]); newEv7.append(ev[i])

	#g = 0; h = 1; i = 0; j = 1; k = 0; l = 1
	a = 0; b = 1; c = 0; d = 1; e = 0; f = 1

	for idx in lstEv:
		newEv[idx] = a; newEv4[idx] = a
		newEv1[idx] = b; newEv5[idx] = b
		newEv2[idx] = c; newEv6[idx] = c
		newEv3[idx] = f; newEv7[idx] = f
		c = d; f = e

	if len(lstEv)==1:
		lstPoss.append(tuple(newEv)); lstPoss.append(tuple(newEv1))
		lstPoss.append(tuple(newEv4)); lstPoss.append(tuple(newEv5))
		return lstPoss

	if len(lstEv) == 2:
		lstPoss.append(tuple(newEv)); lstPoss.append(tuple(newEv1))
		lstPoss.append(tuple(newEv2)); lstPoss.append(tuple(newEv3))
		lstPoss.append(tuple(newEv4)); lstPoss.append(tuple(newEv5))
		lstPoss.append(tuple(newEv6)); lstPoss.append(tuple(newEv7))
		return lstPoss



def sumProbs(): #test function
	gra = [[],[],[0,1],[2],[2]]
	p1 = Node(np.array([.001]), gra[0])
	p2 = Node(np.array([.002]), gra[1]) # earthquake
	p3 = Node(np.array([[.001,.29],[.94,.95]]), gra[2])
	p4 = Node(np.array([.05,.9]), gra[3]) # johncalls
	p5 = Node(np.array([.01,.7]), gra[4])
	prob = [p1,p2,p3,p4,p5] # marycalls
	bn = BN(gra, prob)
	jp = []
	for e1 in [0,1]:
		for e2 in [0,1]:
			for e3 in [0,1]:
				for e4 in [0,1]:
					for e5 in [0,1]:
						jp.append(bn.computeJointProb((e1, e2, e3, e4, e5)))
	print(sum(jp))


def jProb2():
	gra2 = [[],[0],[0],[1,2]]
	ev= (1,1,1,1)

	pp1 = Node( np.array([.5]), gra2[0] )# cloudy
	print( "pp1 false %.4e pp1 true %.4e" % (pp1.computeProb(ev)[0] , pp1.computeProb(ev)[1]))

	pp2 = Node( np.array([.5,.1]), gra2[1] )# sprinkler
	print(float(pp2.computeProb(ev)[0]))
	pp3 = Node( np.array([.2,.8]), gra2[2] )# rain

	pp4 = Node( np.array([[.0,.9],[.9,.99]]), gra2[3] )# wetgrass
	print( "pp2 = 1, pp3 = 1, pp4 false %.4e pp4 true %.4e" % (pp4.computeProb(ev)[0] , pp4.computeProb(ev)[1]))

	prob2 = [pp1,pp2,pp3,pp4]
	#
	bn2 = BN(gra2, prob2)
	#
	jp = []
	for e1 in [0,1]:
		for e2 in [0,1]:
			for e3 in [0,1]:
				for e4 in [0,1]:
					jp.append(bn2.computeJointProb((e1, e2, e3, e4)))

	print("sum joint %.3f (1)" % sum(jp))
	#
	#
	 ### Tests to joint Prob
	ev = (0,0,0,0)
	print( "joint %.4g (0.2)" % bn2.computeJointProb(ev) )

	ev = (1,1,1,1)
	print( "joint %.4g (0.0396)" % bn2.computeJointProb(ev) )
	#

	### Tests to post Prob
	# P(e1|e4=1)
	ev = (-1,[],[],1)
	print("ev : ")
	print(ev)
	print( "post : %.4g (0.5758)" % bn2.computePostProb(ev)  )

	# # P(e4|e1=1)
	ev = (1,[],[],-1)
	print("ev : ")
	print(ev)
	print( "post : %.4g (0.7452)" % bn2.computePostProb(ev)  )

	 # P(e1|e2=0,e3=0)
	ev = (-1,0,0,[])
	print("ev : ")
	print(ev)
	print( "post : %.4g (0.3103)" % bn2.computePostProb(ev)  )


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
	for e1 in [0,1]:
		for e2 in [0,1]:
			for e3 in [0,1]:
				for e4 in [0,1]:
					for e5 in [0,1]:
						jp.append(bn.computeJointProb((e1, e2, e3, e4, e5)))
	print("sum joint %.3f (1)" % sum(jp))

	ev = (-1,[],[],1,1)
	print(ev)
	print( "post : %.4g (0.2842)" % bn.computePostProb(ev))
	ev = ([],-1,[],1,1)
	print(ev)
	print( "post : %.3f (0.176)" % bn.computePostProb(ev))
	ev = ([],0,1,-1,[])
	print(ev)
	print( "post : %.3f (0.900)" % bn.computePostProb(ev))

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


# 	else: #caso com mais de 1 parent , evid = (x,x,x,x,x) !!!!FORCED!!!! ---> caso com +2 pais ?????
# 			a = evid[self.parents[0]] # evid do no do 1 pai
# 			b = evid[self.parents[1]]
# return [1-self.prob[a][b], self.prob[a][b]]
