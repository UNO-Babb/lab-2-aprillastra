#Magic8Ball.py
#Name: April Lastra 
#Date:
#Assignment: Lab 2 

#We will need random for this program, import to use this package.
import random
def main():
response = ["yes, definitely.", "It is certain.", "Without a doubt."
             "Most Likely.", "You may rely on it.", "As I see it, yes.", "Outlook good.",
             "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", 
             "Cannot predict now.", "Don't count on it.", "My reply is no.",
             "My sources say no.", "Outlook not so good.", "Very doubtful."]
  print("Hello, welcome to magic 8 ball!")
  #Prompt the user for their question.

  #Answer question randomly with one of the options from your earlier list.
  length = len(answers)
r = random.random() * 16 
r = int(r) # cut off decimal values 
# 0 - 1 and make it 0 - 15 ?
print(r)
response = answer(r)
print(response)
if __name__ == '__main__':
  main()
