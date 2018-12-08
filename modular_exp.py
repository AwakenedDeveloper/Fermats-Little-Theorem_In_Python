#Written by Jigar D. Prajapti 
#Topic: Using Fermat's Little Theorem to calculate modular exponentiation

import math

def flt():
    print("\n***********************************\n")

    #Get user input i.e the base, the exponent and the modulo
    a = int(input("Enter base(a): ")) 
    exp = int(input("Enter exponent: ")) 
    p = int(input("Enter modulo(p): "))

    #according to Fermat's Little Theorem, a^(p-1) = 1 (mod p)
    modNew = p-1

    #find new exponent by calculating (orignal exp) % modNew
    expNew = exp%modNew

    #below is equal to a^expNew (mod p)
    result = pow(a, expNew, p)

    print("\nFor " + str(a)+"^"+str(exp)+" (mod " + str(p) + "), the answer is: "+ str(result))

    print("\n***********************************\n")

if __name__ == "__main__":
    flt()