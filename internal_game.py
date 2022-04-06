#Imports
from adventurelib import *
Room.items = Bag()


#Define Rooms
science_class = Room("""
	You are in a science class. You don't remember how you
	got there or who you are but you have a feeling you have
	 to get out of there, there is a door which is locked. 
	 Which requires a key.
	""")

hallway_1 = Room("""
	The hallway is dim, There is another class up ahead.
	There might be something useful hidden in a corner.
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

#add some code comments to get a higher grade. (What is the function doing)
#dont needa right it on everyline but wright it really breifly on what it is doing.
#do different varietys of errors not just the same. 