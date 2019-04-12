import random as rd
import math as mt

rd.seed(1)

class Net:

    def train(self, dataset, iterations, learning_rate):
        w1 = rd.random()
        w2 = rd.random()
        b = rd.random()
        for i in range(iterations):
            ri = rd.randint(0, len(dataset) - 1)
            label = dataset[ri]

            z = label[0] * w1 + label[1] * w2 + b
            pred = self.sigmoide(z)
                
            target = label[2]
            dcost_dpred = 2 * (pred - target)

            dcost_dz = dcost_dpred * self.sigmoide_p(z)
                
            dcost_dw1 = dcost_dz * label[0]
            dcost_dw2 = dcost_dz * label[1]
                
            w1 -= learning_rate * dcost_dw1
            w2 -= learning_rate * dcost_dw2
            b -= learning_rate * dcost_dz
	    
        
        return w1, w2, b
      
    def sigmoide(self, t):
	    return 1 / (1 + mt.exp(-t))

    def sigmoide_p(self, t):
	    return self.sigmoide(t) * (1 - self.sigmoide(t))

    def RN(m1, m2):
        return self.sigmoide(m1*w1 + m2*w2 + b)

    def result(self, pred):
        if pred < 0.33:
            print("vittoria in casa")
        elif pred < 0.66:
            print("pareggio")
        else:
            print("vittoria fuori casa")

