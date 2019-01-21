import random

Muskets = ["Jon", "James", "Anthony"]
jewelAmount = 10
alive = True

def musketCheck():
    #lets check the info we have on our musketeers (and their friend for some reason)
    global Muskets
    MusketAges = [23,20,18]
    MusketFriend = "Matt"
    MusketFriendAge = 22
    print("The Muskets are" + str(Muskets) + ", aged " + str(MusketAges) + " respectively, with a friend "+ str(MusketFriend) + " aged " + str(MusketFriendAge) )
    if input("Is the information above True or False? ") == "False":
        Muskets = [str(x) for x in input("Please write the Musket's names ").split(",")]
        MusketAges = [int(x) for x in input("Please write the Musket's ages ").split(",")]
        MusketFriend = input("Please write the Musket's friend's name ")
        MusketFriendAge = input("Please write the Musket's friend's age ")
      

def kingStarting():
    #lets start the game
    if input("Would you like to be king? (yes/no) ") == "yes":
        kingName = input("Great King, what is your name? ")
        jewelAmount = input(kingName + ", how many jewels would you like? ")
        jewelValues = [int(x) for x in input(kingName + ",how much does each of the " + jewelAmount +" jewel(es) cost?").split(",")]
        print("King " + kingName + " that value is worth " + str(sum(jewelValues)))
        musketCheck()
        
    else:
        print("You've been executed, thanks for your time")
        jewelAmount = 0
        global alive
        alive = False
        return alive
    return jewelAmount
    

def jewelRun():
    #see if you got the jewels
    if alive == True:
        if random.randint(0,101) >= 50:
            print("Your team got away and made " + str(jewelAmount))
        else:
            print("Unfortunately your team was caught, and someone must pay. You can either choose a member or have one randomly selected. Input a number if you have a choice, or 'random'.")
            kingsChoice= input("What is your choice? ")
            if kingsChoice == "random":
                Muskets.pop(random.randint(0,2))
                print("Your surviving team is" + str(Muskets))
            else:
                Muskets.pop(int(kingsChoice))
                print("Your surviving team is " + str(Muskets))
    else:
        print("Since you're dead, you couldn't try to get jewels.")

kingStarting()
jewelRun()

    



