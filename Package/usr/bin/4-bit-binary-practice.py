#!/usr/bin/env python3

import random
import time
import os
import hashlib
from datetime import datetime
import traceback

copyright = "2026 owmyeyesturnondarkmode"
times = []
correct = 0
os.makedirs(f"{os.path.expanduser('~/.local/share/binarypractice')}", exist_ok=True)
homedir = os.path.expanduser('~/.local/share/binarypractice')

def screen_clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("4-Bit Binary to Hexadecimal practice"
          "\n------------------------------------\n")

def practice():
    global times,correct
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
                    given_answer = input("\nHex: ").strip()
                    if len(given_answer) != 1 or given_answer.lower() not in answers:
                        print("\n\033[31mInvalid input!\033[0m\nPlease enter a single hex number.")
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
                ans = input("\nPractice again? (y/n): ").lower()
                if ans == 'y':
                    times = []
                    correct = 0
                    break
                elif ans == 'n':
                    return
                else:
                    print("\033[31mInvalid input!\033[0m\nPlease try again.\n")

def tutor():
    screen_clear()
    if not os.path.exists(f"{homedir}/{hashlib.sha256(os.getlogin().encode()).hexdigest()}"):
        print("Because this is your first time using the tutor, would you like for\nme to show you how to convert binary to decimal? (y/n) ")
        while True:
            choice = input("\n").strip().lower()
            if choice == 'y':
                break
            elif choice == 'n':
                break
            else:
                print("That's not a valid input! Please try again.")
        if choice == 'y':
            screen_clear()
            print("(Press enter to continue through the tutor)\n")
            print("Binary is a number system, like decimal.")
            input()
            print("However, instead of using 10 digits, 0-9, it only uses 0 and 1.")
            input()
            print("The place value of each digit is, instead of 1, 10, 100, etc. powers of 2.")
            input()
            print("That being, 1, 2 ,4 , 8 ,16, etc.")
            input()
            print("So, a strategy to read binary is to add the place values of the digits that are 1.")
            input()
            print("Example:\n"
                  "1  0  1  1\n"
                  "^  ^  ^  ^\n"
                  "8  0  2  1\n\n"
                  "8+0+2+1=11")
            input()
            print("So, 1011 in binary is 11 in decimal.")
            input()
            print("But, commonly in computers, we use somthing called hexadecimal.")
            input()
            tutor_marker = f"{homedir}/{hashlib.sha256(os.getlogin().encode()).hexdigest()}"
            with open(tutor_marker, 'w') as f:
                f.write('')
        elif choice == 'n':
            print("Okay, skipping the binary to decimal tutor.")
            input()
        else:
            screen_clear()
            print("Sorry, something has gone awry in the code, please restart the app.")
            while True:
                None
    print("Hexadecimal is a number system.")
    input()
    print("Like binary and decimal, it's another number system, but it uses 16 digits, 0-f")
    input()
    print("You count like this:\n"
            "0 1 2 3 4 5 6 7 8 9 a b c d e f")
    input()
    print("And why we use hexadecimal is because it cleanly converts from binary,\nsince 1 hex digit perfectly represents 4 binary digits.")
    input()
    print("This app will teach you how to do that.")
    input()
    print("Basically, you convert 4 binary digits to decimal, then if that\nnumber is more than 9, you count how many numbers it is over 9, and\ncount that far into the alphebet (if it's over f, then you messed up),\nand that's your awnser!")
    input()
    print("Going off of the previous example, 1011 is 11, and 11 is 2 over 9, so you count A, B, and that's your awnser!")
    input()
    print("So, 1011 in binary is B in hexadecimal.")
    input()
    print("Eventually, you will memorize the conversions, but for now, you can use this method to convert binary to hexadecimal.")
    input()
    print("But if it isn't over 9, then it's just the number.")
    input()

while True:
    screen_clear()
    try:
        choice = input("Main Menu"
                    "\n1. Fluency Practice"
                    "\n2. Tutor"
                    "\n3. Exit\n\n").strip()
    except KeyboardInterrupt:
        exit(0)
    except EOFError:
        exit(1)
    if choice == '1':
        try:
            practice()
        except Exception as e:
            screen_clear()
            current = datetime.now()
            timestamp = current.strftime('%Y-%m-%d-%H-%M-%S')
            os.makedirs(f"{homedir}/logs/", exist_ok=True)
            os.system(f"touch {homedir}/logs/{timestamp}")
            with open(f"{homedir}/logs/{timestamp}", "w") as errfile:
                    traceback_str = ''.join(traceback.format_exception_only(type(e), e))
                    tb_str = ''.join(traceback.format_tb(e.__traceback__))
                    full_tb = traceback_str + tb_str
                    errfile.write(full_tb)
            print(f"\033[031mSorry! An error has occurred.\033[0m\nThe traceback has been saved here: {homedir}/logs/{timestamp}.txt\n\nPlease report it on github and include the contents of this file here:\nhttps://github.com/owmyeyesturnondarkmode/4-Bit-Binary-Practice/issues/new")
            while True:
                None
    elif choice == '2':
        try:
            tutor()
        except Exception as e:
            screen_clear()
            current = datetime.now()
            timestamp = current.strftime('%Y-%m-%d-%H-%M-%S')
            os.makedirs(f"{homedir}/logs/", exist_ok=True)
            os.system(f"touch {homedir}/logs/{timestamp}")
            with open(f"{homedir}/logs/{timestamp}", "w") as errfile:
                    traceback_str = ''.join(traceback.format_exception_only(type(e), e))
                    tb_str = ''.join(traceback.format_tb(e.__traceback__))
                    full_tb = traceback_str + tb_str
                    errfile.write(full_tb)
            print(f"\033[031mSorry! An error has occurred.\033[0m\nThe traceback has been saved here: {homedir}/logs/{timestamp}.txt\n\nPlease report it on github and include the contents of this file here:\nhttps://github.com/owmyeyesturnondarkmode/4-Bit-Binary-Practice/issues/new")
            while True:
                None
    elif choice == '3':
        exit(0)
    elif choice == 'reset':
        print("Resetting tutor data...")
        tutor_marker = f"{hashlib.sha256(os.getlogin().encode()).hexdigest()}"
        try:
            os.remove(f'{homedir}/{tutor_marker}')
        except FileNotFoundError:
            print("No data to reset.")
        print("Tutor data reset.")
        input()