import PLC_functions as plc
import PLC_filecreate as fc
import time

"""
Note : Enter the path according to your requirements
"""

data = [[127 , 220 , 0 , 0 , 0 , 1 , 1095] , [22 , 240 , 0 , 0 , 0 , 0 , 1708] , [115 , 264 , 0 , 0 , 0 , 0 , 2046] , [33 , 200 , 1 , 1 , 1 , 0 , 3106] , [45 , 209 , 0 , 1 , 0 , 1, 2925] , [35 , 189 ,0 , 0 , 0 , 0 , 2008 ] , [135 , 172 , 0 , 0 , 0, 0 , 700] , [69 , 233 , 0 , 0 , 0 , 0 , 1300] , [91 , 280 , 1 , 0 , 0 , 0 , 2121] , [88 , 245 , 0 , 0 , 0, 0 , 4320] ]

#Key = [ temp , voltage , vibr , condensation , EMI , pollution , MTBF]


a = 1

while(a):

 time.sleep(1)
 #To read the option selected by the user
 dest = 'C:\\Users\\Sahil Basera\\Desktop\\PLC\\'
 name = 'user_inputdata.txt'

 f = open(dest+name , 'r')

 a = int(f.read()) - 1
 f.close()


 #To call temperature prediction function and store result in text file
 T = plc.temppredict(data[a][0])
 fc.createtempfile(T[0])



 #to call voltage prediction function and store result in text file
 V = plc.voltagepredict(data[a][1])
 fc.createvoltagefile(V[0])



 #To call vibration determination function and store result in text file
 Vi = data[a][2]
 fc.createvibrationfile(Vi)


 #To call condensation determination function and store result in text file
 Co = data[a][3]
 fc.createcondensationfile(Co)


 #To call emi determination function and store result in text file
 EMI = data[a][4]
 fc.createemifile(EMI)



#To make pollution determination and store result in a text file
poll = data[a][5]
fc.createpollutionfile(poll)


#To make mtbf determination and store results in a text file
mtbf = data[a][6]
fc.createmtbffile(mtbf)
fc.dispmtbffile(mtbf)

#To make final virtue determination and store results in  text file
fc.finalvirtue(T[0] , V[0])




