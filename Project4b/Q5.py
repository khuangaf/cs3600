import Testing
from Testing import testCarData
from Testing import testPenData
from Testing import average
from Testing import stDeviation
from NeuralNetUtil import buildExamplesFromCarData,buildExamplesFromPenData
from NeuralNet import buildNeuralNet
import cPickle 
from math import pow, sqrt



if __name__ == "__main__":
    pAccuracy = []
    cAccuracy = []
    
    for i in range(5):
        nnet, p = testPenData()
        nnet, c = testCarData()
        pAccuracy.append(p)
        cAccuracy.append(c)
    
    print "PenData:"
    print "Max = " + str(max(pAccuracy)) 
    print "Average = " + str(average(pAccuracy))
    print "SD = " + str(stDeviation(pAccuracy))
    print "CarData:"
    print "Max = " + str(max(cAccuracy)) 
    print "Average = " + str(average(cAccuracy))
    print "SD = " + str(stDeviation(cAccuracy))
    
