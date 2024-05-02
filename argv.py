#!/usr/bin/python
#-*- coding: UTF-8 -*-
from sys import argv
import telebot
from config import token

bot = telebot.TeleBot(token) #smbot

script = argv
com = ''
i=1
while i < len(script):
    com += script[i] + ' '
    i+=1

if com != '':
    bot.send_message(1183409538, com)
