# -*- coding: UTF-8 -*-
import codecs
import sys
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
import os
import json
import io
import time

rootdir="./"

with open(rootdir+'RefreshingData.json',"r",encoding='utf-8') as f:
    thdata=json.load(f)
for i in thdata.keys():
    # if(((int(time.time()) -thdata[i]['lastedit']) < 1296000 ) and thdata[i]['totalreply'] > 1) :
    # thdata[i]['newtitle'] = thdata[i]['title']
    if(int(time.time()) -thdata[i]['lastedit']) < 1296000 and thdata[i]['newtitle']:
        thdata[i]['active'] = True
    
with open(rootdir+'RefreshingData.json',"w",encoding='utf-8') as f:
        f.write(json.dumps(thdata,indent=2,ensure_ascii=False))
