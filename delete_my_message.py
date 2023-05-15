from telethon.sync import TelegramClient
from datetime import datetime, timedelta
import pytz
# api_id and api_hash you must take from https://my.telegram.org/. Create your app (any) and get it.
api_id = 0    # Your api_id in int format (for example, 1234567)
api_hash = '' # Your api_hash in str format (for example, 'deadbeef1337600613')
username = '' # Session name in str format (for example, 'Anon')

client = TelegramClient(username, api_id, api_hash)
client.start()

#dt_until_date = datetime.now() - timedelta(weeks=52)
messages_deleted = 0

print('starting..')
for dialog in client.iter_dialogs():
    print('dialog', dialog.id)
    try:
        for message in client.iter_messages(dialog.id, offset_date=datetime(2023, 1, 1)):
            try:
                messages_deleted += 1
                print('del (', format(messages_deleted), ') msg', message.id, message.date)
                message.delete() 
            except errors.FloodWaitError as e:
                print('flood timeout, sleeping', e.seconds, 'seconds')
                time.sleep(e.seconds)
    except Exception:
        print('error getting messages')
        pass

print('script ended, deletion counter:', format(messages_deleted))
