#_*_ coding: utf-8 _*_

from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os

print('Chatbot criado por Joas')

bot = ChatBot('Teste')

bot.set_trainer(ListTrainer)

for arq in os.listdir('arq'):
	chats = open('arq/' + arq, 'r').readlines()
	bot.train(chats)

while True:
	resq = input ('Você: ')

	resp = bot.get_response(resq)
	print('Asuna: ' + str(resp))
