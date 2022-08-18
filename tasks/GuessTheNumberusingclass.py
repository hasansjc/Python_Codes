class GuessThesecret_number:
    
    def __init__(self, secret_number, min, max, max_guess) -> None:
        self.secret_number = secret_number
        self.count_guesses = 0
        self.max_guess = max_guess
        self.min = min
        self.max = max
        
    def get_guess(self):
        guess = input(f"Enter your guess between {self.min} and {self.max}  ")
        if self.is_valid_secret_number(guess):
            return int(guess)
        else:
            print("Please enter a valid secret_number ")
            return self.get_guess()
        
    def is_valid_secret_number(self, str_secret_number):
        try:
            secret_number = int(str_secret_number)
        except: return False
        
        return self.min <= secret_number <= self.max
    
    def has_won(self, guess):
        if(self.secret_number == guess): 
            print(f"Your guess is right, secret number is {self.secret_number}\n Number of guesses you took = {self.count_guesses} ")
            return True
        else: return False
    
    def play(self):
        while self.count_guesses <= self.max_guess :
            
            guess = self.get_guess()
            self.count_guesses +=1
            
            if(self.count_guesses == self.max_guess):
                
                if not self.has_won(guess):
                    print("sorry You lost the game")
                break
            else:
                
                if self.has_won(guess):
                    break
                
                else:
                    print(f"Wrong guess, Try again, You got {self.max_guess-self.count_guesses} left")
                    if(guess > self.secret_number and self.count_guesses < self.max_guess):
                        print(" Your guess was above our secret number")
                    else:
                        print("Your guess is lower than our secret number")          
                   
game1 = GuessThesecret_number(45,1,100,3)
game1.play() 
        
        
        
        
        