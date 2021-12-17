def isPrime(n):
  # Corner case
  if (n <= 1):
    return False
  
  # Check from 2 to n-1
  for i in range(2, n):
    if (n % i == 0):
      return False
      
  return True
  
def modulus(p, q):
  return p * q
  
def eulerTotient(p, q):
  return (p - 1) * (q - 1) 
  
def findFactors(x):
  factorList = []
  for i in range(1, x + 1):
    if x % i == 0:
      factorList.append(i)
  return factorList
  
def publicKeyCheck(eulerlist, keylist):
  for num in keylist:
    if num in eulerlist:
      if num != 1:
        print('invalid public key')
    else:
      print('public key is valid')
      break

def egcd(a, b):
  s = 0; Os = 1
  t = 1; Ot = 0
  r = b; Or = a

  while r != 0:
      quotient =  Or // r
      Or, r = r, Or - quotient * r
      Os, s = s, Os - quotient * s
      Ot, t = t, Ot - quotient * t

  # return gcd, x, y
  return Or, Os, Ot

def modularInv(a, b):
  gcd, x, y = egcd(a, b)

  if x < 0:
      x += b

  return x
def unicode_andblock(message):
    unic_m=[]
    for l in message:
        m = ord(l)
        unic_m.append(m)
    # create blocks
    sub=[]; result=[]
    for i in unic_m:
        sub+=[i]
        if len(sub)==3: result+=[sub]; sub=[]
    if sub: result+=[sub]
    return result

def enc_formula(my_l):
    return[(x**e)%N for x in my_l]
def encrypt(the_list):
    cipher=[]
    for i in the_list:
        j=enc_formula(i)
        cipher.append(j)
    return cipher

def encrypt_msg(list):
    letters1 =[]
    #detach
    detached= sum(list,[])
    # unicode to characters
    for j in detached:
        m = chr(j)
        letters1.append(m)
    #list to string
    strl =" "
    return (strl.join(letters1))
def dcr_form(my_l):
    return[(x**d)%N for x in my_l]

def decrypt(the_list):
    decipher=[]
    letters=[]
    #decryption
    for i in the_list:
        k=dcr_form(i)
        decipher.append(k)
    #detach
    detached= sum(decipher,[])
    # unicode to characters
    for j in detached:
        m = chr(j)
        letters.append(m)
    #list to string
    strl =" "
    return (strl.join(letters))


def privateKeyCheck(public, private, euler):
  if public * private % euler != 1:
    print('invalid private key') 
  
  else: 
    print('private key is valid')

print('Welcome to the RSA Algorithm Simulator.')
print('First you will need to select two Prime numbers.')

#step one generate two prime numbers
p = int(input('\nEnter a prime number (p): '))
q = int(input('Enter a prime number (q): '))
N = p*q
print("\nChecking to see if inputs are valid: ")
print(isPrime(p))
print(isPrime(q))

print("\nNow printing the Modulus (n):")
print(modulus(p, q))

print("\nNow printing the eulerTotient:")
print(eulerTotient(p, q))

e = publicKey = int(input("\nPlease Enter a number that has no common factors with EulerTotient: "))
print('This will be your public key (e).')

factorsEuler = findFactors(eulerTotient(p,q))

factorsKey = findFactors(publicKey)

print('\nVeryifying public Key:')

publicKeyCheck(factorsEuler, factorsKey)

print('\nGenerating and verifying private Key...')

d = modularInv(publicKey, eulerTotient(p, q) ) 
print('Private Key Successfully Generated.')

privateKeyCheck(publicKey, d, eulerTotient(p, q))

msg = input('\nPlease enter a message to be encrypted.')
new_unic_msg=unicode_andblock(msg)


print('\nNow printing your encrypted message:')

encrypted= encrypt(new_unic_msg)
print(encrypt_msg(encrypted))

print('\nNow printing your decrypted message:')

print(decrypt(encrypted))