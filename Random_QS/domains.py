# You are given a list of email addresses in the format username@domain.Your task is to use the map() function along with a lambda
# domain part from each email address
def domains(emails):
    count = 0
    for i in emails :
        splitmail = i.split("@") 
        print(splitmail)
        count +=1 
    print(count)

    num_domain= map(lambda i : i.split("@")[1],emails)
    print(list(num_domain))

#-----------------------------------------------------------#

# Ask the user for his name then confirm that he has entered his name(not an empty string/integers). 
# then proceed to ask him for his email and print all this data 
def valid_name(name) :
    if name.strip() and not name.isdigit() and name :
        print("thank u for ur help with us")
    else :
        print(" not a valid name ")
