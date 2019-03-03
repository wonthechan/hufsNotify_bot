# 한국외대 공지사항 자동알림봇(텔레그램)
https://t.me/wonthechan_bot

한국외대 웹사이트 공지사항 게시판내 새 글 알림을 전송하는 텔레그램 봇입니다.

30분 간격으로 새 글이 올라왔는지 확인합니다.
현재 [학사공지게시판](http://builder.hufs.ac.kr/user/indexSub.action?codyMenuSeq=37080&siteId=hufs&menuType=T&uId=4&sortChar=AB&linkUrl=04_0202.html&mainFrame=right), [일반공지게시판](http://builder.hufs.ac.kr/user/indexSub.action?codyMenuSeq=37079&siteId=hufs&menuType=T&uId=4&sortChar=AB&linkUrl=04_0202.html&mainFrame=right%27) 의 새 글을 30분 간격으로 확인합니다.

## Environment
# Ubuntu 16.04
# crontab
# Python 3.5.2
* telegram
* BeautifulSoup
* requests
