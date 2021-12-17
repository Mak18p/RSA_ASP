# RSA_ASP
## Project Description

Since our lives are more depending of online exchange, Safer method or environment of exchange are in demand.
This is why I decided to work on the RSA Algorithm for my senior project. In this project, we will be using public,
and private keys to encrypt, and decrypt a message. To produce these keys we will be working with some prime numbers, and math formulas.

This project will be implemented in Python languages, so a proper platform or IDE that can run py files will be needed, such as Spyder, VisualCode, anaconda etc.

## Getting Started 
 To get started we begin with two prime numbers P and Q, the bigger they are the more secure is the encryption, but the longer it will take to process.
 Using the numbers, we will calculate n = P*Q, and T = phi = (P-1)*(Q-1). Next, we can provide a prime number as public key (e), 
 but it must be smaller than T, and be co-primes of T and n.After verifying our public key (e) we can generate the private key (d)
 using the formula e *d) mod T = 1. When both keys are available we can use this formula to Encrypt (m^e mod n), then this formula (m^d mod n) to decrypt.
 
## Coding And Runnig
Part of this project was implemented from another source. The modification made to this project, strengthen the encryption of the message by encrypting
by blocks of character instead of char by char. We created blocks, and used a formula to encrypt, then we decrypt then detach and print. 
## Acknowledgement 


