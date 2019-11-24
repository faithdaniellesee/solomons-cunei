# 50.042 CTF Challenge

## Team members:
- Wong Chi Seng (1002853)
- Gabriel Chan Zheng Yong (1002820)
- See Wan Yi Faith (1002851)

## Challenge description:
Bobby left a secret message for Alice within a pdf file and zipped it tight. Bobby's both a paelographer and HIGHLY skilled cryptographer, although he has a very bad habit of using weak prime numbers and hides his messages in streams? Retrieve the message as the flag in the format ```ctf{text}```.

## Challenge outline:
- Students are given:
  - PDF that is password locked.
  - Server to connect to via netcat on command line that will present them values N and e=3 and a base64 ciphertext that they will have to decipher to obtain the 12-character password to the PDF.
- The PDF contains:
  - Hidden image that needs to be found and deciphered. It will give the key to be used for on the next ciphertext after deciphering.
  - Ciphertext hidden within the metadata of the PDF that will give the flag after deciphering.

## Challenge solution:
1. Unlock 12-character passsword locked PDF
    - Connect via netcat to server on command line where they will be given: values N, e = 3 & a base64 ciphertext, `c29sb21vbnJvY2tz`.
    - Decrypt ciphertext to obtain the PDF plaintext password `solomonrocks` *(using low exponent / weak modulus attack)*:
      - Low exponent attack: Partial plaintext recovery of password where the remaining characters will have to be brute forced
      - Weak modulus attack
2. Uncover hidden image in PDF *(using steganography)*:
    - Open the PDF file using Nano and uncomment `Contents` and `Resources` by removing the `%` sign.
3. Decipher hidden image in PDF:
    - Image of [Babylonian Cuneiform numerals](https://en.wikipedia.org/wiki/Babylonian_cuneiform_numerals#/media/File:Babylonian_numerals.svg) `5, 36, 51` which will be deciphered to give a key of `20211`.
4. Uncover ciphertext `itioydrdiaucoleuntnldzrnpcadaggyzdewrtnenwuosiltousilrz` in PDF metadata under the `Author` field *(using transposition cipher)*.
5. Use the key of `20211` to decrypt the ciphertext to obtain the plaintext `discretionwillprotectyouandunderstandingwillguardyouzzz`.
    - The submitted flag can be either `CTF{discretionwillprotectyouandunderstandingwillguardyouzzz}` or `CTF{discretionwillprotectyouandunderstandingwillguardyou}`. 
