#!/usr/bin/python3

###
# Author: Vincent Lucas <vincent.lucas@gmail.com>
###

import vobject
import sys

###
# Parse an .ics and display the summary and dates.
###
if __name__ == "__main__":
    if(len(sys.argv) != 2):
        print("Usage: " + sys.argv[0] + " filename.ics")
        sys.exit(1)

    # Reads the .ics file and parse it.
    with open(sys.argv[1], 'r') as fd:
        parsedCal = vobject.readOne(fd)

#        parsedCal.prettyPrint()

        for ev in parsedCal.vevent_list:
            print(ev.summary.value)
            print(ev.dtstart.value)
            print(ev.dtend.value)

    sys.exit(0)
