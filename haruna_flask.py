from flask import Flask, request
from telegram_bot.passive_bot import PassiveBot
import json

import haruna_utilities

app = Flask(__name__)

config_dict = json.load(open('config/config.json'))
bot_token = config_dict['telegram_bot']['bot_token']
pb = PassiveBot(config_json_path="config/config.json")

@app.route('/%s' % bot_token, methods=['POST'])
def haruna_interface():

    json_dict = request.get_json(force=True)
    print(json_dict)
    if 'entities' in json_dict['message']:
        for one_item in json_dict['message']['entities']:
            print(one_item)
            if one_item['type'] == 'bot_command':
                command_text = json_dict['message']['text']
                response_message = haruna_utilities.parse_command(command_text, config_dict)
                pb.send_message(response_message)
                break
    else:
        print('no entities')
    return 'ok'

if __name__ == '__main__':
    port_number = config_dict['infra']['port']
    fullchain_path = config_dict['infra']['fullchain_path']
    privkey_path = config_dict['infra']['privkey_path']
    app.run(host='0.0.0.0', port=port_number, ssl_context=(fullchain_path, privkey_path))