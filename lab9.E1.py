import os 
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/configs/"
from cs1033_evaluator import evaluate_lab9
import matplotlib.pyplot as plt

def voltage(R1,R2,Vin):  # to calculate the output voltage 
    return (Vin*(R2/(R1+R2)))
def power(R1,R2,Vin):  #to calculate the power dissipation 
    return ((Vin**2)/(R1+R2))
input_file_name = input()  # Open and read the input file
file=open(input_file_name ,'r')   #open the file
data=file.read()  # read the file
file.close()  # close the file
info=data.split('\n')  # split the data by line
info=[i.split(',') for i in info]  # split the info by ','
Vin=float(info[0][0]) # get v input
Vout=float(info[0][1]) # get vout
tolerance=float(info[0][2]) #get tolerance 
min_p=float('inf')  # Initialize the minimum power to infinity
for i in range(len(info[1])):
    for j in  range(len(info[1])):
        if(i!=j): # Ensure R1 and R2 are different
         # Convert the resistor values to float
            R1=float(info[1][i])
            R2=float(info[1][j])
            v_get=voltage(R1,R2,Vin)   # Calculate the output voltage
            if(v_get-tolerance<=Vout<=v_get+tolerance):   # Check if the calculated voltage is within the tolerance range
                p_get=power(R1,R2,Vin)     # Calculate the power dissipation for this pair
                if(p_get<=min_p):     # check  minimum power 
                    min_p=p_get
                    suitable_R1,suitable_R2=int(R1),int(R2)
                    
file=open('output.txt','w')      #Open the output file in write mode
file.write(f'{suitable_R1}, {suitable_R2}')
file.close()
import matplotlib.pyplot as plt
def graph(R1,R2):
    y_axis=[]
    x_axis=[]
    for RL in range(0,1010,10):
        r=(R2*RL/(R2+RL))
        V_new=(12*(r/(R1+r)))
        x_axis.append(RL)
        y_axis.append(V_new)
    return y_axis,x_axis
y,x=graph(204,150)


plt.plot(x,y)
plt.xlabel('Resistance (ohms)')
plt.ylabel('Volatge (V)')
plt.title('Volatge vs Resistance')
plt.show()
# Your code should be included here. 
# Avoid using the print function in the code, as it may cause errors


################################################################################
# Please do not edit anything below this line.
evaluate_lab9()

##################### End of the programme #####################################