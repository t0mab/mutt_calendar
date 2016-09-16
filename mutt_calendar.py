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
# Ask the user to accept or decline invitation and update the event on the
# server.
#
# @param calDavSession An opened CalDav session.
# @param vcalendar The VCalendar to accept or decline.
###
def accept_invitation(
        calDavSession,
        vcalendar):
    action = input("[NONE/a/d]: ")
    if(action == "a"):
        vcalendar.set_partstat("ACCEPTED")
        calDavSession.set_event(str(vcalendar), uid)
    elif(action == "d"):
        vcalendar.set_partstat("DECLINED")
        calDavSession.set_event(str(vcalendar), uid)

###
# Parse an .ics and display the summary and dates.
#
# @param filename An .ics filename containing an or several events.
###
if __name__ == "__main__":
    # Parse the command line
    if(len(sys.argv) < 2):
        print("Usage: " + sys.argv[0] + " <filename.ics> <[--inter] [--offline]>")
        sys.exit(1)
    # Parse if the user will be asked to accept or decline invitation.
    inter = False
    offline = False
    for arg in sys.argv:
        if(arg == "--inter"):
            inter = True
        if(arg == "--offline"):
            offline = True

    # Load the configuration and configure the CalDav session.
    # TODO: Move the path outside the code.
    pwd = "/home/lucas/software/github/mutt_calendar/"
    conf = load_json(pwd + "conf/conf.json")
    email=conf["email"]

    # Initialize the valendar with a local file.
    vcalendar = VCalendar()
    vcalendar.read(sys.argv[1])

    if(not offline):
        calDavSession = CalDavSession(
                conf["user"],
                conf["password"],
                conf["url"])

    # Pretty print the vcalendar for debug purpose.
    #vcalendar.pretty_print()

    # Loop over the vevent contained in the calendar.
    vevents = vcalendar.get_vevents()
    for vevent in vevents:
        event = None
        if(not offline):
            # Try to get the last version of this vevent from the server.
            event = calDavSession.get_event(VEvent.get_uid(vevent))
            # There is a new version: then print it and ask to accept
            # or decline invitation if requested.
            if(event):
                vcalendar = VCalendar(event)
                vcalendar.print()
                if(inter):
                    accept_invitation(calDavSession, vcalendar)
        # There is no new version: simply display the local version of the
        # vevent.
        else:
            VEvent.print(vevent)

    if(not offline):
        # Close the CalDav session.
        calDavSession.close()

    sys.exit(0)
