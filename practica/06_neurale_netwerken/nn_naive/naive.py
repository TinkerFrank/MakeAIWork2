import math

# Define dimensions

nrOfRows = 3
nrOfColumns = 3
nrOfSymbols = 2

# Define general constants

weightGain = 0.005
costThreshold = 0.1

# Define relevant functions

def softMax (inVec):
    expVec = [math.exp (inScal) for inScal in inVec]
    aSum = sum (expVec)
    return [expScal / aSum for expScal in expVec]

def costFunc (outVec, modelVec):
    return sum ([(lambda x: x * x) (zipped [0] - zipped [1]) for zipped in zip (outVec, modelVec)])
    
# Define flow graph elements    
class Node:
    def __init__ (self):
        self.inLinks = []
        self.value = None
    
    def __call__ (self):
        if self.inLinks:
            # Compute value if there are input links, if there aren't assume it's an input node, whose value is explicitly set
            self.value = sum ([inLink () for inLink in self.inLinks])
            
        return self.value
    
class Link:
    def __init__ (self, inNode = None, outNode = None):
        self.inNode = inNode
        outNode.inLinks.append (self)
        
        self.weight = 1
        
    def adaptWeight (self, cost):
        self.weight += weightGain * cost * self.weight #weightgain = learningrat, cost = error
    
    def __call__ (self):
        return self.weight * self.inNode ()

# Instantiate 2 layers of nodes        
    
inNodes = [[Node () for iColumn in range (nrOfColumns)] for iRow in range (nrOfRows)]  
outNodes = [Node () for iSymbol in range (nrOfSymbols)]

# Build dataflow graph by connecting the nodes with links

links = []
for inRow in inNodes:
    for inNode in inRow:
        for outNode in outNodes:
            links.append (Link (inNode, outNode))

# Define symbols

symbolVecs = {'O': (1, 0), 'X': (0, 1)}
symbolChars = dict ((value, key) for key, value in symbolVecs.items ())           
          
# Define datasets (training set should normally be much larger than test set for best results)
          
trainingSet = (
    ((
        (1, 1, 1),
        (1, 0, 1),
        (1, 1, 1)
    ), 'O'),
    ((
        (0, 1, 0),
        (1, 0, 1),
        (0, 1, 0)
    ), 'O'),
    ((
        (0, 1, 0),
        (1, 1, 1),
        (0, 1, 0)
    ), 'X'),
    ((
        (1, 0, 1),
        (0, 1, 0),
        (1, 0, 1)
    ), 'X')
)

testSet = (
    ((
        (0, 1, 1),
        (1, 0, 1),
        (1, 1, 0)
    ), 'O'),
    ((
        (1, 0, 1),
        (1, 0, 1),
        (1, 1, 0)
    ), 'O'),
    ((
        (1, 0, 0),
        (1, 1, 1),
        (0, 0, 1)
    ), 'X'),
    ((
        (0, 0, 1),
        (1, 1, 1),
        (1, 0, 0)
    ), 'X')
)

# Compute average cost over all training items, with current weights

def computeAverageCost ():
    # Init accumulated cost
    accumulatedCost = 0
   
    # Accumulate cost over all training items
    for trainingItem in trainingSet:
    
        # Set input values for current trainingItem       
        for iRow in range (nrOfRows):
            for iColumn in range (nrOfColumns):
                inNodes [iRow][iColumn] .value = trainingItem [0][iRow][iColumn]
                
        # Accumulate cost, so compute sum of "error energy" over whole training set
        accumulatedCost += costFunc (softMax ([outNode () for outNode in outNodes]), symbolVecs [trainingItem [1]])
        
    # Divide accumulated cost by nr of training items to obtain average cost per training item
    # This makes the accumulated cost scale invariant with respect to the size of the training
    # Since the cost per training item <= 1, the average cost will be <= 1 
    return accumulatedCost / len (trainingSet)
    
# Learn with the aid of training set
    
averageCost = computeAverageCost ()
iterationIndex = 0
while averageCost > costThreshold:
    bestCostIncrease = 0
    bestLink = None
    
    # Try to adjust the most effective link weight (so no steepest descent, but just most 'sensitive' weight)
    for link in links:
        # Vary one weight
        link.adaptWeight (averageCost)
        
        newAverageCost = computeAverageCost ()
        costIncrease = newAverageCost - averageCost
       
        if abs (costIncrease) > abs (bestCostIncrease):
            bestCostIncrease = costIncrease
            bestLink = link
            
        # Undo weight variation (and go on varying next weight)          
        link.adaptWeight (-averageCost)
      
    # Apply most effective weight variation, but in the right direction
    bestLink.adaptWeight (-averageCost if bestCostIncrease > 0 else averageCost)
    averageCost = computeAverageCost ()
    print ('Iteration:', iterationIndex + 1, 'Average cost:', averageCost)
    
    iterationIndex += 1
    
# Apply what has been learned to test set
    
for testItem in testSet:
    # Set input values for current testItem       
    for iRow in range (nrOfRows):
        for iColumn in range (nrOfColumns):
            inNodes [iRow][iColumn] .value = testItem [0][iRow][iColumn]

    outVec = softMax ([outNode () for outNode in outNodes])
    print ('Offered as:', testItem [1], 'Reconstructed as:', symbolChars [(round (outVec [0]), round (outVec [1]))], ', probabilities : ', outVec)