from datetime import datetime
from cs1033_evaluator import evaluate_L6_E2

def days_to_birthday(date):
    '''
    Calculates the number of days that have passed since the 1st of January 
    to the given date.

    :param date: A date string in the format of yyyy-mm-dd
    :return: The number of days to the date from 1st of January 
             (eg: date->2021-01-01, return->1)
    '''

    # Convert the date string to a datetime object
    datetime_object = datetime.strptime(date, "%Y-%m-%d")

    # Extract only the date and remove the timestamp
    date = datetime_object.date()

    # Find the number of days since the begining of the year
    num_days = date.timetuple().tm_yday

    return num_days


# Please do not edit anything above this line.
################################################################################


# Your code should be included here. 
# You may use the days_to_birthday(date) function in your solution.



##################### End of the programme #####################################
file_name=input()   #get the file name
open_file=open(file_name,'r')     # to open the fie
num=open_file.read()    # to close the file
open_file.close()   # to close the file
user_data=num.split("\n")  # split the user data
indivual_data=[i.split(' ') for i in user_data]  #iterate to get indivual data
file=open('output.txt','a')
count_year=[[],[]]   # to count the entrance of year
for i in indivual_data: 
        num_days=days_to_birthday(i[1])  
        num_days=f'{num_days:03}' 
        DOB_parts=i[1].split("-") # spliting the DOB
        NIC=DOB_parts[0]
        if(i[2]=='F'):    # check wether Female 
            num_days=int(num_days)+500
        if(DOB_parts[0] in count_year[0]):
            index1=count_year[0].index(DOB_parts[0])
            count_year[1][index1]=count_year[1][index1]+1
        else:
            count_year[0].append(DOB_parts[0])
            count_year[1].append(1)
        
        NIC=str(NIC)+str(num_days)+f'{count_year[1][count_year[0].index(DOB_parts[0])]:03}'  # final NIC no 
        final_data=i[0]+' '+ NIC+'\n' # NIC no respective to user's name
        file.write(final_data) #write the final the data
file.close()   # close the file
        
        
        
        ################################################################################
# Please do not edit anything below this line.
evaluate_L6_E2()