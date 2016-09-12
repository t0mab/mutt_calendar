###
# Author: Vincent Lucas <vincent.lucas@gmail.com>
###

import vobject

from src.VEvent import *

class VCalendar:
    def __init__(
            self,
            vcalendar_text = None):

        self.vcalendar = None
        self.parse(vcalendar_text)

    def parse(
            self,
            vcalendar_text = None):

        if(vcalendar_text != None):
            self.vcalendar = vobject.readOne(vcalendar_text)

    ###
    # Read an .ics.
    #
    # @param filename An .ics filename containing an or several events.
    ###
    def read(
            self,
            filename):
        # Reads the .ics file.
        with open(filename, 'r', encoding='utf8', errors="backslashreplace") \
                as fd:
            self.parse(fd.read())

    def get_uids(
            self):
        uids = []
        for vevent in self.get_vevents:
            uids.append(VEvent.get_uid(vevent))

        return uids

    def get_vevents(
            self):
        return self.vcalendar.vevent_list

    ###
    # TODO
    ###
#    def create_vevent(
#            self,
#            summary,
#            dtstart = None,
#            dtend = None,
#            location = None,
#            attendees = None,
#            privacy_class = "PULBIC",
#            repeat = None):
#        self.vcalendar = vobject.iCalendar()
#        self.vcalendar.add('vevent')
#        self.vcalendar.vevent.add('summary').value = summary
#        self.vcalendar.vevent.add('dtstart').value = datetime.datetime()

    def pretty_print(
            self):
        self.vcalendar.prettyPrint()

    def print(
            self):
        for vevent in self.vcalendar.vevent_list:
            VEvent.print(vevent)

    def __repr__(
            self):
        return self.__str__()

    def __str__(
            self):
        return self.vcalendar.serialize()
