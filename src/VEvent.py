###
# Author: Vincent Lucas <vincent.lucas@gmail.com>
###

import vobject

###
# Class to manage calendar events.
#
# This is an abstract class with only static methods.
###
class VEvent:
    ###
    # Set participation status (RFC 5545).
    #
    # @param vevent The event to modify.
    # @param email The user email for which the participation is set.
    # @param parstat The participation state :
    #   - NEEDS-ACTION
    #   - ACCEPTED
    #   - DECLINED
    #   - TENTATIVE
    #   - DELEGATED
    ###
    def set_partstat(
            vevent,
            email,
            partstat):
        email_str = "mailto:"+email
        for attendee in vevent.attendee_list:
            if(attendee.value == email_str):
                vevent.attendee.PARTSTAT_param = [ partstat ]

    ###
    # Return the uid of the given VEvent.
    #
    # @param event The provided VEvent.
    #
    # @return The Vevent uid value or an empty string if it does not exists.
    ###
    def get_uid(
            vevent):
        return vevent.getChildValue("uid", "")

    ###
    # TODO
    ###
#    def create_vevent(
#            vevent,
#            summary,
#            dtstart = None,
#            dtend = None,
#            location = None,
#            attendees = None,
#            privacy_class = "PULBIC",
#            repeat = None):
#        vcalendar = vobject.iCalendar()
#        vcalendar.add('vevent')
#        vcalendar.vevent.add('summary').value = summary
#        vcalendar.vevent.add('dtstart').value = datetime.datetime()

    ###
    # Print a summary of the provided event.
    #
    # @param vevent The event to print.
    ###
    def print(
            vevent):
        location = vevent.getChildValue("location")
        summary = vevent.getChildValue("summary", "")
        dtstart = vevent.getChildValue("dtstart")
        dtend = vevent.getChildValue("dtend")
        organizer = vevent.getChildValue("organizer")

        event_str = "\n"
        if(location):
            event_str += "[" + location + "] - "
        event_str += summary

        if(dtstart and dtend):
            start_day = dtstart.strftime("%d/%m/%Y")
            end_day = dtend.strftime("%d/%m/%Y")
            end_another_day = ""
            event_str += "\n[" + start_day + "] " + dtstart.strftime("%H:%M")
            if(start_day != end_day):
                end_another_day = "[" + end_day + "] "
            event_str += \
                " - " + end_another_day + dtend.strftime("%H:%M")

        event_str += "\n\n"
        if(organizer):
            event_str += "[ORGANIZER]: " + vevent.organizer.CN_param + "\n"

        for attendee in vevent.attendee_list:
            event_str += "[" + attendee.PARTSTAT_param + "]: " \
                + attendee.CN_param + "\n"

        print(event_str)
