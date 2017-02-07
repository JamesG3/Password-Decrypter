
from time import clock
import hashlib

counter = 0

start = clock()
print 'start at:%f'%start
formspring = open('formspring.txt','r')
rock = open('RockyouEnhanced2.0.txt', 'r')
result = open('formspring_Decrypt2.txt', 'w')

#salt = 0
dic = {}
for line in formspring:
	dic[line[:-2]] = 1


for line in rock:
	counter+=1
	if counter%100000 == 0:
		print counter/100000		# print a number when each 100,000 lines from rockyou list is read.
	#if salt == 100:
	#	salt = 0
	for salt in xrange(100):						#for every line in rockyou, add salt from 00 to 99, check if exist in formspring
		plaintext = str(salt)[::-1] + line[:-1]
	#plaintext = str(salt).zfill(3) + line[:-1]
		if hashlib.sha256(plaintext).hexdigest() in dic:
			result.write(hashlib.sha256(plaintext).hexdigest()+ ' ' + plaintext[2:] + ' salt: %s'%str(salt)[::-1] +'\n')
			break

end = clock()
print "Finish, use %f second" %(end-start)

formspring.close()
result.close()
rock.close()