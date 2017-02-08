# Password-Decrypter
This is my solution of the homework from Information security.
For the given four lists which are leaked from database, get password in plain text format.
## yahoo
Extract plaintext using **format filter**:  
Yahoo list is a plaintext file, so we can easily find the *username & password* part from this file. To get these plaintext password, i delete those configuration informations from the file, leave those lines which contain *username & password* in the file.  
After that, i wrote a Python program to extract all the passwords, and wrote them into a new file **“YahooPsw.txt”**
## linkedin:
Using **SHA1** and **dictionary attack**:  
For each line in linkedin, there are 40 characters in hex format.  
After searching from google, i found there are several popular ways to Encrypt plaintext: **SHA1**, **MD5**, **SHA256**, because there are 40 characters in each line, the most likely method to Encrypt linkedin password is **SHA1**, which yields a string with length 40 in hex format.  
To proof this guess, i try to decrypt some lines using a [decrypt website][1]. After tried several times, i decrypted some password successfully, and those decrypted plaintext look like human password (consisted with english words, numbers, and special characters)!  
So **SHA1** is the method which linkedin password is encrypted.
However, i’ve noticed that a large number of lines in linkedin are start with ‘00000’.  I decrypt them using [decrypter website][2], then encrypt the output using **SHA1**, i found the re-encrypted result is exactly same with the original one from the **6th** character.  
Because of the large amount of possibilities, using **brute force** seems time-wasted and less-effective. So i use **dictionary attack**, which is a more effective method because the passwords in the dictionary are all human created. So there is a possibility that people use exactly same passwords with others, following the same pattern.  
Then i downloaded several dictionaries from internet ([hashkiller][3], [rockyou][4],[uniqpass][5]), some of them are really huge (hashkiller dictionary is 5GB!!).  
Obviously, the larger the dictionary is, the more password could be decrypted, but it also could be time consuming.  
So i decide to use the most popular one: **rockyou dictionary**, which is only 140MB. Then i wrote a **filter** to compare two different dictionaries, and output the passwords which are included in the second dictionary but not in the first dictionary. I used this **filter** to enhance **rockyou** dictionary with passwords from **yahoo** and **uniqpass**, yields a **rockyouEnhanced2.0.txt**, which is 181MB.  
I build a dictionary using Python to save all the **SHA1** translation and the corresponding **original plaintext** from **rockyouEnhanced2.0.txt**. Then read each line from **Linkedin.txt**, to check if it exists in the dictionary. If exist, write the translation and plaintext into the output file.   
**The output file `Linkedin_Decrypt2.txt` is 37.7 MB, 744045 lines. So the success-rate is 744045/6143150 ≈ 0.12** 
## xsplit
Using **SHA1** and **dictionary attack**:  
For xsplit password list, everything is exactly same with linkedin except the format.  
Still, using **rockyouEnhanced2.0.txt** as dictionary to crack the xsplit password.  
**The output file `xsplit_Decrypt2.txt` is 69.5 MB, 720706 lines. So the success-rate is 720706/2500000 ≈ 0.28**
## formspring
Using **SALT+SHA256** and **dictionary attack** and **brute-force**  
For each line in **formspring.txt**, there are 64 characters in hex format, which is possibly encrypted using **SHA256** (yields a 64 characters in hex format). However, using this [decrypter website][6], i couldn’t translate them into plaintext.  
I don’t know how to decrypt them until i saw [this news][7].   
And from [this link][8], i know several popular methods to **add salt**.  
So i started to try different combinations to add salt, and used dictionary attack to verify my guess. After i add a ‘0’ before or after the plaintext, some lines were written in the output file. It could be coincidence because the password could start with ‘0’, however, it also could be a way to add salt.  
This is the screenshot when i add ‘0’ in the front of plaintext
![]()  
Although there are only 9 lines, but they share a common character: **starts with two digits of number!!** However, i only add one digit in front of them. So, the salt might be two digit in front of the text!  
Then i tried **’00’ + plaintext**, yields an 33KB output file:
![]()  
It seemed closer to the answer! After i tried some different two digits salt, i found the size of output files are similar (around 33 KB).  
So, formspring might use **SHA256(SALT+Password)** (SALT is a two digits number which **changes randomly** or **increases with a same speed**)  
After i know what the salt possibly is, i tried to find the pattern of how it changes. But failed.  
Since i already know that **the salt could be any number form 00 to 99**, i wrote a loop **to add 00 to 99** in front of every password in the dictionary and check if the SHA256 translation is existed in the formspring.txt.  
**After 84 minutes, it yields an 2.9 MB outputfile `formspring_Decrypt2.txt` with 35058 lines. So the success rate is 35058/419564 ≈ 0.08**. Based on the rate from **linkedin** and **xsplit**, this is a reasonable hit rate.  
Then i open the output file **`formspring_Decrypt2.txt`** to check what are those passwords like.  
In this password list, every password looks exactly like a password! There is no obvious missed or extra part in each password. Beside, based on a reasonable hit rate, i think these are all the passwords can be Decrypted using **rockyouEnhanced2.0.txt**.  

## Other techniques i considered to crack passoword
- Using hashcat as tool to crack password
- Using brute-force to crack password (it may take a long time)
- Using web crawling to crack password (also could be a time consuming way, decrypt websites like [hashkiller][9] may have their own mechanism to prevent fast-speed web crawling)
- Download a hashkiller dictionary, use dictionary attack (This is the most effective way, because hashkiller dictionary is more than 5 GB)

## Several ways passwords were stored:
1. **Plaintext:** this is the most dangerous way, once the database is leaked, the loss is huge.
2. **Using One-Way Hash Encryption (MD5, SHA1, SHA256, SHA512, etc):** In this way, even if the databased is leaked, the encrypted text cannot be decrypted theoretically. However, hackers can use dictionary attack to try those popular passwords, if the password is not complicated enough (in other word, if your password is contained in the dictionary), it may be easy to decrypted.
3. **Using One-Way Hash Encryption add Salt:** Before saving the password into database, add a unique string for each password, then hash the whole string. In formspring.txt, the salt is from ’00’ to  ’99’, which is easy to crack.
	However, if the “salt” is the hash value of a part of username, or the first 6 digits of the double hash value of the username, it is hard to crack the password even if the database is leaked. There are several ways to [add salt][10], if the salt is added properly, it could be really difficult to encrypt.

[1]:	https://hashkiller.co.uk/sha1-decrypter.aspx
[2]:	https://hashkiller.co.uk/sha1-decrypter.aspx
[3]:	https://hashkiller.co.uk/downloads.aspx
[4]:	https://wiki.skullsecurity.org/Passwords
[5]:	https://dazzlepod.com/uniqpass/
[6]:	https://md5hashing.net/hash/sha256
[7]:	https://www.itnews.com.au/news/formspring-420000-lost-passwords-were-encrypted-salted-308425
[8]:	http://security.stackexchange.com/questions/17798/how-can-crackers-reconstruct-200k-salted-password-hashes-so-fast
[9]:	https://hashkiller.co.uk/sha1-decrypter.aspx
[10]:	http://security.stackexchange.com/questions/17798/how-can-crackers-reconstruct-200k-salted-password-hashes-so-fast

