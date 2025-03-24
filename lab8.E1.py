from cs1033_evaluator import evaluate_lab8
# Please do not edit anything above this line.
################################################################################

import math
# Your code should be included here. 
# You should define and use the analyseSeriesCircuit(), analyseParallelCircuit() functions in your solution.
def analyseParallelCircuit(data):  #function to analyze a parallel circuit
    Angular_frequnecy=2*math.pi*float(data[5])  #to find angular frequency
    ZL=Angular_frequnecy*float(data[2])/1000    #to get the inductive reactance
    ZC=1/(Angular_frequnecy*float(data[3])/1000000)    # to find the capacitive reactance
    Ztotal=1/((1/float(data[1]))**2+((1/ZL-1/ZC)**2))**(1/2)   # to get total impedance
    I=float(data[4])/Ztotal   # current value
    angle=math.degrees(math.atan((1/ZL-1/ZC)*float(data[1]))) #phase angle
    return round(ZL,1),round(ZC,1),round(Ztotal,1),round(I,1),round(angle,1) 

def analyseSeriesCircuit(data):    #function to analyze a series circuit
    Angular_frequnecy=2*math.pi*float(data[5])   #to find angular frequency
    ZL=Angular_frequnecy*float(data[2])/1000     #to get the inductive reactance
    ZC=1/(Angular_frequnecy*float(data[3])/1000000)    # to find the capacitive reactance
    Ztotal=((float(data[1]))**2 + (ZL-ZC)**2)**(1/2)    # to get total impedance
    I=float(data[4])/Ztotal           # current value
    angle=math.degrees(math.atan((ZL-ZC)/int(data[1])))   #phase angle
    return round(ZL,1),round(ZC,1),round(Ztotal,1),round(I,1),round(angle,1) 

# Read the input file name
File_name = input()  # read input file
file = open(File_name, 'r')  # open file in read mode
info = file.read()  # read the file
file.close()  # close the file

list_out_line = info.split('\n')  # split into a list
data_list = [i.split(' ') for i in list_out_line ]  # split by space and ensure no empty lines

# Open result.txt in write mode
file_=open('result.txt', 'w') 
for induvidual_data in data_list:
    if induvidual_data[0] == 'series':  # check whether series or not
        ZL, ZC, Ztotal, I, angle = analyseSeriesCircuit(induvidual_data)  # call series function
    else:
        ZL, ZC, Ztotal, I, angle = analyseParallelCircuit(induvidual_data)  # call parallel function
    final = f"{ZL} {ZC} {Ztotal} {I} {angle}\n"  # create the output line
    file_.write(final)  # write to file
file_.close()  # close the file
################################################################################
# Please do not edit anything below this line.
evaluate_lab8()

##################### End of the program #####################################