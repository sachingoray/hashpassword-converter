import hashlib

#ASKING THE USER FOR THE IMPUT
password =input("enter the password to hash with SHA-256: " )

#encode the given password into the hashpassword

result = hashlib.sha256(password.encode()).hexdigest()
print ("this is your converted hash password by SHA-256 algoritm:  ", result)
