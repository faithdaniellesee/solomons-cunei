#!/usr/bin/env python3
# Present skeleton file for 50.042 FCS
# Tan Zhao Tong 1003031
# Lab 4

# constants
FULLROUND = 31

# S-Box Layer
sbox = [0xC, 0x5, 0x6, 0xB, 0x9, 0x0, 0xA, 0xD,
        0x3, 0xE, 0xF, 0x8, 0x4, 0x7, 0x1, 0x2]

# PLayer
pmt = [0, 16, 32, 48, 1, 17, 33, 49, 2, 18, 34, 50, 3, 19, 35, 51,
       4, 20, 36, 52, 5, 21, 37, 53, 6, 22, 38, 54, 7, 23, 39, 55,
       8, 24, 40, 56, 9, 25, 41, 57, 10, 26, 42, 58, 11, 27, 43, 59,
       12, 28, 44, 60, 13, 29, 45, 61, 14, 30, 46, 62, 15, 31, 47, 63]

# Rotate left: 0b1001 --> 0b0011

def rol(val, r_bits, max_bits): return \
    (val << r_bits % max_bits) & (2**max_bits - 1) | \
    ((val & (2**max_bits - 1)) >> (max_bits - (r_bits % max_bits)))

# Rotate right: 0b1001 --> 0b1100


def ror(val, r_bits, max_bits): return \
    ((val & (2**max_bits - 1)) >> r_bits % max_bits) | \
    (val << (max_bits - (r_bits % max_bits)) & (2**max_bits - 1))


def genRoundKeys(key):
    realKey = {0: 32, 1: 0, 2: 13835058055282163712, 3: 5764633911313301505, 4: 6917540022807691265, 5: 12682149744835821666, 6: 10376317730742599722, 7: 442003720503347, 8: 11529390968771969115, 9: 14988212656689645132, 10: 3459180129660437124, 11: 16147979721148203861, 12: 17296668118696855021, 13: 9227134571072480414, 14: 4618353464114686070, 15: 8183717834812044671, 16: 1198465691292819143, 17: 2366045755749583272, 18: 13941741584329639728, 19: 14494474964360714113, 20: 7646225019617799193, 21: 13645358504996018922, 22: 554074333738726254, 23: 4786096007684651070, 24: 4741631033305121237, 25: 17717416268623621775, 26: 3100551030501750445, 27: 9708113044954383277, 28: 10149619148849421687, 29: 2165863751534438555, 30: 15021127369453955789, 31: 10061738721142127305, 32: 7902464346767349504}
    keyRegister = key
    keyDict = dict()
    keyDict[0] = 32
    # key = 0b1001
    for i in range(1,33):
        kI = bin(keyRegister)[2:]
        keyDict[i] = int(('0'*(80 - len(kI)) + kI)[:64],2)
        rKey = rol(keyRegister,61,80)
        bKey = bin(rKey)[2:]
        bKey = '0'*(80 - len(bKey)) + bKey
        fromSBox = bin(sbox[int(bKey[:4],2)])[2:]
        # print(fromSBox)
        sKey = '0'*(4 - len(fromSBox)) + fromSBox + bKey[4:]
        lsb = bin(i)[2:]
        rcPart = bin(int(sKey[60:65],2) ^ int(lsb,2))[2:]
        finalKey = sKey[:60] + '0'*(5-len(rcPart)) + rcPart + sKey[65:]
        keyRegister = int(finalKey,2)
        
    # print(keyDict)
    return keyDict

def addRoundKey(state, Ki):
    state = state ^ Ki
    return state


def sBoxLayer(state):
    sBox = {'0':'c','1':'5','2':'6','3':'b','4':'9','5':'0','6':'a','7':'d','8':'3','9':'e','a':'f','b':'8','c':'4','d':'7','e':'1','f':'2'}
    sState = hex(state)[2:]
    
    newState = ''
    if len(sState) != 16:
        sState = '0'*(16-len(sState)) + sState
    
    for i in (sState):
        newState += sBox[i]
    return int(newState,16)

def invSBoxLayer(state):
    sBox = {'c':'0','5':'1','6':'2','b':'3','9':'4','0':'5','a':'6','d':'7','3':'8','e':'9','f':'a','8':'b','4':'c','7':'d','1':'e','2':'f'}
    sState = hex(state)[2:]
    # print(hex(state)[2:])
    newState = ''
    if len(sState) != 16:
        sState = '0'*(16-len(sState)) + sState
    for i in (sState):
        newState += sBox[i]
    return int(newState,16) 


def pLayer(state):
    newState = [0]*64
    sState = bin(state)[2:]
    if len(sState) != 64:
        sState = '0'*(64-len(sState)) + sState
    # print(sState)
    for i in range(0,len(sState)):
        newState[pmt[i]] = sState[i]
    return int(''.join(newState),2)

def invPLayer(state):
    newState = [0]*64
    sState = bin(state)[2:]
    if len(sState) != 64:
        sState = '0'*(64-len(sState)) + sState
    for i in range(0,len(sState)):
        newState[i] = sState[pmt[i]]
    return int(''.join(newState),2)


def present_round(state, roundKey):
    state = addRoundKey(state, roundKey)
    state = sBoxLayer(state)
    state = pLayer(state)
    return state


def present_inv_round(state, roundKey):
    state = invPLayer(state)
    state = invSBoxLayer(state)
    state = addRoundKey(state, roundKey)
    return state


def present(plain, key):
    K = genRoundKeys(key)
    state = plain
    for i in range(1, FULLROUND + 1):
        state = present_round(state, K[i])
    state = addRoundKey(state, K[32])
    return state


def present_inv(cipher, key):
    K = genRoundKeys(key)
    state = cipher
    state = addRoundKey(state, K[32])
    for i in range(FULLROUND, 0, -1):
        state = present_inv_round(state, K[i])
    return state

if __name__ == "__main__":

    # Testvector for key schedule
    key1 = 0x00000000000000000000
    keys = genRoundKeys(key1)
    # first key starts from 1
    keysTest = {0: 32, 1: 0, 2: 13835058055282163712, 3: 5764633911313301505, 4: 6917540022807691265, 5: 12682149744835821666, 6: 10376317730742599722, 7: 442003720503347, 8: 11529390968771969115, 9: 14988212656689645132, 10: 3459180129660437124, 11: 16147979721148203861, 12: 17296668118696855021, 13: 9227134571072480414, 14: 4618353464114686070, 15: 8183717834812044671, 16: 1198465691292819143, 17: 2366045755749583272, 18: 13941741584329639728, 19: 14494474964360714113, 20: 7646225019617799193, 21: 13645358504996018922, 22: 554074333738726254, 23: 4786096007684651070, 24: 4741631033305121237, 25: 17717416268623621775, 26: 3100551030501750445, 27: 9708113044954383277, 28: 10149619148849421687, 29: 2165863751534438555, 30: 15021127369453955789, 31: 10061738721142127305, 32: 7902464346767349504}
    for k in keysTest.keys():
        assert keysTest[k] == keys[k]
    
    # Testvectors for single rounds without keyscheduling
    plain1 = 0x0000000000000000 #16
    key1 = 0x00000000000000000000 #20
    round1 = present_round(plain1, key1)
    round11 = 0xffffffff00000000 # 8 - 8 
    assert round1 == round11

    round2 = present_round(round1, key1)
    round22 = 0xff00ffff000000
    assert round2 == round22

    round3 = present_round(round2, key1)
    round33 = 0xcc3fcc3f33c00000
    assert round3 == round33

    # invert single rounds
    plain11 = present_inv_round(round1, key1)
    assert plain1 == plain11
    plain22 = present_inv_round(round2, key1)
    assert round1 == plain22
    plain33 = present_inv_round(round3, key1)
    assert round2 == plain33
  
    # Everything together
    # print("----- 1 -----")
    plain1 = 0x0000000000000000
    key1 = 0x00000000000000000000
    cipher1 = present(plain1, key1)
    plain11 = present_inv(cipher1, key1)
    assert plain1 == plain11

    # print("----- 2 -----")
    plain2 = 0x0000000000000000
    key2 = 0xFFFFFFFFFFFFFFFFFFFF
    cipher2 = present(plain2, key2)
    plain22 = present_inv(cipher2, key2)
    assert plain2 == plain22

    # print("----- 3 -----")
    plain3 = 0xFFFFFFFFFFFFFFFF
    key3 = 0x00000000000000000000
    cipher3 = present(plain3, key3)
    plain33 = present_inv(cipher3, key3)
    assert plain3 == plain33

    # print("----- 4 -----")
    plain4 = 0xFFFFFFFFFFFFFFFF
    key4 = 0xFFFFFFFFFFFFFFFFFFFF
    cipher4 = present(plain4, key4)
    plain44 = present_inv(cipher4, key4)
    assert plain4 == plain44

    