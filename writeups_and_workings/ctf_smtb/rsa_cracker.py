'''
General RSA implementation: phi(n) = (p-1)(q-1)

'''
import pyaes
import pbkdf2
import binascii
# from Crypto.PublicKey import RSA
# from 
# from base64 import b64encode, b64decode
# # import gmpy2
# # from gmpy2 import root, invert

# n = 2857033
# e = 1531081
# p = 1597
# q = 1789


def unpack_bigint(b):
    b=bytearray(b)
    return sum((1<<(bi*8))* bb for (bi,bb) in enumerate(b))

# def square_multiply(a,x,n):
#     exponent = "{0:b}".format(x)
#     res = 1
#     for i in exponent:
#         res = (res**2)%n
#         if i == '1':
#             res = (res*a)%n
#     return res

# def get_phi(p,q):
#     return (p-1)*(q-1)

# def get_n():
#     return p*q

# def eea(a,b):
#     if a == 0:
#         return (b, 0, 1)
#     else:
#         g, y, x = eea(b % a, a)
#         return (g, x - (b // a) * y, y)

# def mod_inv(e,phi_n):
#     g,x,y = eea(e,phi_n)
#     if g != 1:
#         return "Does not exist"
#     else:
#         return x%phi_n

# def pack_bigint(i):
#     b=bytearray()
#     while i:
#         b.append(i&0xFF)
#         i>>=8
#     return b


# def decrypt_message(cipher,d,n):
#     # cipher = b64decode(message)
#     # d = mod_inv(e,get_phi(p,q))
#     # cipher = unpack_bigint(cipher)
#     print(cipher)
#     decr = square_multiply(cipher,d,n)
#     # print(decr)
#     decr = pack_bigint(decr).decode('utf-8')
#     return repr(decr)

# def bitstring_to_bytes(s):
#     v = int(s, 2)
#     print(v)
#     b = bytearray()
#     while v:
#         b.append(v & 0xff)
#         v >>= 8
#     return bytes(b[::-1])


# def fermat_factor(n):
#     assert n % 2 != 0
#     a = gmpy2.isqrt(n)
#     b = gmpy2.square(a) - n

#     while not gmpy2.is_square(b):
#         a += 1
#         b = gmpy2.square(a) - n

#     p = a + gmpy2.isqrt(b)
#     q = a - gmpy2.isqrt(b)

#     return int(p), int(q)


rsa_key = RSA.importKey(open('public_key.pem','r').read())
# print(rsa_key.n,rsa_key.e)
# key = "MB4wDQYJKoZIhvcNAQEBBQADDQAwCgIDK5hJAgMXXMk="
# big_int = unpack_bigint(b64decode(key))
# decr = decrypt_message(cipher,p,q)
# print(decr)
print(p,q)
# print(get_phi(p,q))
d = mod_inv(rsa_key.e,get_phi(p,q))
print(d)
cipher = "10000000001001101011010011011011010110101011011001001111011001000001111100010111101101100011011011010110101011001000100100010111011101110000110101011001010110010011110110010000000100100001000101001000010111110111000111100011011011010110101011"
blocks = []
block_1 = '10000000001'
for i in range(11):
    blocks.append(cipher[i*22:(i+1)*22])
print(blocks)
strings = []
for i in blocks:
    # convert = bitstring_to_bytes(block_1)
    convert = int(i,2)
    dec = decrypt_message(convert,d,rsa_key.n)
    strings.append(dec)
# # bigg = pack_bigint(int(strings[9])).decode('utf-8')
# a = ''
# for x in strings: a += x
# print(a)

password = 's3cr3t*c0d3'
salt = b'\x7f\x8a\x91\xab\xc2\x0c\xe6\x8d\xc0\xd7\xba! \xd2\x80\xa1M'
print(salt)
passwordSalt = salt
# key = pbkdf2.PBKDF2(password, passwordSalt).read(32)
print('AES encryption key:', binascii.hexlify(key))
iv = "57116448576878005380785937564945681393249968307171981972903895716101015138040"
to_decrypt = "cee979b86e2c59f6caab3c6055fbfa" # transpositional
to_decrypt = "c9ee7aa5693542f0d7b63a615af6" # substitutional
to_decrypt = "ccf27fb3733944e0" # vigenere
to_decrypt = "c9f371b069" # shift
key = "c531048c47c13a7092d6ad8b36c0cc86bcef6fd4b8063acb7831c4fd2b523d68"
key = binascii.unhexlify(key)
aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(int(iv)))
decrypted = aes.decrypt(binascii.unhexlify(to_decrypt))
print('Encrypted:', decrypted)

strin = "IYTNANDTLRTRSEEDSENRLIFOAPHLUISWSOTGLDSGAEIDSTANAPSVANTSNASHIRIELHTAINARIUATCAOHVENHAETAYSOAOFFAPRD"
strin = "THISISTHEFLAGTHATYOUHAVEFINALLYATTAINEDAFTERUSINGTRANSPOSITIONALCIPHERANDRSAANDAESANDPASSWORDSOLVER"
print(strin.lower())

new_str = strin.replace('A','e')
new_str = new_str.replace('S','t')
new_str = new_str.replace('T','a')
new_str = new_str.replace('I','o')
new_str = new_str.replace('N','i')
new_str = new_str.replace('I','n')
new_str = new_str.replace('E','s')
new_str = new_str.replace('R','h')
new_str = new_str.replace('L','r')
new_str = new_str.replace('D','l')
new_str = new_str.replace('O','d')
new_str = new_str.replace('H','c')
print(strin[:33],strin[33:66],strin[66:99])


# 6, 
