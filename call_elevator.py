client_secret = 'H1fM0hP0kO3tT8uW4rB3cG3tX4wL6bV0wD5tN4uL6lG2yO2mC6'
client_id = '555dbfe3-a660-4cdd-b984-782db54521da'
building_id = '9990000508'

# Porter detects someone in the active zone and approaches.
# Porter recognizes Betty due to her SmartKey / phone. 
# Porter greets her: "Welcome, Betty. Heading home?"
# Porter hears Betty say "let's go"

# Building Door opens due to Porter / SmartKey
# Betty & Porter enter & walk to elevator

# Porter calls elevator using KONE API: POST /call { lobby, Betty's floor}

d = {
      "template": {
              "data": [
                        {"name":"sourceAreaId", "value": "area:9990000508:1000"},
                              {"name":"destinationAreaId", "value": "area:9990000508:2000"}
                      ]
                }
    }

#area_from = 'area:9990000508:1000'
#area_to = 'area:9990000508:2000'

# Wait for elevator to reach us.


# import httplib
import http.client
import json

# conn = httplib.HTTPSConnection("api.kone.com")
conn = http.client.HTTPSConnection("api.kone.com")

#payload = "{\"template\":{\"data\":[{\"value\":\"%s\",\"name\":\"%s\"}]}}"
payload = json.dumps(d)
print ('sending', payload)

headers = {
            'x-ibm-client-id': client_id,
                'x-ibm-client-secret': client_secret,
                    'content-type': "application/vnd.collection+json",
                        'accept': "application/vnd.collection+json"
                            }

conn.request("POST", "/api/building/%s/call" %building_id, payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))