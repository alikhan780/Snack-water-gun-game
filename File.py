import random

"""snake= 1
water =-1
gun=0"""

computer=random.choice([1,-1,0])
yourinput=input("enter your choice")
dict1={"s":1,"w":-1,"g":0}
dict2={1:"snake", -1:"water", 0:"gun"}
you=dict1[yourinput]
print(f"you choose {dict2[you]}\ncomputer choose {dict2[computer]}")
if(computer== you):
    print("game draw")
else:
    if(computer==1 and you==0):
      print("you win")
    elif(computer ==0 and you==1):
      print("oops! you lose")
    elif(computer==-1 and you==1):
      print("oops! you lose")
    elif(computer==1 and you==1):
      print("you win")
    elif(computer==0 and you==1):
      print("you win")
    elif(computer==-1 and you==0):
      print("you win")
