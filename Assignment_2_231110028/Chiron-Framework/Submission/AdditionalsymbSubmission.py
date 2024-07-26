import re
import ast
import numpy as np
from z3 import *
import argparse
import json
import sys

sys.path.insert(0, '../KachuaCore/')

from sExecutionInterface import *
import z3solver as zs
from irgen import *
from interpreter import *
import ast
import fnmatch

def example(s):
    # To add symbolic variable x to solver
    s.addSymbVar('x')
    s.addSymbVar('y')
    # To add constraint in form of string
    s.addConstraint('x==5+y')
    s.addConstraint('And(x==y,x>5)')
    # s.addConstraint('Implies(x==4,y==x+8')
    # To access solvers directly use s.s.<function of z3>()
    print("constraints added till now",s.s.assertions())
    # To assign z=x+y
    s.addAssignment('z','x+y')
    # To get any variable assigned
    print("variable assignment of z =",s.getVar('z'))

def checkEq(args,ir):
    # Loading the json file and load the complete program in testData1 and program with some unknown constant parameters in testData2
    file1 = open("../Submission/testData2.json","r+")
    file2 = open("../Submission/testData1.json","r+")
    testData1=json.loads(file1.read())
    testData2=json.loads(file2.read())


    s = Solver()

    #testData2 = convertTestData(testData2)
    exp=[]
    # Initialize the condition
    tmp = BoolVal(True)

    # Iterate through the test cases

    round=0
    output_variable = {'x': 'o1', 'y': 'o2', 'z': 'o3'}
    #define all the output variable name
    o1=Int('o1')
    o2=Int('o2')
    o3=Int('o3')
    
    #define all the variables and unknown constant parameters 
    x = Int('x')
    y = Int('y')
    z =  Int('z')
    c1 = Int('c1')
    c2 = Int('c2')  
    c3 = Int('c3')
    exp = BoolVal(True)
   
    #stored the input and output of first test case to form test suite
    results = []
    for (test_case_id, test_case_data) in (testData1.items()):
    
        params = test_case_data["params"]
        symb_enc = test_case_data["symbEnc"]
        params2 = ast.literal_eval(params)
        symb_enc2 = ast.literal_eval(symb_enc)

        updated_values = []
        for key, expression in symb_enc2.items():
            updated_value= eval(expression, params2)
            # print(updated_values)
            updated_values.append(updated_value)
        results.append(updated_values)
    

    # now we convert the testData2.json to Program_2_logic
    for key, testcase_data in testData2.items():
        symb_enc = eval(str(testcase_data["symbEnc"]))
        constraints = eval(str(testcase_data["constraints"]))
        
        exp_bool = BoolVal(True)
        if(len(constraints)>1):
            for i in range(len(constraints)):
                if(i==0):
                    exp_bool=And(True,constraints[i])
                else:
                    exp_bool=And(exp_bool,constraints[i])
        else:
            exp_bool=And(True,constraints[0])

        tr = BoolVal(True)
        pattern = "c*"
        count=0
        for (key, value), (key2, value2) in zip(output_variable.items(), symb_enc.items()):
            if fnmatch.fnmatch(value2,pattern):
                continue
            else:

                if count==0:
                    tr=And(True,eval(value)==eval(value2))
                    count=count+1
                else:
                    tr=And(tr,eval(value)==eval(value2))



            
        
        
        if(round==0):
            Program_2_logic = And(True, Implies(exp_bool, tr))
            round=round+1
        else:
            Program_2_logic = And(Program_2_logic, Implies(exp_bool, tr))

        
    #stored all the inputs with AND condition on input set and store all them in a list   
    expressions_list = []

    # Iterate through the JSON data
    for key, data in testData1.items():
        params_str = data.get("params", "{}")
        params_dict = ast.literal_eval(params_str)

        test_case_expressions = []
        #this is the limitation of this code that we only extract only x and y
        variables_to_extract = ['x', 'y']
        for var_name in variables_to_extract:
            if var_name in params_dict:
                var_value = params_dict[var_name]
                var = Int(var_name)
                expr = var == var_value
                test_case_expressions.append(expr)

        test_case_expression = And(*test_case_expressions)

        expressions_list.append(test_case_expression)
    # here we are taking outputs of testsuite modified them from x to o1 and y to o2 then do AND of both of them
    count=0
    for key, value in testData2.items():
        conditions = []
        var_counter = 1
        for sublist in results:
            sublist_conditions = []
            
            for value in sublist:
                if var_counter <= 2: #Here 2 specify to fetch x and y only
                    var_name = 'o' + str(var_counter)
                    var = Int(var_name)
                    constraint = var == value
                    sublist_conditions.append(constraint)
                
                var_counter += 1 
            var_counter=1
            sublist_condition = And(sublist_conditions)
            conditions.append(sublist_condition)


       #Now we make the final logic as mention in the step4
        count=0
        Final_Logic=BoolVal(True)
        Cases=BoolVal(True)
        
        for i,j in zip(conditions,expressions_list):
            Cases=Implies(j,And(Program_2_logic,i))
            if(count==0):
                Final_Logic=And(True,Cases)
                count=count+1
            else:
                Final_Logic=And(Final_Logic,Cases)
    print(Final_Logic)
    s.add(Final_Logic)
    
    
    result = s.check()


    if result == sat:
        model = s.model()
        x_value = model[x].as_long()
        y_value = model[y].as_long()
        c1_value = model[c1].as_long()
        c2_value = model[c2].as_long()

        print("both programs are equivalent and Satisfying values:")
        print("c1 =", c1_value)
        print("c2 =", c2_value)
    else:
        print("both programs are not equivalent.")

if __name__ == '__main__':
    cmdparser = argparse.ArgumentParser(
        description='symbSubmission for assignment Program Synthesis using Symbolic Execution')
    cmdparser.add_argument('progfl')
    cmdparser.add_argument(
        '-b', '--bin', action='store_true', help='load binary IR')
    cmdparser.add_argument(
        '-e', '--output', default=list(), type=ast.literal_eval,
                               help="pass variables to kachua program in python dictionary format")
    args = cmdparser.parse_args()
    ir = loadIR(args.progfl)
    checkEq(args,ir)
    exit()
