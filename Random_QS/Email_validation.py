# define a function to validate an email that entered with user : 
def validemail(email) :

    if "@" in email and "." in email :
        new_list = email.split("@")
        if  not new_list[0]   :
            print("invalid email")
            return False    
        elif '.' in new_list[1][-1] or '@' in new_list[1][-1] :
            print("invalid email")
            return False
        elif  '.' in new_list[1][0]  :
            print("invalid email")
            return False
        else :       
            print ("valid email")
            return True
    else :
        return False


#-----------------------------------------------------------------------------#

# make sure that the clients will enter a valid email to appear to their the second step which is enter ur pass.
#  if not happened we will exit the system 

def check(username):
    users=[

        { "name" : "raiis" ,"pass" : "12345"} ,   
            { "name" : "ali" , "pass" : "24685"}
    ]  
    
    for key in users :
        if username == key["name"] :
            pass1 = input("enter ur pass : ")
            if pass1 == key["pass"] :
                print("thanks for verifyng ur account ")
                break
            else:
                break
        else : 
            continue
    else :
        exit()

#-----------------------------------------------------------------------#

def Validemail(email) :
    if "@" in email and "." in email :
        new_list = email.split("@")
        if  not new_list[0]   :
            print("invalid email")
            return False    
        elif '.' in new_list[1][-1] or '@' in new_list[1][-1] :
            print("invalid e8mail")
            return False
        elif  '.' in new_list[1][0]  :
            print("invalid email")
            return False
        else :       
            print ("valid email")
            return True
    else :
        return False

#---------------------------------------------------------------------------------#

# validate an email depends on conditons, use try and except func with allowing up to 5 user attempts before raising an exception.

def valid_email(email) :
    
        if "@" in email and "." in email :
            new_list = email.split("@")
            try:
                if  not new_list[0]  or  '.' == new_list[1][-1] or '@' == new_list[1][-1]  or  '.' == new_list[1][0] :
                    return False
                else:
                    print("valid email")
                    return True
                   
            except ValueError : return False
            except IndexError :return False
            except SyntaxError : return False