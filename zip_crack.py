import zipfile

wordlist = 'rockyou.txt'
zip_file = 'secret.zip'
# initialize the Zip File object
zip_file = zipfile.ZipFile(zip_file)
# count the number of words in this wordlist
num_words = len(list(open(wordlist, "rb")))
# print the total number of passwords
print "Total passwords to test: " + str(num_words)

with open(wordlist, "rb") as wordlist:
    for i, word in enumerate(wordlist):
        if i <=27 :
            print 'trying: ' + word.strip() + ' number ' + str(i)
        else:
            break
        # try:
        #     zip_file.extractall(pwd=word.strip())
        # except Exception:
        #     print "not the password"
        #     continue
        # print "[+] Password found: " + word.decode().strip()
        # exit(0)
print "[!] Password not found, try other wordlist."
