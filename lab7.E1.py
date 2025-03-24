def output_value(i):
    p=float(i[3])*10**3 # get the load in Newtons
    L=float(i[0])  #get the length
    E=float(i[1])*10**9 #get the  Young's modulus
    I=float(i[2]) #get the  moment of inertia
    D_max=f"{(p*(L**3))/(48*E*I):.6f}" # detremine the maximum deflection to given beam
    S_max=f"{(p*L)/(4*I):.2f}"  # detremin the maximum bending stress to given beam
    L=f"{L:.1f}"
    return L,D_max,S_max 
input_file=input()  #get input for file name
file=open(input_file,'r') # to open file
data=file.read()   # to read file
file.close   # to close the file
list_out_line=data.split('\n')  # split the data by line
data_list=[i.split(' ') for i in list_out_line]  #split data by sapce
Beam_number=1    #for count the no of beams
for individual_data in data_list:  #to iterate the data
    L,D,S=output_value(individual_data)   #call the function to get the output
    print("Beam",str(Beam_number)+":","Length:",L,"m,","Max Deflection:",D,"m,","Max Bending Stress:",S,"Pa") #output the given format
    Beam_number+=1 # to count next beam number
    