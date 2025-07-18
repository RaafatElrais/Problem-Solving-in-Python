# . Write a program that build a Mario pyramid like below:

def Mar_pyramids(x) :

    for i in range(1,x+1) :
        print(" " * (x-i),"*" * i)
        
#-----------------------------------------------------------------
# create mario pyramids with a list 

def pyramids_with_list(x) :
    My_list=[]
    for i in range(1,x+1) :
        My_list.append(" ")
    print(My_list)
    print('--------------------------------')
    for i in range(1,x+1):
        My_list.append("*")
        My_list.remove(' ')
        print(My_list)
