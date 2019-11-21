'''
General RSA implementation: phi(n) = (p-1)(q-1)

'''
from base64 import b64encode, b64decode
import primes_template as prime
import math
import gmpy2
from gmpy2 import root

e = 3
# p = 302239968944794134660889979148054548249
# q = 302239968944794134818677484631621172519 

p = 12779877140635552275193974526927174906313992988726945426212616053383820179306398832891367199026816638983953765799977121840616466620283861630627224899026453
q = 12779877140635552275193974526927174906313992988726945426212616053383820179306398832891367199026816638983953765799977121840616466620283861630627224899027521

def unpack_bigint(b):
    b=bytearray(b)
    return sum((1<<(bi*8))* bb for (bi,bb) in enumerate(b))



def square_multiply(a,x,n):
    exponent = "{0:b}".format(x)
    res = 1
    for i in exponent:
        res = (res**2)%n
        if i == '1':
            res = (res*a)%n
    return res

def get_phi():
    return (p-1)*(q-1)
def get_n():
    return p*q

def eea(a,b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = eea(b % a, a)
        return (g, x - (b // a) * y, y)

def mod_inv(e,phi_n):
    g,x,y = eea(e,phi_n)
    if g != 1:
        return "Does not exist"
    else:
        return x%phi_n

def pack_bigint(i):
    b=bytearray()
    while i:
        b.append(i&0xFF)
        i>>=8
    return b


def encrypt_message():
    d = mod_inv(e, get_phi())
    message = "helloworldthis" #shitsucks"
    long_int = unpack_bigint(message.encode('utf-8'))
    print(long_int)
    print((long_int**3).bit_length() > get_n().bit_length())
    cipher = square_multiply(long_int,e,get_n())
    return b64encode(pack_bigint(cipher)).decode('utf-8')

def decrypt_message(message):
    cipher = b64decode(message)
    d = mod_inv(e,get_phi())
    decr = square_multiply(unpack_bigint(cipher),d,get_n())
    decr = pack_bigint(decr).decode('utf-8')
    return decr

# implement low exponent attack
def attack(c,e,n):
    m = root(c,e)
    print(int(m))
    m = pack_bigint(int(m)).decode('utf-8')
    return m

# retrieve p and q, calculate d and get the message
def fermat_factor(n):
    assert n % 2 != 0
    a = math
    b = gmpy2.square(a) - n

    while not gmpy2.is_square(b):
        a += 1
        b = gmpy2.square(a) - n

    p = a + gmpy2.isqrt(b)
    q = a - gmpy2.isqrt(b)

    return int(p), int(q)

print(get_n())
cipher = encrypt_message()
m = attack(unpack_bigint(b64decode(cipher)),3,get_n())
print(m)
