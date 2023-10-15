import telebot 
from telebot import types

BOT_TOKEN = "6307221119:AAEyY703wrchFq04HZVTRKltho2XJfsOliI"
bot = telebot.TeleBot(BOT_TOKEN)

name = ''
age = ''
phone = ''

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id, 'Привет! Я бот, который поможет зарегистрироваться на курс. Оставь свои данные; и с тобой свяжемся?')
    bot.send_message(message.from_user.id, 'Напиши полное ФИО')
    bot.register_next_step_handler(message, get_age)

def get_age(message):
  global name
  name = message.text
  print(name)
  bot.send_message(message.from_user.id, 'Напиши возраст')
  bot.register_next_step_handler(message, get_phone)

def get_phone(message):
  global age 
  age = message.text
  print(age)
  bot.send_message(message.from_user.id, 'Напиши номер телефона')
  bot.register_next_step_handler(message, confirm)

def confirm(message):
  phone = message.text
  print(phone)
 
  keyboard = types.InlineKeyboardMarkup()
  key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
  keyboard.add(key_yes)
  key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
  keyboard.add(key_no)
  bot.send_message(message.from_user.id, 'Имя: ' + name + "\nВозраст: "+age+"\nНомер телефона: "+phone, reply_markup= keyboard)
  
@bot.callback_query_handler(func = lambda call: True)
def callback_worker(call):
  if call.data == "yes":
    bot.send_message(call.message.chat.id, 'Отлично! Теперь я могу вам связаться если вам нужно.')
    a = call.message.text

    with open('user_data.txt', 'a') as file:
      file.write(f"{a} \n\n")
  
    

bot.polling()