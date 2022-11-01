# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

def string(s):
    a={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           a["UPPER_CASE"]+=1
        elif c.islower():
           a["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ",s )
    print ("No. of Upper case characters : ", a["UPPER_CASE"])
    print ("No. of Lower case Characters : ", a["LOWER_CASE"])

string('The quick Brown Fox')