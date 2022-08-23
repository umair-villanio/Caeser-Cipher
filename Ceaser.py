print("Welcome to Caesar Cipher Encrypt/Decrypt\n========================================")
print('')
print("Encryption: 1")
print("Decryption: 2\n")

ed = int(input("Enter method:"))

caeser_db={"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,"m":12,"n":13,"o":14,"p":15,"q":16,"r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25}

plain_txt = input("Enter the plain text: ")

p_txt = plain_txt.lower()

key = int(input("Enter the key: "))

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)


def encrypt(word):
    
    cipher_txt=[]
    global key
    
    for i in word:
        if i.isalpha():                                                    
            p_num = caeser_db[i]+key
        
            if p_num>25:
                p_num = p_num-26

            key_lis = list(caeser_db.keys())
            val_lis = list(caeser_db.values())
            pos = val_lis.index(p_num)
        
            cipher_txt.append(key_lis[pos].upper())
            continue
    
        cipher_txt.append(i)
    print(''.join(cipher_txt))


def decrypt(word):
    
    decipher_txt=[]
    global key
    
    
    for i in word:
        if i.isalpha():
            p_num = caeser_db[i]-key
        
            if p_num<0:
                p_num = p_num+26

            key_lis = list(caeser_db.keys())
            val_lis = list(caeser_db.values())
            pos = val_lis.index(p_num)
        
            decipher_txt.append(key_lis[pos].upper())
            
            continue
        

        decipher_txt.append(i)
    print(''.join(decipher_txt))


def switch(type):
    if type==1:
        encrypt(p_txt)
    if type==2:
        decrypt(p_txt)

switch(ed)

End = input("Press Enter to close the program ")
