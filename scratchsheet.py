from math import gcd
import random
p,q=11,13
#print(p,q)
n=p*q
t=(p-1)*(q-1)
list_ofE=[]
list_a =[] 
list_b =[]
list_c =[]
e = 0
for i in range(t):
    if gcd(i,t) == 1:
        list_a.append(i)
    if gcd(i,n) == 1:
        list_b.append(i)
list_ofE = list(set(list_a) & set(list_b))
for v in list_ofE:
    if v<= 1:
        list_ofE.remove(v)
#print("choose a public key", list_ofE)
e= random.choice(list_ofE)
#e =input('Your public key:')
#print(list_ofE)
print("the public key is",str(e))

for j in range (n):
    if (e * j) % t == 1:
        if j > e:
            list_c.append(j)
    #print(list_c)
        d = random.choice(list_c)
print ("The private key is", str(d))
#mssg =input("enter message:")  
dicts = {}
keys = range(1,26) 
values = ['abcdefghijklmnopqrstuvwxyz']
#for i in mssg:
    #for 

#enc_m =pow(int(mssg),e)%n
#print('The encrypted message is:',str(enc_m))

#dec_m = pow(enc_m,d)%n
#print('The decrypted message is:',str(dec_m))

def encrypt(e, N, msg):
  cipher = ""

  for c in msg:
      m = ord(c)
      cipher += str(pow(m, e, N)) + " "

  return cipher

def decrypt(d, N, cipher):
  msg = ""

  parts = cipher.split()
  for part in parts:
      if part:
          c = int(part)
          msg += chr(pow(c, d, N))

  return msg

message = input('\nPlease enter a message to be encrypted.')

cipher = encrypt(e ,n , message)

print('\nNow printing your encrypted message:')

print(encrypt(e,n , message))

print('\nNow printing your decrypted message:')

print(decrypt(d,n , cipher))