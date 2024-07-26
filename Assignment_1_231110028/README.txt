
Inside Chiron-framework folder we have two folders KachuaCore and Submission.Inside submission KachuaCore we have example folder where all 
5 test cases are stored and in submission folder we have fuzzsubmission.py in which we have define all 3 function.

we have 5 test cases
all test case are store in example folder which is present in kachua core folder


1st testcase is task2.tl which has 4 inputs
to run this use the following command:

kachua.py -t 30 --fuzz -d{':x':200,':y':220,':m':140,':d':60} ./example/task2.tl

2nd testcase is task4.tl which has 2 inputs
to run this use the following command:
kachua.py -t 30 --fuzz -d{':x':200,':y':220} ./example/task4.tl

3rd testcase is task5.tl which has 2c inputs
to run this use the following command:
kachua.py -t 40 --fuzz -d{':x':200,':y':220} ./example/task5.tl


4th testcase is task6.tl which has 3 inputs
to run this use the following command:
kachua.py -t 40 --fuzz -d{':x':200,':y':220,':z':60} ./example/task6.tl

5th testcase is task7.tl which has 2 inputs
to run this use the following command:
kachua.py -t 40 --fuzz -d{':x':200,':y':220} ./example/task7.tl
