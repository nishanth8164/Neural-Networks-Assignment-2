def Full_name(first_name="first name",last_name='last name'):# Here i have created Full name method by passing arguments first name and last name 
    return first_name+' '+last_name # Here i have conacatinted both first name and last name which i have returned it as a string to the function
first_name=input("Enter your first name:/n")# Used input function to accept a string from the user and stored in a variable
last_name=input("Enter your last name:/n")
full_name=Full_name(first_name,last_name)#passed variables to the function
print(full_name)

def string_alternative(string):
    o=''
    for i in range(0,len(string)):
        if(i%2==0):
            o=o+string[i]
    return o

print(string_alternative('Good evening'))
