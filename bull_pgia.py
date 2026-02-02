# Liad Itzhak
# Dvir Gozali
# Hadar Shapira
import random
from SQLmanager import *

db = connect()

class BullPgia:
    def __init__(self):
        self.num = None
        self.nums = []
        self.history=[]
    def game(self):
        _input=input("enter the length of target between 1-10: ")
        idiot_count = 0
        while not (_input.isnumeric() and 0 < int(_input) < 10) :
            _input = input("enter the length of target between 1-10: ")
            idiot_count += 1
            if idiot_count == 2:
                print("idiot")
                exit()
        self.num=int(_input)
        self._start_game()
        # print(f"\t {self.nums}")

        attempts = 0
        for i in range(max(self.num+2,10)):
            attempts += 1
            guess_str = input(f"enter {self.num} different numbers: ")
            idiot_count=0
            while len(guess_str)>self.num or len(guess_str)<=0:
                guess_str = input(f"enter {self.num} different numbers: ")
                idiot_count+=1
                if idiot_count==2:
                    print("idiot")
                    exit()
            # bulls
            bulls=0
            for i in range(len(guess_str)):
                if guess_str[i] == self.nums[i]:
                    bulls+=1
            cows=len(set(self.nums) & set(guess_str))-bulls
            #history
            item={"guess": guess_str, "bulls": bulls, "cows": cows, "attempt": attempts}
            self.history.append(item)

            print(f"guess:{guess_str}\ncows: {cows}\nbulls: {bulls}")

            if bulls==self.num:
                print("\nyou win!!!!!!!!!!!!!")

                secret = ''
                for dig in self.nums:
                    secret = secret + str(dig)
                add_history(db, secret, attempts)
                best = minimum_attempt(db)
                print(f"best game:  {best} attempts")
                exit()
        print("\nyou lose!!!!!!!!!!!!!!!!!!")
    def _start_game(self):
        _nums=set()
        while len(_nums)<self.num:
            _nums.add(str(random.randint(0, 9)))
        self.nums=list(_nums)

game=BullPgia()
game.game()