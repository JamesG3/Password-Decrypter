import hashlib
from time import clock

start=clock()
print "start decrypting"

source = open('Linkedin.txt', 'r+')						#the Encrypted file
rocklist = open('rockyouEnhanced2.0.txt', 'r')			#dictionary
result = open('Linkedin_Decrypt2.txt', 'w')				#output file

dic = {}

for line in rocklist:								#build a hash table
	plaintext = line[:-1]
	dic[hashlib.sha1(plaintext).hexdigest()[5:]] = plaintext

for line in source:									#check every line in the hashtable
	if line[5:-1] in dic:							##if exist, write file
		result.write(line[:-1]+'  '+dic[line[5:-1]]+'\n')


end=clock()

print "Finish, use %f seconds" %(end-start)

source.close()
rocklist.close()
result.close()