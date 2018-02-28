#! /usr/bin/python
# -*- coding: utf-8 -*-

import telegram
import logging
import random
from datetime import datetime, timedelta
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


#bot = telegram.Bot(token='251187693:AAFjWHcpWBBAQzZRuWat-vLWA6hWAouFAJo')

def start(bot, update):
	bot.sendMessage(update.message.chat_id, text="Hey there!")

def sendImage(bot, update):
	bot.sendImage(update.message.chat_id)

def echo(bot, update):
	bot.sendMessage(update.message.chat_id, text=update.message.text)

def pokemon(bot, update):
	m = update.message.text
	i = m.find('@')
	n = ''

	if i == -1:
		n = m[9:].strip()
	else:
		n = m[9:i].strip()

	if n.isdigit() != True:
		bot.sendMessage(update.message.chat_id, text= "Use digits")
	elif int(n) > 0 and int(n) < 152:
		bot.sendMessage(update.message.chat_id, text='http://bulbapedia.bulbagarden.net/wiki/' + pokemons[int(n) - 1] + '_(Pok%C3%A9mon)')
		bot.sendPhoto(update.message.chat_id, photo=open(pokeimgs[int(n) - 1], 'rb'))
	else:
		bot.sendMessage(update.message.chat_id, text="Only first generation pokémon can be searched.")

def bulbasaur(bot, update):
	bot.sendPhoto(update.message.chat_id, photo='http://cdn.bulbagarden.net/upload/2/21/001Bulbasaur.png')

def random_rick(bot, update):
	character = rm_characters[random.randint(0, len(rm_characters))]
	bot.sendMessage(update.message.chat_id, text= character + '\n\n' + create_rm_url(character))

def create_rm_url(name):
	return 'http://rickandmorty.wikia.com/wiki/' + name.replace(' ','_')

def chicken(bot, update):
	bot.sendSticker(update.message.chat_id, sticker= 'CAADBAAD_gADOvl8BrS0X6IhobrmAg')

def ylonz(bot, update):
	td = datetime(2018, 4, 21, 11) - datetime.now()
	d = td.days, td.seconds/3600, (td.seconds/60)%60, td.seconds % 60
	bot.sendMessage(update.message.chat_id, text="%s dagar, %s timmar, %s minuter, %s sekunder kvar till Ylonz!" % (d[0], d[1], d[2], d[3]))

def nope(bot, update):
	bot.sendMessage(update.message.chat_id, text="nope.")

def kandi_done(bot, update):
	m = update.message.text.split(" ")
	if len(m) < 3:
		bot.sendMessage(update.message.chat_id, text="You need to give a first and last name")
	else:
		first_name = m[1].capitalize()
		surname = m[2].capitalize()
		url = "https://aaltodoc.aalto.fi/handle/123456789/12/discover?filtertype_1=author&filter_relational_operator_1=equals&filter_1=" + surname + "%2C+" + first_name + "&filtertype_3=title&filter_relational_operator_3=contains&filter_3=&submit_apply_filter=Apply&query="
		page = requests.get(url)
		if page.text.find("Search produced no results.") == -1:
		    bot.sendMessage(update.message.chat_id, text="Yees! Congrats " + first_name + "!\n")
		else:
		    bot.sendMessage(update.message.chat_id, text="Nope.\n")

def walter_finland(bot, update):
	td = datetime(2018, 5, 28) - datetime.now()
	d = td.days, td.seconds/3600, (td.seconds/60)%60, td.seconds % 60
	bot.sendMessage(update.message.chat_id, text="Om ungefär %s dagar, %s timmar, %s minuter, %s sekunder är Walter i Finland!" % (d[0], d[1], d[2], d[3]))


rm_characters = ["Abradolf Lincler", "Albert Einstein", "Alexander", "Alien Morty", "Alien Parasites", "Alien Rick", "Amish Cyborg", "Annie", "Antenna Morty", "Antenna Rick", "Ants in my Eyes Johnson", "Armagheadon", "Arthricia", "Artist Morty", "Attila Starwar", "Baby Legs", "Baby Wizard", "Bearded Lady", "Benjamin", "Beta-Seven", "Beth Sanchez (C-500A)", "Beth Smith", "Beth Smith (C-132)", "Beth Smith (C-137)", "Beth Smith (Evil Rick's Target Dimension)", "Beth's Mytholog", "Big Boobed Waitress", "Birdperson", "Blamphs", "Blim Blam", "Blue Shirt Morty", "Bobby Moynihan", "Brad", "Brad Anderson", "Centaur", "Chris", "Chris (The Ricks Must Be Crazy)", "Coach Feratu", "Comedian", "Courier Flap", "Cousin Nicky", "Cowboy Morty", "Cowboy Rick", "Creepy Little Girl", "Cromulons", "Cronenberg Morty", "Cronenberg Rick", "Cult Leader Morty", "Cyclops Morty", "Cyclops Rick", "Cynthia", "Cynthia (Rixty Minutes)", "Dale", "Daron Jefferson", "David Letterman", "Davin", "Diseases", "Donna Gueterman", "Doofus Rick", "Dr. Glip-Glop", "Dr. Schmidt", "Dr. Xenon Bloom", "Duck With Muscles", "Eric Stoltz Mask Morty", "Ethan", "Evil Beth Clone", "Evil Jerry Clone", "Evil Morty", "Evil Rick", "Evil Summer Clone", "Eyeholes Man", "Fart", "Father Bob", "Fish Morty", "Fish Rick", "Fleeb", "Flex Xando", "Frank Palicky", "Frankenstein's Monster", "Fulgora", "Gar Gloonch", "Gar's Mytholog", "Garblovians", "Garmanarnar", "Gazorpazorpfield (Character)", "Gene Vagina", "General Nathan", "General Star", "Ghost in a Jar", "Glenn", "Glenn (Rixty Minutes)", "Glexo Slim Slom", "Goddess Beth", "Gromflomites", "Hammerhead Morty", "Hamsters In Butts", "Hamurai", "Hole in the Wall Where the Men Can See it All", "Hunter", "Hunter's Dad", "Hydrogen-F", "Ice-T", "Ideal Jerry", "Jacob", "Jamey", "Jan Michael Vincent", "Jerry Smith", "Jerry Smith (C-137)", "Jerry Smith (C-500A)", "Jerry Smith (Dimension 5-126)", "Jerry Smith (Evil Rick's Target Dimension)", "Jerry's Mytholog", "Jessica", "Jessica's Friend", "Jew", "Johnny Depp", "Jon", "Joyce Smith (C-137)", "Karen Entity", "Katherine Heffelfinger", "Kevin", "King Flippy Nips", "King Jellybean", "Kristen Stewart", "Krombopulos Michael", "Kyle", "Leonard Smith (C-137)", "Lighthouse Chief", "Little Dipper", "Loggins", "Long Sleeved Morty", "Lucy", "Ma-Sha", "Magma-Q", "Magnesium-J", "Man Painted Silver Who Makes Robot Noises", "Maximums Rickimus", "MC Haps", "Melissa", "Michael Denny and the Denny Singers", "Michael McLick", "Michael Thompson", "Morty Jr.", "Morty Smith", "Morty Smith (C-132)", "Morty Smith (Evil Rick's Target Dimension)", "Morty Smith (replacement dimension)", "Mr. Beauregard", "Mr. Benson", "Mr. Booby Buyer", "Mr. Goldenfold", "Mr. Marklovitz", "Mr. Meeseeks", "Mr. Needful", "Mr. Poopybutthole", "Mr. Sneezy", "Mrs. Pancakes", "Mrs. Refrigerator", "Mrs. Sanchez", "Mrs. Sullivan", "Mysterious Rick", "Nancy", "Numbericons", "Octopus Man", "Pat Gueterman", "Paul Fleishman", "Pencilvester", "Phillip Jacobs", "Photography Raptor", "Pichael Thompson", "Pickle Rick", "Pickles the Drummer", "Piece of Toast", "Poncho", "Prince Nebulon", "Professor Tock", "Purge Planet Ruler", "Quantum Rick", "Randy Dicknose", "Real Fake Doors Salesman", "Regular Legs", "Reverse Giraffe", "Revolio Clockberg Jr.", "Rick Prime", "Rick Sanchez", "Rick Sanchez (Dimension C-132)", "Rick Sanchez (Evil Rick's Target Dimension)", "Rick Sanchez (replacement dimension)", "Rick Sanchez (Rick and Morty in: Adventure to an Alternate Universe!)", "Rick's Father", "Ricktiminus Sancheziminius", "Riq IV", "Robot Morty", "Robot Rick", "Roger", "Ron Benson", "Ruben", "Scary Brandon", "Scary Terry", "Scroopy Noopers", "Scropon", "Self-Congratulatory Jerry", "Shlaammi", "Shleemypants", "Shmlamantha Shmlicelli", "Shmlangela Shmlobinson-Shmlower", "Shmlona Shmlobinson", "Shmlonathan Shmlower", "Shmlony Shmlicelli", "Shrimply Pibbles", "Simon", "Sleepy Gary", "Slippery Stair", "Slow Mobius", "Snuffles", "Solicitor Rick", "Squanchy", "Stealy", "Steven Phillips", "Stu", "Summer Smith", "Summer Smith (C-132)", "Summer Smith (C-137)", "Summer Smith (Evil Rick’s Target Dimension)", "Taddy Mason", "Tammy Gueterman", "The One True Morty", "The President", "The President of the Miniverse", "The Scientist Formerly Known as Rick", "Three Unknown Things", "Tinkles", "Tiny Rick", "Toby Matthews", "Todd Crystal", "Tophat Jones", "Tortured Mortys", "Traflorkians", "Trunk People", "Two Guys with Handlebar Mustaches", "Uncle Steve", "Unity", "Unmuscular Michaels", "Unnamed Uncle", "Vampire Master", "Yellow Shirt Rick", "Zarbadar Gloonch", "Zarbadar’s Mytholog", "Zeep Xanflorp", "Zeta Alpha Rick"]
pokemons = ["Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard", "Squirtle", "Wartortle", "Blastoise", "Caterpie", "Metapod", "Butterfree", "Weedle", "Kakuna", "Beedrill", "Pidgey", "Pidgeotto", "Pidgeot", "Rattata", "Raticate", "Spearow", "Fearow", "Ekans", "Arbok", "Pikachu", "Raichu", "Sandshrew", "Sandslash", "Nidoran♀", "Nidorina", "Nidoqueen", "Nidoran♂", "Nidorino", "Nidoking", "Clefairy", "Clefable", "Vulpix", "Ninetales", "Jigglypuff", "Wigglytuff", "Zubat", "Golbat", "Oddish", "Gloom", "Vileplume", "Paras", "Parasect", "Venonat", "Venomoth", "Diglett", "Dugtrio", "Meowth", "Persian", "Psyduck", "Golduck", "Mankey", "Primeape", "Growlithe", "Arcanine", "Poliwag", "Poliwhirl", "Poliwrath", "Abra", "Kadabra", "Alakazam", "Machop", "Machoke", "Machamp", "Bellsprout", "Weepinbell", "Victreebel", "Tentacool", "Tentacruel", "Geodude", "Graveler", "Golem", "Ponyta", "Rapidash", "Slowpoke", "Slowbro", "Magnemite", "Magneton", "Farfetch'd", "Doduo", "Dodrio", "Seel", "Dewgong", "Grimer", "Muk", "Shellder", "Cloyster", "Gastly", "Haunter", "Gengar", "Onix", "Drowzee", "Hypno", "Krabby", "Kingler", "Voltorb", "Electrode", "Exeggcute", "Exeggutor", "Cubone", "Marowakv", "Hitmonlee", "Hitmonchan", "Lickitung", "Koffing", "Weezing", "Rhyhorn", "Rhydon", "Chansey", "Tangela", "Kangaskhan", "Horsea", "Seadra", "Goldeen", "Seaking", "Staryu", "Starmie", "Mr._Mime", "Scyther", "Jynx", "Electabuzz", "Magmar", "Pinsir", "Tauros", "Magikarp", "Gyarados", "Lapras", "Ditto", "Eevee", "Vaporeon", "Jolteon", "Flareon", "Porygon", "Omanyte", "Omastar", "Kabuto", "Kabutops", "Aerodactyl", "Snorlax", "Articuno", "Zapdos", "Moltres", "Dratini", "Dragonair", "Dragonite", "Mewtwo", "Mew"]
pokeimgs = ['gen1/1.png', 'gen1/2.png', 'gen1/3.png', 'gen1/4.png', 'gen1/5.png', 'gen1/6.png', 'gen1/7.png', 'gen1/8.png', 'gen1/9.png', 'gen1/10.png', 'gen1/11.png', 'gen1/12.png', 'gen1/13.png', 'gen1/14.png', 'gen1/15.png', 'gen1/16.png', 'gen1/17.png', 'gen1/18.png', 'gen1/19.png', 'gen1/20.png', 'gen1/21.png', 'gen1/22.png', 'gen1/23.png', 'gen1/24.png', 'gen1/25.png', 'gen1/26.png', 'gen1/27.png', 'gen1/28.png', 'gen1/29.png', 'gen1/30.png', 'gen1/31.png', 'gen1/32.png', 'gen1/33.png', 'gen1/34.png', 'gen1/35.png', 'gen1/36.png', 'gen1/37.png', 'gen1/38.png', 'gen1/39.png', 'gen1/40.png', 'gen1/41.png', 'gen1/42.png', 'gen1/43.png', 'gen1/44.png', 'gen1/45.png', 'gen1/46.png', 'gen1/47.png', 'gen1/48.png', 'gen1/49.png', 'gen1/50.png', 'gen1/51.png', 'gen1/52.png', 'gen1/53.png', 'gen1/54.png', 'gen1/55.png', 'gen1/56.png', 'gen1/57.png', 'gen1/58.png', 'gen1/59.png', 'gen1/60.png', 'gen1/61.png', 'gen1/62.png', 'gen1/63.png', 'gen1/64.png', 'gen1/65.png', 'gen1/66.png', 'gen1/67.png', 'gen1/68.png', 'gen1/69.png', 'gen1/70.png', 'gen1/71.png', 'gen1/72.png', 'gen1/73.png', 'gen1/74.png', 'gen1/75.png', 'gen1/76.png', 'gen1/77.png', 'gen1/78.png', 'gen1/79.png', 'gen1/80.png', 'gen1/81.png', 'gen1/82.png', 'gen1/83.png', 'gen1/84.png', 'gen1/85.png', 'gen1/86.png', 'gen1/87.png', 'gen1/88.png', 'gen1/89.png', 'gen1/90.png', 'gen1/91.png', 'gen1/92.png', 'gen1/93.png', 'gen1/94.png', 'gen1/95.png', 'gen1/96.png', 'gen1/97.png', 'gen1/98.png', 'gen1/99.png', 'gen1/100.png', 'gen1/101.png', 'gen1/102.png', 'gen1/103.png', 'gen1/104.png', 'gen1/105.png', 'gen1/106.png', 'gen1/107.png', 'gen1/108.png', 'gen1/109.png', 'gen1/110.png', 'gen1/111.png', 'gen1/112.png', 'gen1/113.png', 'gen1/114.png', 'gen1/115.png', 'gen1/116.png', 'gen1/117.png', 'gen1/118.png', 'gen1/119.png', 'gen1/120.png', 'gen1/121.png', 'gen1/122.png', 'gen1/123.png', 'gen1/124.png', 'gen1/125.png', 'gen1/126.png', 'gen1/127.png', 'gen1/128.png', 'gen1/129.png', 'gen1/130.png', 'gen1/131.png', 'gen1/132.png', 'gen1/133.png', 'gen1/134.png', 'gen1/135.png', 'gen1/136.png', 'gen1/137.png', 'gen1/138.png', 'gen1/139.png', 'gen1/140.png', 'gen1/141.png', 'gen1/142.png', 'gen1/143.png', 'gen1/144.png', 'gen1/145.png', 'gen1/146.png', 'gen1/147.png', 'gen1/148.png', 'gen1/149.png', 'gen1/150.png', 'gen1/151.png']

def main():
	# Read token file
	# The token should never be shared, be sure to have "token.txt" in gitignore
	tokenfile = open('token.txt', 'r')
	token = tokenfile.read()
	# The token string contains a newline character, which is removed with [:-1]
	updater	= Updater(token=token[:-1])
	dp = updater.dispatcher

	# Map commands to functions
	# These are the keywords a telegram user can call the bot with
	dp.add_handler(CommandHandler("start", start))
	dp.add_handler(CommandHandler("bulbasaur", bulbasaur))
	dp.add_handler(CommandHandler("pokemon", pokemon))
	dp.add_handler(CommandHandler("random_rick", random_rick))
	dp.add_handler(CommandHandler("chicken", chicken))
	dp.add_handler(CommandHandler("ylonz", ylonz))
	dp.add_handler(CommandHandler("eSamuelKlarMedSinKandi", nope))
	dp.add_handler(CommandHandler("eDavisKlarMedSinKandi", nope))
	dp.add_handler(CommandHandler("eWalterRedanIFinland", walter_finland))
	dp.add_handler(CommandHandler("kandi_done", kandi_done))
	#dp.add_handler(MessageHandler([Filters.text], echo))

	# starts the bot
	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
	main()
