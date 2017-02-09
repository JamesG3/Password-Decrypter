#pick the password out from the original file
yahoo = open('Yahoo.txt', 'r')
result = open('YahooPsw.txt','w')

for line in yahoo:
	tem = line[(line.index(':')+1):]
	result.write(tem[(tem.index(':')+1):])

yahoo.close()
result.close()