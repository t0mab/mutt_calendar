###
# Author: Vincent Lucas <vincent.lucas@gmail.com>
###

import json

###
# Load json data from the given file.
#
# @param filename The filename to read the json data from.
#
# @return The json data in a string format. Or None on error.
###
def load_json(
        filename):

    json_data = None
    with open(filename) as fd:
        json_data = json.load(fd)

    return json_data
