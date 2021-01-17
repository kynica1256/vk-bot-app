import eel
import time
import re
import os
import sys
import json
import fileinput
import subprocess

eel.init('web')
@eel.expose
def status():
    with open("status.txt", "r", encoding="utf-8") as f:
        r = f.read()
        f.close()
    u = json.loads(r)
    print(u)
    if u["status"] == "false":
        subprocess.call('python-3.8.2.exe', shell=True)
        with open("status.txt", "w+", encoding="utf-8") as d:
            d.seek(0)
            d.close()
        with open("status.txt", "w+", encoding="utf-8") as o:
            o.write('{"status":"true"}')
            o.close()
    else:
        pass
@eel.expose
def install():
    subprocess.call('pip install requests', shell=True)
    subprocess.call('pip install vk api', shell=True)
    subprocess.call('pip install apiai', shell=True)
    subprocess.call('pip install pymorphy2', shell=True)
@eel.expose
def my_python_method(token, name):
    os.mkdir(str(name))
    with open(str(name)+'/'+str(name)+'.txt', 'w', encoding='utf-8') as file:
        file.close()
    with open(str(name) +'/'+str(name)+'.py', 'w', encoding='utf-8') as f:
        f.close()
    with open('name.txt', 'a', encoding='utf-8') as f1:
        f1.write(str(name)+'\n')
        f1.close()
@eel.expose
def getProject():
    with open('name.txt', 'r') as f2:
        b = f2.readlines()
        print(b)
        f2.close()
        return b
@eel.expose
def rm_file(name_1):
    import os, sys
    length = len(name_1[len(name_1)-1])
    len1 = name_1[len(name_1)-1]
    path1 = os.path.join(os.path.abspath(os.path.dirname(__file__)),len1[0:length-1]+'/'+len1[0:length-1]+'.py')
    os.remove(path1)
    path2 = os.path.join(os.path.abspath(os.path.dirname(__file__)),len1[0:length-1]+'/'+len1[0:length-1]+'.txt')
    os.remove(path2)
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), len1[0:length-1])
    os.rmdir(path)
@eel.expose
def clean_txt():
    f = open("name.txt","r+")
    d = f.readlines()
    print(d[-1])
    f.seek(0)
    for i in d:
        if i != d[-1]:
            f.write(i)
    f.truncate()
    f.close()
@eel.expose
def getProject1():
    with open('name.txt', 'r') as f3:
        b1 = f3.readlines()
        print(b1)
        f3.close()
        return b1
@eel.expose
def start(name):
    string = name.replace("\n","")
    p = os.path.abspath(string+'.py')
    print(p[0:len(p)-3])
    f=os.popen('cd '+p[0:len(p)-3]+' && python '+string+'.py')
    #f.close()
    #print('cd '+p[0:len(p)-(len(string)+3)]+' && python '+string+'.py')
    #subprocess.call('cd '+p[0:len(p)-3]+' && python '+string+'.py', shell=False)
    #os.system('cd '+p[0:len(p)-3]+' && python '+string+'.py')
@eel.expose
def alg(name, json_ob):
    print(name)
    print(json_ob)
    string = name.replace("\n","")
    with open(string+'/'+string+'.txt', 'w+', encoding='utf-8') as gf:
        gf.seek(0)
        gf.close()
    with open(string+'/'+string+'.txt', 'a', encoding='utf-8') as fg:
        fg.write(str(json_ob))
        fg.close()
@eel.expose
def stop():
    subprocess.call('taskkill /f /IM python.exe', shell=True)
    #os.system('taskkill /f /IM python.exe')
@eel.expose
def open_read(name):
    string = name.replace("\n","")
    with open(string+'/'+string+'.txt', 'r', encoding='utf-8') as fh:
        red = fh.read()
        print(red)
        m = red.replace("'", '"')
        return m
@eel.expose
def rm_text(val):
    for line in fileinput.input('name.txt', inplace=1):
        sys.stdout.write(line.replace(val, ''))
    path1 = os.path.join(os.path.abspath(os.path.dirname(__file__)),val[0:len(val)-1]+'/'+val[0:len(val)-1]+'.py')
    os.remove(path1)
    path2 = os.path.join(os.path.abspath(os.path.dirname(__file__)),val[0:len(val)-1]+'/'+val[0:len(val)-1]+'.txt')
    os.remove(path2)
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), val[0:len(val)-1])
    os.rmdir(path)
@eel.expose
def creat_bot(token, name, json_ob):
    string = name.replace("\n","")
    with open(string+'/'+string+'.txt', 'w+', encoding='utf-8') as gf1:
        gf1.seek(0)
        gf1.close()
    with open(string+'/'+string+'.txt', 'a', encoding='utf-8') as fg1:
        g = str(json_ob)
        m = g.replace("'", '"')
        fg1.write(m)
        fg1.close()
    with open(string+'/'+string+'.py', 'w+', encoding='utf-8') as gf:
        gf.seek(0)
        gf.close()
    with open(string+'/'+string+'.py', 'a', encoding='utf-8') as f:
        p = string+'.txt'
        f.write('#Greetings from the developer')
        f.write('\n'+'from datetime import date')
        f.write('\n'+'import pymorphy2')
        f.write('\n'+'import vk_api'+'\n'+'token='+'"'+str(token)+'"')
        f.write('\n'+'import json')
        f.write('\n'+'import requests')
        f.write('\n'+'from random import randint')
        f.write('\n'+'vk = vk_api.VkApi(token = token)')
        f.write('\n'+'vk._auth_token()')
        f.write('\n'+'value = {"offset":0,"count":20,"filter":"unanswered"}')
        f.write('\n'+'morph = pymorphy2.MorphAnalyzer()')
        f.write('\n'+'while True:')
        f.write('\n'+'    messages = vk.method("messages.getConversations",value)')
        f.write('\n'+'    if messages["count"] >= 1:')
        f.write('\n'+'        user_id = messages["items"][0]["last_message"]["from_id"]')
        f.write('\n'+'        text = messages["items"][0]["last_message"]["text"]')
        f.write('\n'+"        with open('"+p+"', 'r', encoding='utf-8') as f:")
        f.write('\n'+'            red = f.read()')
        f.write('\n'+'            json_c = json.loads(red)')
        f.write('\n'+'            try:')
        f.write('\n'+'                if text == "token":')
        f.write('\n'+'                    pass')
        f.write('\n'+'                else:')
        f.write('\n'+'                    cen = requests.get("https://vkontaktbot.ru/censored/profanity.txt")')
        f.write('\n'+'                    t = cen.text.encode("utf-8").decode("unicode-escape")')
        f.write('\n'+'                    p = t.split()')
        f.write('\n'+'                    io = text.split()')
        f.write('\n'+'                    var = False')
        f.write('\n'+'                    for iop in io:')
        f.write('\n'+'                        n = io.index(iop)')
        f.write('\n'+'                        p1 = morph.parse(iop)[0]')
        f.write('\n'+'                        p2 = p1.normal_form')
        f.write('\n'+'                        io[n] = str(p2)')
        f.write('\n'+'                    for k in io:')
        f.write('\n'+'                        if k in io:')
        f.write('\n'+'                            f = json_c.items()')
        f.write('\n'+'                            for k, v in f:')
        f.write('\n'+'                                uy = k.split()')
        f.write('\n'+'                                if "/*filter*/" in uy:')
        f.write('\n'+'                                    for ui in io:')
        f.write('\n'+'                                        for po in p:')
        f.write('\n'+'                                            if ui == po:')
        f.write('\n'+'                                                n = io.index(po)')
        f.write('\n'+'                                                io[n] = "/*filter*/"')
        f.write('\n'+'                                                opo = " ".join(io)')
        f.write('\n'+'                                                if opo == k:')
        f.write('\n'+'                                                    var = True')
        f.write('\n'+'                                                    sp = json_c[opo].split()')
        f.write('\n'+'                                                    for i in sp:')
        f.write('\n'+'                                                        if "/*date*/" == i:')
        f.write('\n'+'                                                            now = date.today()')
        f.write('\n'+'                                                            n = sp.index("/*date*/")')
        f.write('\n'+'                                                            sp[n] = str(now)')
        f.write('\n'+'                                                        elif "/*offendingphrase*/" == i:')
        f.write('\n'+'                                                            req = requests.get("https://evilinsult.com/generate_insult.php?lang=ru&type=json")')
        f.write('\n'+'                                                            json_req = json.loads(req.text)')
        f.write('\n'+'                                                            sp[sp.index("/*offendingphrase*/")] = str(json_req["insult"])')
        f.write('\n'+'                                                        elif "/*random*/" == i:')
        f.write('\n'+'                                                            sp[sp.index("/*random*/")] = str(randint(1, 100))')
        f.write('\n'+'                                                        else:')
        f.write('\n'+'                                                            pass')
        f.write('\n'+'                                                    line = " ".join(sp)')
        f.write('\n'+'                                                    vk.method("messages.send",{"user_id":user_id,"random_id":randint(1,1000),"message": line})')
        f.write('\n'+'                    if var == False:')
        f.write('\n'+'                        sp = json_c[text].split()')
        f.write('\n'+'                        for i in sp:')
        f.write('\n'+'                            if "/*date*/" == i:')
        f.write('\n'+'                                now = date.today()')
        f.write('\n'+'                                n = sp.index("/*date*/")')
        f.write('\n'+'                                sp[n] = str(now)')
        f.write('\n'+'                            elif "/*offendingphrase*/" == i:')
        f.write('\n'+'                                req = requests.get("https://evilinsult.com/generate_insult.php?lang=ru&type=json")')
        f.write('\n'+'                                json_req = json.loads(req.text)')
        f.write('\n'+'                                sp[sp.index("/*offendingphrase*/")] = str(json_req["insult"])')
        f.write('\n'+'                            elif "/*random*/" == i:')
        f.write('\n'+'                                sp[sp.index("/*random*/")] = str(randint(1, 100))')
        f.write('\n'+'                            else:')
        f.write('\n'+'                                pass')
        f.write('\n'+'                        line = " ".join(sp)')
        f.write('\n'+'                        vk.method("messages.send",{"user_id":user_id,"random_id":randint(1,1000),"message": line})')
        f.write('\n'+'            except:')
        f.write('\n'+'                sp = json_c["else"].split()')
        f.write('\n'+'                for b in sp:')
        f.write('\n'+'                    if "/*date*/" == b:')
        f.write('\n'+'                        now = date.today()')
        f.write('\n'+'                        n = sp.index("/*date*/")')
        f.write('\n'+'                        sp[n] = str(now)')
        f.write('\n'+'                    elif "/*offendingphrase*/" == b:')
        f.write('\n'+'                         req = requests.get("https://evilinsult.com/generate_insult.php?lang=ru&type=json")')
        f.write('\n'+'                         json_req = json.loads(req.text)')
        f.write('\n'+'                         sp[sp.index("/*offendingphrase*/")] = str(json_req["insult"])')
        f.write('\n'+'                    elif "/*random*/" == b:')
        f.write('\n'+'                         sp[sp.index("/*random*/")] = str(randint(1, 100))')
        f.write('\n'+'                    else:')
        f.write('\n'+'                         pass')
        f.write('\n'+'                line = " ".join(sp)')
        f.write('\n'+'                vk.method("messages.send",{"user_id":user_id,"random_id":randint(1,1000),"message": line})')
        f.close()
@eel.expose
def creat_dialogflow(token, dialog_token, lang, inak, name, status):
    string = name.replace("\n","")
    print(status)
    with open(string+'/'+string+'.py', 'w+', encoding='utf-8') as f:
        f.seek(0)
        f.close()
    with open(string+'/'+string+'.py', 'a', encoding='utf-8') as f1:
        f1.write('#Greetings from the developer')
        f1.write('\n'+'import json')
        f1.write('\n'+'import vk_api')
        f1.write('\n'+'import time')
        f1.write('\n'+'from random import randint')
        f1.write('\n'+'import apiai')
        f1.write('\n'+'import requests')
        f1.write('\n'+'token="'+token+'"')
        f1.write('\n'+'dialog_token="'+dialog_token+'"')
        f1.write('\n'+'vk = vk_api.VkApi(token = token)')
        f1.write('\n'+'vk._auth_token()')
        f1.write('\n'+'value = {"offset":0,"count":20,"filter":"unanswered"}')
        f1.write('\n'+'while True:')
        f1.write('\n'+'    messages = vk.method("messages.getConversations",value)')
        f1.write('\n'+'    if messages["count"] >= 1:')
        f1.write('\n'+'        user_id = messages["items"][0]["last_message"]["from_id"]')
        f1.write('\n'+'        text = messages["items"][0]["last_message"]["text"]')
        f1.write('\n'+'        req = apiai.ApiAI(dialog_token).text_request()')
        f1.write('\n'+'        req.lang = "'+lang+'"')
        f1.write('\n'+'        req.session_id = "Dialog"')
        f1.write('\n'+'        req.query = text')
        f1.write('\n'+'        response_json = json.loads(req.getresponse().read().decode("utf-8"))')
        f1.write('\n'+'        response = response_json["result"]["fulfillment"]["speech"]')
        f1.write('\n'+'        if response:')
        f1.write('\n'+'            answer = response')
        f1.write('\n'+'        else:')
        f1.write('\n'+'            answer = "'+inak+'"')
        f1.write('\n'+'        vk.method("messages.send",{"user_id":user_id,"random_id":randint(1,1000),"message":answer})')
        f1.write('\n'+'    time.sleep(1)')
@eel.expose
def creat_dialogdir(json_ob, name):
    string = name.replace("\n","")
    with open(string+'/'+string+'.txt', 'w+', encoding='utf-8') as gf1:
        gf1.seek(0)
        gf1.close()
    with open(string+'/'+string+'.txt', 'a', encoding='utf-8') as fg1:
        g = str(json_ob)
        m = g.replace("'", '"')
        fg1.write(m)
        fg1.close()
eel.start('main.html', size=(700, 700))
