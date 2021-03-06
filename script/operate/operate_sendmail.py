#!/usr/bin/python
#-*- coding: utf-8 -*-

import re
import commands
import time

def run(ip,user,cmd):
    cmds = """ sudo ssh -oConnectTimeout=10 %s@%s "%s" """ % (user,ip,cmd)
    try:
        out = commands.getoutput(cmds)
    except Exception,e:
        out = "error"
    return out

def start_stop_sendmail(action,ip,configfile):
    cmd = """ less %s |grep 'sendmail:1'|wc -l """ % configfile
    out = commands.getoutput(cmd)
    if int(out) == 1:
        if action == "stop":
            cmd = """ service sendmail stop """
            run(ip,'root',cmd)
            cmd = """ service sendmail status """
            out = run(ip,'root',cmd)
            if re.search('is stopped',out):
                print "%s sendmail stop sucess." % ip
            else:
                print "%s sendmail stop fail." % ip
        elif action == "start":
            cmd = """ service sendmail start """
            run(ip,'root',cmd)
            cmd = """ service sendmail status """
            out = run(ip,'root',cmd)
            if re.search('is running',out):
                print "%s sendmail start sucess." % ip
            else:
                print "%s sendmail start fail." % ip
    else:
        pass
