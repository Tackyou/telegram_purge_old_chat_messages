# telegram data purge
This is a more extreme and very fast version of https://github.com/seabasssec/del_my_message

Deletes everything that you're allowed to delete from telegram.<br>
Including messages from other people, photos, files, etc. everything that was sent.<br>
Deletions are for both sides (purge).<br>
One restriction: Only for chats and groups you are currently in.<br>
<b>--------------------------------------</b><br>
<b>BE CAREFUL!</b><br>
Please note that the script deletes EVERYTHING up to specified date. Including data in your public & private channels, even saved messages.<br>
<b>--------------------------------------</b><br>
You can change the date by searching this part of the code: offset_date=datetime(2023, 1, 1)
Everything before that date, will be deleted. Y, M, D

Before working with Telegram’s API, you need to get your own API ID and hash:<br>

&nbsp;&nbsp;&nbsp;&nbsp;1. Login to your Telegram account (https://my.telegram.org/) with the phone number of the developer account to use.<br>
&nbsp;&nbsp;&nbsp;&nbsp;2. Click under API Development tools.<br>
&nbsp;&nbsp;&nbsp;&nbsp;3. A Create new application window will appear. Fill in your application details. There is no need to enter any URL, and only the first two fields (App title and Short name) can currently be changed later.<br>
&nbsp;&nbsp;&nbsp;&nbsp;4. Click on Create application at the end. Remember that your API hash is secret and Telegram won’t let you revoke it. Don’t post it anywhere!<br>

requirements:<br>
&nbsp;&nbsp;&nbsp;&nbsp;telethone (pip3 install -U telethon --user)<br> 
&nbsp;&nbsp;&nbsp;&nbsp;pytz<br>

It is also worth noting that telegram traffic is blocked in some countries. In this case, use a proxy.<br>
