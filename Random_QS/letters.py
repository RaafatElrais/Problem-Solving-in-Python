# This program counts the number of vowels in a given word.
# It considers 'a', 'u', 'i', 'o', and 'e'
def vowels_num(z) :
    count = 0
    y= 'auioe'
    for i in z:
        if i in y:
            count += 1
        else :
            continue 
    print(count) 

#-------------------------------------------------------------------#

# This program counts up the 'i' in a given word.
def num_char(y) :
    count=0
    for i in range(len(y)):
        if y[i] == "i":
            count+=1
        else :
            continue
        print(f"index number {i} and the number of I is {count}")
