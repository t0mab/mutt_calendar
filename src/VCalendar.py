###
# Author: Vincent Lucas <vincent.lucas@gmail.com>
###

import vobject

from src.CalDavSession import *

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
    # Set participation status (RFC 5545) :
    # - NEEDS-ACTION
    # - ACCEPTED
    # - DECLINED
    # - TENTATIVE
    # - DELEGATED
    ###
    def set_partstat(
            self,
            partstat):
        for ev in self.vcalendar.vevent_list:
            # TODO check for each participant
            #ev.attendee.PARTSTAT_param = [ 'ACCEPTED' ]
            ev.attendee.PARTSTAT_param = [ partstat ]

    ###
    # Read an .ics.
    #
    # @param filename An .ics filename containing an or several events.
    ###
    def read(
            self,
            filename):
        # Reads the .ics file.
        with open(filename, 'r') as fd:
            self.parse(fd.read())

    def get_uids(
            self):
        uids = []
        for ev in self.vcalendar.vevent_list:
            uids.append(ev.uid.value)

        return uids

    ###
    # TODO
    ###
    def create_vevent(
            self,
            summary,
            dtstart = None,
            dtend = None,
            location = None,
            attendees = None,
            privacy_class = "PULBIC",
            repeat = None):
        self.vcalendar = vobject.iCalendar()
        self.vcalendar.add('vevent')
        self.vcalendar.vevent.add('summary').value = summary
        self.vcalendar.vevent.add('dtstart').value = datetime.datetime()

    def pretty_print(
            self):

        self.vcalendar.prettyPrint()

    def print(
            self):

        for ev in self.vcalendar.vevent_list:
            print(ev.summary.value)
            print(ev.dtstart.value)
            print(ev.dtend.value)
            print("[ORGANIZER]: " \
                    + ev.organizer.CN_param)
            # TODO check for each participant
            print("[" + ev.attendee.PARTSTAT_param + "]: " \
                    + ev.attendee.CN_param)

    def __repr__(
            self):
        return self.__str__()

    def __str__(
            self):
        return self.vcalendar.serialize()
