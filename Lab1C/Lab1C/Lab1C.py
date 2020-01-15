#Michael Lopez
#LAB 1C Room Checker 
#SE126

#EDIT 1B using functions

#VARIABLE DICTIONARY
#-------------------
#roomCount = count of rooms checked
#people = input(people attending)
#roomCap = input(capacity of a room)
#over = fire regualtion 
#under = remaining seats

#INTIALIZATION
#-------------
roomCount = 0 
roomCap = 0
people = 0
answer = "y"

#FUNCTIONS
#---------
def capacity(ca):
#FUNCTION THAT PROMPTS USER FOR ROOM CAPACITY
    ca = int(input("What is the room's Max Capacity?: "))
    return ca

def attendees(pp):
#FUNCTION THAT PROMPTS USER FOR ATTENDEES
    pp = int(input("How many people are attending?:   "))
    return pp

def choice(an):
#FUNCTION THAT ALLOWS PASSAGE THROUGH OUR JOURNEY
    an = input("Would you like to check another room? [yY/nN] ")
    return an

def register(pp , ca):
    #FUNCTION FOR THE MATH
    fr = pp - ca
    return fr


#PROGRAM START
#-------------

print("\n\tWelcome to RoomChecker Pro!")

answer = input("Would you like to check a room today? [yY/nN] ")

while (answer == "y" or answer == "Y"): 
    
    roomCap = capacity(roomCap)#FUNCTION CALL
    people = attendees(people)#FUNCTION CALL

    if people <= roomCap:
        print("\n\tFire Regulation allows this room suitable to be used.")
        print("ROOM CAPACITY:  ", roomCap)
        print("ATTENDING:      ", people)
        under = roomCap - people
        print("REMAINING SEATS: ", under)

    if people > roomCap:
        print("\n\tFire Regulation Code DOES NOT permit this room for use. There are too many people.")
        print("ROOM CAPACITY:  ", roomCap)
        print("ATTENDING:      ", people)
        over = register(people, roomCap)#FUNCTION CALL
        print("REMOVAL REQUIRED: ", over)

    roomCount = roomCount + 1
    
    answer = choice(answer)#FUNCTION CALL

print("\n\tROOMS CHECKED: ", roomCount)
print("\tThanks for using my program!")

