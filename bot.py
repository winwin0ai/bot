from Salahtimes import salahtimes
import telebot
from telebot import types
import json
from map import get_lat_long

def get_address(bot,message,chat_id):
        address = message.text
        lat, lng, whole_add = get_lat_long(address)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Yes")
        button2 = types.KeyboardButton("No")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, f"Is this the correct address:\n{whole_add}",reply_markup=markup)
        chat_id[str(message.chat.id)] = {'user':message.from_user.username,'lat':lat,'lng':lng, "whole":whole_add}
        return chat_id

def run():
    global chat_id

    chat_id = {}
    bot = telebot.TeleBot('BOT-API')

    try:
        with open('chat.json', 'r') as f:
            chat_id = json.load(f)
    except:
        chat_id = {}
    print(f"loaded from file: {chat_id}")

    @bot.message_handler(commands=['start'])
    def handle_start(message):
        
        bot.reply_to(message, "Welcome to salah time bot,\nthis bot tells the salah time based on your city\n\nPlease provide the address to search at:")
        chat_id = {}
        # print(chat_id)

    @bot.message_handler(func=lambda message: True)
    def handle_message(message):
        global chat_id
        
        if isinstance(message.text, str) and message.text!="/setaddress" and message.text != "/gettime" and message.text != "Get Time" and message.text != "Update Address" and message.text!="Yes" and message.text!="No":
            chat_id = get_address(bot,message,chat_id=chat_id)

        if message.text.startswith('/setaddress') or message.text.startswith('Update Address'):
            bot.send_message(message.chat.id, "Provide the address")

        elif message.text.startswith('/gettime') or message.text.startswith('Get Time'):
        
            lat_to_check = chat_id[str(message.chat.id)]["lat"] 
            lng_to_check = chat_id[str(message.chat.id)]["lng"]
            add = chat_id[str(message.chat.id)]["whole"]
            times = salahtimes(lat_to_check,lng_to_check,add)
            bot.reply_to(message,times)


        if message.text.startswith("Yes"):
            markup = types.ReplyKeyboardRemove()

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("Get Time")
            button2 = types.KeyboardButton("Update Address")
            markup.add(button1,button2)
            bot.send_message(message.chat.id,"Address saved.",reply_markup=markup)

            with open('chat.json', 'w') as f:
                json.dump(chat_id,f,indent=4)

        elif message.text.startswith("No"):
            bot.send_message(message.chat.id,"Please Provide Address Again")

        print(chat_id)

    bot.polling()


run()