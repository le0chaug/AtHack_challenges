
def my_function(x):
    return pow(x,3)+10*pow(x,2)+x*7 + 6

plaintext = "AtHackCTF{}"

cipher = [317336]
for i in plaintext : 
   cipher.append(my_function(ord(i)))
print("cipher = " ,cipher)

