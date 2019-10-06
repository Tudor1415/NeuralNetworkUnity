# from ..Math.LinearAlgebra.Matrix import Matrix
class ANNNeuron:
    def __init__(self, weights, activation):
        self.weights = weights
        self.weightedSum = self.weightedSum()
        if activation:
            self.output = self.getActivation(activation)
        else:
            self.output = self.weightedSum

    def __str__(self):
        return f"The output of this neuron is {self.output} !"

    def getActivation(self, activation):
        if activation == "sigmoid":
            return 1 / (1 + 2.718281828**(-1*self.weightedSum))
        elif activation == "tanh":
            return 1-(2/(1 + 2.718281828**(2*self.weightedSum)))
        else:
            return eval(activation.replace("x", str(self.weightedSum)))

    def weightedSum(self):
        r = 0
        for i in self.weights:
            r += i[1] * i[0]
        return r

class ANNLayer:
    def __init__(self, layerType="Dense", neurons=0, activation=None, weights=[], dropoutValue=0, id=0):
        self.layerType = layerType
        self.neuronsNumber = neurons
        self.activation = activation
        self.neurons = self.getNeurons()
        self.weights = weights
        self.id = id

    def getNeurons(self):
        return [ANNNeuron(self.weights, self.activation) for _ in range(self.neuronsNumber)]

    def getMatrixOutput(self):
        return [i.output for i in self.neurons]

    def __str__(self):
        return f"The {self.id} layer has {self.neuronsNumber} neurons !"

class ANN:
    def __init__(self, *layers):
        self.network = layers

    def add(self, l):
        if isinstance(l, layer):
            self.network.append(l)


neuron1 = ANNNeuron([[5,4],[3,2],[1,0]], activation="sigmoid")
print(neuron1)
layer1 = ANNLayer(neurons = 3, weights = [[5,4],[3,2],[1,0]], activation="sigmoid")
print(layer1)
