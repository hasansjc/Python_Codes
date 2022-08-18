else:
        print(f"Wrong guess, Try again, You got {max_number_of_attemps-number_of_attempts} left")
        if(num > secret_numnber):
            print(" Your guess was above our secret number")
        else:
            print("Your guess is lower than our secret number")