
# Compare Hash Values

## Description
As a security analyst, one of the security controls we can implement is hashing. It produces a code that cannot be decrypted. It works by uniquely identifying the contents of a file, later
known as a unique identifier (hash value or digest). For example, a malicious program may mimic an original program. If one code line is different from the original program, it produces a different hash value. Security teams can then identify the malicious program and work to mitigate the risk.

## Generate Hashes
First, `ls` command shows the files within the directory.

![image](https://github.com/user-attachments/assets/2c142168-759a-4454-8b3f-a0ba71a735b7)

We can find if the files are really different or not by using the `sha256` command. From the picture below we can see both files have different hash values.

![image](https://github.com/user-attachments/assets/b3bd0f9e-4d55-4b85-b173-2a4ac7e93d38)

## Compare Hashes Files
Let’s generate the hash of the `file1.txt` and `file2.txt` to a new file for `file1hash` and `file2hash` respectively.  

![image](https://github.com/user-attachments/assets/df7a124a-d159-4a02-ae6e-92499ea2dca2)

Inspect the contents of them by using `cat` commands. Last but not least, compare both files by using `cmp` command.

![image](https://github.com/user-attachments/assets/d7417c54-0e46-46f6-8cf3-db92c873538f)

![image](https://github.com/user-attachments/assets/a5240c79-bf75-45ae-aa85-81c15b05452f)

![image](https://github.com/user-attachments/assets/4afa463d-c9c1-4480-b518-85e7165c2987)
