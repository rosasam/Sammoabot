#! /usr/bin/python
# -*- coding: utf-8 -*-

import telegram
import logging
import random
from datetime import datetime, timedelta
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests
import re # Regex

MADNESS = False

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def start(bot, update):
	bot.sendMessage(update.message.chat_id, text="Hey there!")

def sendImage(bot, update):
	bot.sendImage(update.message.chat_id)

def echo(bot, update):
	bot.sendMessage(update.message.chat_id, text=update.message.text)

def chicken(bot, update):
	bot.sendSticker(update.message.chat_id, sticker= 'CAADBAAD_gADOvl8BrS0X6IhobrmAg')

def ylonz(bot, update):
	td = datetime(2018, 4, 21, 11) - datetime.now()
	d = td.days, td.seconds/3600, (td.seconds/60)%60, td.seconds % 60
	bot.sendMessage(update.message.chat_id, text="%s dagar, %s timmar, %s minuter, %s sekunder kvar till Ylonz!" % (d[0], d[1], d[2], d[3]))

def znoly(bot, update):
	td = datetime(2018, 4, 21, 11) - datetime.now()
	d = td.days, td.seconds/3600, (td.seconds/60)%60, td.seconds % 60
	r = ("%s dagar, %s timmar, %s minuter, %s sekunder kvar till Ylonz!" % (d[0], d[1], d[2], d[3]))[::-1]
	bot.sendMessage(update.message.chat_id, text=r)


def nope(bot, update):
	bot.sendMessage(update.message.chat_id, text="nope.")


def kandi_done(bot, update):
	m = update.message.text.split(" ")
	if len(m) < 3:
		bot.sendMessage(update.message.chat_id, text="You need to give a first and last name")
	else:
		first_name = m[1].capitalize()
		surname = m[2].capitalize()
		url = "https://aaltodoc.aalto.fi/handle/123456789/1/discover?filtertype_1=author&filter_relational_operator_1=equals&filter_1=" + surname + "%2C+" + first_name + "&filtertype_2=title&filter_relational_operator_2=contains&filter_2=&submit_apply_filter=Apply&query="
		page = requests.get(url)
		if page.text.find("Search produced no results.") == -1:
		    bot.sendMessage(update.message.chat_id, text="Yees! Congrats " + first_name + "!\n")
		else:
		    bot.sendMessage(update.message.chat_id, text="Nope.\n")


def walter_finland(bot, update):
	arrivaldate = datetime(2018, 5, 28, 0, 50)
	td = arrivaldate - datetime.now()

	d = td.days, td.seconds/3600, (td.seconds/60)%60, td.seconds % 60
	if datetime.now() > arrivaldate:
		bot.sendMessage(update.message.chat_id, text="VÄLKOMMEN TILL FINLAND WALTER!  🇫🇮🇫🇮🎉🎉")
		bot.sendMessage(update.message.chat_id, text="(Wait for it...)")
		bot.send_audio(update.message.chat_id, audio=open('hej_walter.mp3', 'rb'))
	else:
		bot.sendMessage(update.message.chat_id, text="Om ungefär %s dagar, %s timmar, %s minuter, %s sekunder är Walter i Finland!" % (d[0], d[1], d[2], d[3]))


def enable_madness(bot, update):
	sender = update.message.from_user
	id = sender.id
	sammoa_id = 108853562
	if id == sammoa_id:
		print("Madness activated")
		MADNESS = True
		bot.sendMessage(update.message.chat_id, text="RIP chat")
	else:
		bot.sendMessage(update.message.chat_id, text="Sorry, " + sender.first_name +
			", you don't have permission to do that.")
		logger.info("Madness attempted to activate with id: " + str(id) +
			", name: " + sender.first_name)


def disable_madness(bot, update):
    sender = update.message.from_user
    id = sender.id
    sammoa_id = 108853562
    if id == sammoa_id:
        MADNESS = False
        bot.sendMessage(update.message.chat_id, text="Stopping the madness")
    else:
        bot.sendMessage(update.message.chat_id, text="Sorry, " + sender.first_name +
            ", you don't have permission to do that.")

def check_madness(bot, update):
	if MADNESS:
		bot.sendMessage(update.message.chat_id, text="True")
	else:
		bot.sendMessage(update.message.chat_id, text="False")

def text_madness(bot, update):
	message = update.message.text
	if True:
		if not re.search(':D$', message, re.IGNORECASE) is None:
			bot.send_photo(update.message.chat_id, photo=open('media/DD.jpg', 'rb'))

		if not re.search('tasty', message, re.IGNORECASE) is None:
			bot.send_audio(update.message.chat_id, audio=open('media/tasty.ogg', 'rb'))

		if not re.search('yee+t', message, re.IGNORECASE) is None:
			bot.send_photo(update.message.chat_id, photo=open('media/tommy.jpg', 'rb'))

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
	dp.add_handler(CommandHandler("chicken", chicken))
	dp.add_handler(CommandHandler("ylonz", ylonz))
	dp.add_handler(CommandHandler("znoly", znoly))
	dp.add_handler(CommandHandler("eSamuelKlarMedSinKandi", nope))
	dp.add_handler(CommandHandler("eDavisKlarMedSinKandi", nope))
	dp.add_handler(CommandHandler("eWalterRedanIFinland", walter_finland))
	dp.add_handler(CommandHandler("kandi_done", kandi_done))
	dp.add_handler(CommandHandler("enablemadness", enable_madness))
	dp.add_handler(CommandHandler("disablemadness", disable_madness))
	dp.add_handler(CommandHandler("checkmadness", check_madness))
	dp.add_handler(MessageHandler(Filters.text, text_madness))
	#dp.add_handler(MessageHandler([Filters.text], echo))
	# starts the bot
	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
	main()
