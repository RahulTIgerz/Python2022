#Imports
from adventurelib import *
Room.items = Bag()


#Define Rooms
science_class = Room("""
You are in a science class. 
You don't remember how you got there or who you are but you have a feeling you have to get out of there.
There is a door which is locked. 
\nLook for a door key.
""")

hallway_1 = Room("""
The hallway is dim, There is another class to the east.
There might be something useful hidden in a corner.
\n You should look for a key or some sort 
""")

english_class = Room("""
The class has lots of books shelfs full with books, 
there is a secret passage but you need a key.
The key might be inside the tilted book.  
""")

secret_passage = Room("""
The secret passage is really dark, you see that there is a girl below 
she is laughing uncontrollably. Now you realise you need to get back.
There is a class room down ahead, drop down from the vent.
Did you pickup a vent key in the hallway?, it might be back the hallway.
""")

hallway_2 = Room("""
This hallway looks exactly the same as the one earlier. However you look 
behind and see that the girl is chasing you, you need to go west to the stairs 
to hide so she can't get to you.
""")

start_of_stairs = Room("""
You are hiding behind the starting of the stairs, she has gone up to look
for u. You feel a sharp katana, with the katana you may have the chance to defeat her
and go back home. Go north and fight her, make sure you don't forget the katana
""") 

boss_room = Room("""
You see her up next to a door which may be the way back, she is holding a
bloody knife. She sees you too and you know that she isnt going down 
without a slash. 
""")

#Define Connections
science_class.east = hallway_1
hallway_1.east = english_class
science_class.west = hallway_2
hallway_2.west = start_of_stairs
start_of_stairs.north = boss_room   


#Define Items
Item.description = "" #This adds a blank description to each item

door_key = Item("door key", "key" ,"door")
door_key.description = ("The door key is black, try it out on the science class door ")

book_key = Item("book key","key", "book")
book_key.description = ("The key is silver and rusty, maybe it could be used in the secret passage")

vent_key = Item("vent key", "vent","key")
vent_key.description = ("The vent key is white, it would be used to get out of a vent ")

katana = Item("katana","sword","weapon","blade")
katana.description = ("An authentic japanese katana, when unsheaved it is very sharp. It has a mysterious dark alluring aura ")

#Define Bags
science_class.items.add(door_key)
english_class.items.add(book_key)
secret_passage.items.add(vent_key)
boss_room.items.add(katana)


#Add Items to Bags



#Define any variables
current_room = science_class
inventory = Bag()
door_opened = False

#Binds (eg "@when(look"))

@when ("go DIRECTION")
def travel(direction):
	global current_room
	if direction in current_room.exits():
		current_room = current_room.exit(direction)
		print(f"You go {direction}.")
		print(current_room)

@when("look")
def look():
	print(f"there are exits to the {current_room.exits()}.")
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

@when("use key")
@when("use door key")
def open_door():
	global current_room
	if inventory.find("door key") and current_room == science_class:
		print("You put the key inside the door hole and twist it, you hear a click")
		global door_opened 
		door_opened = True
	else:
		print("door is locked")


@when("use key")
@when("use book key")
def open_door():
	global current_room
	if inventory.find("door key") and current_room == english_class:
		print("")
		global door_opened 
		door_opened = True
	else:
		print("door is locked")

@when("use key")
@when("use vent key")
def open_door():
	global current_room
	if inventory.find("door key") and current_room == secret_passage:
		print("")
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



#Main Function 
def main():
	print(current_room)
	start()

if __name__ == '__main__':
	main()

#add some code comments to get a higher grade. (What is the function doing)
#dont needa wright it on everyline but wright it really breifly on what it is doing.
#do different varietys of errors not just the same.
#add loops(while,for) 
