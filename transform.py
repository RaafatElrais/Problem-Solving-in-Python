import pandas as pd
df = pd.read_csv(r'E:\ITI ismailia\python\day5\transform as CSV\Emails.csv')
# define a function to validate an email that entered with user : 
def validemail(email) :

    if "@" in email and "." in email :
        new_list = email.split("@")
        if  not new_list[0]   :
            return False    
        elif '.' == new_list[1][-1] or '@' ==  new_list[1][-1] :
            return False
        elif  '.' == new_list[1][0]  :
            return False
        else :       
            return True
    else :
        return False
    
email = df.head(60)
validemail_with_set= set(email for email in df['Email'] if validemail(email) == True) 
domains_list_set= set(email.split('@')[1] for email in validemail_with_set )
print(domains_list_set)
count = 0
for i in domains_list_set :
    count +=1
print(f'number of unique domains is {count}') 