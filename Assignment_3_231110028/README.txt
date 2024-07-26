Total  5 test cases.

general command to run 


 $  python ./chiron.py --SBFL ./example/sbfl1.tl --buggy ./example/sbfl1_buggy.tl -vars '[":x", ":y", ":z"]' --timeout 10 --ntests 20 --popsize 100 --cxpb 1.0 --mutpb 1.0 --ngen 100 --verbose True

  #we can change -ngen parameter value to run it for more iteration
1. sbfl2.tl and sbfl2_buggy.tl (with 2 variable x,y)
  

 command to run:python ./chiron.py --SBFL ./example/sbfl2.tl --buggy ./example/sbfl2_buggy.tl -vars '[\":x\", \":y\"]' --timeout 10 --ntests 20 --popsize 10 --cxpb 1.0 --mutpb 1.0 --ngen 10 --verbose True

2. s3.tl and s3_buggy.tl (with 3 variable x,y,z)
    
   command to run:python ./chiron.py --SBFL ./example/s3.tl --buggy ./example/s3_buggy.tl -vars '[\":x\", \":y\",\":z\"]' --timeout 10 --ntests 20 --popsize 10 --cxpb 1.0 --mutpb 1.0 --ngen 10 --verbose True

3. s4.tl and s4_buggy.tl (with 2 variable x,y)
    
   command to run:python ./chiron.py --SBFL ./example/s4.tl --buggy ./example/s4_buggy.tl -vars '[\":x\", \":y\"]' --timeout 10 --ntests 20 --popsize 10 --cxpb 1.0 --mutpb 1.0 --ngen 10 --verbose True


4. s5.tl and s5_buggy.tl (with 2 variable x,y)
    
   command to run:python ./chiron.py --SBFL ./example/s5.tl --buggy ./example/s5_buggy.tl -vars '[\":x\", \":y\"]' --timeout 10 --ntests 20 --popsize 10 --cxpb 1.0 --mutpb 1.0 --ngen 10 --verbose True

5. s6.tl and s6_buggy.tl (with 3 variable x,y,z)
   command to run :python ./chiron.py --SBFL ./example/s6.tl --buggy ./example/s6_buggy.tl -vars '[\":x\", \":y\", \":z\"]' --timeout 10 --ntests 20 --popsize 10 --cxpb 1.0 --mutpb 1.0 --ngen 10 --verbose True