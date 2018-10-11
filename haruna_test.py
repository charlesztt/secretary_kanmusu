from telegram_bot.passive_bot import PassiveBot

def send_a_message():
    pb = PassiveBot(config_json_path='./config/config.json')
    pb.send_message('Hello')

if __name__ == '__main__':
    send_a_message()