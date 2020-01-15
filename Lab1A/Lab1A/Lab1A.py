#Michael Lopez
#LAB 1A Room Checker 
#SE126

#Write a program that determines whether a meeting room is in violation of fire regulations regarding the maximum room capacity. 

#VARIABLE DICTIONARY
#-------------------
#roomCount = count of rooms checked
#people = input(people attending)
#roomCap = input(capacity of a room)
#over = fire regualtion 
#under = allows for more people

#INTIALIZATION
#-------------
roomCount = 0 
answer = "y"

#START
print("\n\tWelcome to RoomChecker Pro!")

answer = input("Would you like to check a room today? [y/n] ")

while (answer == "y" or answer == "Y"): #while loop
    
    
    roomCap = int(input("What is the room's Max Capacity?: "))
    people = int(input("How many people are attending?: "))
    
    if people <= roomCap:
        print("\n\tFire Regulation allows this room suitable to be used.")
        print("ROOM CAPACITY:  ", roomCap)
        print("ATTENDING:      ", people)
        under = roomCap - people
        print("REMAINING SEATS: ", under)

    if people > roomCap:
        print("\n\tFire Regulation Code DOES NOT permit this room for use. There are too many people.")
        print("ROOM CAPACITY:   ", roomCap)
        print("ATTENDING:        ", people)
        over = people - roomCap #math for how many people must be removed
        print("REMOVAL REQUIRED:", over)

    roomCount = roomCount + 1
    
    answer = input("Would you like to check another room? [y/n] ") #Loop escape

print("\n\tROOMS CHECKED: ", roomCount)
print("\tThanks for using my program!")
