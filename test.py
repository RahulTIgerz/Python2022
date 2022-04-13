"""#Excercise 4.1 
print("Hello world")
print("Rahul Rao Nilapu")
print("Mrs White")
print("Kings High School")
print("5")
print("2047")
print("2122")
print("94")
print("53")
print("Tekken 7")
print("Digital Technology")

#Excercise 4.4
print("We/'re no strangers to love")
print("Frankly, my dear, I don/'t give a damn.")
print(" My definiton of a string is collection of characters these can be letters and numbers.")
print("An integer a whold number , this is numbers like 1,2,3.")
print("A float is a number which is not fully a whole number such as 1.5.")
print(543/3) 
print(543//3)
print(543%3)
print(1000%9)
print(3%5)
print(5%5)
print(555/2)
print(123/2)
print(123//2)
print(123%2)
print(764%2)
print(165//2)
print(1.2+1.3)
print(1+2)
print(10-0.5)
print(8.5-2)
print(4//2)
print(2*0.5)
print(1*2)
print("Rahul")
print("Rahul")
print("Rahul")
print("Rahul")
print("Rahul")
print("Rahul")
print("Rahul")
print("Rahul")
print("Rahul")
print("Rahul")
print("Rahul")
print("Rahul\nRahul\nRahul\nRahul\nRahul\nRahul\nRahul\nRahul\nRahul\nRahul")
print("5+10="+str(5+10))
print("15/2="+str(15/2))
print("30/2*5="+str(30/2*5))
print("30/2*5="+str(30//2*5))
#Excercise 5.4 
player_lives = 3
user_login = "login name"
money_storer = "$4.50"
phone_number = "03 456 3210"
rahul_name = "rahul" #print(rahul_name) doesnt need any quotes arround it. Because it will look for the variable player_name.
rahul_age = 15
current_year = "2022"
print(rahul_name)
print(rahul_age)
print(current_year)
rahul_surname = "rao"
rahul_school = "King's High School"
rahul_fav_food = "sushi"
rahul_imaginary_pet_name = "Snowy"
chocolate_blocks_count = 1
players_score = 5
players_highest_score = 20
laps_track = 1
amo_left = 40
current_gear = 2
current_speed = "20mps"
#Excersice 5.6
money = 200 
hat  = 20
top = 30
pants = 15
belt = 60 
shoes = 40
print(money)
print("buying a hat")
money = (money) - (hat)
print("You now have the following amount left over")
print(money)
print("buying a top")
money = (money) - (top)
print("You now have the following amount left over")
print(money)
print("buying pants")
money = (money) - (pants)
print("You now have the following amount left over")
print(money)
print("buying a belt")
money = (money) - (belt)
print("You now have the following amount left over")
print(money)
print("buying shoes")
money = (money) - (shoes)
print("You now have the following amount left over")
print(money)

#Excersice 6.3
input("Enter hi, then press enter")
input("Type your name, then press enter")
input("Type your age, then press enter")
player_name = input("Type in your name")
player_age = input("Type in your age")
fav_movie = input("Type in your favourite movie")
fav_book = input("Type in your favourite book")
an_advective = input("Type in an adjective")
an_noun = input("Type an noun")
an_verb = input("Type in a verb")
print(f"Welcome there {player_name} nice to meet you")
print("Excuse me what is your age," , player_age,", you are",player_age,"years old?")
print("So," + player_name + ", you are " + player_age + "years old")
print(f"{player_name} whats your favourite movie")
print("I love, ", fav_movie, "too")
print("I like " + fav_movie + " and " + fav_book +  " so much")
print(f"Do you like {an_verb}")
print(f"It is nice to meet you {player_name}")
player_age = int(input("What is your age"))
player_age += 10
print(player_age)
player_birth = 2022 - player_age + 10 # I added ten because the value got changed by +10 
print(player_birth) 
player_apples = int(input("How much apples do you have?"))
player_friends = int(input("How many friends do you have?"))
shared_apples = player_apples // player_friends
print(shared_apples)
player_pizzas = int(input("How many pizzas do you want"))
player_feeding = int(input("How many people are you feeding"))
pizza_slices = 8
print(player_pizzas * player_feeding * pizza_slices)
player_dollars = int(input("How many dollars do you have"))
tv_price = int(input("How much does a tv cost "))
print("You have")
print(player_dollars - tv_price)
tv_price = tv_price * 0.8 
print(tv_price)
player_bitcoins =float(input("How much bitcoins do you have"))
bitcoin_value =float(4339900)  
print(player_bitcoins * bitcoin_value) 
income = int(input("How much money do you earn each week"))
tax = float(input("What is your tax rate eg(0.15)"))
print(income * tax)
book = input("Can you give me a name of a book")
print(book)
num = int(input("Could i have a number"))
str(print(book * num)) 

#Exercises 7.5
ice_cream = int(input("How many ice creams do you need"))
if ice_cream > 0 and ice_cream <= 20:
	print("Ok I will go get it")
elif ice_cream < 20:
	print("sorry there isn't enough ice cream")

far_travel = int(input("How far do you need to travel (just a number)"))
if far_travel > 200:
	print("You might need to fill up petral")

age = int(input("How old are you"))
if age >= 18:
	print("You are now considered as an adult")
elif age < 18: 
	print("You are a minor")

fav_movie = input("Whats you favourite movie")
if fav_movie == ("Lord of the Rings"):
	print("You have excellent tastes")
else: print("It is cleary a superior film")

darth_plagueis_the_wise = input("Have you heard the tale of Darth Plagueis the Wise")
if darth_plagueis_the_wise.lower() == "no":
	print("Did you ever hear the tragedy of Darth Plagueis The Wise? I thought not. It’s not a story the Jedi would tell you. It’s a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life… He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway to many abilities some consider to be unnatural. He became so powerful… the only thing he was afraid of was losing his power, which eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. Ironic. He could save others from death, but not himself.")
else: print("You must be a fan")

passion_christ = input("Who directed Passion of the Christ")
if passion_christ.lower() == "mel gibson":
	print("correct")
else:
	print("Mel Gibson did")	

score = 0
question_1 = int(input("What is 1 + 1?"))
if question_1 == 2:
	print("correct")
	score += 1
else:
	print("incorrect")

question_2 = input("Who is president of USA?")
if question_2.lower() == ("joe biden"):
	print("correct")
	score += 1  
else:
	print("incorrect")

question_3 = input("Who is prime minister of NZ?")
if question_3.lower() == ("jacinda ardern"):
	print("correct")
	score += 1
else:
	print("incorrect")

question_4 = int(input("What is 10 -5?"))
if question_4 == 5:
	print("correct")
	score += 1
else:
	print("incorrect")

question_5 = input("Did you enjoy the quiz?")		
if question_5.lower() == ("yes"):
	print("Bonus point")
	score += 1
else:
	print("... point deduction")
	score -= 1

print(score)	


#Excersise 8.7 
fibonacci_sequence = [0,1,1,2,3,5,8,13,21,34]
print(fibonacci_sequence)

fav_fruits = ["mango","strawberry","water mellon", "grapes", "apples"]
print(fav_fruits)

fav_yt = ["Socksfor1","Socksfor2","Socksfor3","SocksReact","FatMemeGod" ]
print(fav_yt)

fav_songs = []
fav_songs.append("Tabun")
fav_songs.append("Yoru ni kakeru")
fav_songs.append("Haruka")
fav_songs.append("Ano Yume o Nazotte")
fav_songs.append("Halzion")
print(fav_songs)

books = []
book = input("What are your top 5 favourite books")
books.append(book)
books.sort()
print(books)

pizza_toppings = []
pizza_toppings = input("Would you like some toppings such as Pepperoni, Ham, Pineapple, Cheese, Tomatoes, Spinnach")
if pizza_toppings == ("Pepperoni"):
	pizza_toppings.append("Pepperoni")
if pizza_toppings == ("Ham"):
	pizza_toppings.append(pizza_toppings)
if pizza_toppings == ("Pineapple"):
	pizza_toppings.append(pizza_toppings)
if pizza_toppings == ("Cheese"):
	pizza_toppings.append(pizza_toppings)
if pizza_toppings == ("Tomatoes"):
	pizza_toppings.append(pizza_toppings)
if pizza_toppings == ("Spinnach"):
	pizza_toppings.append(pizza_toppings)
else:
	print()
print(pizza_toppings)

fruits_list = ["Mango","Strawberry","Grape","Apple","Bannana"]
fruit = input("Could you give me a name of a fruit")
if fruit == ["Mango" or "Strawberry" or "Grape" or "Apple" or "Bannana"]:
	print("Sorry im not after that fruit ")
else:
	fruits_list.append(fruit)
print(fruits_list)		 

name_list = ["Rahul","Gayatri","Prasanth","Uma","Babu"]
name_list.sort()
name_list.reverse()
print(name_list)

prime_numbers = [ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
prime_numbers.reverse()
print(prime_numbers)
print("The lenght of this list is 25 numbers long ")

comman_verbs = ["run"," jump","read","roll"]
comman_verbs.sort()
print(comman_verbs)


"""#Exercise 9.2 
print("Hi, welcome to Ice Crea, Maker")
order_complete = False
toppings_list = []

toppings_available = ["vanila","strawberry","chocolate","sprinkles","nuts","raisens","chocolate sauce","flake","m&ms"]
print("vanila\nstrawberry\nchocolate\nsprinkles\nnuts\nraisens\nchocolate sauce\nflake\nm&ms")
topping = input("Please choose your topping from the list")
if topping.lower() == toppings_available:
	print("Sweet")
else:
	print("That is not an available topping")
	print(toppings_available)



while order_complete == False:
	topping = input("What topping? - push enter to finish")
	if topping == "":
		print("Order Done")
		order_complete = True 
	elif topping in toppings_list:
		print("You already have that topping")
	else:
		print("Great, adding it to the list")
print("Here are your toppings")

topping_count = 0
while topping_count <6:
		topping_count += 1
		


# #Excercise 9.3"""  
# increments = 0
# while increments <100:
# 	increments += 2
# print(increments)	

# blast_off = 10
# while blast_off 10:
# 	blast_off 

# """	