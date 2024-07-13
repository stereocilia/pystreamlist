#
# This script reads a yaml file of streaming radio stations, identified by
# uuid as provided by the radio-browser.info API and fetches the most current
# streaming url for each.
#
# A playlist file is then generated for each radio station that contains the best
# urls for that station.
#
# These playlist files can be imported by streaming software to play you stations
#
# The goal is to have the best url for any given radio station so that if it changes over time,
# you can update your software accordingly
#

from pyradios import RadioBrowser
from dotenv import load_dotenv
import yaml
import re
import os

load_dotenv()

#TODO: Move this to a dot env file or get it from the command line
STATIONS_FILENAME = os.getenv('PYSTREAMLIST_STATIONS_FILENAME')
OUTPUT_PATH = os.getenv('PYSTREAMLIST_OUTPUT_PATH')

def main():
	rb = RadioBrowser() 

	#TODO: This goes in a try structure
	with open(STATIONS_FILENAME) as f:
	    my_stations = yaml.safe_load(f)

	for station in my_stations:
		# fetch station results by uuid
		result_station = rb.station_by_uuid(station['uuid'])[0]

		# create a filename for the playlist that will be created, based on the friendly name for this station
		file_name = createFileName( station['friendly_name'] )

		# output the generated file name to the console
		print(result_station['name'] + ', Generating playlist: ' + file_name)

		# open the playlist
		f = open(OUTPUT_PATH + file_name, 'w')

		# write the stream url to the playlist
		f.write(result_station['url'])

		# close the file handle
		f.close()

def createFileName(friendly_name):
	return re.sub("\s", "_", friendly_name.casefold()) + '.m3u'

main()