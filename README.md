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
  - Webpage where they have to enter a hash value obtained using the Grøstl cryptographic hash function: `Please provide your proof of work, a Grøstl hash value ending in 16 bit's set to 0, it must be of length 21 bytes, starting with QN+yjqWfMwADrUsv.`
    - An input of the correct hash value gives them the PDF password.
- The PDF contains:
  - Hidden image *(using steganography)*: Image content are Babylonian cuneiform numerals that will give the key of `20211` after deciphering.
  - Cipher text hidden within the metadata of the PDF: Cipher text to be decrypted using the key obtained from the image to obtain the flag: `CTF{discretion_will_protect_you_and_understanding_will_guard_you}`.
