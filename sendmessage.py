#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
import telebot, os
from datetime import datetime
from config import token

bot = telebot.TeleBot(token)   #smbot
filename = "complete.txt"
isExisting = os.path.exists(filename)

#рассылка бота мне сообщения, при обновлении файла
def send_news():
    mtime = os.path.getmtime(filename)
    mtime_readable = datetime.fromtimestamp(mtime)
    delta_new = datetime.now() - mtime_readable
    diff_in_minutes = delta_new.total_seconds() / 60
    #print(delta_new, diff_in_minutes)
    if diff_in_minutes < 2:
        #print('новый файл')
        docu = open(filename, 'rb')
        bot.send_message(1183409538, f'🤖 Для вас новый файл:')
        bot.send_document(1183409538, docu)
    else:
        return
if isExisting :
    send_news()