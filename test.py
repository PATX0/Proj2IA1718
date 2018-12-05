from BN import *


def sum():
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
