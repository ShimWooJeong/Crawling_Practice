from os import close
import urllib.request as req
import re
# 웹 스크래핑

rep = req.urlopen('https://daum.net') #1. 원하는 주소로 가서
#urlopen 메소드는 특정 주소의 데이터를 다운

data = rep.read().decode('utf8') #2. 그 데이터를 텍스트로 만들고

result = re.findall('https://[./-_0-9a-zA-Z]+.jpg', data) #3. 그 텍스트에서 정규식을 이용해 원하는 정보를 뽑아내고
#data 속에서 .jpg를 찾아라
for link in result:
    idx = link.rfind('/')
    #link.rfind('/') 문자열을 오른쪽부터 찾아 들어가서 /이 문자가 나타나는 그 때 인덱스 반환
    #이유는 이미지 파일명이 / 이후에 적혀있기 때문에
    with open(link[idx+1:], "wb") as f:
        #link라는 문자열 슬라이싱, idx+1부터 끝:까지 슬라이싱한 것을 파일명으로 만듬
        pic = req.urlopen(link)
        f.write(pic.read()) #4. 거기에 맞는 처리를 해줌
        #pic에 대한 데이터를 읽어서 그대로 저장

        #http://... 링크 주소에 가서 request를 보내 response를 받은 데이터를 byte 단위로 씀 
 
#[0-9a-zA-Z]가 들어있는데 이것이 반복한다해서 +를 붙임
#\w는 모든 문자열을 의미
#print(result)

#f = open('daum.html', 'w') #byte형태로 받아오면 utf8로 decode할 필요없이 받아올 수 있음
#f.write(rep.read().decode('utf8'))
#f.close()

#print(rep.getheaders())
#getheaders 메소드는 header안에 들어있는 메소드들이 리스트화되어 가져옴
#getheader("") 메소드는 특정 값에 맞는 것을 가져옴
#status 메소드는 이 요청이 어떤 상태로 반환이 되었나
