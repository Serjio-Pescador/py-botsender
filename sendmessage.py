#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
import telebot, os
from datetime import datetime
from config.py import token

bot = telebot.TeleBot(token)   #smbot

#рассылка бота мне сообщения, при обновлении файла
def send_news():
    filename = "complete.txt"
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

send_news()