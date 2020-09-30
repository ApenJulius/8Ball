from os import system
system("title " + "Magic 8ball")

import random

import sys,time

def sprint(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(3./90)


ans = True

while ans:
    question = input(" Ask the magic 8 ball a question (enter to quit):".lower())

    answers = random.randint(1,8)

    if question == "":
        sys.exit()

    elif question == "parles-tu francais":
         sprint(" Désolé, J'apprends le français\n")
    elif answers == 1:
        sprint(" It is certain\n")


    elif answers == 2:
        sprint(" Outlook good\n")


    elif answers == 3:
         sprint(" You may rely on it\n")


    elif answers == 4:
         sprint(" Ask again later\n")


    elif answers == 5:

         sprint(" Concentrate and ask again\n")


    elif answers == 6:
         sprint(" Reply hazy, try again\n")


    elif answers == 7:
         sprint(" My reply is no\n")


    elif answers == 8:
         sprint(" My sources say no\n")
