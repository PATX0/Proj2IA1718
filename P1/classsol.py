import numpy as np
from sklearn import neighbors, datasets, tree, linear_model

from sklearn.externals import joblib
import timeit

from sklearn.model_selection import cross_val_score

consonants = chr(98)+chr(99)+chr(100)+chr(102)+chr(103)+chr(104)+chr(106)+chr(107)+chr(108)+chr(109)+chr(110)+chr(112)+chr(113)+chr(114)+chr(115)+chr(116)+chr(118)+chr(119)+chr(120)+chr(121)+chr(122)+chr(231)+chr(66)+chr(67)+chr(68)+chr(70)+chr(71)+chr(72)+chr(74)+chr(75)+chr(76)+chr(77)+chr(78)+chr(80)+chr(81)+chr(82)+chr(83)+chr(84)+chr(86)+chr(87)+chr(88)+chr(89)+chr(90)+chr(199)   # all consonants
vowels = chr(97)+chr(101)+chr(105)+chr(111)+chr(117)+chr(250)+chr(225)+chr(224)+chr(233)+chr(237)+chr(243)+chr(234)+chr(227)+chr(245)+chr(244)+chr(226)+chr(65)+chr(69)+chr(73)+chr(79)+chr(85)+chr(218)+chr(193)+chr(192)+chr(201)+chr(205)+chr(211)+chr(202)+chr(195)+chr(213)+chr(212)+chr(194)  # all vowels

normal_vowels = "aeiou"

def countLetters(word, letters): # Counts letters of word present in letters
    count = 0
    for i in word:
        if i in letters:
            count += 1
    return count

def features(X):
    
    F = np.zeros((len(X),5))
    for x in range(0,len(X)):
        F[x,0] = countLetters(X[x], vowels) # number of vowels
        F[x,1] = countLetters(X[x], consonants) # number of consonants
        F[x,2] = len(X[x])  # word size
        F[x,3] = 0#countLetters(X[x], "a") # occurences of letter "a"
        F[x,4] = countLetters(X[x], "o") # occurences of letter "o"

    return F     

def mytraining(f,Y):
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(f, Y)
    return clf
    
#def mytrainingaux(f,Y,par):
#    return clf

def myprediction(f, clf):
    Ypred = clf.predict(f)
    return Ypred

