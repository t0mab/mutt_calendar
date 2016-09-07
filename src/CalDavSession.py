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
