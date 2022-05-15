 
#Imports
from adventurelib import * #This saying that the game is gonna run by adventurelib
Room.items = Bag()


#Define Rooms - What the Rooms in my game are 
science_class = Room("""	
The first room, The science class.
The room is very dark and gloomy however 
You see there is a Black door.
\nLook for a door key and take it,\n then use it, open door to see where it takes you. \n (You can say door and door key ) .
""")

hallway_1 = Room("""
The mysterious hallway with Blinkering Lights.
There is an unlocked door stained with blood up ahead.  
\n You should look for a key or some sort,\n it may be useful to you soon. 
""")
#\n means to make a new line, it is an efficiant way to make a new line

english_class = Room("""
The detention room, The english class.
The room is creepily quiet that it gives you chills up your spine.
There is a partially covered secret passage that requires a key.
\n Do you have a book key on you,\n I heard it was in the hallway.\n you should probably look for another key in this room.   
""")

secret_passage = Room("""
The spy vent, The secret passage.
Over here you can see everything underneath, 
You see a girl laughing crazily.
You then instantly get the feeling shes bad news and you need to escape.
There is a vent maybe that leads to the way out ?
\n Did you get a vent key in english class, \n If so use it on the vent.
""")

science_class_midgame = Room("""
The first room, The science class.
Your back to the dark gloomy room 
however you notice an unlocked door on your west.
\n Check if there is anything here, then head on out. \n Be careful you do not know where she is or what she has planned
""")

hallway_2 = Room("""
"BEEP"
Shoot you here the alarm go off, quick
There is a gap underneath the stairs up ahead 
\nGo east towards the stairs and hide.
""")
#I have a while loop for this which keeps telling them to hide

start_of_stairs = Room("""
She arrives into the hallway and does not see you, 
She then goes up the stairs armed with a knife.
You feel something poking you on your back. 
\n Look for what it is,\n and maybe it could help you defeat her.\n Go upstairs (North) to face her. 
""")  

boss_room = Room("""
The Final Room, The Boss Room.
You See her next to a Door with a Mystery Sign (?)
If you picked up the sword you can unleash a suprise slash. 
""")
#You can't break the game and defeat her without a sword, because she won't notice you until you strike her down. You will need to go back and grab the sword.


#Define Connections - The directions to the rooms (north, east , south , west)
science_class.east = hallway_1
hallway_1.east = english_class
english_class.south = secret_passage
secret_passage.south = science_class_midgame 
science_class_midgame.west = hallway_2
hallway_2.east = start_of_stairs	
start_of_stairs.north = boss_room

#Define Items 
#In the game if you have an item you can still look at it, this will tell you the description
Item.description = "" #This adds a blank description to each item

door_key = Item("door key", "door")
door_key.description = ("The door key is black, try it out on the science class door ")

book_key = Item("book key", "book")
book_key.description = ("The key is silver and rusty, maybe it could be used in the secret passage")

vent_key = Item("vent key", "vent")
vent_key.description = ("The vent key is white, it would be used to get out of a vent ")

katana = Item("katana","sword","weapon","blade")
katana.description = ("An authentic japanese katana, when unsheaved it is very sharp. It has a mysterious dark alluring aura ")

#Define Bags - In order, adding them to rooms
science_class.items.add(door_key)
hallway_1.items.add(book_key)
english_class.items.add(vent_key)
boss_room.items.add(katana)

#Define any variables 
current_room = science_class
inventory = Bag()
door_opened = False

#Binds (eg "@when(look")) 

while hide != "hide" or "hide behind stairs":
	hide = input("Hurry up , hide behind the stairs")


@when("slash")
@when("suprise slash")
@when("attack")
@when("suprise")
@when("suprise attack")
@when("kill")
@when("sneak attack")
@when("suprise kill")
@when("use sword")
def suprise_slash():
	global current_room
	if inventory.find("katana") and current_room == boss_room:
		print("You swiftly slash her from behind splashing her blood everywhere,\n she falls to the ground saying \n 'You , You have defeated me. You have won this time but this won't be the last of me '")
		player_name = input("'*puff *puff could you do me a favour and tell me your name'")
		print(f"'Well done {player_name} but I won't let you win next time'")
		print("You then walk towards the mysterious door (?) and open it \n the door blinds you with light however you continue to walk forwards. \n You have now reached the ending of the game, much more could await you.")


 
@when("look")
@when("look for")
def look():
	if len(current_room.items) > 0:
		print("You see the:")
		for item in current_room.items:
			print(item)


@when("get ITEM")
@when("take ITEM")
@when("pick up ITEM")
def pickup(item):
	if item in current_room.items:
		t = current_room.items.take(item) #"t" (a temporary variable)
		inventory.add(t)
		print(f"You pick up the {item}")
	else:
		print(f"You don't see the {item}")


@when("use door key")
def open_door():
	global current_room
	if inventory.find("door key") and current_room == science_class:
		print("You put the key inside the door hole and twist it,\n you hear a click")
		print(current_room.exits())
		global door_opened 
		door_opened = True

	else:
		print("door is locked")


@when("use book key")
def open_door():
	global current_room
	if inventory.find("book key") and current_room == english_class:
		print("You put the key inside the partially covered key hole and twist it,\n you hear a click")
		global door_opened 
		door_opened = True
	else:
		print("door is locked")

@when("use vent key")
def open_door():
	global current_room
	if inventory.find("vent key") and current_room == secret_passage:
		print("You put the key inside the vent exit key hole and twist it,\n you hear a click")
		global door_opened 
		door_opened = True
	else:
		print("door is locked")


@when("open door")
def exit_startingroom():
	global current_room 
	if door_opened == True and current_room == science_class:
		print("You go to next room")
		current_room = hallway_1
		print(current_room)
	else:
		print("door is locked")
	 
@when("inventory")
@when("show inventory")
@when("what is in my pocket")
def player_inventory():
	print("You are carrying")
	for item in inventory:
		print(item)
		

@when("look at ITEM")
def look_at(item):
	if item in inventory:
		t = inventory.find(item)
		print(t.description)
	else:
		print(f"You aren't carrying an {item}")

@when ("go DIRECTION") 
def travel(direction):
	global current_room
	if door_opened == True:
		current_room = current_room.exit(direction)
		print(f"You go {direction}.")
		print(current_room)

#Main Function 
def main():
	print(current_room)
	start()

if __name__ == '__main__':
	main()


#! I need to run this in school computer then, 
#! I upload completed game to Classroom as a Python file then,
#! Work a bit more on about my Evidence of testing ( Subheadings)	
#! Upload recording of me playing

#@Could add a function which takes you to any room you have been too, this could be hard. (Ask Mrs White about this prior she can help you out)
#@add some code comments to get a higher grade. (What is the function doing), if needed add some more.
#@dont needa wright it on everyline but wright it really breifly on what it is doing.
#@do different varietys of errors not just the same. 