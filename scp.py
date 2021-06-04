import os
import random
import shutil
import sys
from time import sleep

import requests
from bs4 import BeautifulSoup


def rprint(no):
    no = str(no)
    print(no.center(shutil.get_terminal_size().columns))


rprint("""\
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


def help():
    print("Type an scp number to see the entry\n")
    print("logout: Exit SCP-OS\n")
    print("help: See this page\n")
    print('r: random scp\n')


def set_num(num):
    num = str(num)
    if len(num) == 1:
        num += str('00')
    elif len(num) == 2:
        num += str('0')
    return str(num)


help()
while True:
    command = input(f'\n\n:')
    if command == '':
        continue
    elif command == 'help':
        help()
    elif command == 'logout':
        rprint("Shutting down...\n")
        quit()
    elif command == '001':
        rprint('UNAUTHORIZED ACCESS.')
        quit()
    else:
        if command == 'r':
            command = random.randint(0, 6000)
            command = set_num(command)
        URL = f"http://www.scpwiki.com/scp-{command}"

        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        # title = soup.find(id='page-title').text.strip()
        page = soup.find(id='page-content')
        for child in page.children:
            schild = str(child)
            if schild[0:3] == '<p>':
                rprint(child.text.strip())
                print()
