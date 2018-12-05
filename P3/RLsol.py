# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 20:31:54 2017

@author: mlopes
"""
import numpy as np

def Q2pol(Q, eta=5):
    pol = np.exp(eta*Q)/np.dot(np.exp(eta*Q),np.array([[1,1],[1,1]]))
    return pol

class myRL:

    def __init__(self, nS, nA, gamma):
        self.nS = nS
        self.nA = nA
        self.gamma = gamma
        self.Q = np.zeros((nS,nA))
        
    def traces2Q(self, trace):
        # implementar esta funcao
        self.Q = np.zeros((self.nS, self.nA))
        nQ = np.zeros((self.nS,self.nA))
        while True:            
            for tt in trace:
                nQ[int(tt[0]),int(tt[1])] = nQ[int(tt[0]),int(tt[1])] + 0.01 * (tt[3] + self.gamma * max(nQ[int(tt[2]),:]) - nQ[int(tt[0]),int(tt[1])])
            err = np.linalg.norm(self.Q-nQ)
            self.Q = np.copy(nQ)
            if err<1e-4:
                break        
        
        return self.Q
    
    def learnedTraj(self, fmdp):
        return fmdp.runPolicy(4,5,Q2pol(self.Q))[1]
