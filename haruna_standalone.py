from telegram_bot.passive_bot import PassiveBot
from apscheduler.schedulers.blocking import BlockingScheduler
import json

def haruna_standalone():
    pb = PassiveBot(config_json_path="config/config.json")
    quote_dict = json.load(open("data/kanmusu_quotes.json"))

    start_quote = quote_dict['haruna_kai_ni']['start_quotes']['zh_cn']
    print(start_quote)
    pb.send_message(start_quote)

    hourly_notification_list = quote_dict['haruna_kai_ni']['hourly_notification']['zh_cn']
    scheduler = BlockingScheduler(timezone='US/Eastern')

    for hour_id, hourly_notification in enumerate(hourly_notification_list):
        scheduler.add_job(pb.send_message,
                          args=[hourly_notification],
                          trigger='cron',
                          hour=hour_id)
    scheduler.start()

if __name__ == "__main__":
    haruna_standalone()