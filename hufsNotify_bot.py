import requests
from bs4 import BeautifulSoup
import os

import telegram

bot = telegram.Bot(token='632325521:AAED2kE4qeRUahZU6gvGxiW44vzhEeDLNlQ')
#chat_id = bot.getUpdates()[-1].message.chat.id
chat_id = 656764398
# 파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 공지 게시판 크롤링
req = requests.get('http://builder.hufs.ac.kr/user/indexSub.action?codyMenuSeq=37080&siteId=hufs&menuType=T&uId=4&sortChar=AB&linkUrl=04_0202.html&mainFrame=right')
req.encoding = 'utf-8'

html = req.text
soup = BeautifulSoup(html, 'html.parser')
nums = soup.select('td.no > span.mini_eng')

latest_num = nums[0].text.strip()

with open(os.path.join(BASE_DIR, 'hak_latest_num.txt'), 'r') as f_read:
    before = f_read.readline()
    f_read.close()
    if before != latest_num:
        cnt = int(latest_num)-int(before)

        for i in range(0,cnt):
            title_latest = nums[i].findNext('td').text.replace('\n','').replace('\t','').replace(' ','')
            link_latest = 'http://builder.hufs.ac.kr/user/' + nums[i].findNext('a').get('href')
            final_message = "(새 학사 공지 알림)\n" + title_latest + "\n" + link_latest
            bot.sendMessage(chat_id=chat_id, text=final_message)

        with open(os.path.join(BASE_DIR, 'hak_latest_num.txt'), 'w+') as f_write:
            f_write.write(latest_num)
            f_write.close()
