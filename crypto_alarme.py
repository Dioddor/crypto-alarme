import telebot
import requests
import time

# Telegram Bot Konfiguration
telegram_token = '6847845306:AAEfh6equcbYEXoh6Fh3_3YD8_IO-b48Pek'
bot = telebot.TeleBot(telegram_token)

# API Key für die Crypto Price API
api_key = 'RMEF9UcxIbzTc3t7aEpGLg==oZNpNyLkqJxYutfk'

# Handler für das '/price' Kommando
@bot.message_handler(commands=['price'])
def send_price(message):
    try:
        # Extrahieren der Kryptowährung aus der Nachricht
        crypto = message.text.split()[1].upper()
        
        # Abrufen des aktuellen Preises der Kryptowährung von der Crypto Price API
        api_url = f'https://api.api-ninjas.com/v1/cryptoprice?symbol={SOLUSDT}'
        headers = {'X-Api-Key': api_key}
        response = requests.get(api_url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            price = data['price']
            timestamp = data['timestamp']
            bot.reply_to(message, f'Der aktuelle Preis von {crypto} ist {price}. Zeitstempel: {timestamp}')
        else:
            bot.reply_to(message, 'Es gab ein Problem beim Abrufen des Preises. Bitte überprüfen Sie die Kryptowährung und versuchen Sie es erneut.')
    except IndexError:
        bot.reply_to(message, 'Bitte geben Sie eine Kryptowährung an. Beispiel: /price BTC')

# Handler für unbekannte Befehle
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Unbekannter Befehl. Bitte verwenden Sie /price {Kryptowährung} um den Preis abzurufen.")

# Starten des Bots
bot.polling()
