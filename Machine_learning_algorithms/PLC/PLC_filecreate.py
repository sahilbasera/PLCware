import datetime

"""
This Python program creates text files and stores/extracts data from it
for interfacing purposes
NOTE : Adjust Paths according to your preferred locations 
"""


#This stores the temperature predictions in a text file 


def createtempfile(a):
    dest = 'C:\\Users\\Sahil Basera\\Desktop\\PLC\\'
    name = 'Prediction_tempdata.txt'
    
    #To add results in the test file  

    f = open(dest+name , 'w')
    f.write(str(a) + '\n')
    f.close()
   


#This stores the voltage predictions in a text file

def createvoltagefile(a):
    dest = 'C:\\Users\\Sahil Basera\\Desktop\\PLC\\'
    name = 'Prediction_voltagedata.txt'

    #To add results in the text file
    
    f = open(dest+name , 'w')
    f.write(str(a) + '\n')
    f.close()

# This stores the condensation , emi predictions in a text file

def createcondensationfile(condensation) :
    dest =  'C:\\Users\\Sahil Basera\\Desktop\\PLC\\'
    name = 'Prediction_condensationdata.txt'

    #To add results in a test file

    f = open(dest+name , 'w')

    if(condensation == 1):
        f.write('Present\n')
        
    elif (condensation == 0) :
        f.write('Absent\n')
    f.close()   

def createemifile(emi) :
    dest =  'C:\\Users\\Sahil Basera\\Desktop\\PLC\\'
    name = 'Prediction_emidata.txt'

    #To add results in a test file

    f = open(dest+name , 'w')

    if(emi == 1) :
        f.write('Present\n')
        
    if(emi == 0) :
        f.write('Absent\n')

    f.close()
    
def createvibrationfile(vibration):
    dest =  'C:\\Users\\Sahil Basera\\Desktop\\PLC\\'
    name = 'Prediction_vibrationdata.txt'

    #To add results in a test file

    f = open(dest+name , 'w')

    if(vibration == 1):
        f.write('Significant\n')

    elif(vibration == 0) :
        f.write('Negligible\n')

    f.close()
     
def createpollutionfile(pollution):
    dest =  'C:\\Users\\Sahil Basera\\Desktop\\PLC\\'
    name = 'Prediction_pollutiondata.txt'

    #To add results in a test file

    f = open(dest+name , 'w')

    if(pollution == 1):
        f.write('Significant\n')

    elif(pollution == 0) :
        f.write('Negligible\n')

    f.close()
     
def createmtbffile(mtbf):

 dest = 'C:\\Users\\Sahil Basera\\Desktop\\PLC\\'
 name = 'Prediction_MTBFremdaysdata.txt'

 f = open(dest+name , 'w')

 now = datetime.datetime.now()
 rdays = mtbf - 653

 f.write(str(rdays))
 f.write('\n')
 f.close()

def dispmtbffile(mtbf) :
 dest = 'C:\\Users\\Sahil Basera\\Desktop\\PLC\\'
 name = 'Prediction_MTBFuserdata.txt'

 f = open(dest+name , 'w')
 f.write(str(mtbf))
 f.close()
def finalvirtue(temppred , voltpred ):
 dest = 'C:\\Users\\Sahil Basera\\Desktop\\PLC\\'
 name = 'Prediction_virtuedata.txt'

 f = open(dest+name , 'w')
 if (temppred == 100 or voltpred == 100) :
  Z = 100
 else :
  Z = temppred*0.6 + voltpred*0.4
 f.write(str(Z))
