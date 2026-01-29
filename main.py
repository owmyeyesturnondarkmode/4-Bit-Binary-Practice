import random
import time
import os

times = []
correct = 0
random.seed(os.urandom(16))

def screen_clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("4-Bit Binary to Hexadecimal practice"
          "\n------------------------------------\n")

def practice():
    global correct
    count = 0
    awnsers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
    while count+1 <= 20:
        awnser = random.choice(awnsers)
        question = bin(int(awnser, base=16))[2:].zfill(4)
        screen_clear()
        print(f"{count+1}/20\n")
        print(question)
        start = time.time()
        given_awnser = input("\nHex: ")
        end = time.time()
        elapsed = end - start
        times.append(elapsed)
        if given_awnser.lower() == awnser:
            print("\nCorrect!")
            correct += 1
        else:
            print(f"\nIncorrect! The correct awnser was {awnser.upper()}.")
        count += 1
        print(f"Time: {elapsed:.2f}s")
        input("\nPress Enter to continue...")
    screen_clear()
    average_time = sum(times) / len(times)
    print(f"Practice complete!\nCorrect: {correct}/20\nAverage Time: {average_time:.2f}s")
    ans = input("\nPractice again? (y/n): ").lower()
    if ans == 'y':
        practice()
    elif ans == 'n':
        exit(1)

screen_clear()
input("Press Enter to start practice...")
practice()