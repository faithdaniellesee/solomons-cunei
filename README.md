# 50.042 CTF Challenge

## Team members:
- Wong Chi Seng (1002853)
- Gabriel Chan Zheng Yong (1002820)
- See Wan Yi Faith (1002851)

## Challenge description:
You may crash into walls, discover new secrets and be transfigured. Find out Solomon's secret ;)  

## Challenge outline:
- Students are given:
  - Webpage with a single file upload button and the instructions: "Upload a PDF with the same SHA1 value: (given SHA1 value)" *(using SHAttered)*.
  - PDF that is password locked.
- Students are to create a PDF with the same SHA1 value and upload it onto the webpage to obtain the password to unlock the PDF.
- The PDF contains:
  - Hidden image *(using steganography)*: Image content are Babylonian cuneiform numerals that will give the key of 20211 after deciphering.
  - Cipher text hidden within the metadata of the PDF: Cipher text to be decrypted using the key obtained from the image.
