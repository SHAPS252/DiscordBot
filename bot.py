import urllib.request
from bs4 import BeautifulSoup
import asyncio

import os
import discord
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
client = discord.Client()



@client.event
async def on_ready():
#    TELLS THAT THE CONNECTION WAS SUCCESSFUL
	print(f'{client.user.name} has established connection.')


@client.event
async def on_message(message):
#    WHERE THE LOOKUP OCCURS
	if message.author == client.user:
#        MAKES SURE THAT THE BOT DOES NOT RECURSIVELY RUN
		return
	if '/ud' in message.content:
#        CHECKS FOR THE KEY AND MESSAGE
		string = message.content
		string = string.split(" ")
		search = string[1:]
#        PARSE PHRASE FOR LOOKUP
		url = "https://www.urbandictionary.com/define.php?term="
		for term in search:
#            BUILDS UP URL FOR WEB SCRAPE
			url+= ("+"+term)

		try:
#            THE ACTUAL PARSING OF THE WEBPAGE TO GET THE 'DEFINITION'
			html = urllib.request.urlopen(url)
			soup = BeautifulSoup(html, 'html.parser')

			definition = soup.find(class_='meaning').get_text()
			await message.channel.send(definition)
		except:
			msg = "Phrase doesn't exist in the dictionary surprisingly."
			await message.channel.send(msg)


client.run(token)
