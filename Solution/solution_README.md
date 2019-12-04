# 50.042 CTF Challenge

## Challenge solution:
1. Unlock 12-character passsword locked zip file:
    - Using the given values in the `students_README.md`:
      - N = `91348998827750122993315803945306966072648090575002239502799599978804238369231`
      - e = `3`
      - A base64 ciphertext = `iegMRFmQmQ7a69yrb0JGbhUl6ydi6iHHIftbfVfOBx0=`
    - Decrypt ciphertext to obtain the PDF plaintext password `solomonrocks` *(using weak modulus attack)* by running the `rsa.py` file.
2. Uncover hidden image in PDF *(using steganography)*:
    - Open the PDF file using Nano and uncomment `Contents` and `Resources` by removing the `%` sign.
3. Decipher hidden image in PDF:
    - Image of [Babylonian Cuneiform numerals](https://en.wikipedia.org/wiki/Babylonian_cuneiform_numerals#/media/File:Babylonian_numerals.svg) `5, 36, 51` which will be deciphered to give a key of `20211`.
4. Uncover ciphertext `itioydrdiaucoleuntnldzrnpcadaggyzdewrtnenwuosiltousilrz` in PDF metadata under the `Author` field *(using transposition cipher)*.
5. Use the key of `20211` to decrypt the ciphertext to obtain the plaintext `discretionwillprotectyouandunderstandingwillguardyouzzz`.
    - The submitted flag would be `CTF{discretionwillprotectyouandunderstandingwillguardyou}`.
