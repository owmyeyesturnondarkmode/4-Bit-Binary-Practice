#!/usr/bin/env python3

import random
import time
import os

copyright = "2026 owmyeyesturnondarkmode"
times = []
correct = 0

def screen_clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("4-Bit Binary to Hexadecimal practice"
          "\n------------------------------------\n")

screen_clear()
try:
    input("Press Enter to start practice...")
except KeyboardInterrupt:
    exit(0)
except EOFError:
    exit(1)

while True:
    while True:
        count = 0
        answers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
        while count+1 <= 20:
            answer = random.choice(answers)
            question = bin(int(answer, base=16))[2:].zfill(4)
            screen_clear()
            print(f"{count+1}/20\n")
            print(question)
            start = time.time()
            while True:
                try:
                    given_answer = input("\nHex: ").strip()
                except KeyboardInterrupt:
                    exit(0)
                except EOFError:
                    exit(1)
                if len(given_answer) != 1 or given_answer.lower() not in answers:
                    print("\n\033[31mInvalid input!\033[0m\nPlease enter a single hex number.]]")
                else:
                    break
            end = time.time()
            elapsed = end - start
            times.append(elapsed)
            if given_answer.lower() == answer:
                print("\n\033[32mCorrect!\033[0m")
                correct += 1
            else:
                print(f"\n\033[31mIncorrect!\033[0m \nThe correct answer was {answer.upper()}.")
            count += 1
            print(f"Time: {elapsed:.2f}s")
            input("\nPress Enter to continue...")
        screen_clear()
        average_time = sum(times) / len(times)
        print(f"Practice complete!\nCorrect: {correct}/20\nAverage Time: {average_time:.2f}s")
        while True:
            try:
                ans = input("\nPractice again? (y/n): ").lower()
            except KeyboardInterrupt:
                exit(0)
            except EOFError:
                exit(1)
            if ans == 'y':
                times = []
                correct = 0
                break
            elif ans == 'n':
                exit(0)
            else:
                print("\033[31mInvalid input!\033[0m\nPlease try again.\n")