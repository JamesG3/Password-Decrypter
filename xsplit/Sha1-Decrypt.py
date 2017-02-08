import hashlib
from time import clock

start=clock()
print "start decrypting"

source = open('xsplit_leak.txt', 'r+')				#the Encrypted file
rocklist = open('rockyouEnhanced2.0.txt', 'r')		#dictionary
result = open('xsplit_Decrypt2.txt', 'w')			#output file

dic = {}

for line in rocklist:				#build a hash table
	plaintext = line[:-1]
	dic[hashlib.sha1(plaintext).hexdigest()] = plaintext

for line in source:					#check every line in the hashtable
	if line[-42:-2] in dic:			#if exist, write file
		result.write(line[:-2]+'  '+dic[line[-42:-2]]+'\n')


end=clock()

print "Finish, use %f second" %(end-start)

source.close()
rocklist.close()
result.close()