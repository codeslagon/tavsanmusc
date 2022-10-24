#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

HELP_1 = """<u>✅Sadece Gruptaki Adminler İçin Komutlar<u>✅

**➥ /durdur - Akışı duraklatır.
**➥ /devam - Akışı devam ettirir.**
**➥ /son - Akışı Sonlandırır.**
**➥ /atla - Diğer parça ya atlar.**
**✦ atla komutu aynı zamanda sıraya aldığınız istediğiniz parçaya atlar.( Örnek : /atla 3 -  3. Parçaya atlar )**
**➥ /karistir - Sıraya alınan Parçaları karışık oynatır.**
**➥ /tekrarla - oynatılan parçayı istediğiniz kadar tekrar eder.
**✦(örneğin: /tekrarla 4 - Parçayı 4 kez tekrarlar.)**
**➥ /restart - Admin Önbelleğini yeniler.
**➥ /yetkiver - Grubunuzda yetkisiz üyeye yetki vererek botu kullandırabilirsiz.**
**➥ /yetkial - Grubunuzdaki botu kullanan yetkisiz üyeden bot yetkisini alır.**
**➥ /oynatmodu - Botun kullanım ayarlarını yapabilirsiniz.**
**➥ /ayarlar ve ya /settings - komutu kullanarak botun grup içi **ayarlarını yapabilirsiniz.
**/yetkilistesi [kullanıcıadı] - Grubunuzda bota yetki verdiğiniz kişiler.**"""


HELP_2 = """<u>✅Oynat Komutları<u>

**➥ /oynat - Şarkı oynatır.
✦ /oynat komutu aynı zamanda canlı yayında destekler.(örnek: /oynat kralfm canlı)
➥ /vplay - Video Oynatır.
✦ /vplay komutu aynı zamanda canlı yayınıda destekler.(örnek: /vplay kralfm canlı)
➥ /settings - Bu komutu Grubunuzda yazarak komutları görebilirsiniz.
✅Oynatma Listeleri:
/playlist : komutla Listenize Eklediğiniz şarkılara Bakabilirsiniz..
/deleteplaylist : Oynatma Listenizdeki Şarkıları Silebilirsiniz..
/oynat Komutunu Atarak Ekranda Çıkan Playlist tıklayıp direk Listenizi oynayabilirsiniz**."""


HELP_3 = """<u>✅Bot Komutları <u>

**/stats : Bottaki Tüm İstatistikleri Görebilirsiniz. En Çok Müzik Oynatan Gruplar, Kullanıcılar, En Çok Oynatılan Müzikler Ve Daha Fazlası...
/sudolist : Bot sudo List.
/lyrics [Müzik Adı] : Sözlerine Bakmak İstediğiniz Şarkıyı Arayabilirsiniz.
/bul [Müzik Adı] veya [Youtube Linki] : Youtubedan İndirmek İstediğiniz Şarkıyı İndirebilirsiniz.
/sira : Sırada Olan Müzikler Listesini Görebilirsiniz.**"""

HELP_4 = """<u>✅Extra  Komutları <u>

/start : Botun Başlatma Panelini Gösterir. 

/settings ve ya /ayarlar : Ayarlar Menüsüne Ulaşabilirsiniz.

/yardim : Botun Yardım Menüsüne Ulaşırsınız.**
"""

HELP_5 = """🔰**<u>ADD & REMOVE SUDO USERS :</u>**
/addsudo [Username or Reply to a user]
/delsudo [Username or Reply to a user]

🛃**<u>HEROKU:</u>**
/usage - Dyno Usage.

🌐**<u>CONFIG VARS:</u>**
/get_var - Get a config var from Heroku or .env.
/del_var - Delete any var on Heroku or .env.
/set_var [Var Name] [Value] - Set a Var or Update a Var on heroku or .env. Seperate Var and its Value with a space.

🤖**<u>BOT COMMANDS:</u>**
/reboot - Reboot your Bot. 
/update - Update Bot.
/speedtest - Check server speeds
/maintenance [enable / disable] 
/logger [enable / disable] - Bot logs the searched queries in logger group.
/get_log [Number of Lines] - Get log of your bot from heroku or vps. Works for both.
/autoend [enable|disable] - Enable Auto stream end after 3 mins if no one is listening.

📈**<u>STATS COMMANDS:</u>**
/activevoice - Check active voice chats on bot.
/activevideo - Check active video calls on bot.
/stats - Check Bots Stats

⚠️**<u>BLACKLIST CHAT FUNCTION:</u>**
/blacklistchat [CHAT_ID] - Blacklist any chat from using Music Bot
/whitelistchat [CHAT_ID] - Whitelist any blacklisted chat from using Music Bot
/blacklistedchat - Check all blacklisted chats.

👤**<u>BLOCKED FUNCTION:</u>**
/block [Username or Reply to a user] - Prevents a user from using bot commands.
/unblock [Username or Reply to a user] - Remove a user from Bot's Blocked List.
/blockedusers - Check blocked Users Lists

👤**<u>GBAN FUNCTION:</u>**
/gban [Username or Reply to a user] - Gban a user from bot's served chat and stop him from using your bot.
/ungban [Username or Reply to a user] - Remove a user from Bot's gbanned List and allow him for using your bot
/gbannedusers - Check Gbanned Users Lists

🎥**<u>VIDEOCALLS FUNCTION:</u>**
/set_video_limit [Number of Chats] - Set a maximum Number of Chats allowed for Video Calls at a time. Default to 3 chats.
/videomode [download|m3u8] - If download mode is enabled, Bot will download videos instead of playing them in M3u8 form. ByDefault to M3u8. You can use download mode when any query doesnt plays in m3u8 mode.

⚡️**<u>PRIVATE BOT FUNCTION:</u>**
/authorize [CHAT_ID] - Allow a chat for using your bot.
/unauthorize [CHAT_ID] - Disallow a chat from using your bot.
/authorized - Check all allowed chats of your bot.

🌐**<u>BROADCAST FUNCTION:</u>**
/broadcast [Message or Reply to a Message] - Broadcast any message to Bot's Served Chats.

<u>options for broadcast:</u>
**-pin** : This will pin your message 
**-pinloud** : This will pin your message with loud notification
**-user** : This will broadcast your message to the users who have started your bot.
**-assistant** : This will broadcast your message from assistant account of your bot.
**-nobot** : This will force your bot to not broadcast message

**Example:** `/broadcast -user -assistant -pin Hello Testing`

"""
