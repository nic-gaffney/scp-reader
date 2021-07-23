import os
import random
import shutil
import sys
from time import sleep

import requests
from bs4 import BeautifulSoup

def rprint(no, text):
    no = str(no)
    text += (no.center(shutil.get_terminal_size().columns) + "\n")
    return text

def help():
    print("Type an scp number to see the entry\n")
    print("logout: Exit SCP-OS\n")
    print("save: Save the previous SCP data to SCPNUMBER.txt\n")
    print("help: See this page\n")
    print('r: random scp\n')


def set_num(num):
    num = str(num)
    if len(num) == 1:
        num += str('00')
    elif len(num) == 2:
        num += str('0')
    return str(num)

def main():
    print("""\
                    ,#############,
                    ##           ##
                m####             ####m
            m##*'        mmm        '*##m
            ###'         mm###mm         '###
        ###        m#############m        ###
        ##       m####*'  ###  '*####        ##
        ##      m####      ###      ####m      ##
    ##      ####      #######      ####      ##
    m#      ###'        #####        '###      #m
    ##     ####           #           ####     ##
    ##     ###    wwwwwwww wwwwwwww    ###     ##
    ##     #######'   *       *   '######m      '##
    ##     *#*'######             ######'*#*     ##
    ##         '#######m     m#######'         ##
    *#m          '###############'          m#*
        ##m ,m,        ''*****''        ,m, m##
        *##'*###m                   m###*'##*
                '*#######m     m#######*'
                    '*#######*'
                    SCP  READER
    \n\n""")





    help()
    main_text = ""
    prev_scp = 'NO_SCP'
    while True:
        command = input(f'\n\n:')
        if command == '':
            continue
        elif command == 'help':
            help()
        elif command == 'logout':
            print("Shutting down...\n")
            quit()
        elif command == '001':
            print('UNAUTHORIZED ACCESS.')
            quit()
        elif command == 'save':
            with open(f'{prev_scp}.txt', 'w') as f:
                f.write(main_text)
        else:
            if command == 'r':
                main_text = ""
                command = random.randint(0, 6000)
                command = set_num(command)
            URL = f"http://www.scpwiki.com/scp-{command}"
            main_text = ""
            page = requests.get(URL)
            soup = BeautifulSoup(page.content, 'html.parser')
            # title = soup.find(id='page-title').text.strip()
            page = soup.find(id='page-content')
            for child in page.children:
                schild = str(child)
                if schild[0:3] == '<p>':
                    main_text = rprint(child.text.strip(), main_text)
                elif schild[0:12] == '<blockquote>':
                    main_text = rprint(child.text.strip(), main_text)
            print(main_text)
            prev_scp = command


if __name__ == '__main__':
    main()