###
# Author: Vincent Lucas <vincent.lucas@gmail.com>
###

import vobject

from src.VEvent import *

###
# Class to manage calendars.
###
class VCalendar:
    ###
    # Instantiates an new calendar with the provided vCalendar text if any
    # provided.
    #
    # @param vcalendar_test The calendar text with vCalendar format.
    ###
    def __init__(
            self,
            vcalendar_text = None):

        self.vcalendar = None
        self.parse(vcalendar_text)

    ###
    # Parse and load the provided vCalendar text.
    #
    # @param vcalendar_test The calendar text with vCalendar format.
    ###
    def parse(
            self,
            vcalendar_text = None):

        if(vcalendar_text != None):
            self.vcalendar = vobject.readOne(vcalendar_text)

    ###
    # Read an .ics file.
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

    ###
    # Returns the event uids from this calendar.
    #
    # @return The event uid list. Returns an empty list if this calendar does
    # not contain any event.
    ###
    def get_uids(
            self):
        uids = []
        for vevent in self.get_vevents:
            uids.append(VEvent.get_uid(vevent))

        return uids

    ###
    # Returns the vevent list.
    #
    # @return the vevent list.
    ###
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

    ###
    # Print this calendar in a pleasant way.
    ###
    def pretty_print(
            self):
        self.vcalendar.prettyPrint()

    ###
    # Print a brief description of this calendar events.
    ###
    def print(
            self):
        for vevent in self.vcalendar.vevent_list:
            VEvent.print(vevent)

    ###
    # Returns the text serialized form of this calendar.
    #
    # @return The text serialized form of this calendar.
    ###
    def __repr__(
            self):
        return self.__str__()

    ###
    # Returns the text serialized form of this calendar.
    #
    # @return The text serialized form of this calendar.
    ###
    def __str__(
            self):
        return self.vcalendar.serialize()
