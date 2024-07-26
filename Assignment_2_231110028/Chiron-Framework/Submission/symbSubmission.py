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
    #load the testData.json for both the files
    file1 = open("../Submission/testData1.json","r+")
    file2 = open("../Submission/testData2.json","r+")
    testData1=json.loads(file1.read())
    testData2=json.loads(file2.read())
    s = zs.z3Solver()
    for key1 in testData1.keys():
        for key2 in testData2.keys():
            if(testData1[key1]['params']==testData2[key2]['params']):
                json_params_string1 = testData1[key1]['params'].replace("'", "\"")
                json_params_string2 = testData2[key2]['params'].replace("'", "\"")
                json_string1 = testData1[key1]['symbEnc'].replace("'", "\"")
                json_string2 = testData2[key2]['symbEnc'].replace("'", "\"")
                d1 = eval(json_string1)
                d2 = eval(json_string2)
                d3 = eval(json_params_string1)
                d4 = eval(json_params_string2)
                for key in d3.keys():
                    t=key
                    #print(t)
                    s.addSymbVar(f'{t}')
                for key in d3.keys():
                    t=key
                    s.addConstraint(f"{d1[f'{t}']}=={d2[f'{t}']}")


    res=s.s.check()
    print(res)
    if str(res)=="sat":
        print("both programs are  equivalent")
        m=s.s.model()
        print(m)
    else:
        print("both programs are not  equivalent")


    print("-------")
    #print(testData)
    file1.close()
    file2.close()
    # s.addSymbVar('x')
    # s.addSymbVar('y')
    # s.addSymbVar('c1')
    # s.addSymbVar('c2')
    # s.addConstraint('x+c1'==d)
    # s.addConstraint(d1['y']==d2['y'])

   
    #testData = convertTestData(testData)
    #print(testData)
    # output = args.output
    # example(s)
    # TODO: write code to check equivalence


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
