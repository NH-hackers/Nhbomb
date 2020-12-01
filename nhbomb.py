#colors values 
Red = '\033[1;31m'
Blue= '\033[1;32m'
Endc = '\033[0m'
import subprocess
import sys
import os
import random
import subprocess
import sys
import time
import platform
import webbrowser
line = '--------------------------------------------'

def clr():
    try:
        if os.name == "nt":
            os.system('cls')
        else :
            os.system('clear')
    except:
            print(Blue+line,'\n')
            print('\n\tSomething Wrong to Clear ..\n\n       Please Contact To Developer ')
            print('\n\t     Error : 500\n')
            print(line)
            print(Red+'\n\t\t[ Sub Menu ]')
            print(Blue +'''\n[01] Contact To Developer\n[02] Again Run HPomb Tool''')
            error500 = input('\nChoose One Options : ')
            if error500 == 1:
                subprocess.call([sys.executable, 'core/contact.py'])
            else: 
                subprocess.call([sys.executable, 'hpomb.py'])
            

def banner():
    clr()
    logo="""

███╗   ██╗██╗  ██╗                  
████╗  ██║██║  ██║                  
██╔██╗ ██║███████║                  
██║╚██╗██║██╔══██║                  
██║ ╚████║██║  ██║                  
╚═╝  ╚═══╝╚═╝  ╚═╝                  
                                    
██████╗  ██████╗ ███╗   ███╗██████╗ 
██╔══██╗██╔═══██╗████╗ ████║██╔══██╗
██████╔╝██║   ██║██╔████╔██║██████╔╝
██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗
██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝
╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ 
               ""","""
----------------   ----------------------
|  nikhil3711  |   | Version : 1.0.2020 |
----------------   ----------------------

\tCreated by https://github.com/nikhil3711

-------------------------------------------- """
    print(Red+logo[0]+Blue+logo[1])

def installational():
    banner()
    install = '.install'
    instflw = open(install,'a')
    instfl = open(install,'r')
    instflr = instfl.read()
    if instflr :
        pass
    else:
        print('\t Please Wait HPomb Install\n\n')
        os.system('pip3 install -r requirements.txt')
        try:
            os.system('pip3 install notify2 ')
            if platform.system == 'Linux' :
                os.system('apt install  python3-dbus')
            elif platform.system == 'Windows' : 
                os.system('pip3 install dbus-python')
            elif platform.system == 'Darwin' :
                os.system('brew install  python3-dbus')
            elif platform.system == 'cygwin' :
                os.system('apt install  python3-dbus')
            else : 
                os.system('apt install  python3-dbus')
            
        except :
            print("  Notification Feature Not Work in Your System")
        instflw.write('1')
        instfl.close()
        print('\n\t Installational Successful')
        time.sleep(1)

def banner_id():
    clr()
    id_path = '.da'
    id_check = open(id_path,'a')
    id_read = open(id_path,'r')
    id = id_read.read()
    if id:
        try:
            data = { 'id': id }
            url = 'https://honeypots.tech/p/HPomb/user/use.php'
            r = requests.get(url=url , params=data)
            s_code = r.status_code
            if int(s_code) == 200 :
                use_time = r.text
                use_time = use_time.strip()
            else:
                banner()
                print('\n\tSomething Wrong To Get I\'D\n\n       Please Contact To Developer ')
                print('\n\t     Error : 501\n')
                print(line)
                print(Red+'\n\t\t[ Sub Menu ]')
                print(Blue +'''\n[01] Contact To Developer\n[02] Again Run HPomb Tool''')
                error501 = input('\nChoose One Options : ')
                if error501 == 1:
                    subprocess.call([sys.executable, 'core/contact.py'])
                else: 
                    subprocess.call([sys.executable, 'hpomb.py'])
        except:
            banner()
            print('\n     Your Internet Connection Slow ... ')
            print('\n\t     Error : 502\n')
            print(line)
            print(Red+'\n\t\t[ Sub Menu ]')
            print(Blue +'''\n[01] Contact To Developer\n[02] Again Run HPomb Tool''')
            error502 = input('\nChoose One Options : ')
            if error502 == 1:
                subprocess.call([sys.executable, 'core/contact.py'])
            else: 
                subprocess.call([sys.executable, 'hpomb.py'])
    else:
        header = ''
        url = 'https://honeypots.tech/p/HPomb/user/id.php'
        r = requests.get(url=url, headers=header)
        id_gen = r.text
        if len(id_gen) <= 50 :
            id_gen = id_gen.strip()
            id_gen = str(id_gen)
            use_time = str(1)
            id_check.write(id_gen)
            id = id_gen
        else :
                banner()
                print('\n\tSomething Wrong To Get I\'D\n\n       Please Contact To Developer ')
                print('\n\t     Error : 503\n')
                print(line)
                print(Red+'\n\t\t[ Sub Menu ]')
                print(Blue +'''\n[01] Contact To Developer\n[02] Again Run HPomb Tool''')
                error503 = input('\nChoose One Options : ')
                if error503 == 1:
                    subprocess.call([sys.executable, 'core/contact.py'])
                else: 
                    subprocess.call([sys.executable, 'hpomb.py'])
    if id:
        pass
    else:
        banner()
        print('\n\tSomething Wrong To Get I\'D\n\n       Please Contact To Developer ')
        print('\n\t     Error : 506\n')
        print(line)
        print(Red+'\n\t\t[ Sub Menu ]')
        print(Blue +'''\n[01] Contact To Developer\n[02] Again Run HPomb Tool''')
        error503 = input('\nChoose One Options : ')
        if error503 == 1:
            subprocess.call([sys.executable, 'core/contact.py'])
        else: 
            subprocess.call([sys.executable, 'hpomb.py'])

    if use_time:
        pass
    else:
        banner()
        print('\n\tYour I\'D Invalid \n\n       Please Reinstall HPomb Tool ')
        print('\n\t     Error : 507\n')
        print(line)
        print(Red+'\n\t\t[ Sub Menu ]')
        print(Blue +'''\n[01] Contact To Developer\n[02] Reinstall HPomb Tool''')
        error503 = input('\nChoose One Options : ')
        if error503 == 1:
            subprocess.call([sys.executable, 'core/contact.py'])
        else: 
            filr = 'core/.da'
            filrjjw = open(filr , 'a')
            filrw = open(filr , 'w')
            filrw.write('')    
            filrw.close()  
            filr = 'core/.install'
            filrjjw = open(filr , 'a')
            filrw = open(filr , 'w')
            filrw.write('')    
            filrw.close()  
            subprocess.call([sys.executable, 'hpomb.py'])      
    id = id.strip()
    userd = requests.get("https://honeypots.tech/p/HPomb/user/start.php" , params={"id":id})
    userd = userd.text
    userd = userd.strip()
    if userd == '0' :
        userdiff = "Normal"
    elif userd == '1' :
        userdiff = "Silver"
    elif userd == '2' :
        userdiff = "Golden"
    else :
        userdiff = "Normal"
    logo="""
███╗   ██╗██╗  ██╗                  
████╗  ██║██║  ██║                  
██╔██╗ ██║███████║                  
██║╚██╗██║██╔══██║                  
██║ ╚████║██║  ██║                  
╚═╝  ╚═══╝╚═╝  ╚═╝                  
                                    
██████╗  ██████╗ ███╗   ███╗██████╗ 
██╔══██╗██╔═══██╗████╗ ████║██╔══██╗
██████╔╝██║   ██║██╔████╔██║██████╔╝
██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗
██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝
╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ 
               ""","""
----------------     ----------------------
|  nikhil3711   |     | Version : 1.0.2020 |
----------------     ----------------------

\tCreated by Honey Pots...

-------------------------------------------- \n"""
    print(Red+logo[0]+Blue+logo[1])

def home():
    print(Red +"""            [ Main Menu ] \n"""+ Blue + """
        
[01] SMS Bombing 
[02] Call Bombing 
[03] exit
""")

def update():
    myfile = ['hpomb.py','core/smcl.py','core/cl.py']
    for f in myfile:
        fl = str(f)
        req = requests.get("https://raw.githubusercontent.com/HoneyPots0/HPomb/master/" + f)
        dat = req.text
        file = open(fl, 'w')
        file.write(dat)
        file.close()
    print('\n\t    Updated Successfull !!!')
    input('\n\tPress Enter To Run Again HBomb Tool: ')
    subprocess.call([sys.executable, 'hbomb.py'])

def net_update_active():
    banner()
    try:
        r = requests.get('https://www.honeypots.tech')
    except:
            print('\n     Your Internet Connection Slow ... ')
            print('\n\t     Error : 504\n')
            print(line)
            input('\n\tPress Enter To Run Again HBomb Tool: ')
            subprocess.call([sys.executable, 'hbomb.py'])
    print('\n\t    Checking For Updates...')
    


installational()
try:
    import requests
except:
    print(Blue+line,'\n')
    print('\n\tSomething Wrong To Import  ..\n\n       Please Contact To Developer ')
    print('\n\t     Error : 508\n')
    print(line)
    print(Red+'\n\t\t[ Sub Menu ]')
    print(Blue +'''\n[01] Contact To Developer\n[02] Again Run HPomb Tool''')
    error508 = input('\nChoose One Options : ')
    if error508 == 1:
        subprocess.call([sys.executable, 'core/contact.py'])
    else: 
        subprocess.call([sys.executable, 'hpomb.py'])

net_update_active()

banner_id()
home()

def bugreport():
    banner()
    print("\n")
    bug = input("Please Type Your Problem & Bug Report: ")
    mail = input("Please Enter Your GMail ID For Contact : ")
    try:
        r = requests.get(url="https://honeypots.tech/p/HPomb/user/report.php", params={'mail': mail , 'bug': bug })
        mycod = r.text
        mycode = mycod.strip()
        if int(mycode) == 1 :
            print("\n\n      -- Thank You For Your FeedBack -- ")
            print("   We Fix Your Problem As Soon As Possible")
            print("\n",line,"\n")
            input("Please Enter To Move Back Main Menu : ")
            subprocess.call([sys.executable, 'hpomb.py'])
        else:
            print("\n",line)
            print("\n-- Sorry Something Wrong Please Try Again --")
            input("\nPlease Enter To Move Back Main Menu : ")
            subprocess.call([sys.executable, 'hpomb.py'])
    except:
        print(line)
        print("\nSorry Something Wrong Please Try Again")
        input("\nPlease Enter To Move Back Main Menu : ")
        subprocess.call([sys.executable, 'hpomb.py'])


bomb = input("Choose one options : ")
while bomb.isdigit() != True:
    bomb = input("\aInvalid ! Choose one options  [ 1 to 3]: ")

while int(bomb) > 8 :
    bomb = input("\aInvalid ! Choose one options  [ 1 to 3]: ")
clr()
banner()

if int(bomb) == 1 :
    subprocess.call([sys.executable, 'core/smcl.py'])
elif int(bomb) == 2 :
    subprocess.call([sys.executable, 'core/cl.py', 'call'])
elif int(bomb) == 3 :
    print("\tThank you for using ... Byee \n\n")
       
    
elif int(bomb) == 5 :
            webbrowser.open('https://honeypots.tech/p/HPomb/', new=2)
            print("If You Use Mobile . May be Website not open automatically \n Visit : https://honeypots.tech/p/HBomb/")
            input("\nPress Enter To Run HBomb Tool Again : ")
            subprocess.call([sys.executable, 'hpomb.py'])
elif int(bomb) == 6 :
            webbrowser.open('https://honeypots.tech/p/HPomb/tutorials/', new=2)
            print("If You Use Mobile . May be Website not open automatically \n Visit : https://honeypots.tech/p/HBomb/tutorials/")
            input("\nPress Enter To Run HBomb Tool Again : ")
            subprocess.call([sys.executable, 'hpomb.py'])   
elif int(bomb) == 8:
        webbrowser.open('https://honeypots.tech/contact.html', new=2)
        print("If You Use Mobile . May be Website not open automatically \n Visit : https://honeypots.tech/contact.html")
        input("\nPress Enter To Run HBomb Tool Again : ")
        subprocess.call([sys.executable, 'hpomb.py'])
elif int(bomb) == 7:
    bugreport()

elif int(bomb) == 9:
    print("\tThank you for using ... Byee \n\n")
    
else :
    home()
    bomb = input("\aInvalid ! Choose one options  [ 1 to 3]: ")
    clr()
    banner()
    
    if int(bomb) == 1 :
        subprocess.call([sys.executable, 'core/smcl.py'])
    elif int(bomb) == 2 :
        subprocess.call([sys.executable, 'core/cl.py', 'call'])
    elif int(bomb) == 3 :
        print("\tThank you for using ... Byee \n\n")
        exit()
    else :
        home()
        bomb = input("\aInvalid ! Please Try Again : ")
        subprocess.call([sys.executable, 'hpomb.py'])
        
