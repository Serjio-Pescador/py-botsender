#!/usr/bin/python
#-*- coding: UTF-8 -*-
from sys import argv
import telebot
from config import token, receivers

bot = telebot.TeleBot(token)

script = argv
com = ''
i=1
while i < len(script):
    com += script[i] + ' '
    i += 1

if com != '':
    for receiver in receivers:
        bot.send_message(receiver, com)
