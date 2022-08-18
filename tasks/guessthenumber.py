import random

secret_numnber = random.randrange(1,100)

print("++++++++++++++++++++++++++++++++++++++++++\n+++++  Guess the secret number game  ++++++\n++++++++++++++++++++++++++++++++++++++++++\n")

print("The number is between 1 to 100 range \n")
number_of_attempts = 0
max_number_of_attemps = 10

while (number_of_attempts < max_number_of_attemps):
    
    num = int(input("Enter the number"))
    number_of_attempts+=1

    if(secret_numnber == num):
        print(f"Yayyyy, You guessed it right, YOU WON !!!\n No. of attemps {number_of_attempts}")
        break
    
    else:
        print(f"Wrong guess, Try again, You got {max_number_of_attemps-number_of_attempts} left")
        if(num > secret_numnber):
            print(" Your guess was above our secret number")
        else:
            print("Your guess is lower than our secret number")

if(number_of_attempts == 5):
    print("Maximum attemps reached, Sorry you lost")
        
