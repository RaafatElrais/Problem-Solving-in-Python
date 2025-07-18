# Write a program that generate a multiplication table from 1 to the number passed 

def multiple_num(y) :
    for i in range(y+1):
        for j in range(1,i+1) :
            print(f"{j}x{i} = {j*i} ")



#--------------------------------------------------------------#

#  Write a program that generate a multiplication table from 1 to the number passed.

def multi_number(x) :
    My_list=[]
    for i in range(1,x+1):
        temp=[]
        for j in range(1,i+1) :
            
            temp.append(j*i)
        My_list.append(temp)

    print(My_list)

num = int(input(" enter a number : "))
multi_number(num)

#-----------------------------------------------------#

#Fill an array of 5 elements from the user, Sort it in descending and ascending orders then display the output

def sorted_list():

    new_list=[]
    y = int(input("How Many Num that u wanna add : "))
    for i in range (y):
        x= int(input(" Enter a Number That u Wanna add it in ur new list : "))
        list.append(x)
    ascending_order = sorted(new_list) 
    decending_order = sorted(new_list,reverse = True)
    return ascending_order,decending_order