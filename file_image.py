fr = open('image.png', 'rb')
#r로 읽는 건 txt모드니까 byte 모드로
fw = open('image_copy.png', 'wb')
fw.write(fr.read())
fr.close()
fw.close()
# with open('image.png', 'rb') as fr: 처럼 with 구문은 colse가 필요없음