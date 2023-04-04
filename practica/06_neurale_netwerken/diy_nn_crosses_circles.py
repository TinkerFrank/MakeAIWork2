import random
import math

cross = [[1,0,1],
         [0,1,0],
         [1,0,1]]

circle = [[1,1,1],
          [1,0,1],
          [1,1,1]]

unfinished = [[1,0,1],
              [0,0,0],
              [1,0,1]]

#honestly just checking for position 2,2 in the 3x3 matrix should already give a good baseline accuracy
X_train = [ [[1,1,1],
            [1,0,1],
            [1,1,1]],

           [[0,1,0],
            [1,0,1],
            [0,1,0]],
    
           [[1,0,1],
            [0,1,0],
            [1,0,1]],

           [[0,1,0],
            [1,1,1],
            [0,1,0]],
         ]

#where 1 = cross and 0 = circle
y_train=[[0,0,1,1]]


'''Begin met een directe, intuitieve implementatie met behulp van de zelf te onwerpen
klassen Node en Link, de softmax function aan de uitgangs-laag en het back-
propagation algorithm, gebruikmakend van willekeurige variaties van de weight factors.
Varieer 1 weight factor per leercyclus over de hele trainingset en behoud alleen de
wijziging die gemiddeld over deze cyclus het beste scoort. Gebruik de mean squared
error als cost function'''


#decided to skip node-link in favor of building own matrix class

class Matrix:

    def __init__(self, input):
        self.input = input
        self.rows = len(self.input)
        self.cols = len(self.input[0])
    
    def shape(self):
        shape = [self.rows, self.cols]
        return(shape)
    
    def getArray(self): #better to name value so matrix.value
        return(self.input)

    def getvalue(self,i,j): #matrices start at 1,1 arrays start at 0,0
        if (i>0 and j>0):
            value = self.input[i-1][j-1]
            return(value)
        else:
            print('out of bounds value request, matrices start at 1,1')

    def flatten(self):
        flatmatrix = [[item for i in self.input for item in i]]  #list comprehension > for loops
        return(Matrix(flatmatrix))

    
    def flat_transpose(self):
        flat = [[item for i in self.input for item in i]]  #list comprehension > for loops
        flat_t = [[row[i] for row in flat] for i in range(len(flat[0]))]
        #list(map(list, zip(*weightsMatrix.flatten()))) #mapping > list comprehension > for loops, functions > objects, haskell way
        return(Matrix(flat_t))


    def __mul__(self, b):   
        
        if (self.cols == b.rows):
            #initiate resultmatrix and populate with zeros
            resultMatrix = [[0 for i in range(b.cols)] for j in range(self.rows)] 
            #fill resultmatrix with dot product values
            for row in range(self.rows):
                for col in range(b.cols):
                    for i in range(self.cols):
                        resultMatrix[row][col] += self.input[row][i]*b.input[i][col]
            return(resultMatrix)
        else:   
            return(print('not multiplicable'))

#generate a matrix containing the weights (2x (1x9), classification) using a random function
def rndarray(amount):
    #random.seed(42)
    array=[round(random.uniform(0,1),2) for i in range(amount)]
    return (array)

weightsMatrix = Matrix([rndarray(9),rndarray(9)])

def initializeBias():
    return random.uniform(0, 1)


# Input: 3x3 matrix
# Output: 2x1 matrix
def predict_class(inputMatrix):
    print("Weight Matrix Shape:", weightsMatrix.shape())
    # Flatten and transpose inputmatrix
    transposedinputMatrix = inputMatrix.flat_transpose()
    print("Transposed Input Shape:", transposedinputMatrix.shape())
    the2nodevalues =  Matrix(weightsMatrix*transposedinputMatrix)
    print("Node Values:", the2nodevalues.getArray())
    # Apply activation function sigmoid (binary)
    flatnodes =  the2nodevalues.flatten().getArray()[0]
    activationvalues = map(lambda x: round(1/(1+math.exp(-x)),2), flatnodes) 
    # converting to list, evaluated on demand 
    av = list(activationvalues)
    print('Sigmoid Binary Activation values:',av)
    if (softmax(flatnodes)[0]>0.5):
        return(1)
    else:
        return(0)

def softmax(x):
    exp_x = [math.exp(i) for i in x]
    sum_exp = sum(exp_x)
    return [es / sum_exp for es in exp_x]


print(predict_class(Matrix(circle)))

def train(self, training_inputs, labels):
       for inputs, label in zip(training_inputs, labels):
           prediction = predict_class(inputs)
           error = label - prediction
            # recalculate weights
           for i in range(len(inputs)):
               self.weights[i] += error * inputs[i] * self.learning_rate

           self.bias += error * self.learning_rate

#train(X_train,y_train) 





class Perceptron:
    def __init__(self, w, learning_rate):
        self.weights = w
        self.bias = 0
        self.learning_rate = learning_rate

    def predict(self, inputs):
        # Calculate weighted sum of inputs
        weighted_sum = sum([self.weights[i] * inputs[i] for i in range(len(inputs))]) + self.bias
        # # Apply sigmoid activation function
        # return(1 / (1 + math.exp(-weighted_sum)))
        # softmax
        explist = [math.exp(input) for i in input]
        sum_explist = sum(explist)
        return(explist/sum_explist)
    



    def train(self, training_inputs, labels):
        for inputs, label in zip(training_inputs, labels):
            prediction = self.predict(inputs)
            error = label - prediction

            # recalculate weights
            for i in range(len(inputs)):
                self.weights[i] += error * inputs[i] * self.learning_rate

            self.bias += error * self.learning_rate


class test:
    def __init__(self) -> None:
        pass
