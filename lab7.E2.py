import os 
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/configs/"
import matplotlib.pyplot as plt
from cs1033_evaluator import evaluate_lab7

MODEL_1_INPUT_FILE, MODEL_2_INPUT_FILE, MODEL_3_INPUT_FILE = input().split()
################################################################################
# Please do not edit anything above this line.


# Function to read a file and return speed list.
def get_speed(file_name):
    speed = []
################## YOUR CODE STARTS HERE. ######################################
# Read the file and get the values into the list.
    file=open(file_name,'r')  # to open the file in reading mode
    speed_data=file.read()
    file.close()     # to close the file
    data=speed_data.split("\n") #split the speed_data by line
    data=[i.split() for i in data] # split the data by the space
    ################## YOUR CODE ENDS HERE. ########################################     
    for i in range(len(data)):
        if(len(data[i])!=0):
            speed.append(int(data[i][1]))   #append the speed to list
    return speed


# Function gets the filename and returns the speeds in metres per second format.
def convert_kmph_to_ms(filename):
################## YOUR CODE STARTS HERE. ######################################
# Read the values using get_speed function and return the converted values as a list.
    speed=get_speed(filename)  #to call the get_speed function
    speeds = [round((i)*(1000/3600),4) for i in speed]    #to change spped value in ms^-1
    return speeds
################## YOUR CODE ENDS HERE. ########################################

# Function gets the speeds as a list of integers in metres per second format and returns the acceleration.
def get_acceleration(speeds):
    #Acceleration list is initialized to zero.
    #i.e. acceleration at time=0 is zero.
    acceleration = [0]
################## YOUR CODE STARTS HERE. ######################################
    #Write the code to calculate the acceleration.    
    for i in range(len(speeds)):
        if(i>0):  
            acceleration.append(round((speeds[i]-speeds[i-1])/0.1,2))   # append the acceleration
    
################## YOUR CODE ENDS HERE. ########################################
    return acceleration  # to return acceleration 
######## WRITE THE CODE FOR TASK 1.4 and 1.5 BELOW #############################

        # Use MODEL_1_INPUT_FILE, MODEL_2_INPUT_FILE, MODEL_3_INPUT_FILE variable 
        # names instead of 'model1.txt', 'model2.txt', 'model3.txt' to read files
model_list=[MODEL_1_INPUT_FILE, MODEL_2_INPUT_FILE, MODEL_3_INPUT_FILE]  #assign all files to a list
file=open('max_acceleration.txt','a')  # to open the file in appending mode
acceleration_list=[]
for i in model_list:   # iterate the files ,which is in the list
    speeds=convert_kmph_to_ms(i)  #to call then convert_kmph_to_ms fucntion
    acceleration=get_acceleration(speeds)  # to call get_acceleration fucntion
    acceleration_list.append(acceleration)
    maximum_acceleration=max(acceleration)  # get the maximum value of accleration
    file.write(f"model{model_list.index(i)+1} {maximum_acceleration}\n")  # to write the data
    
file.close()    # to close the file

# Plotting the lines with different styles
# plt.plot(time, model_acceleration[0] , label='model_1')      
x=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
# Adding labels and title
plt.xlabel('Time(s)')
plt.ylabel('Acceleration(ms-2)')
plt.title('Acceleration Vs Time')
plt.plot(x,acceleration_list[0],color='pink')
plt.plot(x,acceleration_list[1],color='blue')
plt.plot(x,acceleration_list[2],color='yellow')
plt.show()

################################################################################
# Please do not edit anything below this line.
evaluate_lab7()

##################### End of the programme #####################################