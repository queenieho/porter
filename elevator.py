import json
import time
import http.client
import requests

client_id="555dbfe3-a660-4cdd-b984-782db54521da"
client_secret="H1fM0hP0kO3tT8uW4rB3cG3tX4wL6bV0wD5tN4uL6lG2yO2mC6"
building_id=9990000508

headers = {
    'x-ibm-client-id': client_id,
    'x-ibm-client-secret': client_secret,
    'accept': "application/vnd.collection+json",
    'content-type': "application/vnd.collection+json"
    }

def get_call_object(call_object_url):
	# Read current call status
	response = requests.get(call_object_url, headers=headers)
	return response

def get_deckstate_object(deckstate_object_url):
	# Read current deckstate status
	response = requests.get(deckstate_object_url, headers=headers)
	return response

def call_elevator(building_id, from_area, to_area):
	print ('calling')
	payload = """{ 
		"template": { 
			"data": [ 
				{"name":"sourceAreaId", "value": "%s"}, 
				{"name":"destinationAreaId", "value": "%s"} 
			] 
		} 
	}""" % (from_area, to_area)
	response = requests.post("https://api.kone.com/api/building/%s/call" % building_id, headers=headers, data=payload)
	return response.headers["Location"] # returns call id thing to use for status check

def wait_for_elevator_at_start(call_object):
	callstate=None
	decklevel=None
	while True:
		response = get_call_object(call_object)
		response = json.loads(response.content)
		# Find the current callState value from the response
		for item in response["collection"]["items"][0]["data"]:
			if item["name"] == "callState":
				callstate = item["value"]
				break
		if callstate != 0:
			print ("Elevator has arrived!")
			break
	time.sleep(1)

def wait_for_elevator_at_dest(call_object):
	callstate=None
	decklevel=None
	while True:
		response = get_call_object(call_object)
		response = json.loads(response.content)
		# print (response)
		# Find the current callState value from the response
		for item in response["collection"]["items"][0]["data"]:
			if item["name"] == "callState":
				callstate = item["value"]
				break
		# Find information where the elevator is
		for item in response["collection"]["links"]:
			if item["rel"] == "deckstate item":
				deckstate = item["href"]
				# print (deckstate)
				break

		if callstate:
			response = get_deckstate_object(deckstate)
			response = json.loads(response.content)
			# print (response)
			for item in response["collection"]["items"][0]["data"]:
				if item["name"] == "level":
					decklevel = item["value"]
					break

		# print ("Current callState=%s and deck level=%s" % (callstate, decklevel))
		if callstate == 7 or callstate == 8:
			print ('**** Arriving at your floor ****')
			break
	time.sleep(1)
