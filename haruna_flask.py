from flask import Flask, request
import json

app = Flask(__name__)

config_dict = json.load(open('config/config.json'))
bot_token = config_dict['telegram_bot']['bot_token']

@app.route('/%s' % bot_token, methods=['POST'])
def hello():
    if request.method == 'POST':
        print(request.get_json(force=True))
    return 'ok'

if __name__ == '__main__':
    port_number = config_dict['infra']['port']
    fullchain_path = config_dict['infra']['fullchain_path']
    privkey_path = config_dict['infra']['privkey_path']
    app.run(host='0.0.0.0', port=port_number, ssl_context=(fullchain_path, privkey_path))