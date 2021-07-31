import random
a=input("Choose between Stone,Paper,Scissor -  ")
gamewinuser=0
comp=random.randint(1,3)
if (comp==1):
    comp="stone"
elif(comp==2):
    comp="paper"
elif(comp==3):
    comp="scissor"
    #seprated up one is computer one and down one is for user
if(a=="stone" and comp=="paper"):
    gamewinuser=False
elif(a=="paper" and comp=="stone"):
    gamewinuser=True
elif(a=="scissor" and comp=="stone"):
    gamewinuser=False
elif(a=="stone" and comp=="scissor"):
    gamewinuser=True
elif(a=="stone"and comp=="stone"):
    gamewinuser="TIE"
    #stone part compeleted
if(a=="stone" and comp=="paper"):
    gamewinuser=False
elif(a=="paper" and comp=="stone"):
    gamewinuser=True
elif(a=="paper" and comp=="scissor"):
    gamewinuser=False
elif(a=="scissor" and comp=="paper"):
    gamewinuser=True
elif(a=="paper"and comp=="paper"):
    gamewinuser="TIE"
    #paper part compeleted
if(a=="scissor" and comp=="stone"):
    gamewinuser=False
elif(a=="scissor" and comp=="paper"):
    gamewinuser=True
elif(a=="scissor" and comp=="stone"):
    gamewinuser=False
elif(a=="stone" and comp=="scissor"):
    gamewinuser=True
elif(a=="scissor"and comp=="scissor"):
    gamewinuser="TIE"
    #scissor part completed
if gamewinuser==True:
    print(f"YOU WON! Computer Choose {comp}")
elif gamewinuser==False:
    print(f"YOU LOOSE! Computer Choose {comp}")
elif gamewinuser=="TIE":
    print(f"TIE! Computer Also  Choose {comp}")





    









            
        
        
     




