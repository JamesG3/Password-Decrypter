from time import clock

start = clock()
print 'start at:%f'%start
rock = open('rockyou_original.txt','r')
yahoo = open('YahooPsw.txt', 'r')
newpsw = open('newPsw.txt', 'w')			#those Psws which are not included in the rockyou.txt but in YahooPsw.txt

dic = {}

for line in rock:
	dic[line[:-1]] = 1
for line in yahoo:
	if line[:-2] not in dic:				#find those new Psws and save them into newPsw.txt
		newpsw.write(line)

end=clock()
print 'end:%f'%end
print 'use:%f second'%(end-start)

rock.close()
yahoo.close()
newpsw.close()