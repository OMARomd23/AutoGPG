import random
import os
import time
import shutil
from playwright.sync_api import Playwright, sync_playwright
from click.decorators import command
import colorama
from colorama import Fore, Style
colorama.init()
def print_funky_text(text):
    for char in text:
        if char == '\n':
            print()
        elif char == ' ':
            print(' ', end='')
        else:
            foreground_colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
            foreground_color = random.choice(foreground_colors)
            
            colored_char = f"{foreground_color}{char}{Style.RESET_ALL}"
            print(colored_char, end='')
print_funky_text("""
##############################################################################
          _    _ _______ ____     _____ _____   _____ 
     /\  | |  | |__   __/ __ \   / ____|  __ \ / ____|
    /  \ | |  | |  | | | |  | | | |  __| |__) | |  __ 
   / /\ \| |  | |  | | | |  | | | | |_ |  ___/| | |_ |
  / ____ \ |__| |  | | | |__| | | |__| | |    | |__| |
 /_/    \_\____/   |_|  \____/   \_____|_|     \_____|
                                                      Made By OUMESSAOUD Omar
##############################################################################
""")

foreground_colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
foreground_color = random.choice(foreground_colors)
print(foreground_color,"""What do you want to do :
1 : To import a key
2 : To encrypt using a key that is already imported
""")
def moving(path):
    move=input("enter the distination folder: ")
    files=os.listdir(f'{path}')
    for j in files:
        if j.endswith(".gpg"):
            shutil.move(f"{path}/{j}",f"{move}/{j}")
            print(f"moving {j}...")
            time.sleep(1)
def encrypting():    
    global path #making path variable accessable from everywhere on the script
    path =input("enter the path to the files: ")
    try :
        os.listdir(f'{path}')
    except FileNotFoundError:
        print("Path does not exists!")
        encrypting() #recall the function if the path is wrong
    recipient=input("enter recipient username: ")
    files = os.listdir(f"{path}")
    for i in files: #looping on the list to get the names of files
        os.system(f'gpg -e -r {recipient} {path}/{i}')
        print(f"encrypting {i}...")
        time.sleep(1)
    print("""
Would you like to move your encrypted files somewhere else?
Choose yes only if you have already encrypted some files and you wish to move them!
      """)
    w=["y",'Y',"n","N"]
    confirm=input("(Y)es or (N)o ?")
    while confirm not in w:
        confirm=input("(Y)es or (N)o ?")
    if confirm == "Y" or confirm == "y":
        moving(path)
    else: exit()
def importingonline():
    global text
    global path
    text = ""
    def run(playwright: Playwright) -> None:
        global text  # Access the global variable within the function
        global key_name
        key_name = input("Enter the key name: ")
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://keyserver.ubuntu.com/")
        page.get_by_placeholder("Search for an OpenPGP Public Key, ie 0x...").fill(key_name)
        page.get_by_placeholder("Search for an OpenPGP Public Key, ie 0x...").click()
        page.get_by_role("button", name=" Search Key").click()
        # Find all <pre> elements inside <body>
        pre_elements = page.query_selector_all("body > pre")
        if len(pre_elements) > 1:
            # Get the first link inside the second <pre> element
            link_element = pre_elements[1].query_selector("a")
            if link_element:
                link_element.click()
        
        # Get the text inside <body><pre>...</pre></body>
        text = page.inner_text("body > pre")
        # ---------------------
        context.close()
        browser.close()
    path =input("enter the path to save the file: ")
    try :
        os.listdir(f'{path}')
    except FileNotFoundError:
        print("Path does not exists!")
        importingonline()
    with sync_playwright() as playwright:
        run(playwright)
    with open(f'{path}/{key_name}.txt', '+a')as key:
        key.write(text)
    print(f'importing {key_name}...')
    time.sleep(1)
    os.system(f'gpg --import {f"{path}/{key_name}"}.txt')
    time.sleep(1)
    confirm=input("""
Woud yu like to encrypt some files?
(Y)es or (N)
    """)
    w = ["y", 'Y', "n", "N"]
    while confirm not in w:
        confirm=("""
Woud yu like to encrypt some files?
(Y)es or (N)
    """)
    if confirm == "n" or confirm == "N":
        return "okay"
    else:encrypting()
def importinglocal():
    print("Note! You have to put all the files in one directory before starting.")
    pubkey=input('enter the path of the directory containing the public key files you want to import: ')
    files=os.listdir(f'{pubkey}')
    for i in files:
        os.system(f'gpg --import {i}')
        time.sleep(1)
    os.system('gpg --list-keys')
    confirm=input("""
Woud yu like to encrypt some files?
(Y)es or (N)
    """)
    w = ["y", 'Y', "n", "N"]
    while confirm not in w:
        confirm=("""
Woud yu like to encrypt some files?
(Y)es or (N)
    """)
    if confirm == "n" or confirm == "N":
        return "okay"
    else:encrypting()
choice=input("I CHOOSE: ")
while choice not in ["1","2"]:
    choice=input("I CHOOSE: ")
if choice == "1":
    confirm = input("""
From where do you want to import the key?
1 : local machine
2 : The Ubuntu key server
    From: """)
    while choice not in ["1", "2"]:
            confirm = input("""
From where do you want to import the key?
1 : local machine
2 : The Ubuntu key server
    From: """)
    if confirm == "1":importinglocal()
    else:importingonline()
elif choice == "2":
    encrypting()
