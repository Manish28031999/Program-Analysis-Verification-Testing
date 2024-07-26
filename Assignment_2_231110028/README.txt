First we generate testdata.json for both the programs
then we need to run symbSubmission.py engine to find the value of constant parameters if they exists.
We have to create one .kw(in my case eqtest2.kw which already stored in Submission folder) to run symbSubmission.py

Test Case 1 
        It takes two variable x,y and two constant parameters c1,c2
        first generate the testdata.json file for both programs and rename them as testData1.json and testData2.json(Assuming 
        user inside KachuaCore folder and programs inside example folder.)

        1.eqtest1.tl(with constant parameters)

         python ./kachua.py -t 100 -se ./example/eqtest1.tl -d '{\":x\": 5, \":y\": 100}' -c '{\":c1\": 1,\":c2\": 1}'

        2. eqtest2.tl(without any constant parameters)

          python ./kachua.py -t 100 -se ./example/eqtest2.tl -d '{\":x\": 5, \":y\": 100}' -c '{\":c1\": 1,\":c2\": 1}'
       
        then run symbSubmission.py engine by using following command
          python symbSubmission.py -b eqtest2.kw -e '[\"x\", \"y\"]'

Test Case 2
        It takes two variable x,y and two constant parameters c1,c2
        first generate the testdata.json file for both programs and rename them as testData1.json and testData2.json(Assuming 
        user inside KachuaCore folder and programs inside example folder.)

        1.Example1_p1.tl(with constant parameters)

         python ./kachua.py -t 100 -se ./example/Example1_p1.tl -d '{\":x\": 5, \":y\": 100}' -c '{\":c1\": 1,\":c2\": 1}'

        2. Example1_p2.tl(without any constant parameters)

          python ./kachua.py -t 100 -se ./example/Example1_p2.tl -d '{\":x\": 5, \":y\": 100}' -c '{\":c1\": 1,\":c2\": 1}'

        then run symbSubmission.py engine by using following command

          python symbSubmission.py -b eqtest2.kw -e '[\"x\", \"y\"]'
         
Test Case 3
        It takes three variable x,y,z and two constant parameters c1,c2
        first generate the testdata.json file for both programs and rename them as testData1.json and testData2.json(Assuming 
        user inside KachuaCore folder and programs inside example folder.)
       
        1.Example2_p1.tl(with constant parameters)
          python ./kachua.py -t 100 -se ./example/Example2_p1.tl -d '{\":x\": 5, \":y\": 100,\":z\": 100}' -c '{\":c1\": 1,\":c2\": 1}'
       
          
        2. Example2_p1.tl(without any constant parameters)
            python ./kachua.py -t 100 -se ./example/Example2_p2.tl -d '{\":x\": 5, \":y\": 100,\":z\": 100}' -c '{\":c1\": 1,\":c2\": 1}'
        

         then run symbSubmission.py engine by using following command

          python symbSubmission.py -b eqtest2.kw -e '[\"x\", \"y\",\"z\"]'

Test case 4
      
        It takes two variable x,y and two constant parameters c1,c2
        first generate the testdata.json file for both programs and rename them as testData1.json and testData2.json(Assuming 
        user inside KachuaCore folder and programs inside example folder.)

       1.Example3_p2.tl(with constant parameters)
          python ./kachua.py -t 100 -se ./example/Example3_p2.tl -d '{\":x\": 5, \":y\": 100,\":z\": 100}' -c '{\":c1\": 1,\":c2\": 1}'
       
       2.Example3_p1.tl(without constant parameters)
          python ./kachua.py -t 100 -se ./example/Example3_p1.tl -d '{\":x\": 5, \":y\": 100,\":z\": 100}' -c '{\":c1\": 1,\":c2\": 1}'
    
       then run symbSubmission.py engine by using following command
          python symbSubmission.py -b eqtest2.kw -e '[\"x\", \"y\"]'


Test case 5

         It takes four variable p,q,r,y and four constant parameters c1,c2,c3,c4
        first generate the testdata.json file for both programs and rename them as testData1.json and testData2.json(Assuming 
        user inside KachuaCore folder and programs inside example folder.)
     
        
       1.Example4_p1.tl(with constant parameters)
         python ./kachua.py -t 100 -se ./example/Example4_p1.tl -d '{\":p\": 5, \":q\": 100,\":r\": 100,\":y\": 100}' 
                 -c '{\":c1\": 1,\":c2\": 1,\":c3\": 1,\":c4\": 1}'

       2.Example4_p2.tl(without constant parameters)
         python ./kachua.py -t 100 -se ./example/Example4_p2.tl -d '{\":p\": 5, \":q\": 100,\":r\": 100,\":y\": 100}' 
                 -c '{\":c1\": 1,\":c2\": 1,\":c3\": 1,\":c4\": 1}'


         
        then run symbSubmission.py engine by using following command
          python symbSubmission.py -b eqtest2.kw -e '[\"p\", \"q\", \"r\", \"y\"]'


For Additional approach if we want to run then use following command
python AdditionalsymbSubmission.py -b eqtest2.kw -e '[\"x\", \"y\"]'   
        
        
       
        