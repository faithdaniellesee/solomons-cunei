'''
General RSA implementation: phi(n) = (p-1)(q-1)

'''
from base64 import b64encode, b64decode
import gmpy2
from gmpy2 import root, invert

e = 65537
p = 302239968944794134660889979148054548249
q = 302239968944794134818677484631621172519


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

def get_phi(p,q):
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
    phi = get_phi(p,q)
    message = "solomonrocks"
    long_int = unpack_bigint(message.encode('utf-8'))
    # print((long_int**3).bit_length() > get_n().bit_length())
    cipher = square_multiply(long_int,e,get_n())
    return b64encode(pack_bigint(cipher)).decode('utf-8')

def decrypt_message(message,p,q):
    cipher = b64decode(message)
    d = mod_inv(e,get_phi(p,q))
    decr = square_multiply(unpack_bigint(cipher),d,get_n())
    decr = pack_bigint(decr).decode('utf-8')
    return decr

# retrieve p and q, calculate d and get the message
def fermat_factor(n):
    assert n % 2 != 0
    a = gmpy2.isqrt(n)
    b = gmpy2.square(a) - n

    while not gmpy2.is_square(b):
        a += 1
        b = gmpy2.square(a) - n

    p = a + gmpy2.isqrt(b)
    q = a - gmpy2.isqrt(b)

    return int(p), int(q)

print(get_n())
cipher = encrypt_message()
print(cipher)
p,q = fermat_factor(get_n())
print(p,q)
decr = decrypt_message(cipher,p,q)
print(decr)
