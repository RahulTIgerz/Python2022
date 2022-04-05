#Imports
from adventurelib import *
Room.items = Bag()


#Define Rooms
science_class = Room("""
	You are in a science class. You don't remember how you
	got there or who you are but you have a feeling you have
	 to get out of there, there is a door which is locked.
	""")

hallway_1 = Room("""
	You are in a dim hallway, There is another class up ahead.
	There might be something useful hidden in a corner.
	""")



#Define Connections



#Define Items



#Define Bags



#Add Items to Bags



#Define any variables
current_room = science_class


#Binds (eg "@when(look"))



#Main Function 
def main():
	print(current_room)
	start()

if __name__ == '__main__':
	main()
