import domains 
import letters
import Numbers
import Mario_Pyramids
import Email_validation

emails = [
    "ali@gmail.com",
    "sara@yahoo.com",
    "mohamed@outlook.com",
    "noha@iti.gov.eg"
    ]
domains.domains(emails)
print('*************************')
name = input(" Enter ur Name : ")
domains.valid_name(name)

print('-------------------------------------------------------------------------')
x = input("Enter a word: ")
letters.vowels_num(x)

print('*************************')

word = input("Enter a word: ")
letters.num_char(word)

print('-------------------------------------------------------------------------')

x = int(input(" enter a number : "))
Numbers.multiple_num(x)
print("i hope that u r happy with us")

print('*************************')

num = int(input(" enter a number : "))
Numbers.multi_number(num)

print('*************************')

print( Numbers.sorted_list())

print('-------------------------------------------------------------------------')

x = int(input(" enter a number : ")) 
Mario_Pyramids.Mar_pyramids(x)

print('*************************')

num_of_row = int(input(" Enter Numbers of Pyramids Number of : "))
Mario_Pyramids.pyramids_with_list(num_of_row)

print('-------------------------------------------------------------------------')

email= input("Enter ur email : ")
print(Email_validation.validemail(email))

print('*************************')

username = input("Enter ur username : ")
Email_validation.check(username)

print('*************************')

emails = [
    "ali@gmail.com",
    "sara@yahoo.com",
    "mohamed@outlook.com",
    "noha@iti.gov.eg"
    ]
validmails = list(filter(Email_validation.Validemail,emails))
print(validmails)

print('*************************')

trial_num = 5
for i in range(trial_num) :
    print(f"this is ur {i+1} out of {trial_num} chance honey")
    ur_email = input("Enter ur Email please : ")
    if Email_validation.valid_email(ur_email):
        break
else :
    raise "if u would like to be scammer please reach us out we almost here to learn"

print('-----------------------------------------------')