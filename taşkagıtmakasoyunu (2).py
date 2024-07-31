import random

choices=["rock","paper","scissor"]
computer=random.choice(choices)
player=None
while player not in choices:
    player=input("rock ,paper or scissors?:" ).lower()

if computer==player:
 print("computer:"+computer)
 print("player:"+player)
 print("Tie")
elif computer=="rock":
   if player=="scissors":
       print("computer:"+computer)
       print("player:"+player)
       print("you lose")
   if player=="paper":
       print("computer:"+computer)
       print("player:"+player)
       print("you lose")
elif computer=="scissors":
   if player=="rock":
       print("computer:"+computer)
       print("player:"+player)
       print("you lose")
   if player=="paper":
       print("computer:"+computer)
       print("player:"+player)
       print("you lose")
elif computer=="paper":
   if player=="scissors":
       print("computer:"+computer)
       print("player:"+player)
       print("you lose")
   if player=="rock":
       print("computer:"+computer)
       print("player:"+player)
       print("you lose")