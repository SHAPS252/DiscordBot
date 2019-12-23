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
	print(f'{client.user.name} has established connection.')


@client.event
async def on_message(message):
	if message.author == client.user:
		return
	if '/ud' in message.content:
		string = message.content
		string = string.split(" ")
		search = string[1:]
		url = "https://www.urbandictionary.com/define.php?term="
		for term in search:
			url+= ("+"+term)

		try:
			html = urllib.request.urlopen(url)
			soup = BeautifulSoup(html, 'html.parser')

			definition = soup.find(class_='meaning').get_text()
			await message.channel.send(definition)
		except:
			msg = "Phrase doesn't exist in the dictionary surprisingly."
			await message.channel.send(msg)


client.run(token)


# URL FROM WHICH TO PASS IN CMD ARGUMENT FOR EXTRACTION
# search = "ajdkah"
# search = search.split(' ')
# url = "https://www.urbandictionary.com/define.php?term="
# for term in search:
# 	url += ("+"+term)

# try:
# 	html = urllib.request.urlopen(url)
# 	# BEAUTIFUL SOUP OBJECT TO PARSE
# 	soup = BeautifulSoup(html, 'html.parser')

# 	# TEST
# 	definition = soup.find(class_='meaning').get_text()
# 	print(definition)
# except:
# 	print("Phrase doesn't exist in the dictionary surprisingly.")

# html = urllib.request.urlopen(url)

# # BEAUTIFUL SOUP OBJECT TO PARSE
# soup = BeautifulSoup(html, 'html.parser')

# # TEST
# definition = soup.find(class_='meaning').get_text()
# class_= 'shrug space'
# print(definition)
