import random

def getRandPwd(pass_len):
    char = "<>/?':;{[]}+=-_*&^%$2345#sdfghjklzqwertyuRTYUIOPASDiopacvbnmx@QWEFGHJKLZXCVBNM!167890`~,.\\"
    password = ""
    for x in range(0,pass_len):
       password += random.choice(char)
    
    return password

def makeFile(website):
    with open("password.txt","a") as f:
        len_pass = int(input("Enter The Length Of Password : "))
        f.write(f"{website} : {getRandPwd(len_pass)}\n")
        f.close()

if __name__ == "__main__":
    while True:
        web = input("Enter The Name Of Website : ")
        makeFile(web)