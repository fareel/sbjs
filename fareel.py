
#Fareel Bots js bypas kickall bypass 15/11/2021
from FarelBots.Fareel import*
from FareelBots.ttypes import Message
from FareelBots.ttypes import ContentType as Type
from FareelBots.ttypes import ChatRoomAnnouncementContents
from FareelBots.ttypes import ChatRoomAnnouncement
from FarelBots.thrift.unverting import *
from FarelBots.thrift.TMultiplexedProcessor import *
from FarelBots.thrift.TSerialization import *
from FarelBots.thrift.TRecursive import *
from FarelBots.thrift import transport, protocol, server
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, multiprocessing, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib3, urllib.parse, html5lib, wikipedia, atexit, timeit, pafy, youtube_dl, traceback
from googletrans import Translator
from threading import Thread,Event
import wikipedia as wiki
from subprocess import check_output
from Naked.toolshed.shell import execute_js
import sys,traceback
from zalgo_text import zalgo
_session = requests.session()
botStart = time.time()
#==========Fareel Team ßots_========
farel = LineFareel("imel mu","paswod mu")
farel.log("Auth Token : " + str(farel.authToken))
#==========Fareel Team ßots_========
print ("💘💘💘💘🔰Fareel🔰💘💘💘💘")
print ("===========login success================")
FarelKiler = FarelPoll(farel)
call = farel
lineProfile = farel.getProfile()
mid = farel.getProfile().mid
KAC = [farel]
Bots = [mid]
creator = [mid]
owner = [mid]
admin = [mid]
staff = [mid]
Saints = admin + owner + staff
Team = creator + owner + admin + staff + Bots
Setbot = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot)

protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectcancel = []
welcome = []
msg_dict = {}
msg_dict1 = {}
settings = {
    "Picture":False,
    "group":{},
    "groupPicture":False,
    "changePicture":False,
    "changeProfileVideo": False,
    "ChangeVideoProfilevid":{},
    "ChangeVideoProfilePicture":{},
    "comment":"╭──────────────────╮\n├🔥ɴᴜᴍᴘᴀɴɢ ᴘʀᴏᴍᴏ ʏᴀ ᴋᴀᴋᴀᴋ    \n╰──────────────────╯\n╭──────────────────\n├🔥ʀᴇᴀᴅʏ ʙᴏᴛ ᴘʀᴏᴛᴇᴄᴛ\n├🔥ʀᴏᴏᴍ sᴍᴜʟᴇ / ᴇᴠᴇɴᴛ \n├🔥ʀᴇᴀᴅʏ sʙ ᴏɴʟʏ \n├🔥sʙ ᴏɴʟʏ + ᴀᴊs \n├🔥sʙ + ᴀssɪsᴛ + ᴀᴊs \n├🔥ʟᴏɢɪɴ ᴊs / ʙʏᴘᴀs\n├🔥ɴᴇᴡ ᴘᴇᴍʙᴜᴀᴛᴀɴ sᴄ ʙᴏᴛ \n├🔥ɴᴇᴡ ʙᴇʟᴀᴊᴀʀ ʙᴏᴛ \n├🔥ᴘᴇᴍᴀsᴀɴɢ sʙ ᴋᴇ ᴛᴇᴍᴘʟᴀᴛᴇ\n├🔥ʀᴇᴀᴅʏ ᴀᴋᴜɴ ᴄᴏɪɴ\n├🔥ʀᴇᴀᴅʏ ᴄᴏɪɴ ɢɪғᴛ \n╰────────────────── \n╭─────────────────\n├ line.me/ti/p/~fareelkiller\n╰─────────────────",
    "autoJoinTicket":False,
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ]
}

wait = {
    "limit": 1,
    "owner":{},
    "admin":{},
    "addadmin":False,
    "delladmin":False,
    "Staff":{},
    "addStaff":False,
    "dellStaff":False,
    "bots":{},
    "addbots":False,
    "dellbots":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Talkblacklist":{},
    "Talkwblacklist":False,
    "Talkdblacklist":False,
    "talkban":True,
    "contact":False,
    'autoJoin':True,
    'autoAdd':True,
    'leaveMsg':True,
    'left':True,
    'autoLeave':False,
    'autoLeave1':False,
    "detectMention":False,
    "Mentionkick":False,
    "welcomeOn":True,
    "sticker":False,
    "selfbot":True,
    "likeOn":False,
    'autoBlock':False,
    "unsend":True,
    "arespon":True,
    "mention1":True,    
    "changevp": False,
    "Respontag":"sᴇᴋᴀʟɪ ʟᴀɢɪ ᴛᴀɢ, ᴍᴀᴜ ᴀʙɪ ᴅᴇsᴀʜɪɴ",
    "welcome":"Selamat datang & semoga betah n bahagia",
    "message":"╭──────────────────╮\n├🔥ɴᴜᴍᴘᴀɴɢ ᴘʀᴏᴍᴏ ʏᴀ ᴋᴀᴋᴀᴋ    │\n╰──────────────────╯\n╭──────────────────\n├🔥ʀᴇᴀᴅʏ ʙᴏᴛ ᴘʀᴏᴛᴇᴄᴛ\n├🔥ʀᴏᴏᴍ sᴍᴜʟᴇ / ᴇᴠᴇɴᴛ \n├🔥ʀᴇᴀᴅʏ sʙ ᴏɴʟʏ \n├🔥sʙ ᴏɴʟʏ + ᴀᴊs \n├🔥sʙ + ᴀssɪsᴛ + ᴀᴊs \n├🔥ʟᴏɢɪɴ ᴊs / ʙʏᴘᴀs\n├🔥ɴᴇᴡ ᴘᴇᴍʙᴜᴀᴛᴀɴ sᴄ ʙᴏᴛ \n├🔥ɴᴇᴡ ʙᴇʟᴀᴊᴀʀ ʙᴏᴛ \n├🔥ᴘᴇᴍᴀsᴀɴɢ sʙ ᴋᴇ ᴛᴇᴍᴘʟᴀᴛᴇ\n├🔥ʀᴇᴀᴅʏ ᴀᴋᴜɴ ᴄᴏɪɴ\n├🔥ʀᴇᴀᴅʏ ᴄᴏɪɴ ɢɪғᴛ \n╰────────────────── \n╭─────────────────\n├ line.me/ti/p/~fareelkiller\n╰─────────────────",
    }

read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

with open('creator.json', 'r') as fp:
    creator = json.load(fp)
with open('owner.json', 'r') as fp:
    owner = json.load(fp)

Setbot = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot)

mulai = time.time()

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

def restart_program(): 
    python = sys.executable
    os.execl(python, python, * sys.argv)

def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)
def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "╭──[ᴅᴀғᴛᴀʀ ᴊᴀɴᴅᴀ {}]──\n├ ".format(str(len(mid)))
        arr = []
        no = 1
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "├ "
            else:
                try:
                    textx += "╰──[Fareel Bots]──".format(str(farel.getGroup(to).name))
                except:
                    pass
        farel.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        farel.sendMessage(to, "[ ɪɴғᴏ ] ᴇʀᴏʀ :\n" + str(error))

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = " ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += settings["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n???[ {} ]".format(str(farel.getGroup(to).name))
                except:
                    no = "\n???[ Success ]"
        farel.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        farel.sendMessage(to, "ᴊᴏɴᴇs")

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = " ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = farel.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += "welcome"
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n???[ {} ]".format(str(farel.getGroup(to).name))
                except:
                    no = "\n???[ Success ]"
      #  client.sendMessage(to, textx)
    except Exception as error:
        farel.sendMessage(to)

def leaveMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Member Keluar「{}」\nByee  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = farel.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["leftmsg"]+"\nDari group "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(aditmadzs.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        farel.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        farel.sendMessage(to, "ᴊᴏɴᴇs")
        
def executeCmd(msg, text, txt, cmd, msg_id, receiver, sender, to, setKey):
    if cmd.startswith('ex\n'):
      if sender in clientMid:
        try:
            sep = text.split('\n')
            ryn = text.replace(sep[0] + '\n','')
            f = open('exec.txt', 'w')
            sys.stdout = f
            print(' ')
            exec(ryn)
            print('\n%s' % str(datetime.now()))
            f.close()
            sys.stdout = sys.__stdout__
            with open('exec.txt','r') as r:
                txt = r.read()
            farel.sendMessage(to, txt)
        except Exception as e:
            pass
      else:
        farel.sendMessage(to, 'ᴀᴘᴀʟᴜ !')
    elif cmd.startswith('exc\n'):
      if sender in clientMid:
        sep = text.split('\n')
        ryn = text.replace(sep[0] + '\n','')
        if 'print' in ryn:
        	ryn = ryn.replace('print(','farel.sendExecMessage(to,')
        	exec(ryn)
        else:
        	exec(ryn)
      else:
        farel.sendMessage(to, 'ᴀᴘᴀʟᴜ !')        
def changeProfileVideo(to):
    if settings['changevp']['picture'] == True:
        return farel.sendMessage(to, "Foto tidak ditemukan")
    elif settings['changevp']['video'] == True:
        return farel.sendMessage(to, "Video tidak ditemukan")
    else:
        path = settings['changevp']['video']
        files = {'file': open(path, 'rb')}
        obs_params = farel.genOBSParams({'oid': farel.getProfile().mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = farel.server.postContent('{}/talk/vp/upload.nhn'.format(str(farel.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return farel.sendMessage(to, "Gagal update profile")
        path_p = settings['changevp']['picture']
        settings['changevp']['status'] = True
        farel.updateProfilePicture(path_p, 'vp')                   
def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = farel.genOBSParams({'oid': mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4', 'name': 'GEGE.mp4'})
        data = {'params': obs_params}
        r_vp = farel.server.postContent('{}/talk/vp/upload.nhn'.format(str(farel.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        farel.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile %s"%str(e))
def cloneProfile(mid):
    contact = farel.getContact(mid)
    if contact.videoProfile == None:
        farel.cloneContactProfile(mid)
    else:
        profile = farel.getProfile()
        profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
        farel.updateProfile(profile)
        pict = farel.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus, saveAs="tmp/pict.bin")
        vids = farel.downloadFileURL( 'http://dl.profile.line-cdn.net/' + contact.pictureStatus + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = farel.getProfileDetail(mid)['result']['objectId']
    farel.updateProfileCoverById(coverId)
def restoreProfile():
    profile = farel.getProfile()
    profile.displayName = settings['myProfile']['displayName']
    profile.statusMessage = settings['myProfile']['statusMessage']
    if settings['myProfile']['videoProfile'] == None:
        profile.pictureStatus = settings['myProfile']['pictureStatus']
        farel.updateProfileAttribute(8, profile.pictureStatus)
        farel.updateProfile(profile)
    else:
        farel.updateProfile(profile)
        pict = farel.downloadFileURL('http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'], saveAs="tmp/pict.bin")
        vids = farel.downloadFileURL( 'http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'] + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = settings['myProfile']['coverId']
    farel.updateProfileCoverById(coverId)
def logError(text):
    farel.log("[ Fareel ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Makassar")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("errorLog.txt","a") as error:
        error.write("\n[{}] {}".format(str(time), text))
        
def sendTemplates(to, data):
    data = data
    url = "https://api.line.me/message/v3/share"
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi Note 5 Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Mobile Safari/537.36 Line/8.1.1'  
    headers['Content-Type'] = 'application/json'  
    headers['Authorization'] = 'Bearer eyJhbGciOiJIUzI1NiJ9.5uMcEEHahauPb5_MKAArvGzEP8dFOeVQeaMEUSjtlvMV9uuGpj827IGArKqVJhiGJy4vs8lkkseiNd-3lqST14THW-SlwGkIRZOrruV4genyXbiEEqZHfoztZbi5kTp9NFf2cxSxPt8YBUW1udeqKu2uRCApqJKzQFfYu3cveyk.GoRKUnfzfj7P2uAX9vYQf9WzVZi8MFcmJk8uFrLtTqU'
    sendPost = requests.post(url, data=json.dumps(data), headers=headers)
    print(sendPost)
    return sendPost
def sendTextTemplate(to, text):
    data = {
            "type": "flex",
            "altText": "Fareel Bots",
            "contents":{
  "type": "bubble",
  "size": "micro",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text":  text,
            "size": "xs",
            "wrap": True,
            "weight": "regular",
            "offsetStart": "3px"
          }
        ],
        "margin": "xs",
        "spacing": "md",
        "backgroundColor": "#ffffff"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Fareel Bots",
            "align": "center",
            "size": "xs"
          }
        ],
        "paddingAll": "2px",
        "backgroundColor": "#000000",
        "margin": "xs"
      }
    ],
    "paddingAll": "0px",
    "borderWidth": "2px",
    "borderColor": "#FF0000",
    "cornerRadius": "10px",
    "spacing": "xs"
  },
  "styles": {
    "body": {
      "backgroundColor": "#ffff00"
    }
  }
}
}
    farel.postTemplate(to, data)
 
def sendTextTemplate1(to, text):
    data = {
                                "type": "flex",
                                "altText": "{} ᴘᴀᴘᴀ ᴋᴜʀᴀɴɢ ᴅᴇsᴀʜᴀɴ".format(farel.getProfile().displayName),
                                "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": text,
            "size": "md",
            "weight": "bold",
            "wrap": True,
            "color": "#40E0D0",
            "align": "center"
          },
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#00008B"
    },
    "header": {
      "backgroundColor": "#00008B"
    }
  },  
  "hero": {
    "type": "image",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "url": "https://media.tenor.com/images/842c542426869f999afaeb7d8c7940b3/tenor.gif",
    "size": "full",
    "margin": "xl"
  },
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "ᴏᴡɴᴇʀ",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#7CFC00",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/~fareelkiller"
        },
        "align": "center"
      },
      {
        "type": "separator",
        "color": "#E5E4E2"
      },
      {
        "type": "text",
        "text": "ᴘᴇsᴀɴ",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#FFD700",
        "action": {
          "type": "uri",
          "uri": "line://app/1602687308-GXq4Vvk9/?type=text&text=Order"
        },
        "align": "center"
      }
    ]
  },
  "header": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "Fareel Bots",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#F0F8FF",
        "align": "center"
      }
    ]
  }
}
}
    farel.postTemplate(to, data)
    
def sendTextTemplate7(to, text):
    data = {
                                "type": "flex",
                                "altText": "{} ᴘᴀᴘᴀ ᴋᴜʀᴀɴɢ ᴅᴇsᴀʜᴀɴ".format(farel.getProfile().displayName),
                                "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": text,
            "size": "md",
            "weight": "bold",
            "wrap": True,
            "color": "#40E0D0",
            "align": "center"
          },
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#00008B"
    },
    "header": {
      "backgroundColor": "#00008B"
    }
  },  
  "hero": {
    "type": "image",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "url": "https://media.giphy.com/media/NTj6PZtxqt6U91ksRZ/giphy.gif",
    "size": "full",
    "margin": "xl"
  },
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "ᴏᴡɴᴇʀ",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#7CFC00",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/fareelkiller"
        },
        "align": "center"
      },
      {
        "type": "separator",
        "color": "#E5E4E2"
      },
      {
        "type": "text",
        "text": "ᴘᴇsᴀɴ",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#FFD700",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/fareelkiller"
        },
        "align": "center"
      }
    ]
  },
  "header": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "Fareel Bots",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#F0F8FF",
        "align": "center"
      }
    ]
  }
}
}
    farel.postTemplate(to, data)
    
def sendTextTemplate2(to, text):
    data = {
                                "type": "flex",
                                "altText": "{} ᴘᴀᴘᴀ ᴋᴜʀᴀɴɢ ᴅᴇsᴀʜᴀɴ".format(farel.getProfile().displayName),
                                "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": text,
            "size": "md",
            "weight": "bold",
            "wrap": True,
            "color": "#40E0D0",
            "align": "center"
          },
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#00008B"
    },
    "header": {
      "backgroundColor": "#00008B"
    }
  },  
  "hero": {
    "type": "image",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "url": "https://media.giphy.com/media/nbBbfmBVnuIYZ5itAc/giphy.gif",
    "size": "full",
    "margin": "xl"
  },
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "ᴏᴡɴᴇʀ",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#7CFC00",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/fareelkiller"
        },
        "align": "center"
      },
      {
        "type": "separator",
        "color": "#E5E4E2"
      },
      {
        "type": "text",
        "text": "ᴘᴇsᴀɴ",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#FFD700",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/fareelkiller"
        },
        "align": "center"
      }
    ]
  },
  "header": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "ᴏʟᴇɴɢ ʙᴏᴛ",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#F0F8FF",
        "align": "center"
      }
    ]
  }
}
}
    farel.postTemplate(to, data)
    
def sendTextTemplate3(to, text):
    data = {
                                "type": "flex",
                                "altText": "{} ᴘᴀᴘᴀ ᴋᴜʀᴀɴɢ ᴅᴇsᴀʜᴀɴ".format(farel.getProfile().displayName),
                                "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": text,
            "size": "md",
            "weight": "bold",
            "wrap": True,
            "color": "#40E0D0",
            "align": "center"
          },
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#00008B"
    },
    "header": {
      "backgroundColor": "#00008B"
    }
  },  
  "hero": {
    "type": "image",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "url": "https://media0.giphy.com/media/xVxio2tNLAM5q/200w.webp?cid=19f5b51a5c44951d4b47664273e6c074",
    "size": "full",
    "margin": "xl"
  },
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "ᴏᴡɴᴇʀ",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#7CFC00",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/~fareelkiller"
        },
        "align": "center"
      },
      {
        "type": "separator",
        "color": "#E5E4E2"
      },
      {
        "type": "text",
        "text": "ᴘᴇsᴀɴ",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#FFD700",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/~fareelkiller"
        },
        "align": "center"
      }
    ]
  },
  "header": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "Fareel Bots",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#F0F8FF",
        "align": "center"
      }
    ]
  }
}
}
    farel.postTemplate(to, data)
    
def sendTextTemplate5(to, text):
    data = {
            "type": "flex",
            "altText": "Fareel Bots",
            "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": text,
            "size": "sm",
            "weight": "bold",
            "wrap": True,
            "color": "#F0F8FF"
          }
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#00008B"
    },
    "header": {
      "backgroundColor": "#00008B"
    }
  },  
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "sᴇᴇ ʏᴏᴜ",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#FFD700",
        "align": "center"
      }
    ]
  },
  "header": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "sᴏᴜɴᴅᴄʟᴏᴜᴅ",
        "size": "md",
        "wrap": True,
        "weight": "bold",
        "color": "#FFD700",
        "align": "center"
      }
    ]
  }
}
}
    farel.postTemplate(to, data)
    
def sendTextTemplate1(to, text):
    data = {
                "type": "template",
                "altText": "Fareel Bots",
                "contents": {
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                               "text": text,
                               "size": "sm",
                               "margin": "none",
                               "color": "#8B008B",
                               "wrap": True,
                               "weight": "regular",
                               "type": "text"
                            }
                        ]
                    }
                }
            }
    farel.postTemplate(to, data)
    
def sendTextTemplate6(to, text):
    data = {
            "type": "flex",
            "altText": "Fareel Bots",
            "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#0000CD"
    }
  },
  "type": "bubble",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "contents": [
              {
                "text": text,
                "size": "md",
                "margin": "none",
                "color": "#FFFF00",
                "wrap": True,
                "weight": "bold",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
  }
}
}
    farel.postTemplate(to, data)
    
def sendTextTemplate3(to, text):
    data = {
            "type": "flex",
            "altText": "Fareel Bots",
            "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": text,
            "size": "sm",
            "weight": "bold",
            "wrap": True,
            "color": "#00FF00"
          }
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#00FFFF"
    },
    "header": {
      "backgroundColor": "#00FFFF"
    }
    },  
     "hero": {
     "type": "image",
     "aspectRatio": "20:13",
     "aspectMode": "cover",
     "url": "https://media.giphy.com/media/67pVlH3LSLDjTBikzf/giphy.gif",
     "size": "full",
     "margin": "xl"
  },  
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "ᴏᴡɴᴇʀ",
        "size": "xxl",
        "wrap": True,
        "weight": "bold",
        "color": "#000000",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/~fareelkiller"
        },
        "align": "center"
      }
    ]
  },
  "header": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "ᴏʟᴇɴɢʙᴏᴛ",
        "size": "md",
        "wrap": True,
        "weight": "bold",
        "color": "#000000",
        "align": "center"
      }
    ]
  }
}
}
    farel.postTemplate(to, data)
    
def sendStickerTemplate(to, text):
    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
    to = op.param1
    data = {
                          "type": "template",
                          "altText": "{} sent a sticker".format(farel.getProfile().displayName),
                          "template": {
                             "type": "image_carousel",
                             "columns": [
                              {
                                  "imageUrl": text,
                                  "size": "full", 
                                  "action": {
                                      "type": "uri",
                                      "uri": "http://line.me/ti/p/~fareelkiller"
           }                                                
 }
]
                          }
                      }
    
def sendStickerTemplate(to, text):
    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
    to = op.param1
    data = {
                          "type": "template",
                          "altText": "{} sent a sticker".format(client.getProfile().displayName),
                          "template": {
                             "type": "image_carousel",
                             "columns": [
                              {
                                  "imageUrl": text,
                                  "size": "full", 
                                  "action": {
                                      "type": "uri",
                                      "uri": "http://line.me/ti/p/~fareelkiller"
           }                                                
 }
]
                          }
                      }
    farel.postTemplate(to, data)    
    
def youtubeMp3(to, link):
    subprocess.getoutput('youtube-dl --extract-audio --audio-format mp3 --output farel.mp3 {}'.format(link))
    try:
        farel.sendAudio(to, 'farel.mp3')
        time.sleep(2)
        os.remove('farel.mp3')
    except Exception as e:
        farel.sendMessage(to, 'Fareel Bots\nʟɪɴᴋ ᴀɴᴅᴀ sᴀʟᴀʜ')
def youtubeMp4(to, link):
    subprocess.getoutput('youtube-dl --format mp4 --output farel.mp4 {}'.format(link))
    try:
        farel.sendVideo(to, "farel.mp4")
        time.sleep(2)
        os.remove('farel.mp4')
    except Exception as e:
        farel.sendMessage(to, ' ᴇʀʀᴏʀ\nʟɪɴᴋ ᴀɴᴅᴀ sᴀʟᴀʜ', contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+client.getContact(clientMid).pictureStatus, 'AGENT_NAME': 'ᴇʀʀᴏʀ', 'AGENT_LINK': 'https://line.me/ti/p/~fareelkiller'})

def delExpire():
    if temp_flood != {}:
        for tmp in temp_flood:
            if temp_flood[tmp]["expire"] == True:
                if time.time() - temp_flood[tmp]["time"] >= 3*10:
                    temp_flood[tmp]["expire"] = False
                    temp_flood[tmp]["time"] = time.time()
                    try:
                        veza = "ʙᴏᴛ ᴀᴋᴛɪғ ʙᴏssᴋᴜ"
                        farel.sendMessage(tmp, veza, {'AGENT_LINK': "https://line.me/ti/p/~fareelkiller", 'AGENT_ICON': "http://klikuntung.com/images/messengers/line-logo.png", 'AGENT_NAME': "Detect Spam "})        
                    except Exception as error:
                        logError(error)

def delExpirev2():
    if temp_flood != {}:
        for tmp in temp_flood:
            if temp_flood[tmp]["expire"] == True:
                    temp_flood[tmp]["expire"] = False
                    temp_flood[tmp]["time"] = time.time()
                    try:
                        veza = "ʙᴏᴛ ᴀᴋᴛɪғ ʙᴏssᴋᴜ"
                        farel.sendMessage(tmp, veza, {'AGENT_LINK': "https://line.me/ti/p/~fareelkiller", 'AGENT_ICON': "http://klikuntung.com/images/messengers/line-logo.png", 'AGENT_NAME': "Detect Spam "})        
                    except Exception as error:
                        logError(error)    

def musik(to):
    contentMetadata={'previewUrl': "http://dl.profile.line-cdn.net/"+farel.getContact(mid).picturePath, 'i-installUrl': 'http://itunes.apple.com/app/linemusic/id966142320', 'type': 'mt', 'subText': farel.getContact(mid).statusMessage if farel.getContact(mid).statusMessage != '' else 'http://line.me/ti/p/~fareelkiller', 'a-installUrl': 'market://details?id=jp.linecorp.linemusic.android', 'a-packageName': 'jp.linecorp.linemusic.android', 'countryCode': 'JP', 'a-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'i-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'text': farel.getContact(mid).displayName, 'id': 'mt000000000d69e2db', 'linkUri': 'https://music.farel.cl/launch?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1','MSG_SENDER_ICON': "https://os.me.naver.jp/os/p/"+mid,'MSG_SENDER_NAME':  farel.getContact(mid).displayName,}
    return farel.sendMessage(to, farel.getContact(mid).displayName, contentMetadata, 19)

def sendMention2(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        farel.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
        farel.sendImageWithURL(msg.to,image)
    except Exception as error:
        farel.sendMessage(to, "[ INFO ] Error :\n" + str(error))
    
def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"],"")
    else:
        cmd = "command"
    return cmd

def help():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = "╭──────────╮" + "\n" + \
                  "├  🔥Fareel Bots" + "\n" + \
                  "╰──────────╯" + "\n" + \
                  "╭──────────╮" + "\n" + \
                  "├🔥" + key + "ᴍᴇ\n" + \
                  "├🔥" + key + "ᴍɪᴅ「@」\n" + \
                  "├🔥" + key + "ɪɴғᴏ「@」\n" + \
                  "├🔥" + key + "ʀᴇsᴛᴀʀᴛ\n" + \
                  "├🔥" + key + "ʀᴜɴᴛɪᴍᴇ\n" + \
                  "├🔥" + key + "kick「@」\n" + \
                  "├🔥" + key + "sᴘ\n" + \
                  "├🔥" + key + "sᴀʏᴀɴɢ / ᴘᴇᴀ\n" + \
                  "├🔥" + key + "glist\n" + \
                  "├🔥" + key + "pass /no remote\n" + \
                  "├🔥" + key + "sapu /no remote\n" + \
                  "├🔥" + key + "#bypass\n" + \
                  "├🔥" + key + "#kickall\n" + \
                  "├🔥" + key + "!cl/!cancel\n" + \
                  "├🔥" + key + "cvp\n" + \
                  "├🔥" + key + "cctv on/off\n" + \
                  "├🔥" + key + "welcome on/off\n" + \
                  "├🔥" + key + "autojoin on/off\n" + \
                  "├🔥" + key + "myname: text\n" + \
                  "├🔥" + key + "myfoto\n" + \
                  "├🔥" + key + "hay " + \
                  "├🔥" + key + "cipok \n" + \
                  "├🔥" + key + "ᴘᴀᴘᴀʏ (ʟᴇғᴛ ɢᴄ)\n" + \
                  "├🔥" + key + "ɢɪɴғᴏ\n" + \
                  "├🔥" + key + "sᴇʟғ ᴏɴ「@」\n" + \
                  "├🔥" + key + "ᴏᴘᴇɴ\n" + \
                  "├🔥" + key + "ᴄʟᴏsᴇ\n" + \
                  "├🔥" + key + "ᴜʀʟɢʀᴜᴘ\n" + \
                  "├🔥" + key + "ɪɴғᴏɢʀᴜᴘ「ɴᴏ」\n" + \
                  "├🔥" + key + "ɪɴғᴏᴍᴇᴍ「ɴᴏ」\n" + \
                  "├🔥" + key + "ʜᴀᴘᴜsᴄʜᴀᴛ\n" + \
                  "├🔥" + key + "ғʀɪᴇɴᴅʟɪsᴛ\n" + \
                  "├🔥" + key + "ɢʀᴏᴜᴘʟɪsᴛ\n" + \
                  "├🔥" + key + "ᴜᴘᴅᴀᴛᴇғᴏᴛᴏ\n" + \
                  "├🔥" + key + "ᴜᴘᴅᴀᴛᴇɢʀᴜᴘ\n" + \
                  "├🔥" + key + "ᴜᴘᴅᴀᴛᴇʙᴏᴛ\n" + \
                  "├🔥" + key + "sᴇᴛᴋᴇʏ「ɴᴇᴡᴋᴇʏ」\n" + \
                  "├🔥" + key + "sᴇʟғ 「ᴏɴ/ᴏғғ」\n" + \
                  "├🔥" + key + "ʙʟᴄ\n" + \
                  "├🔥" + key + "ʙᴀɴ:ᴏɴ\n" + \
                  "├🔥" + key + "ᴜɴʙᴀɴ:ᴏɴ\n" + \
                  "├🔥" + key + "ʙᴀɴ「@」\n" + \
                  "├🔥" + key + "ᴜɴʙᴀɴ「@」\n" + \
                  "├🔥" + key + "ᴛᴀʟᴋʙᴀɴ「@」\n" + \
                  "├🔥" + key + "ᴜɴᴛᴀʟᴋʙᴀɴ「@」\n" + \
                  "├🔥" + key + "ᴛᴀʟᴋʙᴀɴ:ᴏɴ\n" + \
                  "├🔥" + key + "ᴜɴᴛᴀʟᴋʙᴀɴ:ᴏɴ\n" + \
                  "├🔥" + key + "ʙᴀɴʟɪsᴛ\n" + \
                  "├🔥" + key + "ᴛᴀʟᴋʙᴀɴʟɪsᴛ\n" + \
                  "├🔥" + key + "ᴄʟᴇᴀʀʙᴀɴ\n" + \
                  "├🔥" + key + "ʀᴇғʀᴇsʜ\n" + \
                  "├🔥" + key + "myset\n" + \
                  "╰──────────╯"
    return helpMessage

def bot(op):
    global time
    global ast
    global groupParam
    try:   
        if op.type == 0:
            return           
        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        farel.acceptGroupInvitation(op.param1)
                        ginfo = farel.getGroup(op.param1)
                        farel.sendMessage(op.param1,"aĸυ eмooн coĸ \n┣🚫► Group " +str(ginfo.name))
                        farel.leaveGroup(op.param1)
                    else:
                        farel.acceptGroupInvitation(op.param1)
                        ginfo = farel.getGroup(op.param1)
                        farel.sendMessage(op.param1,"Thankyou For Invite" + str(ginfo.name))

        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        farel.acceptGroupInvitation(op.param1)
                        ginfo = farel.getGroup(op.param1)
                        farel.sendMessage(op.param1,"ᴛʜᴀɴᴋs ғᴏʀ ɪɴᴠɪᴛᴇ")
                    else:
                        farel.acceptGroupInvitation(op.param1)
                        ginfo = farel.getGroup(op.param1)
                        farel.sendMessage(op.param1,"ᴛʜᴀɴᴋs ғᴏʀ ɪɴᴠɪᴛᴇ")
        

        if op.type == 13:
            if mid in op.param3:
               if wait["autoReject"] == True:
                   if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                       farel.rejectGroupInvitation(op.param1)

        if op.type == 13:
            if op.param2 in wait["blacklist"]:
                try:
                    farel.cancelGroupInvitation(op.param1,[op.param3])
                    farel.kickoutFromGroup(op.param1,[op.param2])
                    wait["blacklist"][op.param2] = True
                except:
                    try:
                        group = farel.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _dn in gMembMids:
                          if _dn in wait["blacklist"]:
                            farel.cancelGroupInvitation(op.param1,[_dn])
                    except:
                        farel.cancelGroupInvitation(op.param1,[op.param3])
                        farel.kickoutFromGroup(op.param1,[op.param2])
                        wait["blacklist"][op.param2] = True
                        
            if op.param3 in wait["blacklist"]:
                try:
                    farel.cancelGroupInvitation(op.param1,[op.param3])
                    farel.kickoutFromGroup(op.param1,[op.param2])
                    wait["blacklist"][op.param2] = True
                except:
                    try:
                        group = farel.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _dn in gMembMids:
                          if _dn in wait["blacklist"]:
                            farel.cancelGroupInvitation(op.param1,[_dn])
                    except:
                        farel.cancelGroupInvitation(op.param1,[op.param3])
                        farel.kickoutFromGroup(op.param1,[op.param2])
                        wait["blacklist"][op.param2] = True

        if op.type == 17:
            if op.param2 in wait["blacklist"]:
               try:
                   farel.kickoutFromGroup(op.param1,[op.param2])
                   farel.sendMessage(op.param1,"contact ini ʙʟᴀᴄᴋʟɪsᴛ")
               except:
                   pass

        if op.type == 32:
            if wait["backup"] == True:
              if op.param3 in Bots:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            farel.kickoutFromGroup(op.param1,[op.param2])
                            farel.inviteIntoGroup(op.param1,[op.param3])
                    except:
                    	pass
                return

        if op.type == 19 or op.type == 32:
            if mid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in creator:
                    pass
                if op.param2 in admin:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        farel.acceptGroupInvitation(op.param1)
                        farel.inviteIntoGroup(op.param1,[op.param3])
                        farel.kickoutFromGroup(op.param1,[op.param2])
                    except:
                    	pass
                return

        if op.type == 19 or op.type == 32:
            if op.param3 in creator:
              if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                farel.findAndAddContactsByMid(op.param3)
                farel.inviteIntoGroup(op.param1,[op.param3])
                farel.kickoutFromGroup(op.param1,[op.param2])
                wait["blacklist"][op.param2] = True

        if op.type == 19 or op.type == 32:
            if op.param3 in admin:
              if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                farel.findAndAddContactsByMid(op.param3)
                farel.inviteIntoGroup(op.param1,[op.param3])
                farel.kickoutFromGroup(op.param1,[op.param2])
                wait["blacklist"][op.param2] = True

        if op.type == 55:            
            try:
                if op.param1 in read["readPoint"]:
                    if op.param2 in read["readMember"][op.param1]:
                        pass
                    else:
                        read["readMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass
                
        if op.type == 55:
            if op.param2 in wait["blacklist"]:
               try:
                   farel.kickoutFromGroup(op.param1,[op.param2])
                   farel.sendMessage(op.param1,"contact ini ʙʟᴀᴄᴋʟɪsᴛ")
               except:
                   pass

        if op.type == 15:
            if wait["leaveMsg"] == True:
                ginfo = farel.getGroup(op.param1)
                leaveMembers(op.param1, [op.param2])
                contact = farel.getContact(op.param2)
                data = {
                        "type": "flex",
                        "altText": "Fareel Bots",
                        "contents": {
      "type": "bubble",
      "size": "nano",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(farel.getContact(op.param2).pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "  {}".format(farel.getContact(op.param2).displayName),
                    "size": "xs",
                    "color": "#ffffff",
                    "weight": "bold"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "🔥ʙᴀᴘᴇʀ ᴋᴀɴ ᴅɪᴀ ʟᴇғᴛ",
                    "color": "#ebebeb",
                    "size": "xxs",
                    "flex": 0
                  }
                ],
                "spacing": "lg"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "filler"
                      },
                      {
                        "type": "text",
                        "text": "Fareel Bots",
                        "color": "#ffffff",
                        "flex": 0,
                        "offsetTop": "0px"
                      },
                      {
                        "type": "filler"
                      }
                    ],
                    "spacing": "xs"
                  },
                  {
                    "type": "filler"
                  }
                ],
               # "borderWidth": "1px",
                #"cornerRadius": "4px",
            #    "spacing": "xs",
             #   "borderColor": "#ffffff",
              #  "margin": "xs",
             #   "height": "40px"
              }
            ],
            "position": "absolute",
            "offsetBottom": "0px",
            "offsetStart": "0px",
            "offsetEnd": "0px",
            "backgroundColor": "#03303Acc",
            "paddingAll": "0px",
            "paddingTop": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "ʟᴇғᴛ",
                "color": "#ffffff",
                "align": "center",
                "size": "xs",
                "offsetTop": "-3px"
              }
            ],
            "position": "absolute",
            "cornerRadius": "8px",
            "offsetTop": "3px",
            "backgroundColor": "#ff334b",
            "offsetStart": "5px",
            "height": "15px",
            "width": "38px"
          }
        ],
        "paddingAll": "0px"
    }
 }
}
                farel.postTemplate(op.param1, data)
              
        if op.type == 17:
            if wait["welcomeOn"] == True:
                ginfo = farel.getGroup(op.param1)
                welcomeMembers(op.param1, [op.param2])
                contact = farel.getContact(op.param2)
                data = {
                        "type": "flex",
                        "altText": "Fareel Bots",
                        "contents": {
      "type": "bubble",
      "size": "nano",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(farel.getContact(op.param2).pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "  {}".format(farel.getContact(op.param2).displayName),
                    "size": "xs",
                    "color": "#ffffff",
                    "weight": "bold"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "🔥sᴇʟᴀᴍᴀᴛ ᴅᴀᴛᴀɴɢ",
                    "color": "#ebebeb",
                    "size": "xxs",
                    "flex": 0
                  }
                ],
                "spacing": "lg"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "filler"
                      },
                      {
                        "type": "text",
                        "text": "Fareel Bots",
                        "color": "#ffffff",
                        "flex": 0,
                        "offsetTop": "0px"
                      },
                      {
                        "type": "filler"
                      }
                    ],
                    "spacing": "xs"
                  },
                  {
                    "type": "filler"
                  }
                ],
               # "borderWidth": "1px",
                #"cornerRadius": "4px",
            #    "spacing": "xs",
             #   "borderColor": "#ffffff",
              #  "margin": "xs",
             #   "height": "40px"
              }
            ],
            "position": "absolute",
            "offsetBottom": "0px",
            "offsetStart": "0px",
            "offsetEnd": "0px",
            "backgroundColor": "#03303Acc",
            "paddingAll": "0px",
            "paddingTop": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "ᴡʟᴄᴍ",
                "color": "#ffffff",
                "align": "center",
                "size": "xs",
                "offsetTop": "-3px"
              }
            ],
            "position": "absolute",
            "cornerRadius": "8px",
            "offsetTop": "3px",
            "backgroundColor": "#ff334b",
            "offsetStart": "5px",
            "height": "15px",
            "width": "38px"
          }
        ],
        "paddingAll": "0px"
    }
 }
}
                farel.postTemplate(op.param1, data)
        if op.type == 5:
            print ("[ 5 ] ɴᴏᴛɪғɪᴇᴅ ᴀᴜᴛᴏʙʟᴏᴄᴋ ᴄᴏɴᴛᴀᴄᴛ")
            if wait["autoBlock"] == True:
                farel.blockContact(op.param1)
                farel.sendMessage(op.param1, wait["ᴍᴀᴀғ ᴀɪᴍ ᴀᴜᴛᴏʙʟᴏᴄᴋ ᴀɪᴍ ᴀᴋᴛɪғ"])
                
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in Staff:
                    if (wait["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        farel.sendMessage(op.param1, wait["message"])
        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'ɢᴀᴍʙᴀʀɴʏᴀ ᴅɪ ʙᴀᴡᴀʜ':
                                ginfo = farel.getGroup(at)
                                ryan = farel.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 ɢᴀᴍʙᴀʀ ᴅɪ ʜᴀᴘᴜs 」\nᴘᴇɴɢɪʀɪᴍ : "
                                ret_ = "ɴᴀᴍᴀ ɢʀᴏᴜᴘ : {}".format(str(ginfo.name))
                                ret_ += "\nᴡᴀᴋᴛᴜ ᴘᴇɴɢɪʀɪᴍ : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                farel.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                farel.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = farel.getGroup(at)
                                ryan = farel.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "ᴘᴇsᴀɴ ᴅɪ ʜᴀᴘᴜs\n"
                                ret_ += "ᴘᴇɴɢɪʀɪᴍ : {}".format(str(ryan.displayName))
                                ret_ += "\n°ɴᴀᴍᴀ ɢʀᴏᴜᴘ : {}".format(str(ginfo.name))
                                ret_ += "\nᴡᴀᴋᴛᴜ ᴘᴇɴɢɪʀɪᴍ : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\nᴘᴇsᴀɴ ɴʏᴀ : {}".format(str(msg_dict[msg_id]["text"]))
                                farel.sendMessage(at, str(ret_))
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = farel.getGroup(at)
                                ryan = farel.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  "sᴛɪᴄᴋᴇʀ ᴅɪ ʜᴀᴘᴜs\n"
                                ret_ += "ᴘᴇɴɢɪʀɪᴍ : {}".format(str(ryan.displayName))
                                ret_ += "\nɴᴀᴍᴀ ɢʀᴏᴜᴘ : {}".format(str(ginfo.name))
                                ret_ += "\nᴡᴀᴋᴛᴜ ᴘᴇɴɢɪʀɪᴍ : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                farel.sendMessage(at, str(ret_))
                                farel.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e)
            
        if op.type == 19:
            if mid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        farel.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass
            return
        if op.type == 55:
            try:
                if op.param1 in Setmain["RAreadPoint"]:
                   if op.param2 in Setmain["RAreadMember"][op.param1]:
                       pass
                   else:
                       Setmain["RAreadMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass

        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                farel.kickoutFromGroup(op.param1,[op.param2])
                farel.cancelGroupInvitation(op.param1,[op.param3])
            else:
                pass

        
        if op.type == 55:
            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = farel.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        contact = farel.getContact(op.param2)
                        data = {
                                "type": "flex",
                                "altText": "Fareel Bots",
                                "contents":{
      "type": "bubble",
      "size": "nano",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(farel.getContact(op.param2).pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "  {}".format(farel.getContact(op.param2).displayName),
                    "size": "xxs",
                    "color": "#ffffff",
                    "weight": "bold"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": "🔥ɴɢɪɴᴛɪᴘ² ɢᴀʙᴜɴɢ sɪɴɪ",
                    "color": "#ebebeb",
                    "size": "xxs",
                    "flex": 0
                  }
                ],
                "spacing": "lg"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "filler"
                      },
                      {
                        "type": "text",
                        "text": "Fareel Bots",
                        "color": "#ffffff",
                        "flex": 0,
                        "offsetTop": "0px"
                      },
                      {
                        "type": "filler"
                      }
                    ],
                    "spacing": "xs"
                  },
                  {
                    "type": "filler"
                  }
                ],
               # "borderWidth": "1px",
                #"cornerRadius": "4px",
            #    "spacing": "xs",
             #   "borderColor": "#ffffff",
              #  "margin": "xs",
             #   "height": "40px"
              }
            ],
            "position": "absolute",
            "offsetBottom": "0px",
            "offsetStart": "0px",
            "offsetEnd": "0px",
            "backgroundColor": "#03303Acc",
            "paddingAll": "0px",
            "paddingTop": "2px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "cctv",
                "color": "#ffffff",
                "align": "center",
                "size": "xs",
                "offsetTop": "-3px"
              }
            ],
            "position": "absolute",
            "cornerRadius": "8px",
            "offsetTop": "3px",
            "backgroundColor": "#ff334b",
            "offsetStart": "5px",
            "height": "15px",
            "width": "38px"
          }
        ],
        "paddingAll": "0px"
    }
 }
}
                        farel.postTemplate(op.param1, data)                
        if op.type == 25 or op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          farel.kickoutFromGroup(msg.to, [msg._from])
                      except:pass                                        
               if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata:
                 if wait["detectMention"] == True:
                   contact = farel.getContact(msg._from)
                   name = re.findall(r'@(\w+)', msg.text)
                   image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           sendTextTemplate(msg.to, wait["Respontag"])
                           break
                           
               if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata:
                 if wait["Mentionkick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           farel.mentiontag(msg.to,[msg._from])
                           farel.sendMessage(msg.to, "ᴊᴀɴɢᴀɴ ᴛᴀǫ ᴀʙɪ....")
                           farel.kickoutFromGroup(msg.to, [msg._from])
                           break
                           
               if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata:
                 if wait["arespon"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   lists = []
                   for mention in mentionees:
                        if mention ['M'] in mid:
                           contact = farel.getContact(msg._from)
                           farel.sendImageWithURL(msg._from, "http://dl.profile.line-cdn.net{}".format(contact.picturePath))
                           sendMention1(sender, "╭──────────────────╮\n├🔥ɴᴜᴍᴘᴀɴɢ ᴘʀᴏᴍᴏ ʏᴀ ᴋᴀᴋᴀᴋ    │\n╰──────────────────╯\n╭──────────────────\n├🔥ʀᴇᴀᴅʏ ʙᴏᴛ ᴘʀᴏᴛᴇᴄᴛ\n├🔥ʀᴏᴏᴍ sᴍᴜʟᴇ / ᴇᴠᴇɴᴛ \n├🔥ʀᴇᴀᴅʏ sʙ ᴏɴʟʏ \n├🔥sʙ ᴏɴʟʏ + ᴀᴊs \n├🔥sʙ + ᴀssɪsᴛ + ᴀᴊs \n├🔥ʟᴏɢɪɴ ᴊs / ʙʏᴘᴀs / ɴɪɴᴊᴀ\n├🔥ɴᴇᴡ ᴘᴇᴍʙᴜᴀᴛᴀɴ sᴄ ʙᴏᴛ \n├🔥ɴᴇᴡ ʙᴇʟᴀᴊᴀʀ ʙᴏᴛ \n├🔥ᴘᴇᴍᴀsᴀɴɢ sʙ ᴋᴇ ᴛᴇᴍᴘʟᴀᴛᴇ\n├🔥ʀᴇᴀᴅʏ ᴀᴋᴜɴ ᴄᴏɪɴ\n├🔥ʀᴇᴀᴅʏ ᴄᴏɪɴ ɢɪғᴛ \n╰────────────────── \n╭─────────────────\n├ line.me/ti/p/~fareelkiller\n╰─────────────────", [sender])
                           break
                           
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    farel.sendMessage(msg.to,"「ᴄᴇᴋ ɪᴅ sᴛɪᴄᴋᴇʀ」\nsᴛᴋɪᴅ : " + msg.contentMetadata["STKID"] + "\nsᴛᴋᴘᴋɢɪᴅ : " + msg.contentMetadata["STKPKGID"] + "\nsᴛᴋᴠᴇʀ : " + msg.contentMetadata["STKVER"]+ "\n\n「ʟɪɴᴋ sᴛɪᴄᴋᴇʀ」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    farel.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = farel.getContact(msg.contentMetadata["mid"])
                        path = farel.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        farel.sendMessage(msg.to,"ɴᴀᴍᴀ : " + msg.contentMetadata["displayName"] + "\nᴍɪᴅ : " + msg.contentMetadata["mid"] + "\nsᴛᴀᴛᴜs ᴍsɢ : " + contact.statusMessage + "\nᴘɪᴄᴛᴜʀᴇ ᴜʀʟ : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        farel.sendImageWithURL(msg.to, image)
                        
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.contentType == 16:
                        url = msg.contentMetadata["postEndUrl"]
                        farel.likePost(url[25:58], url[66:], likeType=1004)
                        farel.createComment(url[25:58], url[66:], settings["comment"])
                        print ("ᴀᴜᴛᴏ ʟɪᴋᴇ ᴅᴏɴᴇ")
                        sendTextTemplate(msg.to,"👍 ᴀᴜᴛᴏ ʟɪᴋᴇ ᴅᴏɴᴇ")
                        settings["likeOn"] = False
        if op.type == 25 or op.type == 26:	     
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    sendTextTemplate(msg.to,"sᴛᴋɪᴅ : " + msg.contentMetadata["STKID"] + "\nsᴛᴋᴘᴋɢɪᴅ : " + msg.contentMetadata["STKPKGID"] + "\nsᴛᴋᴠᴇʀ : " + msg.contentMetadata["STKVER"]+ "\n\n「ʟɪɴᴋ sᴛɪᴄᴋᴇʀ」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    farel.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = farel.getContact(msg.contentMetadata["mid"])
                        path = farel.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        sendTextTemplate(msg.to,"ɴᴀᴍᴀ : " + msg.contentMetadata["displayName"] + "\nᴍɪᴅ : " + msg.contentMetadata["mid"] + "\nsᴛᴀᴛᴜs ᴍsɢ : " + contact.statusMessage + "\nᴘɪᴄᴛᴜʀᴇ ᴜʀʟ: http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        farel.sendImageWithURL(msg.to, image)
                         
               if msg.contentType == 2:
                   if msg._from in admin:
                       if msg._from in settings["ChangeVideoProfilevid"]:
                            settings["ChangeVideoProfilePicture"][msg._from] = True
                            del settings["ChangeVideoProfilevid"][msg._from]
                            farel.downloadObjectMsg(msg_id,'path','video.mp4')
                            sendTextTemplate(msg.to,"sᴇɴᴅ ɢᴀᴍʙᴀʀɴʏᴀ...")
                            
               if msg.contentType == 1:
                   if msg._from in admin:
                       if msg._from in settings["ChangeVideoProfilePicture"]:
                            del settings["ChangeVideoProfilePicture"][msg._from]
                            farel.downloadObjectMsg(msg_id,'path','image.jpg')
                            farel.nadyacantikimut('video.mp4','image.jpg')
                            sendTextTemplate(msg.to,"ɢᴀɴᴛɪ ᴠɪᴅɪᴏ ᴘʀᴏғɪʟ ᴅᴏɴᴇ!!!")
#===================================[ ] ADD Bots
               if msg.contentType == 13:
                 if msg._from in admin:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        sendTextTemplate(msg.to,"🔥sᴜᴅᴀʜ ᴊᴀᴅɪ ʙᴏᴛ")
                        wait["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        wait["addbots"] = True
                        sendTextTemplate(msg.to,"🔥ᴅᴏɴᴇ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ᴀɴɢɢᴏᴛᴀ ʙᴏᴛ")
                 if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        sendTextTemplate(msg.to,"🔥ᴅᴏɴᴇ ᴍᴇɴɢʜᴀᴘᴜs ᴀɴɢɢᴏᴛᴀ ʙᴏᴛ")
                    else:
                        wait["dellbots"] = True
                        sendTextTemplate(msg.to,"🔥ɪᴛᴜ ʙᴜᴋᴀɴ ᴀɴɢɢᴏᴛᴀ ʙᴏᴛ")
                        
#===================================[ ]  ADD Staff
                 if msg._from in admin:
                  if wait["addStaff"] == True:
                    if msg.contentMetadata["mid"] in Staff:
                        farel.sendMessage(msg.to,"🔥sᴜᴅᴀʜ ᴊᴀᴅɪ sᴛᴀғғ")
                        wait["addStaff"] = True
                    else:
                        Staff.append(msg.contentMetadata["mid"])
                        wait["addStaff"] = True
                        sendTextTemplate(msg.to,"🔥ᴅᴏɴᴇ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ sᴛᴀғғ")
                 if wait["dellStaff"] == True:
                    if msg.contentMetadata["mid"] in Staff:
                        Staff.remove(msg.contentMetadata["mid"])
                        sendTextTemplate(msg.to,"🔥ᴅᴏɴᴇ ᴍᴇɴɢʜᴀᴘᴜs sᴛᴀғғ")
                        wait["dellStaff"] = True
                    else:
                        wait["dellStaff"] = True
                        sendTextTemplate(msg.to,"🔥ɪᴛᴜ ʙᴜᴋᴀɴ sᴛᴀғғ")
#===================================[ ]  ADD admin
                 if msg._from in admin:
                  if wait["addadmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        sendTextTemplate(msg.to,"🔥ɪᴛᴜ ʙᴜᴋᴀɴ ᴀᴅᴍɪɴ")
                        wait["addadmin"] = True
                    else:
                        admin.append(msg.contentMetadata["mid"])
                        wait["addadmin"] = True
                        sendTextTemplate(msg.to,"🔥ᴅᴏɴᴇ ᴍᴇɴᴀᴍʙᴀʜ ᴀᴅᴍɪɴ")
                 if wait["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        admin.remove(msg.contentMetadata["mid"])
                        sendTextTemplate(msg.to,"🔥ᴅᴏɴᴇ ᴍᴇɴɢʜᴀᴘᴜs ᴀᴅᴍɪɴ")
                    else:
                        wait["delladmin"] = True
                        sendTextTemplate(msg.to,"🔥ɪᴛᴜ ʙᴜᴋᴀɴ ᴀᴅᴍɪɴ")
#===================================[ ]  ADD BLACKLIST
                 if msg._from in admin:
                  if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        sendTextTemplate(msg.to,"🔥sᴜᴅᴀʜ ᴀᴅᴀ ᴅɪ ʙʟᴀᴄᴋʟɪsᴛ")
                        wait["wblacklist"] = True
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = True
                        sendTextTemplate(msg.to,"🔥ᴅᴏɴᴇ ᴍᴇɴᴀᴍʙᴀʜ ʙʟᴀᴄᴋʟɪsᴛ ᴜsᴇʀ")
                  if wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        sendTextTemplate(msg.to,"🔥ᴅᴏɴᴇ ᴍᴇɴɢʜᴀᴘᴜs ʙʟᴀᴄᴋʟɪsᴛ ᴜsᴇʀ")
                    else:
                        wait["dblacklist"] = True
                        sendTextTemplate(msg.to,"🔥ᴛɪᴅᴀᴋ ᴀᴅᴀ ʙʟᴀᴄᴋʟɪsᴛ")
#===================================[ ] TALKBAN
                 if msg._from in admin:
                  if wait["Talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        sendTextTemplate(msg.to,"🔥sᴜᴅᴀʜ ᴀᴅᴀ ᴅɪ ᴛᴀʟᴋʙᴀɴ")
                        wait["Talkwblacklist"] = True
                    else:
                        wait["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        wait["Talkwblacklist"] = True
                        sendTextTemplate(msg.to,"🔥ᴅᴏɴᴇ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ᴛᴀʟᴋʙᴀɴ ᴜsᴇʀ")
                  if wait["Talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                         sendTextTemplate(msg.to,"🔥ᴅᴏɴᴇ ᴍᴇɴɢʜᴀᴘᴜs ᴛᴀʟᴋʙᴀɴ ᴜsᴇʀ")
                    else:
                        wait["Talkdblacklist"] = True
                        sendTextTemplate(msg.to,"🔥ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴅɪ ᴛᴀʟᴋʙᴀɴ")
#===================================[ ] UPDATE FOTO
               if msg.contentType == 1:
                 if msg._from in admin:
                    if Setmain["Addimage"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line-apps.com/talk/m/download.nhn?oid="+msgid
                        headers = farel.Talk.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            path = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % Setmain["Img"])
                            with open(path, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            sendTextTemplate(msg.to, "🔥ᴅᴏɴᴇ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ɢᴀᴍʙᴀʀ")
                        Setmain["Img"] = {}
                        Setmain["Addimage"] = False
               if msg.contentType == 2:
               	if settings["changevp"] == True:
               		contact = farel.getProfile()
               		path = farel.downloadFileURL("https://obs.line-scdn.net/{}".format(contact.pictureStatus))
               		path1 = farel.downloadObjectMsg(msg_id)
               		settings["changevp"] = False
               		changeVideoAndPictureProfile(path, path1)
               		sendTextTemplate1(to, "Succces Pp Video")
               if msg.toType == 2:
                 if msg._from in admin:
                   if settings["groupPicture"] == True:
                     path = farel.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     farel.updateGroupPicture(msg.to, path)
                     sendTextTemplate(msg.to, "🔥ᴅᴏɴᴇ ᴍᴇɴɢᴜʙᴀʜ ғᴏᴛᴏ ɢʀᴏᴜᴘ")

               if msg.contentType == 1:
                   if msg._from in admin:
                       if mid in Setmain["RAfoto"]:
                            path = farel.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][mid]
                            farel.updateProfilePicture(path)
                            sendTextTemplate(msg.to,"🔥ғᴏᴛᴏ ᴅᴏɴᴇ ᴅɪ ʀᴜʙᴀʜ")

               if msg.contentType == 1:
                 if msg._from in admin:
                   if settings["changePicture"] == True:
                     path1 = rell.downloadObjectMsg(msg_id)
                     path2 = far.downloadObjectMsg(msg_id)
                     path3 = ajarell.downloadObjectMsg(msg_id)
                     settings["changePicture"] = False
                     rell.updateProfilePicture(path1)
                     rell.sendMessage(msg.to, "🔥ғᴏᴛᴏ ʙᴏᴛ ᴅᴏɴᴇ ᴅɪ ʀᴜʙᴀʜ")
                     far.updateProfilePicture(path2)
                     far.sendMessage(msg.to, "🔥ғᴏᴛᴏ ʙᴏᴛ ᴅᴏɴᴇ ᴅɪ ʀᴜʙᴀʜ")
                     ajsrel.updateProfilePicture(path3)
                     ajsrel.sendMessage(msg.to, "🔥ғᴏᴛᴏ ʙᴏᴛ ᴅᴏɴᴇ ᴅɪ ʀᴜʙᴀʜ")

               if msg.contentType == 0:
                    if Setmain["autoRead"] == True:
                        farel.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == "help":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage = help()
                               sendTextTemplate(msg.to, str(helpMessage))
                                                                                       
                        if cmd == "self on":
                            if msg._from in admin:
                                wait["selfbot"] = True
                                sendTextTemplate(msg.to, "🔥ᴛᴇᴍᴘʟᴀᴛᴇ ᴀᴋᴛɪғ ʙᴏssᴋᴜ")
 
                        elif cmd == "self off":
                            if msg._from in admin:
                                wait["selfbot"] = False
                                sendTextTemplate(msg.to, "ᴛᴇᴍᴘʟᴀᴛᴇ ᴏғғ ʙᴏssᴋᴜ")
                        
                        elif cmd.startswith("broadcast: "):
                           if msg._from in admin:
                             sep = text.split(" ")
                             bc = text.replace(sep[0] + " ","")
                             saya = farel.getGroupIdsJoined()
                             for group in saya:
                                ryan = farel.getContact(mid)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "ʙʀᴏᴀᴅᴄᴀsᴛ ʙʏᴇ "
                                ret_ = "{}".format(str(bc))
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                farel.sendMessage(group, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                
                        elif cmd == "me" or text.lower() == 'gw':                            	
                                contact = farel.getProfile()
                                mids = [contact.mid]
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                status = farel.getContact(sender)                   
                                cover = farel.getProfileCoverURL(sender)                             
                                data = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(farel.getContact(msg._from).pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "{}".format(farel.getContact(sender).displayName),
                    "size": "xxs",
                    "color": "#ffffff",
                    "wrap": True,
                    "offsetStart": "10px"
                  }
                ],
                "height": "17px",
                "offsetTop": "-17px",
                "offsetStart": "18px"
              }
            ],
            "position": "absolute",
            "offsetStart": "2px",
            "offsetEnd": "0px",
            "paddingAll": "20px",
            "paddingTop": "18px",        
            "borderColor": "#ffffff",
            "cornerRadius": "10px",
            "width": "145px",
            "height": "25px",
            "offsetTop": "142px",        
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "COVER",
                "color": "#ffffff",
                "align": "center",
                "size": "xxs",
                "offsetTop": "3px"
              }
            ],
            "position": "absolute",
            "cornerRadius": "20px",
            "offsetTop": "2px",      
            "offsetStart": "2px",
            "height": "25px",
            "width": "53px",
            "borderWidth": "3px",    
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "𝕱𝖆𝖗𝖊𝖊𝖑 𝕭𝖔𝖙𝖘",
                "size": "xxs",
                "color": "#ffffff",
                "style": "normal",
                "weight": "bold",
                "offsetTop": "3px",
                "offsetStart": "7px"
              }
            ],
            "position": "absolute",
            "width": "103px",
            "height": "27px",
            "backgroundColor": "#3366ff",
            "offsetTop": "160px",
            "offsetStart": "40px",
            "borderWidth": "3px",
            "borderColor": "#3300cc",
            "cornerRadius": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(farel.getContact(mid).pictureStatus),
                "size": "full",
                "aspectRatio": "1:1",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "45px",
            "height": "45px",
            "borderWidth": "3px",
            "borderColor": "#3300cc",
            "cornerRadius": "10px",
            "offsetTop": "143px",
            "offsetStart": "2px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "4px",
        "borderColor": "#3300cc",
        "cornerRadius": "10px",
        "height": "200px"      
      }
    },
    {      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": str(farel.getProfileCoverURL(sender)),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "{}".format(farel.getContact(sender).displayName),
                    "size": "xxs",
                    "color": "#ffffff",
                    "wrap": True,
                    "offsetStart": "10px"
                  }
                ],
                "height": "17px",
                "offsetTop": "-17px",
                "offsetStart": "18px"
              }
            ],
            "position": "absolute",
            "offsetStart": "2px",
            "offsetEnd": "0px",
            "paddingAll": "20px",
            "paddingTop": "18px",        
            "borderColor": "#ffffff",
            "cornerRadius": "10px",
            "width": "145px",
            "height": "25px",
            "offsetTop": "142px",        
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "COVER",
                "color": "#ffffff",
                "align": "center",
                "size": "xxs",
                "offsetTop": "3px"
              }
            ],
            "position": "absolute",
            "cornerRadius": "20px",
            "offsetTop": "2px",      
            "offsetStart": "2px",
            "height": "25px",
            "width": "53px",
            "borderWidth": "3px",    
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "𝕱𝖆𝖗𝖊𝖊𝖑 𝕭𝖔𝖙𝖘",
                "size": "xxs",
                "color": "#ffffff",
                "style": "normal",
                "weight": "bold",
                "offsetTop": "3px",
                "offsetStart": "7px"
              }
            ],
            "position": "absolute",
            "width": "103px",
            "height": "27px",
            "backgroundColor": "#3366ff",
            "offsetTop": "160px",
            "offsetStart": "40px",
            "borderWidth": "3px",
            "borderColor": "#3300cc",
            "cornerRadius": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(farel.getContact(mid).pictureStatus),
                "size": "full",
                "aspectRatio": "1:1",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "45px",
            "height": "45px",
            "borderWidth": "3px",
            "borderColor": "#3300cc",
            "cornerRadius": "10px",
            "offsetTop": "143px",
            "offsetStart": "2px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "4px",
        "borderColor": "#3300cc",
        "cornerRadius": "10px",
        "height": "200px"      
      }
    },
    {      
      "type": "bubble",
      "size": "micro",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "image",
            "url": "https://obs.line-scdn.net/{}".format(farel.getContact(mid).pictureStatus),
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "2:3",
            "gravity": "top"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "{}".format(farel.getContact(sender).displayName),
                    "size": "xxs",
                    "color": "#ffffff",
                    "wrap": True,
                    "offsetStart": "10px"
                  }
                ],
                "height": "17px",
                "offsetTop": "-17px",
                "offsetStart": "18px"
              }
            ],
            "position": "absolute",
            "offsetStart": "2px",
            "offsetEnd": "0px",
            "paddingAll": "20px",
            "paddingTop": "18px",        
            "borderColor": "#ffffff",
            "cornerRadius": "10px",
            "width": "145px",
            "height": "25px",
            "offsetTop": "142px",        
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "PROFILE",
                "color": "#ffffff",
                "align": "center",
                "size": "xxs",
                "offsetTop": "3px"
              }
            ],
            "position": "absolute",
            "cornerRadius": "20px",
            "offsetTop": "2px",      
            "offsetStart": "2px",
            "height": "25px",
            "width": "53px",
            "borderWidth": "3px",    
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "𝕱𝖆𝖗𝖊𝖊𝖑 𝕭𝖔𝖙𝖘",
                "size": "xxs",
                "color": "#ffffff",
                "style": "normal",
                "weight": "bold",
                "offsetTop": "3px",
                "offsetStart": "7px"
              }
            ],
            "position": "absolute",
            "width": "103px",
            "height": "27px",
            "backgroundColor": "#3366ff",
            "offsetTop": "160px",
            "offsetStart": "40px",
            "borderWidth": "1px",
            "borderColor": "#3300cc",
            "cornerRadius": "5px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(farel.getContact(mid).pictureStatus),
                "size": "full",
                "aspectRatio": "1:1",
                "aspectMode": "cover"
              }
            ],
            "position": "absolute",
            "width": "45px",
            "height": "45px",
            "borderWidth": "3px",
            "borderColor": "#3300cc",
            "cornerRadius": "10px",
            "offsetTop": "143px",
            "offsetStart": "2px"
          }
        ],
        "paddingAll": "0px",
        "borderWidth": "4px",
        "borderColor": "#3300cc",
        "cornerRadius": "10px",
        "height": "200px"      
      }
      }
  ]
}
                                farel.postFlex(to, data)
 
                        elif cmd == "myset":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "╭──Fareel Bots──\n"
                                if wait["sticker"] == True: md+="├🔥sᴛɪᴄᴋᴇʀ ᴏɴ\n"
                                else: md+="├🔥sᴛɪᴄᴋᴇʀ ᴏғғ\n"
                                if wait["left"] == True: md+="├🔥ʟᴇғᴛ ᴏɴ\n"
                                else: md+="├🔥ʟᴇғᴛ ᴏғғ\n"                        
                                if wait["contact"] == True: md+="├🔥ᴄᴏɴᴛᴀᴄᴛ ᴏɴ\n"
                                else: md+="├🔥ᴄᴏɴᴛᴀᴄᴛ ᴏғғ\n"
                                if wait["talkban"] == True: md+="├🔥ᴛᴀʟᴋʙᴀɴ ᴏɴ\n"
                                else: md+="├🔥ᴛᴀʟᴋʙᴀɴ ᴏғғ\n"
                                if wait["unsend"] == True: md+="├🔥ᴜɴsᴇɴᴅ ᴏɴ\n"
                                else: md+="├🔥ᴜɴsᴇɴᴅ ᴏғғ\n"
                                if wait["Mentionkick"] == True: md+="├🔥ɴᴏᴛᴀɢ ᴏɴ\n"
                                else: md+="├🔥ɴᴏᴛᴀɢ ᴏɴ\n"
                                if wait["detectMention"] == True: md+="├🔥ʀᴇsᴘᴏɴ ᴏɴ\n"
                                else: md+="├🔥ʀᴇsᴘᴏɴ ᴏɴ\n"
                                if wait["autoJoin"] == True: md+="├🔥ᴀᴜᴛᴏᴊᴏɪɴ ᴏɴ\n"
                                else: md+="├🔥ᴀᴜᴛᴏᴊᴏɪɴ ᴏғғ\n"
                                if wait["autoAdd"] == True: md+="├🔥ᴀᴜᴛᴏᴀᴅᴅ ᴏɴ\n"
                                else: md+="├🔥ᴀᴜᴛᴏᴀᴅᴅ ᴏɴ\n"
                                if msg.to in welcome: md+="├🔥ᴡᴇʟᴄᴏᴍᴇ ᴏɴ\n"
                                else: md+="├🔥ᴡᴇʟᴄᴏᴍᴇ ᴏғғ\n"
                                if wait["autoLeave"] == True: md+="├🔥ᴀᴜᴛᴏʟᴇᴀᴠᴇ ᴏɴ\n"
                                else: md+="├🔥ᴀᴜᴛᴏʟᴇᴀᴠᴇ ᴏғғ\n"
                                if msg.to in protectqr: md+="├🔥ᴘʀᴏᴛᴇᴄᴛᴜʀʟ ᴏɴ\n"
                                else: md+="├🔥ᴘʀᴏᴛᴇᴄᴛᴜʀʟ ᴏғғ\n"
                                if msg.to in protectjoin: md+="├🔥ᴘʀᴏᴛᴇᴄᴛᴊᴏɪɴ ᴏɴ\n"
                                else: md+="├🔥ᴘʀᴏᴛᴇᴄᴛᴊᴏɪɴ ᴏғғ\n"
                                if msg.to in protectkick: md+="├🔥 ᴘʀᴏᴛᴇᴄᴛᴋɪᴄᴋ ᴏɴ\n"
                                else: md+="├🔥ᴘʀᴏᴛᴇᴄᴛᴋɪᴄᴋ ᴏғғ\n"
                                if msg.to in protectcancel: md+="├🔥ᴘʀᴏᴛᴇᴄᴛᴄᴀɴᴄᴇʟ ᴏɴ\n"
                                else: md+="├🔥ᴘʀᴏᴛᴇᴄᴛᴄᴀɴᴄᴇʟ ᴏғғ\n╰──────────────╯\n"
                                sendTextTemplate(msg.to, md+"\nᴛᴀɴɢɢᴀʟ : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nᴊᴀᴍ [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")

                        elif cmd == "asem" or text.lower() == 'asemmm' or text.lower() == 'sem' or text.lower() == 'semm':
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "ᴋᴇᴛᴀʜᴜᴀɴ ʟᴜ ᴋᴀᴋ ʙᴇʟᴜᴍ ᴍᴀɴᴅɪ ᴘᴀɴᴛᴇsᴀɴ ʙᴀᴜ ᴀssᴇᴇᴇᴍᴍ😂")

                        elif cmd == "pekok" or text.lower() == 'pekokkk':
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "sᴇsᴀᴍᴀ ᴘᴇᴋᴏᴋ ᴅɪ ʟᴀʀɪɴɢ ᴄᴏʟʟʏ😃😃")

                        elif cmd == "sue":
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "ᴇᴍᴀɴɢ ᴜᴅᴀʜ sᴜᴇ ᴘᴜɴʏᴀ ᴋᴋ, ᴋᴀʟᴏ ɢᴀᴋ sᴜᴇ, ɢᴀᴋ ʙᴀᴋᴀʟᴀɴ ʙɪsᴀ ᴅɪ ᴛᴜsᴜᴋ ᴀɴᴜ ᴋᴋ😂")
                             
                        elif cmd == "dudul" or text.lower() == 'pea':
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "sᴇsᴀᴍᴀ ᴅᴜᴅᴜʟ ᴊᴀɴɢᴀɴ sᴀʟɪɴɢ ʙᴜʟʟʏ ᴋᴋ😂, ᴅɪ ʙᴀᴡᴀʜ ᴍᴜ ᴊᴜɢᴀ ᴜᴅᴀʜ ɢᴜɴᴅᴜʟ ᴋᴋ 😜")
                        
                        elif cmd == "typo" or text.lower() == 'typo':
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "ᴛʏᴘᴏ ᴍᴜʟᴜ sɪʜ, ᴊᴀʀɪ ᴊᴇᴍᴘᴏʟ sᴇᴍᴜᴀ sᴏᴀʟ ɴʏᴀ😂")
                        
                        elif cmd == "aduh" or text.lower() == 'waduh':
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "ᴡᴀᴅᴜʜ ᴋᴇɴᴀᴘᴀ ᴋᴋ\nᴋᴇᴊᴇᴅᴏᴛ ᴘɪɴᴛᴜ ʏᴀ. ᴇᴍᴀɴɢ ᴇɴᴀᴋ😂")
                               
                        elif cmd == "hus" or text.lower() == 'huss':
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "ᴅɪ ʟᴀʀᴀɴɢ ʙʀɪsɪᴋ ᴅɪ ʀᴏᴏᴍ ɪɴɪ ʙᴀɴʏᴀᴋ ʏᴀɴɢ ᴏʟᴇɴɢ😂")
                               
                        elif cmd == "pm":
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "sᴏʀʀʏ ᴀᴋᴜ ᴛɪᴅᴀᴋ ɴᴇʀɪᴍᴀ ᴘᴍ ᴏʀᴀɴɢ ᴊᴏᴍʙʟᴏ ɴɢᴇɴᴇs😜")

                        elif text.lower() == "midku":
                          if wait["selfbot"] == True:
                               sendTextTemplate(msg.to, msg._from)
                               
                        elif cmd == "ngopi" or text.lower() == 'ngopi susu guys':
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "ᴜᴅᴀʜ ᴘᴀᴅᴀ ɴɢᴏᴘɪ ʙᴇʟᴜᴍ ᴋᴋ, ᴋᴀʟᴏ ʙᴇʟᴜᴍ sɪɴɪ ᴋᴋ ɴʏᴜsᴜ ʙᴀʀᴇɴɢ 😜")
                               
                        elif cmd == "nah" or text.lower() == 'nahhh':
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "ɴᴀʜ ɴᴏʜ ɴᴀʜ ɴᴏʜ\nᴘᴀʟᴀᴋ ᴋᴜ ᴍᴜᴍᴇᴛ\nᴋʟᴏ ʟᴜ ʙɪʟᴀɴɢ ɴᴀʜ ɴᴏʜ😂")
                               
                        elif cmd == "salken":
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "sᴀʟᴋᴇɴᴊᴜ ᴋᴋ\nsᴇᴍᴏɢᴀ ᴀᴡᴀʟ ᴋɪᴛᴀ ᴋᴇɴᴀʟ\nʙɪsᴀ ᴊᴀᴅɪ ᴊᴏᴅᴏʜ ʏᴀ ᴋᴋ😍")
                               
                        elif cmd == "bomat":
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "ᴀᴋᴜ ᴍᴀʜ ʙᴏᴅᴏʜ ᴀᴍᴀᴛ\nᴇᴍᴀɴɢ ɴʏᴀ ʟᴜ sɪᴀᴘᴀ😂")
                               
                        elif cmd == "cipok":
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "ᴄɪᴘᴏᴋ ᴄɪᴘᴏᴋ ᴄɪᴘᴏᴋ\nᴋᴇɴᴄɪɴɢ ʟᴜ ᴀᴊᴀ ᴍᴀsɪʜ ɢᴋ ʟᴜʀᴜs\nᴍᴀᴜ ᴄɪᴘᴏᴋ ᴏʀᴀɴɢ😜")

                        elif cmd == "janda":
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "ᴇᴍᴀɴɢ ᴋᴀᴜ ᴊᴀɴᴅᴀ ᴋᴋ\nᴇᴍᴀɴɢ ᴍᴀᴜ sᴀᴍᴀ ᴊᴀɴᴅᴀ ᴀɴᴀᴋ 3 ᴋᴋ\nᴛᴀᴘɪ sᴀʏᴀɴɢ ᴜᴅᴀʜ ᴀɴᴜ ᴘᴜɴʏᴀ ᴋᴋ 😂")

                        elif cmd == "duda":
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "ᴇᴍᴀɴɢ ᴀᴋᴜ ᴅᴜᴅᴀ ᴋᴋ,,,\nᴋʟᴏ ᴋᴋ ᴍᴀᴜ ᴀᴍᴀ ᴅᴜᴅᴀ\nᴀʏᴜᴋ ᴋɪᴛᴀ ᴊᴀᴅɪᴀɴ😂")

                        elif cmd == "salam":
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")

                        elif cmd == "bot":
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "ʙᴀᴛ ʙᴏᴛ ʙᴀᴛ ʙᴏᴛ ᴍᴀᴛᴀᴍᴜ ɪᴛᴜ ʙᴏᴛ\nᴀᴋᴜ ᴍᴀʜ ʙᴜᴋᴀɴ ʙᴏᴛ\nᴛᴀᴘɪ ʙᴀᴘᴀᴋᴇ ʙᴏᴛ 😜")

                        elif cmd == "siang":
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "sɪᴀɴɢ ᴊᴜɢᴀ ᴋᴋ ᴋᴜ sʏᴀɴᴛɪᴋ, ᴜᴅᴀʜ ᴅᴀᴘᴀᴛ ᴛɪᴋᴜɴɢᴀɴ ʙᴇʟᴜᴍ ᴋᴋ 😅")

                        elif cmd == "pagi":
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "ᴘᴀɢɪ ᴊᴜɢᴀ ᴋᴋ, ᴜᴅᴀʜ sᴀʀᴀᴘᴀɴ ʙᴇʟᴜᴍ 😘")

                        elif cmd == "sore":
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "sᴏʀᴇ ᴊᴜɢᴀ ᴋᴋ, ᴜᴅᴀʜ ᴍᴀɴᴅɪ ʙᴇʟᴜᴍ, ᴋᴀʟᴏ ʙᴇʟᴜᴍ sɪɴɪ ᴀᴋᴜ ᴛᴇᴍᴇɴɪ ᴋᴋ ᴍᴀɴᴅɪ 🤗هُ")

                        elif cmd == "malam":
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "ᴍᴀʟᴀᴍ ᴊᴜɢᴀ ᴋᴋ, ᴡᴀᴋᴛᴜ ɴʏᴀ ɴɪᴋᴜɴɢ ᴇɴᴀᴋ ɴʏᴀ ᴍᴀʟᴀᴍ-ᴍᴀʟᴀᴍ ɢɪɴɪ ᴋᴋ 😛")

                        elif cmd == "kojom":
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "ɴᴀʜ ᴋᴀɴ,,,ɴɢᴀᴊᴀᴋɪɴ ᴋᴏᴊᴏᴍ,,,ɴᴛᴀʀ ʙᴏᴊᴏɴᴇ ᴍᴀʀᴀʜ ʙᴀʀᴜ ᴛᴀᴜ ʀᴀsᴀ ᴋᴋ 😜هُ")

                        elif cmd == "nikung":
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "ᴀʏᴜᴋ ᴋᴋ ᴋɪᴛᴀ ɴɪᴋᴜɴɢ, ʟᴀɴɢsᴜɴɢ ᴘᴍ ᴀᴊᴀ ʏᴀ ᴋᴋ😂")

                        elif cmd == "assalamualaikum" or text.lower() == 'asalamualaikum':
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ  ")

                        elif cmd == "susu" or text.lower() == 'nyusu':
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "sᴜsᴜ sᴜsᴜ sᴜsᴜ, ᴅᴀʀɪ ᴋᴇᴄɪʟ ʟᴜ sᴜᴅᴀʜ ᴅɪ ɴʏᴜsᴜɪɴ, ᴍᴀsᴀ ᴍɪɴᴛᴀ ɴʏᴜsᴜ sᴀᴍᴀ ʀᴏɴᴅᴏ ᴋᴋ😂")

                        elif cmd == "setan":
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "sᴇᴛᴀɴ sᴇᴛᴀɴ sᴇᴛᴀɴ, ᴇᴍᴀɴɢ ᴍᴜᴋᴀ ʟᴜ ᴋᴀʏᴀᴋ sᴇᴛᴀɴ ᴋᴋ😂")

                        elif cmd == "makan":
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "ᴜᴅᴀʜ ᴘᴀᴅᴀ ᴍᴀᴋᴀɴ ʙᴇʟᴏᴍ ᴋᴋ, ᴋᴀʟᴏ ʙᴇʟᴏᴍ sɪɴɪ ᴀᴋᴜ sᴜᴀᴘɪɴ ᴋᴋ")

                        elif cmd == "minum":
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "sɪɴɪ ᴋᴋ ᴍɪɴᴜᴍ ʙᴀʀᴇɴɢ ᴋɪᴛᴀ😛")

                        elif cmd == "payment":
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "ᴘᴀʏᴍᴇɴᴛ ᴠɪᴀ ʙᴀɴᴋ\nɴᴏ ʀᴇᴋ : 481901020711531\nᴀᴛᴀs ɴᴀᴍᴀ : muhazir\nʙᴀɴᴋ ʙʀɪ\n\nᴠɪᴀ ᴘᴜʟsᴀ\n08992906209 ")

                        elif cmd == "wa'alaikumsalam" or text.lower() == 'waalaikumsalam':
                          if wait["selfbot"] == True:                            
                               sendTextTemplate(msg.to, "ɴᴀʜ ɢɪᴛᴜ ᴊᴀᴡᴀʙ sᴀʟᴀᴍ sᴇsᴀᴍᴀ ᴍᴜsʟɪᴍ😘😍")
                        elif cmd == "cvp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                            	settings["changevp"] = True
                            	sendTextTemplate(to, "sʜᴀʀᴇ ᴠɪᴅᴇᴏɴʏᴀ")
                        elif cmd == "jandeee":
                          if wait["selfbot"] == True:                            
                               farel.sendMessage(msg.to, "nyaman nyaman nyaman nyaman nyaman nyaman    ❌.👁️.★.★.★.👁️.❌.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.👿.👿.👿 ❌.👁️.★.★.★.👁️.❌.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.☆.👿.👿.👿.\n❌.👁️.★.★.★.👁️.❌.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.☆.👿.👿.👿.\n❌.👁️.★.★.★.👁️.❌.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.☆.👿.👿.👿.")


                        elif cmd == "about":
                                groups = farel.getGroupIdsJoined()
                                contacts = farel.getAllContactIds()
                                blockeds = farel.getBlockedContactIds()
                                crt = "u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540"
                                supp = "u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540"
                                suplist = []
                                lists = []
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                timeNoww = time.time()
                                for i in range(len(day)):
                                   if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                   if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nâ Jam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                data = {
                                        "type": "flex",
                                        "altText": "ᴀʙᴏᴜᴛ",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#000000"
    }
  },
  "type": "bubble",
  "size": "micro",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "url": "https://obs.line-scdn.net/{}".format(farel.getContact(mid).pictureStatus),
            "type": "image"
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "text": "ᴏʟᴇɴɢ\nᴋɪʟʟᴇʀ\nᴛᴇᴀᴍ\nsᴇʟғʙᴏᴛ",
            "size": "xs",
            "color": "#FFFF00",
            "wrap": True,
            "weight": "bold",
            "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#FF0000"
      },
      {
        "contents": [
          {
            "contents": [
              {
                "text": " {}".format(farel.getProfile().displayName),
                "size": "xs",
                "margin": "none",
                "color": "#ADFF2F",
                "weight": "bold",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "contents": [
              {
                "text": "ɢʀᴏᴜᴘ: {}".format(str(len(groups))),
                "size": "xs",
                "margin": "none",
                "color": "#FFFF00",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "text": "ғʀɪᴇɴᴅ: {}".format(str(len(contacts))),
                "size": "xs",
                "margin": "none",
                "color": "#FFFF00",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "text": "ʙʟᴏᴄᴋ: {}".format(str(len(blockeds))),
                "size": "xs",
                "margin": "none",
                "color": "#FFFF00",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "xs",
    "layout": "vertical"
  },
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "ᴏʟᴇɴɢ",
        "size": "xs",
        "wrap": True,
        "weight": "bold",
        "color": "#7CFC00",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/~fareelkiller"
        },
        "align": "center"
      },
      {
        "type": "separator",
        "color": "#000000"
      },
      {
        "type": "text",
        "text": "ᴋɪʟʟᴇʀ",
        "size": "xs",
        "wrap": True,
        "weight": "bold",
        "color": "#7CFC00",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/~fareelkiller"
        },
        "align": "center"
      }
    ]
  }
}
}
                                farel.postTemplate(to, data)

                        elif cmd == "aim":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                  musik(to)
                                  
                        elif cmd == ".me" or text.lower() == 'gue':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                msg.contentType = 13
                                msg.contentMetadata = {'mid': mid}
                                farel.sendContact(to, mid)

                        elif "autoreject " in msg.text.lower():
                            xpesan = msg.text.lower()
                            xres = xpesan.replace("autoreject ","")
                            if xres == "off":
                                settings['autorejc'] = False
                                sendTextTemplate(msg.to,"ᴀᴜᴛᴏʀᴇᴊᴇᴄᴛ ᴏғғ ɢᴀᴋ ᴀᴍᴀɴ ᴅᴀᴅɪ sᴘᴀᴍ")
                            elif xres == "on":
                                settings['autorejc'] = True
                                sendTextTemplate(msg.to,"ᴀᴜᴛᴏʀᴇᴊᴇᴄᴛ ᴏɴ ᴀᴍᴀɴ ᴅᴀʀɪ sᴘᴀᴍ")
                        
                        elif text.lower() == "mid":
                               farel.sendMessage(msg.to, msg._from)
                        elif text.lower() == "mymid":
                               farel.sendMessage(msg.to, msg._from)

                        elif ("Mid " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = farel.getContact(key1)
                               farel.sendMessage(msg.to, "ɴᴀᴍᴀ : "+str(mi.displayName)+"\nᴍɪᴅ : " +key1)
                               farel.sendMessage(msg.to, None, contentMetadata={'u03addfbbbdb20585381383e5d173d28d': key1}, contentType=13)

                        elif ("Info " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = farel.getContact(key1)
                               sendTextTemplate(msg.to, "ɴᴀᴍᴀ : "+str(mi.displayName)+"\nᴍɪᴅ : " +key1+"\nsᴛᴀᴛᴜs ᴍsɢ"+str(mi.statusMessage))
                               farel.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(farel.getContact(key1)):
                                   farel.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   farel.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                        elif cmd == "mybot":
                          if wait["selfbot"] == True:
                            if msg._from in admin or msg._from in creator:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': mid}
                               farel.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': AjsFarelKiler}
                               farel.sendMessage1(msg)
                               msg.contentType = 13

                        elif text.lower() == "hapus chat":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   farel.removeAllMessages(op.param2)
                                   sendTextTemplate(msg.to,"🔥ʜᴀᴘᴜs ᴄʜᴀᴛ ᴅᴏɴᴇ")
                               except:
                                   pass
                                   
                        elif text.lower() == "mykey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sendTextTemplate(msg.to, "「Mykey」\nSetkey bot mu「 " + str(Setmain["keyCommand"]) + " 」")
                               
                        elif cmd.startswith("setkey "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   sendTextTemplate(msg.to, "🔥ɢᴀɢᴀʟ ᴍᴇɴɢɢᴀɴᴛɪ ᴋᴇʏ")
                               else:
                                   Setmain["keyCommand"] = str(key).lower()
                                   sendTextTemplate(msg.to, "🔥sᴇᴛᴋᴇʏ\n🔥ᴅɪ ɢᴀɴᴛɪ ᴊᴀᴅɪ「{}」".format(str(key).lower()))

                        elif text.lower() == "resetkey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               Setmain["keyCommand"] = ""
                               sendTextTemplate(msg.to, "🔥sᴇᴛᴋᴇʏ\n🔥ᴋᴇᴍʙᴀʟɪ ᴋᴇ ᴀᴡᴀʟ")

                        elif cmd == "restart":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sendTextTemplate(msg.to, "🔥ᴡᴀɪᴛ....")
                               Setmain["restartPoint"] = msg.to
                               restartBot()
                               sendTextTemplate(msg.to, "🔥ᴅᴏɴᴇ ʀᴇsᴛᴀʀᴛ...")
                            
                        elif cmd == "runtime":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               eltime = time.time() - mulai
                               bot = "🔥ʙᴏᴛ ᴀᴋᴛɪғ sᴇʟᴀᴍᴀ\n" +waktu(eltime)
                               sendTextTemplate(msg.to,bot)
                            
                        elif cmd == "ginfo":
                          if msg._from in admin:
                            try:
                                G = farel.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "🔥ᴛᴇʀᴛᴜᴛᴜᴘ"
                                    gTicket = "♦️ᴛɪᴅᴀᴋ ᴀᴅᴀ"
                                else:
                                    gQr = "🔥ᴛᴇʀʙᴜᴋᴀ"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(farel.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                sendTextTemplate(msg.to, "🔥Fareel Bots🔥ɢʀᴜᴘ ɪɴғᴏ\n\n🔥ɴᴀᴍᴀ ɢʀᴜᴘ : {}".format(G.name)+ "\n🔥ɪᴅ ɢʀᴜᴘ : {}".format(G.id)+ "\n🔥ᴘᴇᴍʙᴜᴀᴛ : {}".format(G.creator.displayName)+ "\n🔥ᴡᴀᴋᴛᴜ ᴅɪ ʙᴜᴀᴛ : {}".format(str(timeCreated))+ "\n🔥ᴊᴜᴍʟᴀʜ ᴀɴɢɢᴏᴛᴀ : {}".format(str(len(G.members)))+ "\n🔥ᴊᴜᴍʟᴀʜ ᴘᴇɴᴅɪɴɢᴀɴ : {}".format(gPending)+ "\n🔥ɢʀᴜᴘ ǫʀ : {}".format(gQr)+ "\n🔥ɢʀᴜᴘ ᴛɪᴄᴋᴇᴛ : {}".format(gTicket))
                                farel.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                            except Exception as e:
                                sendTextTemplate(msg.to, str(e))

                        elif cmd.startswith("infogrup "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = farel.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = farel.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "🔥ᴛɪᴅᴀᴋ ᴅɪ ᴛᴇᴍᴜᴋᴀɴ"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "🔥ᴛᴇʀᴛᴜᴛᴜᴘ"
                                    gTicket = "♦️ᴛɪᴅᴀᴋ ᴀᴅᴀ"
                                else:
                                    gQr = "🔥ᴛᴇʀʙᴜᴋᴀ"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(farel.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "🔥ᴄᴍᴅ ɢʀᴜᴘ ɪɴғᴏ🔥\n"
                                ret_ += "\n🔥ɴᴀᴍᴀ ɢʀᴜᴘ : {}".format(G.name)
                                ret_ += "\n🔥ɪᴅ ɢʀᴜᴘ : {}".format(G.id)
                                ret_ += "\n🔥ᴘᴇᴍʙᴜᴀᴛ : {}".format(gCreator)
                                ret_ += "\n🔥ᴡᴀᴋᴛᴜ ᴅɪʙᴜᴀᴛ : {}".format(str(timeCreated))
                                ret_ += "\n🔥ᴊᴜᴍʟᴀʜ ᴀɴɢɢᴏᴛᴀ : {}".format(str(len(G.members)))
                                ret_ += "\n🔥ᴊᴜᴍʟᴀʜ ᴘᴇɴᴅɪɴɢᴀɴ : {}".format(gPending)
                                ret_ += "\n🔥ɢʀᴜᴘ ǫʀ : {}".format(gQr)
                                ret_ += "\n🔥ɢʀᴜᴘ ᴛɪᴄᴋᴇᴛ : {}".format(gTicket)
                                ret_ += ""
                                sendTextTemplate(to, str(ret_))
                            except:
                                pass

                        elif cmd.startswith("infomem "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = farel.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = farel.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " "├🔥"+ str(no) + ". " + mem.displayName
                                sendTextTemplate(to," 🔥ɢʀᴜᴘ ɴᴀᴍᴇ : [ " + str(G.name) + " ]\n\n   [ʟɪsᴛ ᴀɴɢɢᴏᴛᴀ ]\n" + ret_ + "\n\n🔥ᴛᴏᴛᴀʟ %i ᴀɴɢɢᴏᴛᴀ🔥" % len(G.members))
                            except: 
                                pass

                        elif cmd == "friendlist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = farel.getAllContactIds()
                               for i in gid:
                                   G = farel.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "├🔥" + str(a) + ". " +G.displayName+ "\n"
                               sendTextTemplate(msg.to,"╭── 🔥ɢʀᴏᴜᴘ ʟɪsᴛ🔥\n│\n"+ma+"│\n╰──🔥ᴛᴏᴛᴀʟ"+str(len(gid))+"ɢʀᴏᴜᴘ🔥")

                        elif cmd == "glist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = farel.getGroupIdsJoined()
                               for i in gid:
                                   G = farel.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "├🔥" + str(a) + ". " +G.name+ "\n"
                               sendTextTemplate(msg.to,"╭── 🔥ɢʀᴏᴜᴘ ʟɪsᴛ🔥\n│\n"+ma+"│\n╰──🔥ᴛᴏᴛᴀʟ"+str(len(gid))+"ɢʀᴏᴜᴘ🔥")

                        elif cmd == "open":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = farel.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   farel.updateGroup(X)
                                   sendTextTemplate(msg.to, "🔥ᴏᴘᴇɴ ᴜʀʟ")

                        elif cmd == "close":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = farel.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   farel.updateGroup(X)
                                   sendTextTemplate(msg.to, "🔥ᴄʟᴏsᴇ ᴜʀʟ")

                        elif cmd == "url grup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   x = farel.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      farel.updateGroup(x)
                                   gurl = farel.reissueGroupTicket(msg.to)
                                   farel.sendMessage(msg.to, "ɴᴀᴍᴀ : "+str(x.name)+ "\nᴜʀʟ ɢʀᴜᴘ : http://line.me/R/ti/g/"+gurl)

#===========BOT UPDATE============#
                        elif cmd == "updategrup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                sendTextTemplate(msg.to,"🔥ᴋɪʀɪᴍ ғᴏᴛᴏɴʏᴀ")

                        elif cmd == "updatebot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["changePicture"] = True
                                sendTextTemplate(msg.to,"🔥ᴋɪʀɪᴍ ғᴏᴛᴏɴʏᴀ")
                                rell.sendMessage(msg.to,"🔥ᴋɪʀɪᴍ ғᴏᴛᴏɴʏᴀ")
                                far.sendMessage(msg.to,"🔥ᴋɪʀɪᴍ ғᴏᴛᴏɴʏᴀ")
                                FarelKilerAjs.sendMessage(msg.to,"🔥ᴋɪʀɪᴍ ғᴏᴛᴏɴʏᴀ")
                                
                        elif cmd == "gf":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["ChangeVideoProfilevid"][msg._from] = True
                                sendTextTemplate(msg.to,"sᴇɴᴅ ᴠɪᴅɪᴏ ɴʏᴀ...")
                                
                        elif cmd.startswith("changedualurl: "):
                            if msg._from in admin:
                                sep = msg.text.split(" ")
                                url = msg.text.replace(sep[0] + " ","")                            
                                farel.downloadFileURL(url,'path','video.mp4')
                                settings["ChangeVideoProfilePicture"][msg._from] = True
                                sendTextTemplate(msg.to, "sᴇɴᴅ ɢᴀᴍʙᴀʀ ɴʏᴀ.....")
                                
                        elif cmd == "myfoto":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["RAfoto"][mid] = True
                                sendTextTemplate(msg.to,"🔥ᴋɪʀɪᴍ ғᴏᴛᴏɴʏᴀ")
                                
                        elif cmd == "cp1":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["RAfoto"][FarelKiler] = True
                                rell.sendMessage(msg.to,"🔥ᴋɪʀɪᴍ ғᴏᴛᴏɴʏᴀ")
                                
                        elif cmd == "cp2":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["RAfoto"][FarelKiler1] = True
                                far.sendMessage(msg.to,"🔥ᴋɪʀɪᴍ ғᴏᴛᴏɴʏᴀ")
                                
                        elif cmd == "cp3":
                            if msg._from in admin:
                                Setmain["RAfoto"][AjsFarelKiler] = True
                                FarelKilerAjs.sendMessage(msg.to,"🔥ᴋɪʀɪᴍ ғᴏᴛᴏɴʏᴀ")

                        elif cmd.startswith("myname: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = farel.getProfile()
                                profile.displayName = string
                                farel.updateProfile(profile)
                                sendTextTemplate(msg.to,"🔥ɴᴀᴍᴀ ᴅɪ ɢᴀɴᴛɪ ᴊᴀᴅɪ " + string + "")

                        elif cmd.startswith("cn1: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = rell.getProfile()
                                profile.displayName = string
                                rell.updateProfile(profile)
                                rell.sendMessage(msg.to,"🔥ɴᴀᴍᴀ ᴅɪ ɢᴀɴᴛɪ ᴊᴀᴅɪ " + string + "")

                        elif cmd.startswith("cn2: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = far.getProfile()
                                profile.displayName = string
                                far.updateProfile(profile)
                                far.sendMessage(msg.to,"🔥ɴᴀᴍᴀ ᴅɪ ɢᴀɴᴛɪ ᴊᴀᴅɪ " + string + "")

                        elif cmd.startswith("cn3: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ajsrel.getProfile()
                                profile.displayName = string
                                ajsrel.updateProfile(profile)
                                ajsrel.sendMessage(msg.to,"🔥ɴᴀᴍᴀ ᴅɪ ɢᴀɴᴛɪ ᴊᴀᴅɪ " + string + "")

#===========BOT UPDATE============#
                        elif cmd == "hay" or text.lower() == 'cipok':
                           if wait["selfbot"] == True:
                            if msg._from in admin:
                             group = farel.getGroup(msg.to)
                            nama = [contact.mid for contact in group.members]
                            k = len(nama)//20
                            for a in range(k+1):
                                txt = u''
                                s=0
                                b=[]
                                for i in group.members[a*20 : (a+1)*20]:
                                    b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                    s += 7
                                    txt += u'@Zero \n'
                                farel.sendMessage(msg.to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)

                        elif cmd == "listbot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                a = 0
                                for m_id in Bots:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +farel.getContact(m_id).displayName + "\n"
                                sendTextTemplate(msg.to,"🔥ʟɪsᴛ ʙᴏᴛ\n\n"+ma+"\n🔥ᴛᴏᴛᴀʟ ʙᴏᴛ ᴀʙɪ「%s」" %(str(len(Bots))))

                        elif cmd == "listadmin":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                a = 0
                                b = 0
                                c = 0
                                for m_id in owner:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +farel.getContact(m_id).displayName + "\n"
                                for m_id in admin:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +farel.getContact(m_id).displayName + "\n"
                                for m_id in Staff:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +farel.getContact(m_id).displayName + "\n"
                                sendTextTemplate(msg.to,"♦️ᴀᴅᴍɪɴ \n\n♦️sᴜᴘᴇʀ ᴀᴅᴍɪɴ :\n"+ma+"\n♦️ᴀᴅᴍɪɴ :\n"+mb+"\n♦️sᴛᴀғғ :\n"+mc+"\n♦️ᴊᴜᴍʟᴀʜ ᴀᴅᴍɪɴ ᴀʙɪ「%s」♦️" %(str(len(owner)+len(admin)+len(Staff))))

                        elif cmd == "cekad":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                a = 0
                                b = 0
                                c = 0
                                for m_id in owner:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +farel.getContact(m_id).displayName + "\n"
                                for m_id in admin:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +farel.getContact(m_id).displayName + "\n"
                                for m_id in Staff:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +farel.getContact(m_id).displayName + "\n"
                                sendTextTemplate(msg.to,"🔥ᴀᴅᴍɪɴ \n🔥sᴜᴘᴇʀ ᴀᴅᴍɪɴ :\n"+ma+"\n🔥ᴀᴅᴍɪɴ :\n"+mb+"\n🔥sᴛᴀғғ :\n"+mc+"\n🔥ᴊᴜᴍʟᴀʜ ᴀᴅᴍɪɴ ᴀʙɪ「%s」" %(str(len(owner)+len(admin)+len(Staff))))

                        elif cmd == "cekpro":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                md = ""
                                a = 0
                                b = 0
                                c = 0
                                d = 0
                                gid = protectqr
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +farel.getGroup(group).name + "\n"
                                gid = protectkick
                                for group in gid:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +farel.getGroup(group).name + "\n"
                                gid = protectjoin
                                for group in gid:
                                    d = d + 1
                                    end = '\n'
                                    md += str(d) + ". " +farel.getGroup(group).name + "\n"
                                gid = protectcancel
                                for group in gid:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +farel.getGroup(group).name + "\n"
                                sendTextTemplate(msg.to,"🔥ᴘʀᴏ ɢʀᴏᴜᴘ\n"+ma+(str(len(protectqr)+len(protectkick)+len(protectjoin)+len(protectcancel))))

                        elif cmd == "fareel":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                farel.sendMessage(msg.to,responsename1)
                                
                        elif cmd == "byeme":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = farel.getGroup(msg.to)
                                farel.leaveGroup(msg.to)

                        elif cmd == "in":
                            if msg._from in admin:
                                G = farel.getGroup(msg.to)
                                ginfo = farel.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                farel.updateGroup(G)
                                invsend = 0
                                Ticket = farel.reissueGroupTicket(msg.to)
                                rell.acceptGroupInvitationByTicket(msg.to,Ticket)
                                far.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = farel.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                farel.updateGroup(G)

                        elif cmd == "out": 
                            if msg._from in admin:
                                G = farel.getGroup(msg.to)
                                rell.leaveGroup(msg.to)
                                far.leaveGroup(msg.to)
                                    
                        elif cmd == "st":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    ginfo = farel.getGroup(msg.to)
                                    farel.inviteIntoGroup(msg.to, [RelAjs])
                                    sendTextTemplate(msg.to,"[ ɢʀᴏᴜᴘ ] \n🔥"+str(ginfo.name)+"\n 🔥sɪᴀᴘ ʙᴀsᴍɪ ᴋɪᴋɪʟ ᴛᴇᴍᴘᴇ")
                                except:
                                    pass 
                                
                        elif cmd == "papay":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = farel.getGroup(msg.to)
                                sendTextTemplate(msg.to, "🔥ɢᴏᴏᴅ ʙʏᴇ ᴄᴀʏᴀɴᴋ🔥\n       "+str(G.name))
                                farel.leaveGroup(msg.to)
                                
                        elif msg.text.lower().startswith("addbot"):
                           if msg._from in admin:
                                try:
                                    farel.findAndAddContactsByMid(Rel)
                                    farel.findAndAddContactsByMid(Rel1)
                                    farel.findAndAddContactsByMid(RelAjs)
                                    farel.sendMessage(msg.to,"Success!!!")
                                    rell.findAndAddContactsByMid(mid)
                                    rell.findAndAddContactsByMid(Rel1)
                                    rell.findAndAddContactsByMid(RelAjs)
                                    rell.sendMessage(msg.to,"Success!!!")
                                    far.findAndAddContactsByMid(mid)
                                    far.findAndAddContactsByMid(Rel)
                                    far.findAndAddContactsByMid(RelAjs)
                                    far.sendMessage(msg.to,"Success!!!")
                                    ajsrel.findAndAddContactsByMid(mid)
                                    ajsrel.findAndAddContactsByMid(Rel)
                                    ajsrel.findAndAddContactsByMid(Rel1)
                                    ajsrel.sendMessage(msg.to,"Success!!!")
                                except:
                                    pass
                                
                        elif cmd == "jn":
                            if msg._from in admin:
                                G = farel.getGroup(msg.to)
                                ginfo = farel.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                farel.updateGroup(G)
                                invsend = 0
                                Ticket = farel.reissueGroupTicket(msg.to)
                                ajsrel.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ajsrel.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ajsrel.updateGroup(G)

                        elif cmd == "by":
                            if msg._from in admin:
                                G = farel.getGroup(msg.to)
                                ajsrel.leaveGroup(msg.to)
                               
                        elif cmd == "speed" or cmd == "sp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                get_profile_time_start = time.time()
                                get_profile = farel.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                sendTextTemplate(msg.to, "ᴡᴀɪᴛ...")
                                sendTextTemplate(msg.to, "╭───────────────────╮\n          %.10f ᴏʟᴇɴɢ\n╰───────────────────╯" % (get_profile_time/3))

                        elif cmd == "lurking on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 Setmain['RAreadPoint'][msg.to] = msg_id
                                 Setmain['RAreadMember'][msg.to] = {}
                                 sendTextTemplate(msg.to, "♦️Lurking berhasil diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurking off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del Setmain['RAreadPoint'][msg.to]
                                 del Setmain['RAreadMember'][msg.to]
                                 sendTextTemplate(msg.to, "♦️Lurking berhasil dinoaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurkers":
                          if msg._from in admin:
                            if msg.to in Setmain['RAreadPoint']:
                                if Setmain['RAreadMember'][msg.to] != {}:
                                    aa = []
                                    for x in Setmain['RAreadMember'][msg.to]:
                                        aa.append(x)
                                    try:
                                        arrData = ""
                                        textx = "  [ Result {} member ]    \n\n  [ Lurkers ]\n1. ".format(str(len(aa)))
                                        arr = []
                                        no = 1
                                        b = 1
                                        for i in aa:
                                            b = b + 1
                                            end = "\n"
                                            mention = "@x\n"
                                            slen = str(len(textx))
                                            elen = str(len(textx) + len(mention) - 1)
                                            arrData = {'S':slen, 'E':elen, 'M':i}
                                            arr.append(arrData)
                                            tz = pytz.timezone("Asia/Jakarta")
                                            timeNow = datetime.now(tz=tz)
                                            textx += mention
                                            if no < len(aa):
                                                no += 1
                                                textx += str(b) + ". "
                                            else:
                                                try:
                                                    no = "[ {} ]".format(str(farel.getGroup(msg.to).name))
                                                except:
                                                    no = "  "
                                        msg.to = msg.to
                                        msg.text = textx+"\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        farel.sendMessage1(msg)
                                    except:
                                        pass
                                    try:
                                        del Setmain['RAreadPoint'][msg.to]
                                        del Setmain['RAreadMember'][msg.to]
                                    except:
                                        pass
                                    Setmain['RAreadPoint'][msg.to] = msg.id
                                    Setmain['RAreadMember'][msg.to] = {}
                                else:
                                    sendTextTemplate(msg.to, "User kosong...")
                            else:
                                sendTextTemplate(msg.to, "Ketik lurking on dulu")

                        elif cmd == "cctv on":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  sendTextTemplate(msg.to, "🔥ᴅɪ ᴀᴋᴛɪғᴋᴀɴ\n🔥 "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n🔥 "+ datetime.strftime(timeNow,'%H:%M:%S')+" ")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "cctv off":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  sendTextTemplate(msg.to, "🔥ᴅɪ ᴍᴀᴛɪᴋᴀɴ\n🔥 "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n🔥 "+ datetime.strftime(timeNow,'%H:%M:%S')+" ")
                              else:
                                  sendTextTemplate(msg.to, "🔥sᴜᴅᴀʜ ᴛɪᴅᴀᴋ ᴀᴋᴛɪғ")

#===========Hiburan============#
                        elif cmd.startswith("sholat: "):
                          if msg._from in admin:
                             sep = text.split(" ")
                             location = text.replace(sep[0] + " ","")
                             with requests.session() as web:
                                  web.headers["user-agent"] = random.choice(settings["userAgent"])
                                  r = web.get("http://api.corrykalam.net/apisholat.php?lokasi={}".format(urllib.parse.quote(location)))
                                  data = r.text
                                  data = json.loads(data)
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  if data[1] != "Subuh : " and data[2] != "Dzuhur : " and data[3] != "Ashar : " and data[4] != "Maghrib : " and data[5] != "Isha : ":
                                         ret_ = "「Jadwal Sholat」"
                                         ret_ += "\n♦️ Lokasi : " + data[0]
                                         ret_ += "\n♦️ " + data[1]
                                         ret_ += "\n♦️ " + data[2]
                                         ret_ += "\n♦️ " + data[3]
                                         ret_ += "\n♦️ " + data[4]
                                         ret_ += "\n♦️ " + data[5]
                                         ret_ += "\n\nTanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                         ret_ += "\nJam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                  sendTextTemplate(msg.to, str(ret_))

                        elif cmd.startswith("cuaca: "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            location = text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apicuaca.php?kota={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                if "result" not in data:
                                    ret_ = "♦️Status Cuaca♦️"
                                    ret_ += "\n♦️ Lokasi : " + data[0].replace("❄Temperatur di kota ","")
                                    ret_ += "\n♦️ Suhu : " + data[1].replace("⛄Suhu : ","") + " C"
                                    ret_ += "\n♦️ Kelembaban : " + data[2].replace("💧Kelembaban : ","") + " %"
                                    ret_ += "\n♦️ Tekanan udara : " + data[3].replace("☁Tekanan udara : ","") + " HPa"
                                    ret_ += "\n♦️ Kecepatan angin : " + data[4].replace("🌀Kecepatan angin : ","") + " m/s"
                                    ret_ += "\n\n♦️Tanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                    ret_ += "\n♦️Jam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                sendTextTemplate(msg.to, str(ret_))

                        elif cmd.startswith("lokasi: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            location = msg.text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apiloc.php?lokasi={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                if data[0] != "" and data[1] != "" and data[2] != "":
                                    link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
                                    ret_ = "♦️Info Lokasi♦️"
                                    ret_ += "\n ♦️Location : " + data[0]
                                    ret_ += "\n ♦️Google Maps : " + link
                                else:
                                    ret_ = "[Details Location] Error : Location not found"
                                sendTextTemplate(msg.to,str(ret_))

                        elif cmd.startswith("lirik: "):
                           if msg._from in admin:
                               sep = msg.text.split(" ")
                               search = msg.text.replace(sep[0] + " ","")
                               params = {'songname': search}
                               with requests.session() as web:
                                   web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                   r = web.get("https://ide.fdlrcn.com/workspace/yumi-apis/joox?{}".format(urllib.parse.urlencode(params)))
                                   try:
                                      data = json.loads(r.text)
                                      for song in data:
                                          songs = song[5]
                                          lyric = songs.replace('ti:','Title - ')
                                          lyric = lyric.replace('ar:','Artist - ')
                                          lyric = lyric.replace('al:','Album - ')
                                          removeString = "[1234567890.:]"
                                          for char in removeString:
                                              lyric = lyric.replace(char,'')
                                          ret_ = "╔══[ Lyric🎵 ]═════════"
                                          ret_ += "\n╠➩ Nama lagu : {}".format(str(song[0]))
                                          ret_ += "\n╠➩ Durasi : {}".format(str(song[1]))
                                          ret_ += "\n╠➩ Link : {}".format(str(song[3]))
                                          ret_ += "\n╚══[ Finish ]═════════\n\nLirik nya :\n{}".format(str(lyric))
                                          farel.sendMessage(msg.to, str(ret_))
                                   except:
                                       sendTextTemplate(to, "♦️Lirik tidak ditemukan")

                        elif cmd.startswith("music "):
                            if msg._from in admin:
                               sep = msg.text.split(" ")
                               query = msg.text.replace(sep[0] + " ","")
                               cond = query.split("-")
                               search = str(cond[0])
                               with requests.session() as web:
                                   web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                   result = web.get("http://api.ntcorp.us/joox/search?q={}".format(str(search)))
                                   data = result.text
                                   data = json.loads(data)
                                   if len(cond) == 1:
                                      num = 0
                                      ret_ = "「 Pencarian Musik 」\n"
                                      for music in data["result"]:
                                          num += 1
                                          ret_ += "\n {}. {}".format(str(num), str(music["single"]))
                                      ret_ += "\n\n「 Total {} Pencarian 」".format(str(len(data["result"])))
                                      farel.sendMessage(to, str(ret_))
                                      sendMention(msg.to, msg._from,"","\nJika ingin menggunakan,\nSilahkan gunakan:\n\nMusik penyanyi-angka")
                                   if len(cond) == 2:
                                        num = int(cond[1])
                                        if num <= len(data["result"]):
                                               music = data["result"][num - 1]
                                               with requests.session() as web:
                                                    web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                                    result = web.get("http://api.ntcorp.us/joox/song_info?sid={}".format(str(music["sid"])))
                                                    data = result.text
                                                    data = json.loads(data)
                                                    if data["result"] != []:
                                                         ret_ = "「 Pencarian Musik 」"
                                                         ret_ += "\n♦️Judul : {}".format(str(data["result"]["song"]))
                                                         ret_ += "\n♦️ Album : {}".format(str(data["result"]["album"]))
                                                         ret_ += "\n♦️ Ukuran : {}".format(str(data["result"]["size"]))
                                                         ret_ += " \n♦️ Link Musik : {}".format(str(data["result"]["mp3"]))
                                                         ret_ += "\n「 Tunggu Musiknya Keluar 」"
                                                         farel.sendImageWithURL(to, str(data["result"]["img"]))
                                                         farel.sendMessage(to, str(ret_))
                                                         farel.sendAudioWithURL(to, str(data["result"]["mp3"][0]))   
                     
                        elif cmd.startswith("music: "):
                           if msg._from in owner or msg._from in admin or msg._from in Staff:
                              sep = msg.text.split(" ")
                              search = msg.text.replace(sep[0] + " ","")
                              params = {'songname': search}
                              with requests.session() as web:
                                  web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                  r = web.get("https://ide.fdlrcn.com/workspace/yumi-apis/joox?{}".format(urllib.parse.urlencode(params)))
                                  try:
                                      data = json.loads(r.text)
                                      for song in data:
                                          ret_ = "╔══( 〘 ᴍᴜsɪᴄ 〙)═══════"
                                          ret_ += "\n╠ ᴊᴜᴅᴜʟ ʟᴀɢᴜ: {}".format(str(song[0]))
                                          ret_ += "\n╠ ᴅᴜʀᴀsɪ: {}".format(str(song[1]))
                                          ret_ += "\n╠ ʟɪɴᴋ: {}".format(str(song[3]))
                                          ret_ += "\n╚══(〘 ᴡᴀɪᴛ ᴀᴜᴅɪᴏ 〙)═══════"
                                      farel.sendMessage(msg.to, str(ret_))
                                      farel.sendMessage(msg.to, "sᴀʙᴀʀ sᴇʙᴇɴᴛᴀʀ ʟᴀɢɪ ʟᴏᴀᴅɪɴɢ")
                                      farel.sendAudioWithURL(msg.to, song[3])
                                  except:
                                      farel.sendMessage(to, "ᴍᴜsɪᴄ ᴇʀʀᴏʀ")

                        elif cmd.startswith("gimage: "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            search = msg.text.replace(sep[0] + " ","")
                            url = "https://api.xeonwz.ga/api/image/google?q={}".format(urllib.parse.quote(search))
                            with requests.session() as web:
                                web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                r = web.get(url)
                                data = r.text
                                data = json.loads(data)
                                if data["data"] != []:
                                    start = timeit.timeit()
                                    items = data["data"]
                                    path = random.choice(items)
                                    a = items.index(path)
                                    b = len(items)
                                    farel.sendMessage(msg.to,"「Google Image」\nType : Search Image\nTime taken : %seconds" % (start))
                                    farel.sendImageWithURL(msg.to, str(path))

                        elif cmd.startswith("farelmp4: "):
                          if msg._from in owner or msg._from in admin or msg._from in Staff:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    me = best.url
                                    hasil = ""
                                    title = "ᴊᴜᴅᴜʟ [ " + vid.title + " ]"
                                    author = '\n\nᴀᴜᴛʜᴏʀ : ' + str(vid.author)
                                    durasi = '\nᴅᴜʀᴀᴛɪᴏɴ : ' + str(vid.duration)
                                    suka = '\nʟɪᴋᴇs : ' + str(vid.likes)
                                    rating = '\nʀᴀᴛɪɴɢ : ' + str(vid.rating)
                                    deskripsi = '\nᴅᴇsᴋʀɪᴘsɪ : ' + str(vid.description)
                                farel.sendVideoWithURL(msg.to, me)
                                sendTextTemplate(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                sendTextTemplate(msg.to,str(e))

                        elif cmd.startswith("farelmp3: "):
                          if msg._from in owner or msg._from in admin or msg._from in Staff:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                bestaudio = vid.getbestaudio()
                                bestaudio.bitrate
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    shi = bestaudio.url
                                    me = best.url
                                    vin = s.url
                                    hasil = ""
                                    title = "♦️ᴊᴜᴅᴜʟ ♦️〘 " + vid.title + " 〙"
                                    author = '\n\n♦️ ᴀᴜᴛʜᴏʀ : ' + str(vid.author)
                                    durasi = '\n♦️ ᴅᴜʀᴀsɪ : ' + str(vid.duration)
                                    suka = '\n♦️ ʟɪᴋᴇ : ' + str(vid.likes)
                                    rating = '\n♦️ ʀᴀᴛɪɴɢ : ' + str(vid.rating)
                                    deskripsi = '\n♦️ ᴅᴇsᴋʀɪᴘ : ' + str(vid.description)
                                farel.sendImageWithURL(msg.to, me)
                                farel.sendAudioWithURL(msg.to, shi)
                                farel.sendText(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                farel.sendText(msg.to,str(e))

                        elif cmd.startswith("profileig: "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                instagram = msg.text.replace(sep[0] + " ","")
                                response = requests.get("https://www.instagram.com/"+instagram+"?__a=1")
                                data = response.json()
                                namaIG = str(data['user']['full_name'])
                                bioIG = str(data['user']['biography'])
                                mediaIG = str(data['user']['media']['count'])
                                verifIG = str(data['user']['is_verified'])
                                usernameIG = str(data['user']['username'])
                                followerIG = str(data['user']['followed_by']['count'])
                                profileIG = data['user']['profile_pic_url_hd']
                                privateIG = str(data['user']['is_private'])
                                followIG = str(data['user']['follows']['count'])
                                link = "♦️ Link : " + "https://www.instagram.com/" + instagram
                                text = "♦️ Name : "+namaIG+"\n♦️ Username : "+usernameIG+"\n♦️ Biography : "+bioIG+"\n♦️ Follower : "+followerIG+"\n♦️ Following : "+followIG+"\n♦️ Post : "+mediaIG+"\n♦️ Verified : "+verifIG+"\n♦️ Private : "+privateIG+"" "\n" + link
                                farel.sendImageWithURL(msg.to, profileIG)
                                farel.sendMessage(msg.to, str(text))
                            except Exception as e:
                                    farel.sendMessage(msg.to, str(e))

                        elif cmd.startswith("cekdate: "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            tanggal = msg.text.replace(sep[0] + " ","")
                            r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                            data=r.text
                            data=json.loads(data)
                            lahir = data["data"]["lahir"]
                            usia = data["data"]["usia"]
                            ultah = data["data"]["ultah"]
                            zodiak = data["data"]["zodiak"]
                            sendTextTemplate(msg.to,"♦️ I N F O R M A S I ♦️\n\n"+"♦️ Date Of Birth : "+lahir+"\n♦️ Age : "+usia+"\n♦️ Ultah : "+ultah+"\n♦️ Zodiak : "+zodiak)

                        elif cmd.startswith("jumlah: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                Setmain["RAlimit"] = num
                                sendTextTemplate(msg.to,"🔥ᴛᴏᴛᴀʟ sᴛᴀɢ ᴅɪ ʀᴜʙᴀʜ ᴊᴀᴅɪ " +strnum)

                        elif cmd.startswith("spamcall: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                sendTextTemplate(msg.to,"🔥ᴛᴏᴛᴀʟ sᴘᴀᴍᴄᴀʟʟ ᴅɪ ʀᴜʙᴀʜ ᴊᴀᴅɪ " +strnum)

                        elif cmd.startswith("stag "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                if msg.contentMetadata is not None and 'MENTION' in msg.contentMetadata:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(Setmain["RAlimit"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                farel.sendMessage(msg)
                                            except Exception as e:
                                                farel.sendMessage(msg.to,str(e))
                                    else:
                                        sendTextTemplate(msg.to,"🔥ᴊᴜᴍʟᴀʜ ᴍᴇʟᴇʙɪʜɪ 1000")
                                        
                        elif cmd == "spamcall":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                             if msg.toType == 2:
                                group = farel.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(wait["limit"])
                                farel.sendMessage(msg.to, "🔥ᴅᴏɴᴇ ᴍᴇɴɢᴜɴᴅᴀɴɢ {} ᴘᴀɴɢɢɪʟᴀɴ ɢʀᴏᴜᴘ".format(str(wait["limit"])))
                                if jmlh <= 1000:
                                  for x in range(jmlh):
                                     try:
                                        farel.acquireGroupCallRoute(to)
                                        farel.inviteIntoGroupCall(to, contactIds=members)
                                     except Exception as e:
                                        farel.sendText(msg.to,str(e))
                                else:
                                    sendTextTemplate(msg.to,"Jumlah melebihi batas")

                        elif 'ID line: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              msgs = msg.text.replace('ID line: ','')
                              conn = farel.findContactsByUserid(msgs)
                              if True:
                                  farel.sendMessage(msg.to, "http://line.me/ti/p/~" + msgs)
                                  farel.sendMessage(msg.to, None, contentMetadata={'mid': conn.mid}, contentType=13)

#===========Protection============#
                        elif 'Welcome ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Welcome ','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "sᴀᴍʙᴜᴛᴀɴ ᴀᴋᴛɪғ"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = farel.getGroup(msg.to)
                                       msgs = "🔥ᴅɪ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                  sendTextTemplate(msg.to, "ᴀᴋᴛɪғ\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = farel.getGroup(msg.to)
                                         msgs = "🔥sᴀᴍʙᴜᴛᴀɴ ᴍᴀᴛɪ\n🔥ᴅɪ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                    else:
                                         msgs = "🔥sᴀᴍʙᴜᴛᴀɴ sᴜᴅᴀʜ ᴍᴀᴛɪ"
                                    sendTextTemplate(msg.to, "🔥ᴛᴇᴡᴀs\n" + msgs)
                                    
                        elif 'Js ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Js ','')
                              if spl == 'on':
                                  if msg.to in protectantijs:
                                       msgs = "🔥sɪᴀᴘ ʙᴀɴᴛᴀɪ ᴋɪᴋɪʟ ᴛᴇᴍᴘᴇ"
                                  else:
                                       protectantijs.append(msg.to)
                                       ginfo = farel.getGroup(msg.to)
                                       msgs = "🔥ᴀɴᴛɪ ᴊs ᴅɪ ᴀᴋᴛɪғᴋᴀɴ\n🔥ᴅɪ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                  sendTextTemplate(msg.to, "🔥sᴜᴄᴄᴇs ᴅɪ ᴀᴋᴛɪғᴋᴀɴ\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectantijs:
                                         protectantijs.remove(msg.to)
                                         ginfo = farel.getGroup(msg.to)
                                         msgs = "🔥ᴀɴᴛɪ ᴊs ᴅɪ ɴᴏɴᴀᴋᴛɪғᴋᴀɴ\n🔥ᴅɪ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                    else:
                                         msgs = ""
                                    sendTextTemplate(msg.to, "🔥sᴜᴅᴀʜ ᴅɪ ɴᴏɴᴀᴋᴛɪғᴋᴀɴ\n" + msgs)
                                    
                        elif 'Gs ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Ghost ','')
                              if spl == 'on':
                                  if msg.to in ghost:
                                       msgs = "🔥sɪᴀᴘ ʙᴀɴᴛᴀɪ ᴋɪᴋɪʟ ᴛᴇᴍᴘᴇ"
                                  else:
                                       ghost.append(msg.to)
                                       ginfo = farel.getGroup(msg.to)
                                       msgs = "🔥sᴜᴄᴄᴇs ɢʜᴏsᴛ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ\n🔥ᴅɪ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                  sendTextTemplate(msg.to, "🔥sᴜᴅᴀʜ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ" + msgs)
                              elif spl == 'off':
                                    if msg.to in ghost:
                                         ghost.remove(msg.to)
                                         ginfo = farel.getGroup(msg.to)
                                         msgs = "🔥sᴜᴄᴄᴇs ɴᴏɴᴀᴋᴛɪғᴋᴀɴ ɢʜᴏsᴛ\n🔥ᴅɪ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                    else:
                                         msgs = ""
                                    sendTextTemplate(msg.to, "🔥ɢʜᴏsᴛ ᴅɪ ɴᴏɴᴀᴋᴛɪғᴋᴀɴ\n" + msgs)

                        elif 'Allprotect ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Allprotect ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = ""
                                  else:
                                       protectqr.append(msg.to)
                                  if msg.to in protectkick:
                                      msgs = ""
                                  else:
                                      protectkick.append(msg.to)
                                  if msg.to in protectjoin:
                                      msgs = ""
                                  else:
                                      protectjoin.append(msg.to)
                                  if msg.to in protectcancel:
                                      ginfo = farel.getGroup(msg.to)
                                      msgs = "🔥ᴘʀᴏ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ\n🔥ᴅɪ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = farel.getGroup(msg.to)
                                      msgs = "🔥ᴘʀᴏ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ\n🔥ᴅɪ ɢʀᴏᴜᴘ \n🔥 " +str(ginfo.name)
                                  sendTextTemplate(msg.to, "sᴇᴍᴜᴀ ᴘʀᴏ ᴀᴋᴛɪғ\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = farel.getGroup(msg.to)
                                         msgs = "🔥ᴅᴏɴᴇ ᴍᴇɴᴏɴᴀᴋᴛɪғᴋᴀɴ ᴘʀᴏ\n🔥ᴅɪ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                    else:
                                         ginfo = farel.getGroup(msg.to)
                                         msgs = "🔥ᴘʀᴏ ᴅɪ ᴍᴀᴛɪᴋᴀɴ\n🔥ᴅɪ ɢʀᴏᴜᴘ : " +str(ginfo.name)
                                    sendTextTemplate(msg.to, "🔥ᴅᴏɴᴇ\n" + msgs)

#=========== KICKOUT ============#
              
                        elif "!patek" in msg.text:
                           if msg._from in Bots:
                            if msg.toType == 2:
                               _name = msg.text.replace("!patek","")
                               gs = farel.getGroup(msg.to)
                               farel.sendMessage(msg.to,"🔥ɪ ᴍ sᴏʀʀʏ🔥")
                               targets = []
                               for g in gs.members:
                                   if _name in g.displayName:
                                       targets.append(g.mid)
                               if targets == []:
                                  farel.sendMessage(msg.to,"Not found")
                              #    else:
                               for target in targets:
                                     if target not in Bots:
                                      try:
                                          klist=[cl]
                                          kicker=random.choice(klist)
                                          kicker.kickoutFromGroup(msg.to,[target])
                                          print (msg.to,[g.mid])
                                      except:
                                          farel.sendMessage(msg.to,"♦️ᴘᴇʀᴍɪsɪ sᴇᴍᴜᴀ ɴʏᴀ♦️") 

                        elif ("Kick " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           farel.kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

#===========admin ADD============#
                        elif ("adminadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           admin.append(target)
                                           sendTextTemplate(msg.to,"🔥ᴅᴏɴᴇ ᴍᴇɴᴀᴍʙᴀʜ ᴀᴅᴍɪɴ🔥")
                                       except:
                                           pass

                        elif ("addstaff " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           Staff.append(target)
                                           sendTextTemplate(msg.to,"🔥ᴅᴏɴᴇ ᴍᴇɴᴀᴍʙᴀʜ sᴛᴀғғ🔥")
                                       except:
                                           pass

                        elif ("Botadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           Bots.append(target)
                                           sendTextTemplate(msg.to,"🔥ᴅᴏɴᴇ ᴍᴇɴᴀᴍʙᴀʜ ʙᴏᴛ🔥")
                                       except:
                                           pass

                        elif ("admindell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           admin.remove(target)
                                           sendTextTemplate(msg.to,"🔥ᴅᴏɴᴇ ᴍᴇɴɢʜᴀᴘᴜs ᴀᴅᴍɪɴ🔥")
                                       except:
                                           pass

                        elif ("staffdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           Staff.remove(target)
                                           sendTextTemplate(msg.to,"🔥ᴅᴏɴᴇ ᴍᴇɴɢʜᴀᴘᴜs sᴛᴀғғ🔥")
                                       except:
                                           pass

                        elif ("Botdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           Bots.remove(target)
                                           sendTextTemplate(msg.to,"🔥ᴅᴏɴᴇ ᴍᴇɴɢʜᴀᴘᴜs ʙᴏᴛ🔥")
                                       except:
                                           pass

                        elif cmd == "admin:on" or text.lower() == 'admin:on':
                            if msg._from in admin:
                                wait["addadmin"] = True
                                sebdTextTemplate(msg.to,"🔥ᴋɪʀɪᴍ ᴄᴏɴᴛᴀᴄᴛ ɴʏᴀ🔥")

                        elif cmd == "admin:off" or text.lower() == 'admin:repeat':
                            if msg._from in admin:
                                wait["delladmin"] = True
                                sendTextTemplate(msg.to,"🔥ᴋɪʀɪᴍ ᴄᴏɴᴛᴀᴄᴛ ɴʏᴀ🔥")

                        elif cmd == "Staff:on" or text.lower() == 'Staff:on':
                            if msg._from in admin:
                                wait["addStaff"] = True
                                sendTextTemplate(msg.to,"🔥ᴋɪʀɪᴍ ᴄᴏɴᴛᴀᴄᴛ ɴʏᴀ🔥")

                        elif cmd == "Staff:off" or text.lower() == 'Staff:repeat':
                            if msg._from in admin:
                                wait["dellStaff"] = True
                                sendTextTemplate(msg.to,"🔥ᴋɪʀɪᴍ ᴄᴏɴᴛᴀᴄᴛ ɴʏᴀ🔥")

                        elif cmd == "bot:on" or text.lower() == 'bot:on':
                            if msg._from in admin:
                                wait["addbots"] = True
                                sendTextTemplate(msg.to,"🔥ᴋɪʀɪᴍ ᴄᴏɴᴛᴀᴄᴛ ɴʏᴀ🔥")

                        elif cmd == "bot:off" or text.lower() == 'bot:repeat':
                            if msg._from in admin:
                                wait["dellbots"] = True
                                sendTextTemplate(msg.to,"🔥ᴋɪʀɪᴍ ᴄᴏɴᴛᴀᴄᴛ ɴʏᴀ🔥")

                        elif cmd == "refresh" or text.lower() == 'refresh':
                            if msg._from in admin:
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                wait["addStaff"] = False
                                wait["dellStaff"] = False
                                wait["addbots"] = False
                                wait["dellbots"] = False
                                wait["wblacklist"] = False
                                wait["dblacklist"] = False
                                wait["Talkwblacklist"] = False
                                wait["Talkdblacklist"] = False
                                sendTextTemplate(msg.to,"🔥sᴜᴅᴀʜ sᴇɢᴀʀ ʙᴏssᴋᴜ🔥")

                        elif cmd == "kojoman" or text.lower() == 'contact admin':
                            if msg._from in admin:
                                ma = ""
                                for i in admin:
                                    ma = farel.getContact(i)
                                    farel.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "tikungan" or text.lower() == 'contact Staff':
                            if msg._from in admin:
                                ma = ""
                                for i in Staff:
                                    ma = farel.getContact(i)
                                    farel.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact bot" or text.lower() == 'contact bot':
                            if msg._from in admin:
                                ma = ""
                                for i in Bots:
                                    ma = farel.getContact(i)
                                    farel.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

#===========COMMAND ON OFF============#
                        elif cmd == "unsend on" or text.lower() == 'unsend on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["unsend"] = True
                                sendTextTemplate(msg.to,"🔥ᴅᴇᴛᴇᴋsɪ ᴜɴsᴇɴᴅ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ??")

                        elif cmd == "unsend off" or text.lower() == 'unsend off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["unsend"] = False
                                sendTextTemplate(msg.to,"🔥ᴅᴇᴛᴇᴋsɪ ᴜɴsᴇɴᴅ ᴅɪ ɴᴏɴᴀᴋᴛɪғᴋᴀɴ🔥")
                                
                        elif cmd == "notag on" or text.lower() == 'notag on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = True
                                sendTextTemplate(msg.to,"🔥ɴᴏᴛᴀɢ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ🔥")

                        elif cmd == "notag off" or text.lower() == 'notag off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["MentionKick"] = False
                                sendTextTemplate(msg.to,"🔥ɴᴏᴛᴀɢ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ🔥")

                        elif cmd == "contact on" or text.lower() == 'contact on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = True
                                sendTextTemplate(msg.to,"🔥ᴅᴇᴛᴇᴋsɪ ᴄᴏɴᴛᴀᴄᴛ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ🔥")

                        elif cmd == "contact off" or text.lower() == 'contact off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = False
                                sendTextTemplate(msg.to,"🔥ᴅᴇᴛᴇᴋsɪ ᴄᴏɴᴛᴀᴄᴛ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ🔥")

                        elif cmd == "respon on" or text.lower() == 'respon on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = True
                                sendTextTemplate(msg.to,"🔥ᴀᴜᴛᴏʀᴇsᴘᴏɴ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ🔥")

                        elif cmd == "respon off" or text.lower() == 'respon off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = False
                                sendTextTemplate(msg.to,"🔥ᴀᴜᴛᴏʀᴇsᴘᴏɴ ᴅɪ ᴍᴀᴛɪᴋᴀɴ🔥")
                                
                        elif cmd == "responpm on" or text.lower() == 'responpm on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["arespon"] = True
                                sendTextTemplate(msg.to,"🔥ʀᴇsᴘᴏɴᴘᴍ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ🔥")

                        elif cmd == "responpm off" or text.lower() == 'responpm off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["arespon"] = False
                                sendTextTemplate(msg.to,"🔥ʀᴇsᴘᴏɴᴘᴍ ᴅɪ ᴍᴀᴛɪᴋᴀɴ🔥")          

                        elif cmd == "autojoin on" or text.lower() == 'autojoin on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = True
                                sendTextTemplate(msg.to,"🔥ᴀᴜᴛᴏ ᴊᴏɪɴ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ🔥")

                        elif cmd == "autojoin off" or text.lower() == 'autojoin off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = False
                                sendTextTemplate(msg.to,"🔥ᴀᴜᴛᴏ ᴊᴏɪɴ ᴅɪ ɴᴏɴᴀᴋᴛɪғᴋᴀɴ🔥")
                                
                        elif cmd == "sticker on" or text.lower() == 'sticker on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = True
                                sendTextTemplate(msg.to,"🔥ᴅᴇᴛᴇᴋsɪ sᴛɪᴄᴋᴇʀ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ🔥")            
                                
                        elif cmd == "sticker off" or text.lower() == 'sticker off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = False
                                sendTextTemplate(msg.to,"🔥ᴅᴇᴛᴇᴋsɪ sᴛɪᴄᴋᴇʀ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ🔥")         

                        elif cmd == "autoleave on" or text.lower() == 'autoleave on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = True
                                sendTextTemplate(msg.to,"🔥ᴀᴜᴛᴏʟᴇᴀᴠᴇ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ🔥")

                        elif cmd == "autoleave off" or text.lower() == 'autoleave off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = False
                                sendTextTemplate(msg.to,"🔥ᴀᴜᴛᴏʟᴇᴀᴠᴇ ᴅɪ ɴᴏɴᴀᴋᴛɪғᴋᴀɴ🔥")

                        elif cmd == "autoadd on" or text.lower() == 'autoadd on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = True
                                sendTextTemplate(msg.to,"🔥ᴀᴜᴛᴏᴀᴅᴅ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ🔥")

                        elif cmd == "autoadd off" or text.lower() == 'autoadd off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = False
                                sendTextTemplate(msg.to,"🔥ᴀᴜᴛᴏᴀᴅᴅ ᴅɪ ɴᴏɴᴀᴋᴛɪғᴋᴀɴ🔥")
                                
                        elif cmd == "left on" or text.lower() == 'left on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["leaveMsg"] = True
                                sendTextTemplate(msg.to,"🔥ʟᴇғᴛ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ🔥")

                        elif cmd == "left off" or text.lower() == 'left off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["leaveMsg"] = False
                                sendTextTemplate(msg.to,"🔥ʟᴇғᴛ ᴅɪ ɴᴏɴᴀᴋᴛɪғᴋᴀɴ🔥")
                                
                        elif cmd == "autoblock on" or text.lower() == 'autoblock on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoBlock"] = True
                                sendTextTemplate(msg.to,"🔥ᴀᴜᴛᴏʙʟᴏᴄᴋ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ🔥")
                                
                        elif cmd == "autoblock off" or text.lower() == 'autoblock off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoBlock"] = True
                                sendTextTemplate(msg.to,"🔥ᴀᴜᴛᴏʙʟᴏᴄᴋ ᴅɪ ɴᴏɴᴀᴋᴛɪғᴋᴀɴ🔥")          

                        elif cmd == "jointicket on" or text.lower() == 'jointicket on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoinTicket"] = True
                                sendTextTemplate(msg.to,"🔥ᴊᴏɪɴᴛɪᴄᴋᴇᴛ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ🔥")

                        elif cmd == "jointicket off" or text.lower() == 'jointicket off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoinTicket"] = False
                                sendTextTemplate(msg.to,"🔥ᴊᴏɪɴᴛɪᴄᴋᴇᴛ ᴅɪ ɴᴏɴᴀᴋᴛɪғᴋᴀɴ🔥")

#===========COMMAND BLACKLIST============#
                        elif ("Talkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["Talkblacklist"][target] = True
                                           sendTextTemplate(msg.to,"🔥ᴅᴏɴᴇ ᴍᴇɴᴀᴍʙᴀʜ ʙʟᴀᴄᴋʟɪsᴛ🔥")
                                       except:
                                           pass

                        elif ("Untalkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["Talkblacklist"][target]
                                           sendTextTemplate(msg.to,"🔥ᴅᴏɴᴇ ᴍᴇɴɢʜᴀᴘᴜs ʙʟᴀᴄᴋʟɪsᴛ🔥")
                                       except:
                                           pass

                        elif cmd == "talkban:on" or text.lower() == 'talkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkwblacklist"] = True
                                sendTextTemplate(msg.to,"🔥ᴋɪʀɪᴍ ᴄᴏɴᴛᴀᴄᴛ ɴʏᴀ🔥")

                        elif cmd == "untalkban:on" or text.lower() == 'untalkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkdblacklist"] = True
                                sendTextTemplate(msg.to,"🔥ᴋɪʀɪᴍ ᴄᴏɴᴛᴀᴄᴛ ɴʏᴀ🔥")

                        elif ("Ban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["blacklist"][target] = True
                                           sendTextTemplate(msg.to,"🔥ᴅᴏɴᴇ ᴍᴇɴᴀᴍʙᴀʜ ʙʟᴀᴄᴋʟɪsᴛ🔥")
                                       except:
                                           pass

                        elif ("Unban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["blacklist"][target]
                                           sendTextTemplate(msg.to,"🔥ᴅᴏɴᴇ ᴍᴇɴɢʜᴀᴘᴜs ʙʟᴀᴄᴋʟɪsᴛ🔥")
                                       except:
                                           pass

                        elif cmd == "ban:on" or text.lower() == 'ban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["wblacklist"] = True
                                sendTextTemplate(msg.to,"??ᴋɪʀɪᴍ ᴄᴏɴᴛᴀᴄᴛɴʏᴀ🔥")

                        elif cmd == "unban:on" or text.lower() == 'unban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["dblacklist"] = True
                                sendTextTemplate(msg.to,"🔥ᴋɪʀɪᴍ ᴄᴏɴᴛᴀᴄᴛɴʏᴀ🔥")

                        elif cmd == "banlist" or text.lower() == 'banlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                sendTextTemplate(msg.to,"🔥ᴛɪᴅᴀᴋ ᴀᴅᴀ ʙʟᴀᴄᴋʟɪsᴛ🔥")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +farel.getContact(m_id).displayName + "\n"
                                sendTextTemplate(msg.to,"🔥ʙʟᴀᴄᴋʟɪsᴛ ᴜsᴇʀ🔥\n\n"+ma+"\n🔥ᴊᴜᴍʟᴀʜ「%s」ʙʟᴀᴄᴋʟɪsᴛ ᴜsᴇʀ🔥" %(str(len(wait["blacklist"]))))

                        elif cmd == "talkbanlist" or text.lower() == 'talkbanlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["Talkblacklist"] == {}:
                                sendTextTemplate(msg.to,"🔥ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴛᴀʟᴋʙᴀɴ ᴜsᴇʀ🔥")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["Talkblacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +farel.getContact(m_id).displayName + "\n"
                                sendTextTemplate(msg.to,"🔥ᴛᴀʟᴋʙᴀɴ ᴜsᴇʀ🔥\n\n"+ma+"\n🔥ᴊᴜᴍʟᴀʜ「%s」ᴛᴀʟᴋʙᴀɴ ᴜsᴇʀ🔥" %(str(len(wait["Talkblacklist"]))))

                        elif cmd == "bl" or text.lower() == 'blc':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                    sendTextTemplate(msg.to,"🔥ᴛɪᴅᴀᴋ ᴀᴅᴀ ʙʟᴀᴄᴋʟɪsᴛ🔥")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = farel.getContact(i)
                                        farel.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "cban" or text.lower() == 'clearban':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              wait["blacklist"] = {}
                              ragets = farel.getContacts(wait["blacklist"])
                              mc = "「%i」ᴜsᴇʀ ʙʟᴀᴄᴋʟɪsᴛ" % len(ragets)
                              sendTextTemplate(msg.to,"🔥ᴅᴏɴᴇ ᴍᴇɴɢʜᴀᴘᴜs ʙᴜʀᴏɴᴀɴ🔥\n  "    +mc)
                              
                        elif text.lower() == 'payment':
                               farel.sendMessage(msg.to, "ᴘᴀʏᴍᴇɴᴛ ᴠɪᴀ ʙᴀɴᴋ\nɴᴏ ʀᴇᴋ : 481901020711531\nᴀᴛᴀs ɴᴀᴍᴀ : muhazir\nʙᴀɴᴋ ʙʀɪ\n\nᴠɪᴀ ᴘᴜʟsᴀ\n08992906209"    +mc)
#===========COMMAND SET============#
                        elif cmd == "#kickall":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                x = farel.getGroup(msg.to)
                                farels = x.id
                                if x.invitee == None:Fareelkiller = []
                                else:Fareelkiller = [contact.mid for contact in x.members]
                                targets = []
                                for a in Fareelkiller:
                                    if a not in admin and a not in Bots:
                                        targets.append(a)
                                Fareelkillers = [contact.mid for contact in x.members]
                                farel.sendMessage(to," ❎ Sorry Ku Js rom ini.☑️")
                                targetk = []
                                cms = 'kickall.js gid={} token={} app={}'.format(farels,farel.authToken, "DESKTOPWIN\t5.24.1\Windows\t10.0")
                                for a in Fareelkillers:
                                    if a not in admin and a not in Bots:
                                        targetk.append(a)
                                for y in targets:
                                    cms += ' uid={}'.format(y)
                                for y in targetk:
                                    cms += ' uik={}'.format(y)
                                print(cms)
                                success = execute_js(cms)
                        elif cmd == "#bypass":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                x = farel.getGroup(msg.to)
                                farels = x.id
                                if x.invitee == None:Fareelkiller = []
                                else:Fareelkiller = [contact.mid for contact in x.invitee]
                                targets = []
                                for a in Fareelkiller:
                                    if a not in admin and a not in Bots:
                                        targets.append(a)
                                Fareelkillers = [contact.mid for contact in x.members]
                                farel.sendMessage(to," ❎ Sorry Ku bypass rom ini.☑️")
                                targetk = []
                                cms = 'dual.js gid={} token={} app={}'.format(farels,farel.authToken, "DESKTOPWIN\t5.24.1\Windows\t10.0")
                                for a in Fareelkillers:
                                    if a not in admin and a not in Bots:
                                        targetk.append(a)
                                for y in targets:
                                    cms += ' uid={}'.format(y)
                                for y in targetk:
                                    cms += ' uik={}'.format(y)
                                print(cms)
                                success = execute_js(cms)
                        if cmd.startswith('pass '):
                            if msg._from in admin:
                                text = text.split(" ")
                                number =msg.text.replace(text[0] + " ","")
                                if number.isdigit():
                                    groups = farel.getGroupIdsJoined()
                                    if int(number) < len(groups) and int(number) >= 0:
                                        groupid = groups[int(number)-1]
                                        try:
                                            x = farel.getGroup(groupid)
                                            farels = x.id
                                            if x.invitee == None:Fareelkiller = []
                                            else:Fareelkiller = [contact.mid for contact in x.invitee]
                                            targets = []
                                            for a in Fareelkiller:
                                                if a not in admin and a not in Bots:
                                                    targets.append(a)
                                            Fareelkillers = [contact.mid for contact in x.members]
                                            targetk = []
                                            cms = 'dual.js gid={} token={}'.format(farels,farel.authToken, "DESKTOPWIN\t5.24.1\Windows\t10.0")
                                            for a in Fareelkillers:
                                                if a not in admin and a not in Bots:
                                                    targetk.append(a)
                                            for y in targets:
                                                cms += ' uid={}'.format(y)
                                            for y in targetk:
                                                cms += ' uik={}'.format(y)
                                            success = execute_js(cms)
                                            if success:
                                                farel.sendMessage(to,"Succes Baypass grup \n " + str(x.name))
                                            else:
                                                farel.sendMessage(to,"Please Check Your Screen")
                                        except:
                                            pass
                        if cmd.startswith('sapu '):
                            if msg._from in admin:
                                text = text.split(" ")
                                number =msg.text.replace(text[0] + " ","")
                                if number.isdigit():
                                    groups = farel.getGroupIdsJoined()
                                    if int(number) < len(groups) and int(number) >= 0:
                                        groupid = groups[int(number)-1]
                                        try:
                                            x = farel.getGroup(groupid)
                                            farels = x.id
                                            if x.invitee == None:Fareelkiller = []
                                            else:Fareelkiller = [contact.mid for contact in x.invitee]
                                            Fareelkillers = [contact.mid for contact in x.members]
                                            targetk = []
                                            cms = 'kickall.js gid={} token={}'.format(farels,farel.authToken, "DESKTOPWIN\t5.24.1\Windows\t10.0")
                                            for a in Fareelkillers:
                                                if a not in admin and a not in Bots:
                                                    targetk.append(a)
                                            for y in targetk:
                                                cms += ' uik={}'.format(y)
                                            success = execute_js(cms)
                                            if success:
                                                farel.sendMessage(to,"Succes menghapus member grup \n " + str(x.name))
                                            else:
                                                farel.sendMessage(to,"Please Check Your Screen")
                                        except:
                                            pass                                         
                        elif cmd == "!cl" or text.lower() == ".cencel":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                xyz = farel.getGroup(to)
                                if xyz.invitee == None:pends = []
                                else:pends = [c.mid for c in xyz.invitee]
                                targp = []
                                for x in pends:
                                  if x not in admin and x not in farel.profile.mid:targp.append(x)
                                imnoob = 'bypass.js gid={} token={}'.format(to, farel.authToken, "DESKTOPWIN\t5.24.1\Windows\t10.0")
                                for x in targp:imnoob += ' uid={}'.format(x)
                                execute_js(imnoob)
                        elif 'Set pesan: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set pesan: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate(msg.to, "🔥Gagal mengganti Pesan Msg")
                              else:
                                  wait["message"] = spl
                                  sendTextTemplate(msg.to, "🔥Pesan Msg🔥\n🔥Pesan Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set welcome: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set welcome: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate(msg.to, "🔥Gagal mengganti Welcome Msg")
                              else:
                                  wait["welcome"] = spl
                                  sendTextTemplate(msg.to, "🔥Welcome Msg🔥\n🔥Welcome Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set respon: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set respon: ','')
                              if spl in [""," ","\n",None]:
                                  farel.sendMessage(msg.to, "🔥Gagal mengganti Respon Msg")
                              else:
                                  wait["Respontag"] = spl
                                  sendTextTemplate(msg.to, "🔥Respon Msg🔥\n🔥Respon Msg diganti jadi :\n\n「{}」".format(str(spl)))
                        elif 'Set left: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set left: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate(msg.to, "🔥Gagal mengganti Respon Msg")
                              else:
                                  wait["left"] = spl
                                  sendTextTemplate(msg.to, "🔥Respon Left🔥\n🔥Respon left diganti jadi :\n\n「{}」".format(str(spl)))
                        elif 'Set spam: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set spam: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate(msg.to, "🔥Gagal mengganti Spam")
                              else:
                                  Setmain["RAmessage1"] = spl
                                  sendTextTemplate(msg.to, "🔥Spam Msg🔥\n🔥Spam Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set sider: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set sider: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate(msg.to, "🔥Gagal mengganti Sider Msg")
                              else:
                                  wait["mention"] = spl
                                  sendTextTemplate(msg.to, "🔥Sider Msg🔥\n🔥Sider Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif text.lower() == "cek pesan":
                            if msg._from in admin:
                               sendTextTemplate(msg.to, "🔥Pesan Msg🔥\n🔥Pesan Msg mu :\n\n「 " + str(wait["message"]) + " 」")

                        elif text.lower() == "cek left":
                            if msg._from in admin:
                               sendTextTemplate(msg.to, "🔥left Msg🔥\n🔥Left Msg mu :\n\n「 " + str(wait["left"]) + " 」")

                        elif text.lower() == "cek welcome":
                            if msg._from in admin:
                               sendTextTemplate(msg.to, "🔥Welcome Msg🔥\n🔥Welcome Msg mu :\n\n「 " + str(wait["welcome"]) + " 」")

                        elif text.lower() == "cek respon":
                            if msg._from in admin:
                               sendTextTemplate(msg.to, "🔥Respon Msg🔥\n🔥Respon Msg mu :\n\n「 " + str(wait["Respontag"]) + " 」")

                        elif text.lower() == "cek spam":
                            if msg._from in admin:
                               sendTextTemplate(msg.to, "🔥Spam Msg🔥\n🔥Spam Msg mu :\n\n「 " + str(Setmain["RAmessage1"]) + " 」")

                        elif text.lower() == "cek sider":
                            if msg._from in admin:
                               sendTextTemplate(msg.to, "🔥Sider Msg🔥\n🔥Sider Msg mu :\n\n「 " + str(wait["mention"]) + " 」")

                        elif text.lower() == "cek":
                            if msg._from in admin:
                               try:farel.inviteIntoGroup(to, ["u45882d0ead1703855dbc60d40e37bec7"]);has = "OK"
                               except:has = "NOT"
                               try:farel.kickoutFromGroup(to, ["u45882d0ead1703855dbc60d40e37bec7"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "⏹️Normal 💯"
                               else:sil = "⏹️Sakit ❎"
                               if has1 == "OK":sil1 = "⏹️Normal 💯"
                               else:sil1 = "⏹️Demam ❎"
                               sendTextTemplate(to, "🔴kick: {} \n🔴Invite: {}".format(sil1,sil))                                                                               

#===========JOIN TICKET============#
                        elif "/ti/g/" in msg.text.lower():
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = farel.findGroupByTicket(ticket_id)
                                     farel.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     farel.sendMessage(msg.to, "Masuk : %s" % str(group.name))

    except Exception as error:
        print (error)
while True:
    try:
        ops = FarelKiler.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                bot(op)
                FarelKiler.setRevision(op.revision)
    except Exception as e:
    	logError(e)
