#Imports
from adventurelib import * 

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


#Define Bags


#Add Items to Bags

#Define any variables
current_room = space
	

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
	global current_room 
	if look in current_room.exits():
		current_room = current_room.exit(direction)
		print(f"You look {direction}.")
		print(current_room)



#Main Functions
def main():
	print(current_room)
	start()

if __name__ == '__main__':
	main()