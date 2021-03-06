#Imports
from adventurelib import * 
Room.items = Bag()


#Define Rooms
space = Room("""
	You are drifting in space. It feels very cold.
	A slate-blue spaceship sits completely silently to your left, 
	its airlock open and waiting.
	""")

spaceship = Room("""
	The bridge if the spaceship is shiny and white, with thousands
	of small, red, blinking lights.
	""")

quaters = Room(""" 
	The quaters is a nice lively place that has enough room for 10 people.
	""") 

cargo = Room(""" 
	Cargo
	""")

hallway = Room(""" 
	You are in a small hallway which is dark and dim, 
	with some small lights
	""") 

mess_hall = Room("""
	The mess_hall is a nice place with lots of food inside.
	""") 

docking = Room( """
	Docking
	""" )

bridge = Room("""
	This bridge is a little bit wobly
	""")

escape_pods = Room("""
	An emergeny escape_pod""") 

#Define Connections
spaceship.east = hallway 
spaceship.south = quaters 
hallway.east = bridge 
hallway.north = cargo 
hallway.south = mess_hall
cargo.east = docking 
bridge.south = escape_pods 
quaters.east = mess_hall

#Define Items 
Item.description = "" #this adds a blank description to each item

knife = Item("a dirty knife","knife")
knife.description = "the knife has a dull sheen to it but it looks rather sharp."

red_keycard = Item("a red keycard","keycard","red card","red card")
red_keycard.desciprion = "Its a red keycard. It probably opens a door or a locker."

oxygen_tank = Item("a oxygen tank","oygen","oxygen tank","tank")
oxygen_tank.description = "Its a tank of oxygen. It would be very usefull out in space."

water_bottle =Item("a water bottle","water","bottle","water bottle")
water_bottle.description = "Its a water bottle. Its use is probably to be consumed."

#Define Bags
mess_hall.items.add(red_keycard)
cargo.items.add(knife)
spaceship.items.add(oxygen_tank)
hallway.items.add(water_bottle) 

#Add Items to Bags

#Define any variables
current_room = space
inventory = Bag()	

#Binds
@when("enter airlock")
@when("enter spaceship")
@when("enter ship")
def enter_spaceship():
	global current_room
	if current_room is not space:
		print("There is no airlock here!")
		return
	else:
		current_room = spaceship
		print("You heave yourself into the spaceship and slam you hand on the button to close the door.")
		print(current_room)

@when ("go DIRECTION")
def travel(direction):
	global current_room
	if direction in current_room.exits():
		current_room = current_room.exit(direction)
		print(f"You go {direction}.")
		print(current_room)


@when("look")
def look():
	print(current_room)
	print(f"there are exits to the {current_room.exits()}.")
	if len(current_room.items) > 0: #if there are some items in the room 
		print("You also see:")
		for item in current_room.items:
			print(item)#print out each item

@when("get ITEM")
@when("take ITEM")
@when("pick up ITEM")
def pickup(item):
	if item in current_room.items:
		t = current_room.items.take(item) #"t" (a temporary variable)
		inventory.add(t)
		print(f"You pick up the {item}")
	else:
		print(f"You don't see a {item}")

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