from random import randint
from termcolor import colored
repeat = True
dictionary = ["letmein","password123","12345","password","1234","123","computer","qwerty","asdf"]	

weak = ["Are you kidding me?","Pathetic, just pathetic.","This is a joke, right?","Do you want to be hacked?","I would say nice try but I shouldn't lie","That's an insult to other passwords","Oh yeah, like that isn't going to be easy to guess...","Don't come crying to me when you're hacked","I hope this account isn't important","Hackers eat passwords like these for breakfast","You do know passwords are supposed to be strong, right?"]

norm = ["Not bad. I'm not saying it's good, just not bad.","You're getting there","Close but no cigar","I've seen POTATOES with better passwords...","I'll give you an A for effort","This might take a hacker half an hour, that's all...","Say 'adios' to your emails if you're going to use this password"]

strong = ["Yeah yeah, like you're going to remeber this...","Looking good so far","Try making your password a little less complicated nextime...","Do you want to make that any longer...","I asked for a password not an essay!","Average. That is an average password.","Strong password, just make sure I'm not there when you try and remember it"]

while repeat:	
  password = input(colored("Enter your password and let our honest program decide its strength.\n\nMy password is:","cyan"))

  if str(password).lower() in dictionary:	
    print(colored("\nSeriously? You're gonna use one of the most commonly used passwords? Come on!\n","red"))
  elif len(password) <= 20:
    print(colored("\n" + weak[randint(0,11)]+"\n","red"))
  elif 20 < len(password) <=30:
    print(colored("\n" + norm[randint(0,6)]+"\n","yellow"))
  else:
    print(colored("\n" + strong[randint(0,7)]+"\n", 'green'))