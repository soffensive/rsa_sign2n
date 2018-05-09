import gmpy2
from gmpy2 import mpz,gcd
import binascii

p_str="19 5B 67 20 C9 75 8B BC 0D C9 66 BF 45 EF 34 F4 EE B5 98 F8 68 AC 6F E9 68 F9 25 8E 52 D9 AF D7".split(" ")
p_str.reverse()

q_str="B9 31 E8 99 AE 70 A0 D2 87 7A DE 50 B8 6B A9 B1 D7 62 31 D9 7D C5 C8 DF 47 1B F1 19 B9 23 8C D6".split(" ")
q_str.reverse()


d_str="81 98 77 41 14 B3 47 70 5E 48 A9 0F 4D 74 E3 33 D2 2A 06 BC 35 C1 0C 32 AD 50 03 50 EC 01 40 30 CD 91 48 AB A3 59 7A FA 0A 02 94 17 33 E6 90 53 22 21 D7 5F 59 06 92 0B FC 6E D6 E6 CF DF 74 08 ".split(" ")
d_str.reverse()
e=65537
p=mpz(long("".join(p_str),16))
q=mpz(long("".join(q_str),16))
d=mpz(long("".join(d_str),16))
n=p*q
# ffffffffffffffffff

m1=mpz(0x0001FFFFFFFFFFFFFFFFFF0043AD847DC0ED5CCFB74F00F2BC517D73C3527481BBDB8AA9157F2DAE1442CFA90000000000000000000000000000000000000000)

m2=mpz(0x0001FFFFFFFFFFFFFFFFFF00DEADBEEFC0ED5CCFB74F00F2BC517D73C3527481BBDB8AA9157F2DAE1442CFA90000000000000000000000000000000000000000)

#print(hex(pow(m,0x10001,n)))
s1=pow(m1,d,n)
s2=pow(m2,d,n)

print hex(s1)
print hex(s2)
print hex(n)
#print gcd(pow(s1,e)-m1,pow(s2,e)-m2) #= 85205463572397714723613165681914612274314959488841993451503280073758366370638881711629980485516487128727859115192963947071771898599882229826565357716737689

gcd_res=mpz(85205463572397714723613165681914612274314959488841993451503280073758366370638881711629980485516487128727859115192963947071771898599882229826565357716737689)
print gcd_res
for my_gcd in xrange(2,1000):
    my_n=gcd_res/my_gcd
    if pow(m1,d,my_n)==s1:
        print "n = %x (gcd: %d)" % (my_n,my_gcd)
        

