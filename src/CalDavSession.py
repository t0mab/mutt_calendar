###
# Author: Vincent Lucas <vincent.lucas@gmail.com>
###

import requests

class CalDavSession:
    def __init__(
            self,
            user,
            password,
            url):

        self.session = requests.Session()
        self.session.auth = (user, password)
        self.url = url

    def close(
            self):

        self.session.close()

    def get_event(
        self,
        eventid):

        value = ""
        caldav_content_type = 'text/calendar; charset=utf8'

        result = self.session.get(self.url + "/" + eventid + ".ics")
        if(result.status_code == 200
                and result.headers['content-type'] == caldav_content_type):
            value = result.text

        return value

    def set_event(
        self,
        event,
        eventid):

        # TODO: get event id from event UID.
        result = self.session.put(self.url + "/" + eventid + ".ics", data=event)
        #result = self.session.put(self.url, data=event)

        # created == 201, modified == 204
        return (result.status_code == 201
                or result.status_code == 204)

    def delete_event(
            ):
        # DELETE url/event.ics
        pass

    def list_calendar_collections(
            ):
#        Example:
#            <C:calendar-home-set xmlns:D="DAV:"
#                    xmlns:C="urn:ietf:params:xml:ns:caldav">
#                <D:href>http://cal.example.com/home/bernard/calendars/</D:href>
#            </C:calendar-home-set>
        pass

# N.B. create a new calendar via MKCALENDAR via DAV:displayname (exemple page
# 24)

# N.B. to create a vevent add the "If-None-Match: *" HTTP header to the PUT
# request.
# "If-Match: *" for updating.
#
# e.g.
#PUT /home/lisa/calendars/events/qwue23489.ics HTTP/1.1
#If-None-Match: *
#Host: cal.example.com
#Content-Type: text/calendar
#Content-Length: xxxx
#
#BEGIN:VCALENDAR
#VERSION:2.0
#PRODID:-//Example Corp.//CalDAV Client//EN
#BEGIN:VEVENT
#UID:20010712T182145Z-123401@example.com
#DTSTAMP:20060712T182145Z
#DTSTART:20060714T170000Z
#DTEND:20060715T040000Z
#SUMMARY:Bastille Day Party
#END:VEVENT
#END:VCALENDAR


# N.B. RRULE management : (see CALDAV:expand in Section 9.6.5.)

# N.B. event search
#REPORT /bernard/work/ HTTP/1.1
#Host: cal.example.com
#Depth: 1
#Content-Type: application/xml; charset="utf-8"
#Content-Length: xxxx
#<?xml version="1.0" encoding="utf-8" ?>
#<C:calendar-query xmlns:D="DAV:"
#xmlns:C="urn:ietf:params:xml:ns:caldav">
#
#<D:prop>
#    <D:getetag/>
#    <C:calendar-data>
#	<C:comp name="VCALENDAR">
#	    <C:prop name="VERSION"/>
#	    <C:comp name="VEVENT">
#	    <C:prop name="SUMMARY"/>
#	    <C:prop name="UID"/>
#	    <C:prop name="DTSTART"/>
#	    <C:prop name="DTEND"/>
#	    <C:prop name="DURATION"/>
#	    <C:prop name="RRULE"/>
#	    <C:prop name="RDATE"/>
#	    <C:prop name="EXRULE"/>
#	    <C:prop name="EXDATE"/>
#	    <C:prop name="RECURRENCE-ID"/>
#	</C:comp>
#	<C:comp name="VTIMEZONE"/>
#	</C:comp>
#    </C:calendar-data>
#</D:prop>
#<C:filter>
#    <C:comp-filter name="VCALENDAR">
#	<C:comp-filter name="VEVENT">
#	    <C:time-range start="20060104T000000Z" end="20060105T000000Z"/>
#	</C:comp-filter>
#    </C:comp-filter>
#</C:filter>
#</C:calendar-query>
#
#
#Partial Retrieval of Recurring Events: CALDAV:limit-recurrence-set
#Expanded Retrieval of Recurring Events: CALDAV:expand


# N.B. get event by id
#REPORT /bernard/work/ HTTP/1.1
#Host: cal.example.com
#Depth: 1
#Content-Type: application/xml; charset="utf-8"
#Content-Length: xxxx
#
#<?xml version="1.0" encoding="utf-8" ?>
#<C:calendar-query xmlns:C="urn:ietf:params:xml:ns:caldav">
#    <D:prop xmlns:D="DAV:">
#	<D:getetag/>
#	<C:calendar-data/>
#    </D:prop>
#    <C:filter>
#	<C:comp-filter name="VCALENDAR">
#	    <C:comp-filter name="VEVENT">
#		<C:prop-filter name="UID">
#		<C:text-match collation="i;octet">DC6C50A017428C5216A2F1CD@example.com</C:text-match>
#		</C:prop-filter>
#	    </C:comp-filter>
#	</C:comp-filter>
#    </C:filter>
#</C:calendar-query>
