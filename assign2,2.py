

# Write a Python program to print a dictionary whose keys should be the 
# alphabet from a-z and the value should be corresponding ASCII values


dict = dict()
alphabet = range(97,123)
for i in alphabet:
    dict[str(i)] = chr(i)
print(dict)