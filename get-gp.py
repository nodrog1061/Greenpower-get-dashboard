import requests
import json

def getData(requestURL = '', jsonFileURL = '', pretyPrint = True, debug = False):
    
    if requestURL == '':

        if jsonFileURL == '':
            jsonFileURL = 'config.json'

    
        #extracts the config and compoles it to non prety mode
        with open(jsonFileURL) as json_file:
            if pretyPrint == True:
                lines = json_file.readlines()
                json_file = '\t'.join([line.strip() for line in lines])
            #print(json_file)
            config = json.loads(json_file)
            #print(config["requestaddress"])

    #sends the get request to the server
    if requestURL == '':
        requestURL = config["requestaddress"]

    data = requests.get(requestURL)
    #print(data.text)
    #tells py its a json file
    data = json.loads(data.text)
    #print(data["time"])
    #{"voltage":19,"voltsLower":11,"current":20,"speed":12,"throttle":98,"rpm":1680,"time":"17:07:59","lat":"50.8575914","lon":"-0.7576133","temp1":"16.2","temp2":"15.9","track":"Goodwood","currLap":4.1916603248984625}

    #sets each json item as a varible for later
    voltage = data["voltage"]
    voltsLower = data["voltsLower"]
    current = data["current"]
    speed = data["speed"]
    throttle = data["throttle"]
    rpm = data["rpm"]
    time = data["time"]
    lat = data["lat"]
    lon = data["lon"]
    temp1 = data["temp1"]
    temp2 = data["temp2"]
    track = data["track"]
    currLap = data["currLap"]
    
    #sends all the varibles back
    return voltage,voltsLower,current,speed,throttle,rpm,time,lat,lon,temp1,temp2,track,currLap

#debug
#voltage,voltsLower,current,speed,throttle,rpm,time,lat,lon,temp1,temp2,track,currLap = getData()
print(getData())

#print(time)