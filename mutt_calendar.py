#!/usr/bin/python3

###
# Author: Vincent Lucas <vincent.lucas@gmail.com>
###

import sys
import vobject

from src.CalDavSession import *
from src.VCalendar import *
from src.utils import *

###
# Parse an .ics and display the summary and dates.
#
# @param filename An .ics filename containing an or several events.
###
if __name__ == "__main__":
    if(len(sys.argv) < 2):
        print("Usage: " + sys.argv[0] + " <filename.ics> [-inter]")
        sys.exit(1)

    inter = (len(sys.argv) == 3 and sys.argv[2] == "-inter")

    vcalendar = VCalendar()
    vcalendar.read(sys.argv[1])

    pwd = "/home/lucas/software/github/mutt_calendar/"
    conf = load_json(pwd + "conf/conf.json")
    calDavSession = CalDavSession(
            conf["user"],
            conf["password"],
            conf["url"])

    if(calDavSession):
        uids = vcalendar.get_uids()
        for uid in uids:
            event = calDavSession.get_event(uid)
            if(event):
                vcalendar = VCalendar(event)
                vcalendar.print()
                #vcalendar.pretty_print()
                if(inter):
                    action = input("[NONE/a/d]: ")
                    if(action == "a"):
                        vcalendar.set_partstat("ACCEPTED")
                        calDavSession.set_event(str(vcalendar), uid)
                    elif(action == "d"):
                        vcalendar.set_partstat("DECLINED")
                        calDavSession.set_event(str(vcalendar), uid)
        calDavSession.close()
    else:
        vcalendar.print()

    sys.exit(0)
