import telebot
import validators
import threading

from VideoDownloader import VideoDownloader

API_KEY = '1806792473:AAGGWRNxfEmBFXt7BeOCaHeQ6Xp0iXCAurA'
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start','help'])
def help(message):
    bot.send_message(message.chat.id, "To download a YouTube video send the video url\nYou can change configurations with /config")

@bot.message_handler(func=lambda message: True)
def message_handler(message):
    thread = threading.Thread(target=checkLink, args=(message,))
    thread.start()

def checkLink(message):
    valid=validators.url(message.text)
    if valid==True:
        chat_id = message.chat.id
        downloader = VideoDownloader(message.text)
        print(message.text)
        #Send video name
        bot.send_message(chat_id, downloader.getVideoName())
        print(downloader.getVideoName())
        #Call download service
        path = downloader.downloadVideo()
        print(path)
        #Send video
        if(path != None):
            video = open(path, 'rb')
            bot.send_video(chat_id, video)
        print('end')
    else:
        bot.send_message(message.chat.id, "Invalid url")

bot.polling()