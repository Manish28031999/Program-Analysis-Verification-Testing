from kast import kachuaAST
import sys
import numpy as np
from z3 import *
sys.path.insert(0, "KachuaCore/interfaces/")
from interfaces.fuzzerInterface import *
sys.path.insert(0, '../KachuaCore/')

# Each input is of this type.
#class InputObject():
#    def __init__(self, data):
#        self.id = str(uuid.uuid4())
#        self.data = data
#        # Flag to check if ever picked
#        # for mutation or not.
#        self.pickedOnce = False
        
class CustomCoverageMetric(CoverageMetricBase):
    # Statements covered is used for
    # coverage information.
    def __init__(self):
        super().__init__()

    # TODO : Implement this
    def compareCoverage(self, curr_metric, total_metric):
        # must compare curr_metric and total_metric
        # True if Improved Coverage else False
        print("current coverage ::: ",curr_metric)
        print("total coverage ::: ",total_metric)
        for i in range(0,len(curr_metric)):
            if(curr_metric[i] not in total_metric):
                return True
        # True if Improved Coverage else False
        return False

    # TODO : Implement this
    def updateTotalCoverage(self, curr_metric, total_metric):
        # Compute the total_metric coverage and return it (list)
        # this changes if new coverage is seen for a
        # given input.
        temp1=np.array(total_metric)
        temp2=np.array(curr_metric)
        union=np.union1d(temp1,temp2)
        total_metric=union
       # total_metric = list(set(total_metric) | set(curr_metric))
       # print("updated total is ::: ",total_metric)
        return total_metric

class CustomMutator(MutatorBase):
    def __init__(self):
        pass

    # TODO : Implement this
    def mutate(self, input_data, coverageInfo, irList):

        
        # Mutate the input data and return it
        # coverageInfo is of type CoverageMetricBase
        # Don't mutate coverageInfo
        # irList : List of IR Statments (Don't Modify)
        # input_data.data -> type dict() with {key : variable(str), value : int}
        # must return input_data after mutation.

         min_num_input = -500
         max_num_input = 500
         def even_mutation(input_data):
             random_number = np.random.randint(1,32)
             mask=1<<random_number
             for i in (input_data.data.keys()):
                 input_data.data[i]=-input_data.data[i]^mask
                 test = np.random.randint(1,1000)
                 if(test%2==0):
                     input_data.data[i]=-input_data.data[i]
                 else:
                     input_data.data[i]=2*input_data.data[i]

         def odd_mutation(input_data):
             random_number1 = np.random.randint(-500,500)
             random_number2 = np.random.randint(-500, 500)
             mask=random_number1^random_number2
             for i in (input_data.data.keys()):
                 input_data.data[i]=input_data.data[i]^mask
                 test = np.random.randint(1,1000)
                 if(test%2==0):
                     input_data.data[i]=-input_data.data[i]
                 else:
                     input_data.data[i]=2*input_data.data[i]
                 
 
             

        # Mutation of 3rd type :- (Choosing from some interesting numbers as input values)

       
       
        # Now, randomly chosing any one of three mutatiors in each fuzz iteration.(Giving more priority to first two mutators as compared to the third mutator.)

         test = np.random.randint(1,1000)
         if(test%2==0):
            even_mutation(input_data)
        
         else:
            odd_mutation(input_data)

         print("Percentage of IR Statements Covered = " , (len(coverageInfo.total_metric))*100/(len(irList)+1),"%")
         return input_data



# Reuse code and imports from
# earlier submissions (if any).
