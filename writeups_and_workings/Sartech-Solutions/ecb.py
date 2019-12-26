#!/usr/bin/env python3
# ECB wrapper skeleton file for 50.042 FCS
# Tan Zhao Tong 1003031
# Lab 4

from present import *
import argparse
import sys
import binascii

nokeybits=80
blocksize=64

'''
args:
    infile: path of input file
    outfile: path of output file
    key: key in integer
    mode: 'e' for encryption, 'd' for decryption
'''
def ecb(infile,outfile,key,mode):
    # print(key)
    # open file handles to both files
    # fin  = open(infile, mode='r', encoding='utf-8', newline='\n')       # read mode
    finb = open(infile, mode='rb')
    # fout  = open(outfile, mode='w', encoding='utf-8', newline='\n')
    fout = open(outfile, mode='wb')      # write mode
    cb = finb.read()

    hexC = binascii.hexlify(cb).decode()
    back = binascii.unhexlify(hexC.encode())
    
    # split by blocks. 16 hex(4bits) = 64 bits per block
    PTb = [hexC[i:i+16] for i in range(0, len(hexC), 16)]
    
    # Encypting/ Decrypting Data
    CTb = [0]*len(PTb)
    if (mode == 'e'):
        for i in range(0, len(PTb)):
            # print(len(PTb[i]))
            state = hex(present(int(PTb[i],16), key))[2:]
            CTb[i] = '0'*(16 - len(state)) + state
            # print(len(CTb[i]))

    else:
        for i in range(0, len(PTb)):
            state = hex(present_inv(int(PTb[i],16), key))[2:]
            CTb[i] = '0'*(16 - len(state)) + state

    # Put Cipher Blocks together
    CT = ''.join(CTb)
    # print(len(CT)) #1852240
    cout = binascii.unhexlify(CT.encode())
    fout.write(cout)

    finb.close()
    fout.close()

if __name__=="__main__":
    parser=argparse.ArgumentParser(description='Block cipher using ECB mode.')
    parser.add_argument('-i', dest='infile',help='input file')
    parser.add_argument('-o', dest='outfile',help='output file')
    parser.add_argument('-k', dest='keyfile',help='key file')
    parser.add_argument('-m', dest='mode',help='mode')

    args=parser.parse_args()
    infile=args.infile
    outfile=args.outfile
    keyfile=int(args.keyfile.encode().decode(),16)
    # print(keyfile)
    # print(args.keyfile.encode())
    # print(binascii.hexlify(args.keyfile.encode()))
    emode=args.mode.lower() # change to lowercase here

    # Check that mode is correct
    # print(emode)
    if(emode != "e" and emode != "d"):
        print("Please use 'e' for encryption and 'd' for decryption")
        sys.exit(2)

    # print(keyfile)
    if(len(hex(keyfile)) > 22):
        print("Please use ensure that the key is 80 bits only.")
        sys.exit(2)

    ecb(infile,outfile,keyfile,emode)


