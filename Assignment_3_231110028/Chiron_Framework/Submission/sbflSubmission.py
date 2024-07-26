#!/usr/bin/env python3

import argparse
import sys
import numpy as np
import math
sys.path.insert(0, "../ChironCore/")
from irhandler import *
from ChironAST.builder import astGenPass
import csv


def fitnessScore(IndividualObject):
    """
    Parameters
    ----------
    IndividualObject : Individual (definition of this class is in ChironCore/sbfl.py)
        This is a object of class Individual. The Object has 3 elements
        1. IndividualObject.individual : activity matrix.
                                    type : list, row implies a test
                                    and element of rows are components.
        2. IndividualObject.fitness : fitness of activity matix.
                                    type : float
        3. Indivisual.fitness_valid : a flag used by Genetic Algorithm.
                                    type : boolean
    Returns
    -------
    fitness_score : flaot
        returns the fitness-score of the activity matrix.
        Note : No need to set/change fitness and fitness_valid attributes.
    """
    # Design the fitness function
    fitness_score = 0
    activity_mat = np.array(IndividualObject.individual, dtype="int")
    activity_mat = activity_mat[:, : activity_mat.shape[1] - 1]
    #print(activity_mat)
    # Use 'activity_mat' to compute fitness of it.
    # ToDo : Write your code here to compute fitness of test-suite

    #Here we apply DDU Metric
    #first Calculate Density

    # Count the total number of elements
    total_elements = sum(len(sublist) for sublist in activity_mat)
    #print(total_elements)   

    # Initialize a variable to store the sum
    total_sum = 0

    # Iterate through the sublists and elements
    for sublist in activity_mat:
        for element in sublist:
            total_sum += element 
    
    #print(total_sum)
    # here total_elements must be a non_zero otherwise it will give divison by zero error.
    density =total_sum/total_elements


    #Now calculate Uniqueness
      
    # Convert each column to a tuple and use a set to find unique columns
    unique_columns = {tuple(column) for column in zip(*activity_mat)}

    # Convert the unique columns back to a list of lists
    unique_columns = [list(column) for column in unique_columns]

    # Find the total number of columns
    num_columns = len(activity_mat[0])
    
    #print(num_columns)
    #print(len(unique_columns))
    # here num_columns must be a non_zero otherwise it will give divison by zero error.
    uniqueness=len(unique_columns)/num_columns

    # Now calculate Diversity
    #All test cases in a test suite must be unique.

    unique_testcases_counts={}
    for row in activity_mat:
        testcase = tuple(row)
        if testcase in unique_testcases_counts:
            unique_testcases_counts[testcase] += 1
        else:
            unique_testcases_counts[testcase] = 1
    
    #print(unique_testcases_counts)
    s = 0 
    for testcase, count in unique_testcases_counts.items():
        s = s + (count * (count-1))

    N = (len(activity_mat) ) # Total Number of testcase in test suite
    #print(N)
    diversity = 1
    if(N!=1):
        diversity = (1-(s/(N*(N-1))))

    density_dash=1-abs(1-2*density)

    fitness_score=density_dash*uniqueness*diversity
    return -1*fitness_score


# This class takes a spectrum and generates ranks of each components.
# finish implementation of this class.
class SpectrumBugs:
    def __init__(self, spectrum):
        self.spectrum = np.array(spectrum, dtype="int")
        self.comps = self.spectrum.shape[1] - 1
        self.tests = self.spectrum.shape[0]
        self.activity_mat = self.spectrum[:, : self.comps]
        self.errorVec = self.spectrum[:, -1]

    def getActivity(self, comp_index):
        """
        get activity of component 'comp_index'
        Parameters
        ----------
        comp_index : int
        """
        return self.activity_mat[:, comp_index]

    def suspiciousness(self, comp_index):
        """
        Parameters
        ----------
        comp_index : int
            component number/index of which you want to compute how suspicious
            the component is. assumption: if a program has 3 components then
            they are denoted as c0,c1,c2 i.e 0,1,2
        Returns
        -------
        sus_score : float
            suspiciousness value/score of component 'comp_index'
        """
        sus_score = 0
        # ToDo : implement the suspiciousness score function.
        # Use list comprehension to extract the column
        column_data = [row[comp_index] for row in self.activity_mat]

        # Print the result
        #print("Extracted column:", column_data)
        #print(self.errorVec)

        Cf=0
        Cp=0
        Nf=0
        Np=0
        for i,j in zip(self.errorVec,column_data):
            if(i==1 and j==1):
                Cf=Cf+1
            if(i==0 and j==1):
                Cp=Cp+1
            if(i==1 and j==0):
                Nf=Nf+1
            if(i==0 and j==0):
                Np=Np+1

        if((math.sqrt((Cf+Nf)*(Cf+Cp)) )!=0):
            sus_score = ( Cf / (math.sqrt((Cf+Nf)*(Cf+Cp)) )) 
        else:
            sus_score=0
        return sus_score

    def getRankList(self):
        """
        find ranks of each components according to their suspeciousness score.

        Returns
        -------
        rankList : list
            ranList will contain data in this format:
                suppose c0,c1,c2,c3 are components and their ranks are
                1,2,3,4 then rankList will be :
                    [[c0,1],
                     [c1,2],
                     [c2,3],
                     [c3,4]]
        """
        rankList = []
        # Find the total number of columns
        num_columns = len(self.activity_mat[0])
        SuspeciousList=[]
        for i in range(0,num_columns):
            temp=[]
            temp = ['C' + str(i), self.suspiciousness(i)]
            #temp.append('C'+str(i))
            #temp.append(self.suspiciousness(i))
            SuspeciousList.append(temp)

        # Sort in descending order based on the second element of each inner list
        rankList = sorted(SuspeciousList, key=lambda x: x[1], reverse=True)
        #ranklist=
        count=1
        for i in range(0,len(rankList)-1):
            rankList[i].append(count)
            if rankList[i][1]==rankList[i+1][1]:
                continue
            else:
                count=count+1
        
        #if rankList[len(rankList)-1][1]==rankList[len(rankList)][1]:
             
        rankList[len(rankList)-1].append(count)
       
        print(self.activity_mat)
        print(self.errorVec)
        print(rankList)       
      

        #just remove the second one
        for item in rankList:
            print(type(item))
            del item[1]
        
        print("Following List contain components according to their rank(rank 1 is the highly suspecious to be buggy)")
        print(rankList)  
        #print(sorted_list_descending)
        # ToDo : implement rankList

        return rankList


# do not modify this function.
def computeRanks(spectrum, outfilename):
    """
    Parameters
    ----------
    spectrum : list
        spectrum
    outfilename : str
        components and their ranks.
    """
    S = SpectrumBugs(spectrum)
    rankList = S.getRankList()
    with open(outfilename, "w") as file:
        writer = csv.writer(file)
        writer.writerows(rankList)
