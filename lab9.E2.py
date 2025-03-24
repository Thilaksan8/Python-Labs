import re
from cs1033_evaluator import evaluate_lab9
level_0_list,level_1_list,level_2_list,level_3_list,level_4_list=[],[],[],[],[] # Global lists for each contamination level
def level(n,m):
    global level_0_list,level_1_list,level_2_list,level_3_list,level_4_list
    S_count,O_count,Na_count,Mg_count,Cl_count=0,0,0,0,0   # Initialize element counts
    for i in n:   # Count the occurrences of each relevant element
        if(i[0]=='S'):S_count+=i[1]  ##get total S_count
        if(i[0]=='O'):O_count+=i[1]  #get total O_count
        if(i[0]=='Na'):Na_count+=i[1]  #get total Na_count
        if(i[0]=='Mg'):Mg_count+=i[1]  #get total Mg_count
        if(i[0]=='Cl'):Cl_count+=i[1]  ##get total Cl_count
    if(S_count>=1 and O_count>=4 and Na_count>=1):  # Check conditions for Level 1
        S_count-=1 #get total S_count
        O_count-=4  #get total O_count
        Na_count-=1 #get total Na_count
        if((S_count>=1 and O_count>=3 and Mg_count>=1) or (O_count>=2 and Cl_count>=3)):level_4_list.append(m)  # If it satisfies Level 1 and also check other levels
        else:level_1_list.append(m) # append the contain into level_1 list
    elif(S_count>=1 and O_count>=3 and Mg_count>=1): # Check conditions for Level 2
        O_count-=3 # get current O count
        if( (O_count>=2 and Cl_count>=3)):level_4_list.append(m) # Check if it also satisfies Level 3
        else:level_2_list.append(m)  # append the contain into level_2 list
    elif(O_count>=2 and Cl_count>=3):level_3_list.append(m) # Check conditions for Level 1 if yes append to level_3_list
    else:level_0_list.append(m) # append the contain into level_0 list
    return level_0_list,level_1_list,level_2_list,level_3_list,level_4_list   #return the level datas
def write_file(file_name,chemical):
    file=open(file_name,'w') #open the file to write level data
    for i in chemical:file.write(i+'\n') #write the level data by line
    file.close() #close the file
INPUT_FILE_NAME = input() #get input file
file=open(INPUT_FILE_NAME,'r') #open file in read mode
data=file.readlines()  # get the all lines to data
file.close()  # close the file
data=[i.split() for i in data] # split the data by space in each line
for contaminant,chemical_formula in data:  # iterate the data
    matches=re.findall(r'([A-Z][a-z]*)(\d*)', chemical_formula) # Use regex to parse the chemical formula into elements and their counts
    elements_counts=[]  # create a list for count of elements
    for element,count in matches: #iterate the matches
        count = int(count) if count else 1  # get integer count values
        elements_counts.append([element, count])    #append the element,count to elements_counts
    level_0_list,level_1_list,level_2_list,level_3_list,level_4_list=level(elements_counts,contaminant) # Call the level function to classify the chemical
write_file('Level_0.txt',level_0_list)    #write the level_0
write_file('Level_1.txt',level_1_list)    #write the level_1
write_file('Level_2.txt',level_2_list)    #write the level_2
write_file('Level_3.txt',level_3_list)    #write the level_3
write_file('Level_4.txt',level_4_list)    #write the level_4
################################################################################
# Do not change anything above this line
################################################################################

# Enter your code here
# Use INPUT_FILE_NAME variable to read the file instead of 'contamination_analysis.txt'

    
################################################################################
# Do not change anything below this line.
evaluate_lab9()