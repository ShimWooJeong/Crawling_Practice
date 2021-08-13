fr = open('test.txt', 'r')
fw = open('test_copy.txt', 'w')
fw.write(fr.read())
fw.close()
fr.close() #파일을 열면 꼭 닫아주어야 함