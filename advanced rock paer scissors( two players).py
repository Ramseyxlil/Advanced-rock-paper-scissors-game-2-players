import random

def Home():
    print ("          ....Ramsey Games...... ")
    print("rock. paper. scissors")
    print ()
    print("choose player")
    print ("1. single player")
    print("2. multiplayer")
    players = int(input("enter the type of player--"))
    if players == 2:
        print("")
        multiplayer ()
    elif players ==1:
        print("")
        singleplayer()
    else:
        players >2
        print ("invalid input")
        Home()

def multiplayer ():
    name = str(input("first player name: "))
    names = str(input("second player name: "))
    print()
    print("first player name: ",name)
    print("secomd player name: ",names )
    while 1:
        print("scissors ---- 1")
        print("rock ---------2")
        print("paper ------- 3")
        print()
        print (name,"turn")
        t = int(input("rock. paper. scissors-"))
        print  (names,"turn")
        u = int(input("rock. paper. scissors-"))
        if t == 1 and u == 1:
            print (name, "=", t)
            print (names, "=", u)
            print (" its a draw")
        elif t==2 and u==2:
            print (name, "=", t)
            print (names, "=", u)
            print ("its a draw")
        elif t==3 and u ==3:
            print (name, "=", t)
            print (names, "=", u)
            print ("its a draw")
        elif t ==1 and u==2:
            print (name, "=", t)
            print (names, "=", u)
            print("Rock smash scissors!")
            print (names, "wins")
        elif t ==1 and u==3:
            print (name, "=", t)
            print (names, "=", u)
            print("scissors cut paper!")
            print (names, "wins")
        elif t==2 and u ==3:
            print(name, "=", t)
            print(names,"=", u)
            print ("paper cover rock!")
            print(name," wins")
        elif t==3 and u ==2:
            print(name, "=", t)
            print(names,"=", u)
            print ("paper cover rock!")
            print(names," wins")
        elif t ==2 and u==1:
            print(name, "=", t)
            print(names,"=", u)
            print ("rock smash scissors!")
            print(name," wins")
        elif t==3 and u==1:
            print(name, "=", t)
            print(names,"=", u)
            print ("scissors cut paper!")
            print(name," wins")
        print(" enter 0 to end game and go to main menu or 5 to continue")
        n = int(input("-->"))
        if n==0:
            Home ()
        else:
            n ==5
            continue
def singleplayer ():
    name = str(input("Player name: "))
    print("player name: ", name)
    while 1:
        print("start game")
        print("scissors ---- 1")
        print("rock ---- 2")
        print("paper ---- 3")
        print ()
        t = random.randint(1,3)

        u =int(input("rock. paper. scissors-"))
        if t == 1 and u == 1:
            print (name, "=", t)
            print ("computer =", u)
            print (" its a draw")
        elif t==2 and u==2:
            print (name, "=", t)
            print ("computer =", u)
            print ("its a draw")
        elif t==3 and u ==3:
            print (name, "=", t)
            print ("computer =", u)
            print ("its a draw")
        elif t ==1 and u==2:
            print (name, "=", t)
            print ("computer =", u)
            print("Rock smash scissors!")
            print ("computer wins")
        elif t ==1 and u==3:
            print (name, "=", t)
            print ("computer =", u)
            print("scissors cut paper!")
            print ("computer wins")
        elif t==2 and u==1:
            print (name, "=", t)
            print ("computer =", u)
            print("rock smash scissors!")
            print (name, "wins")
        elif t==2 and u ==3:
            print(name, "=", t)
            print("computer =", u)
            print ("paper cover rock!")
            print(name, "wins")
        elif t==3 and u ==2:
            print(name, "=", t)
            print("computer =", u)
            print ("paper cover rock!")
            print("computer wins")
        elif t ==2 and u==1:
            print(name, "=", t)
            print("computer =", u)
            print ("rock smash scissors!")
            print(name," wins")
        elif t==3 and u==1:
            print(name, "=", t)
            print("computer =", u)
            print ("scissors cut paper!")
            print(name," wins")
        print(" enter 0 to end game and go to main menu or 5 to continue game")
        n = int(input("-->"))
        if n==0:
            Home ()
        else:
            n==5
            continue

Home ()
        
        
    
    
        
