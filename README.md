# 50.042 CTF Challenge

## Team members:
- Wong Chi Seng (1002853)
- Gabriel Chan Zheng Yong (1002820)
- See Wan Yi Faith (1002851)

## Challenge description:
You may crash into walls, discover new secrets and be transfigured. Find out Solomon's secret ;)  

## Challenge outline:
- Students are given:
  - PDF that is password locked.
  - Server to connect to via netcat on command line that will present them values N and e=3 and a base 64 ciphertext. They will then be tasked to decrypt the ciphertext either by low exponent attack or weak modulus attack. Choosing to use the low exponent attack will result in a partial plaintext recovery and the remaining characters will have to be brute forced.
    - An input of the correct hash value gives them the PDF password.
- The PDF contains:
  - Hidden image *(using steganography)*: Image content is Babylonian cuneiform numerals that will give the key of `20211` after deciphering.
  - The ciphertext is hidden within the metadata of the PDF: Ciphertext (transposition cipher) to be decrypted using the key obtained from the image to obtain the flag: `CTF{discretion_will_protect_you_and_understanding_will_guard_you}`.
