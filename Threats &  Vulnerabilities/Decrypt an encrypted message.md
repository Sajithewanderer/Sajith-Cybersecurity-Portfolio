# Decryption

## Scenario

In this scenario, all of the files in your home directory have been encrypted. You’ll need to use Linux commands to break the Caesar cipher and decrypt the files so that you can read the hidden messages they contain.

## Solution 

1. Read the contents of a file
* Use the `ls` command to list the files in the directory:
`ls /home/analyst`.

   ![image](https://github.com/user-attachments/assets/56115596-c1d4-4883-98d7-d47cf1e3a572)

* List the contents of the README.txt file: 
`cat README.txt`.

   ![image](https://github.com/user-attachments/assets/93bc44f6-6d92-4ea4-ae3d-7bc00b5a8fcf)

The message in the README.txt file advises that the caesar subdirectory contains a hidden file.

2. Find a hidden file
* Use `cd` command to caesar subdirectory and use `ls -a` to list all files including hidden files: `cd caesar` and `ls -a`.

   ![image](https://github.com/user-attachments/assets/8d7bec56-9c09-471c-b6d9-6a3d09c2fd6a)

* Use the `cat` command to list the contents of the hidden file:
`cat .leftShift3`.

   ![image](https://github.com/user-attachments/assets/6060c2fc-8a85-47fe-b0d6-634318eeb020)

>The message appears to be scrambled due to being encrypted with a Caesar cipher. The cipher can be solved by shifting each alphabet character to the left or right by a fixed number of spaces. In this example, the shift is three letters to the left. Thus `"d"` stands for `"a"`, and `"e"`stands for `"b"`.

* Decrypt the Cipher using the command `cat` and `tr`:
`cat .leftShift3 | tr "d-za-cD-ZA-C" "a-zA-Z"`.

   ![image](https://github.com/user-attachments/assets/1207f62b-19e4-4f46-ab19-daa36a2561de)

>The tr command translates text from one set of characters to another, using a mapping. The first parameter to the tr command represents the input set of characters, and the second represents the output set of characters. Hence, if you provide parameters “abcd” and “pqrs”, and the input string to the tr command is “ac”, the output string will be “pr".

4. Decrypt a file 
* Go back to initial working directory and run this command to decrypt a file:
`openssl aes-256-cbc -pbkdf2 -a -d -in Q1.encrypted -out Q1.recovered -k ettubrute`.

   ![image](https://github.com/user-attachments/assets/0bd824c3-c1b0-4631-985a-207a99670c39)

>This command reverses the encryption of the file with a secure symmetric cipher as indicated by AES-256-CBC. The `-pbkdf2` option is used to add extra security to the key, and `-a` indicates the desired encoding for the output. The `-d` indicates decrypting, while `-in` specifies the input file and `-out` specifies the output file. The `-k` specifies the password, which in this example is ettubrute.

* Use the `ls` command and `cat Q1.recovered`.

   ![image](https://github.com/user-attachments/assets/99d14283-1532-4357-9023-8f763820ff82)


