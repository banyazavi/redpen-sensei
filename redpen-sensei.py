import argparse
from leetcode import get_daily_challenge
from telegram import send_message

parser = argparse.ArgumentParser(description='Push a notification by telegram for Leetcode daily challenge.')
parser.add_argument('--token', required=True, help='Telegram token of sender bot')
parser.add_argument('--chat_ids', required=True, help='List of telegram chat ids who recieved a notification. CSV format without whitespace')

args = parser.parse_args()

token = args.token
chat_ids = args.chat_ids.split(sep=',')

challenge = get_daily_challenge()
message = \
f'''[{challenge['date']}] {challenge['id']}. {challenge['title']} ({challenge['difficulty']})
{challenge['link']}'''

for id in chat_ids:
    send_message(token, id, message)
