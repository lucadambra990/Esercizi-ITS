import sys
import random

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <file name>")
    sys.exit(1)

# Ora devo leggere il file binario
data=None
with open(sys.argv[1], "rb") as f:
    data = f.read()

# ora in data o il binario del file (16 byte nel nostro caso)
# Scelgo quale byte modificare

pos = random.randint(0, len(data)-1)

byte=data[pos]

# Ora scelgo quale bit di byte modificare
bit = random.randint(0,7)
mask=1 << bit

byte = byte ^ mask

data = data[:pos] + bytes([byte]) + data[pos+1:]

with open(sys.argv[1],"wb") as f:
    f.write(data)

print(f"Ho modificato il bit {bit} del byte al posto {pos} nel file {sys.argv[1]}")

# its@its-Virtual-Machine:~/Esercizi/Sicurezza/cifra_decifra$ tail -n -99 alice.txt 
# electronic works, harmless from all liability, costs and expenses,
# including legal fees, that arise directly or indirectly from any of
# the following which you do or cause to occur: (a) distribution of this
# or any Project Gutenberg-tm work, (b) alteration, modification, or
# additions or deletions to any Project Gutenberg-tm work, and (c) any
# Defect you cause.

# Section 2. Information about the Mission of Project Gutenberg-tm

# Project Gutenberg-tm is synonymous with the free distribution of
# electronic works in formats readable by the widest variety of
# computers including obsolete, old, middle-aged and new computers. It
# exists because of the efforts of hundreds of volunteers and donations
# from people in all walks of life.

# Volunteers and financial support to provide volunteers with the
# assistance they need are critical to reaching Project Gutenberg-tm's
# goals and ensuring that the Project Gutenberg-tm collection will
# remain freely available for generations to come. In 2001, the Project
# Gutenberg Literary Archive Foundation was created to provide a secure
# and permanent future for Project Gutenberg-tm and future
# generations. To learn more about the Project Gutenberg Literary
# Archive Foundation and how your efforts and donations can help, see
# Sections 3 and 4 and the Foundation information page at
# www.gutenberg.org

# Section 3. Information about the Project Gutenberg Literary
# Archive Foundation

# The Project Gutenberg Literary Archive Foundation is a non-profit
# 501(c)(3) educational corporation organized under the laws of the
# state of Mississippi and granted tax exempt status by the Internal
# Revenue Service. The Foundation's EIN or federal tax identification
# number is 64-6221541. Contributions to the Project Gutenberg Literary
# Archive Foundation are tax deductible to the full extent permitted by
# U.S. federal laws and your state's laws.

# The Foundation's business office is located at 809 North 1500 West,
# Salt Lake City, UT 84116, (801) 596-1887. Email contact links and up
# to date contact information can be found at the Foundation's website
# and official page at www.gutenberg.org/contact

# Section 4. Information about Donations to the Project Gutenberg
# Literary Archive Foundation

# Project Gutenberg-tm depends upon and cannot survive without
# widespread public support and donations to carry out its mission of
# increasing the number of public domain and licensed works that can be
# freely distributed in machine-readable form accessible by the widest
# array of equipment including outdated equipment. Many small donations
# ($1 to $5,000) are particularly important to maintaining tax exempt
# status with the IRS.

# The Foundation is committed to complying with the laws regulating
# charities and charitable donations in all 50 states of the United
# States. Compliance requirements are not uniform and it takes a
# considerable effort, much paperwork and many fees to meet and keep up
# with these requirements. We do not solicit donations in locations
# where we have not received written confirmation of compliance. To SEND
# DONATIONS or determine the status of compliance for any particular
# state visit www.gutenberg.org/donate

# While we cannot and do not solicit contributions from states where we
# have not met the solicitation requirements, we know of no prohibition
# against accepting unsolicited donations from donors in such states who
# approach us with offers to donate.

# International donations are gratefully accepted, but we cannot make
# any statements concerning tax treatment of donations received from
# outside the United States. U.S. laws alone swamp our small staff.

# Please check the Project Gutenberg web pages for current donation
# methods and addresses. Donations are accepted in a number of other
# ways including checks, online payments and credit card donations. To
# donate, please visit: www.gutenberg.org/donate

# Section 5. General Information About Project Gutenberg-tm electronic works

# Professor Michael S. Hart was the originator of the Project
# Gutenberg-tm concept of a library of electronic works that could be
# freely shared with anyone. For forty years, he produced and
# distributed Project Gutenberg-tm eBooks with only a loose network of
# volunteer support.

# Project Gutenberg-tm eBooks are often created from several printed
# editions, all of which are confirmed as not protected by copyright in
# the U.S. unless a copyright notice is included. Thus, we do not
# necessarily keep eBooks in compliance with any particular paper
# edition.

# Most people start at our website which has the main PG search
# facility: www.gutenberg.org

# This website includes information about Project Gutenberg-tm,
# including how to make donations to the Project Gutenberg Literary
# Archive Foundation, how to help produce our new eBooks, and how to
# subscribe to our email newsletter to hear about new eBooks.


# its@its-Virtual-Machine:~/Esercizi/Sicurezza/cifra_decifra$ tail -n -99 alice.txt | head -n 1
# electronic works, harmless from all liability, costs and expenses,
# its@its-Virtual-Machine:~/Esercizi/Sicurezza/cifra_decifra$ echo -n Ciao come va,ok? >ciframi.txt
# its@its-Virtual-Machine:~/Esercizi/Sicurezza/cifra_decifra$ ll
# total 184
# drwxrwxr-x 2 its its   4096 lug 31 18:30 ./
# drwxrwxr-x 3 its its   4096 lug 31 18:04 ../
# -rw-rw-r-- 1 its its 174313 lug 31 18:18 alice.txt
# -rw-rw-r-- 1 its its     16 lug 31 18:30 ciframi.txt
# its@its-Virtual-Machine:~/Esercizi/Sicurezza/cifra_decifra$ openssl enc -e -aes-256-cbc -in ciframi.txt -out ciframi.enc -K 00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff -iv 0102030405060708090a0b0c0d0e0f10 -nopad -nosalt
# its@its-Virtual-Machine:~/Esercizi/Sicurezza/cifra_decifra$ ll -lrt
# total 188
# drwxrwxr-x 3 its its   4096 lug 31 18:04 ../
# -rw-rw-r-- 1 its its 174313 lug 31 18:18 alice.txt
# -rw-rw-r-- 1 its its     16 lug 31 18:30 ciframi.txt
# -rw-rw-r-- 1 its its     16 lug 31 18:36 ciframi.enc
# drwxrwxr-x 2 its its   4096 lug 31 18:36 ./
# its@its-Virtual-Machine:~/Esercizi/Sicurezza/cifra_decifra$ cat ciframi.enc
# ���}�����F1��bits@its-Virtual-Machine:~/Esercizi/Sicurezza/cifra_decifra$ xxd ciframi.enc
# 00000000: fed7 c016 7df0 f5b8 99f5 4631 a7be 6203  ....}.....F1..b.
# its@its-Virtual-Machine:~/Esercizi/Sicurezza/cifra_decifra$ cmp -b -l cirframi.txt ciframi.enc
# cmp: cirframi.txt: No such file or directory
# its@its-Virtual-Machine:~/Esercizi/Sicurezza/cifra_decifra$ cmp -b -l ciframi.txt ciframi.enc
#  1 103 C    376 M-~
#  2 151 i    327 M-W
#  3 141 a    300 M-@
#  4 157 o     26 ^V
#  5  40      175 }
#  6 143 c    360 M-p
#  7 157 o    365 M-u
#  8 155 m    270 M-8
#  9 145 e    231 M-^Y
# 10  40      365 M-u
# 11 166 v    106 F
# 12 141 a     61 1
# 13  54 ,    247 M-'
# 14 157 o    276 M->
# 15 153 k    142 b
# 16  77 ?      3 ^C
# its@its-Virtual-Machine:~/Esercizi/Sicurezza/cifra_decifra$ openssl enc -d -aes-256-cbc -in ciframi.enc -out ciframi.dec -K 00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff -iv 0102030405060708090a0b0c0d0e0f10 -nopad -nosalt
# its@its-Virtual-Machine:~/Esercizi/Sicurezza/cifra_decifra$ ll -lrt
# total 192
# drwxrwxr-x 3 its its   4096 lug 31 18:04 ../
# -rw-rw-r-- 1 its its 174313 lug 31 18:18 alice.txt
# -rw-rw-r-- 1 its its     16 lug 31 18:30 ciframi.txt
# -rw-rw-r-- 1 its its     16 lug 31 18:36 ciframi.enc
# -rw-rw-r-- 1 its its     16 lug 31 18:39 ciframi.dec
# drwxrwxr-x 2 its its   4096 lug 31 18:39 ./
# its@its-Virtual-Machine:~/Esercizi/Sicurezza/cifra_decifra$ cmp ciframi.txt ciframu.dec
# cmp: ciframu.dec: No such file or directory
# its@its-Virtual-Machine:~/Esercizi/Sicurezza/cifra_decifra$ cmp ciframi.txt ciframi.dec
# its@its-Virtual-Machine:~/Esercizi/Sicurezza/cifra_decifra$ cat ciframi.dec
# Ciao come va,ok?its@its-Virtual-Machine:~/Esercizi/Sicurezza/cifra_decifra$ python3 randombit.py ciframi.enc 1 123 "ciao ciao"
# ['randombit.py', 'ciframi.enc', '1', '1', 'ciframi.enc', '1', '123', 'ciao ciao']
# its@its-Virtual-Machine:~/Esercizi/Sicurezza/cifra_decifra$ python3 randombit.py ciframi.enc 1 1 ciframi.enc 1 123 "ciao ciao"
# Usage: randombit.py <file name>
# its@its-Virtual-Machine:~/Esercizi/Sicurezza/cifra_decifra$ python3 randombit.py ciframi.enc
# Ho modificato il bit 2 del byte al posto 8 nel file ciframi.enc
# its@its-Virtual-Machine:~/Esercizi/Sicurezza/cifra_decifra$ openssl enc -d -aes-256-cbc -in ciframi.txt -out ciframi.enc -K 00112233445566778899aabbccddeeff00112233445566778899aabbccddeeff -iv 0102030405060708090a0b0c0d0e0f10 -nopad -nosalt
# its@its-Virtual-Machine:~/Esercizi/Sicurezza/cifra_decifra$ cmp ciframi.txt ciframi.enc
# ciframi.txt ciframi.enc differ: byte 1, line 1
# its@its-Virtual-Machine:~/Esercizi/Sicurezza/cifra_decifra$ cmp -b -l ciframi.txt ciframi.enc
#  1 103 C    237 M-^_
#  2 151 i    273 M-;
#  3 141 a     75 =
#  4 157 o    306 M-F
#  5  40      134 \
#  6 143 c    107 G
#  7 157 o    201 M-^A
#  8 155 m    356 M-n
#  9 145 e    230 M-^X
# 10  40      335 M-]
# 11 166 v    363 M-s
# 12 141 a    206 M-^F
# 13  54 ,    320 M-P
# 14 157 o    137 _
# 15 153 k    302 M-B
# 16  77 ?    302 M-B
# its@its-Virtual-Machine:~/Esercizi/Sicurezza/cifra_decifra$ 
