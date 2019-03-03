# 한국외대 공지사항 자동알림봇(텔레그램)
https://t.me/wonthechan_bot

한국외대 웹사이트 공지사항 게시판내 새 글 알림을 전송하는 텔레그램 봇입니다.

현재 [학사공지게시판](http://builder.hufs.ac.kr/user/indexSub.action?codyMenuSeq=37080&siteId=hufs&menuType=T&uId=4&sortChar=AB&linkUrl=04_0202.html&mainFrame=right), [일반공지게시판](http://builder.hufs.ac.kr/user/indexSub.action?codyMenuSeq=37079&siteId=hufs&menuType=T&uId=4&sortChar=AB&linkUrl=04_0202.html&mainFrame=right%27) 의 새 글을 30분 간격으로 확인합니다.

새 글이 있는 경우 해당 게시물의 제목과 링크를 텔레그램 봇을 통해 사용자에게 알림을 전송합니다.

### Environment
* Ubuntu 16.04
* crontab
* Python 3.5.2
* telegram
* BeautifulSoup
* requests

### Screenshots
![](https://github.com/wonthechan/hufsNotify_bot/blob/master/hufsNotify_bot_screenshot2.png?raw=true)
