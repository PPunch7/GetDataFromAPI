import urllib.request, json
import sys
import datetime

def checkNone(value):
    if value is None or value == 999.9:
        return -999.99
    else:
        return value
    
def dt_format(value):
    dt = value.split('T')
    date = dt[0]
    time = dt[1].split('+')[0]
    return date + ' ' + time

now = datetime.datetime.now()

# file name
now = datetime.datetime.now()
filename = "mwa_obs_" + now.strftime("%Y%m%d") + "_" + now.strftime("%Y%m%d-%H%M%S%f") + ".txt"

# CREATE file
f = open(filename, "w")
f.write("code,site_timestamp,temp,conducted,tds,salinity,deo,depth,ph,nh4,turbid\n")
f.close()

# GET DATA 
url = [LINK]

for u in url:
    print("-------------- Start requesting url: " + u + " --------------")
    response = urllib.request.urlopen(u)
    data = json.loads(response.read())

    # go through the DATA
    for d in data['data']:
        #print (d)

        # get each DATA
        # print(d['datetimes'][0:10],now.strftime("%Y-%m-%d"))
        if d['datetimes'][0:10] == now.strftime("%Y-%m-%d") or d['datetimes'][0:10] == (now + datetime.timedelta(days=-1)).strftime("%Y-%m-%d"):
            sta_id = d['stn_id']
            dt = dt_format(d['datetimes'])
            tmp = checkNone(d['temp'])
            con = checkNone(d['conducted'])
            tds = checkNone(d['tds'])
            sal = checkNone(d['salinity'])
            deo = checkNone(d['deo'])
            dep = checkNone(d['depth'])
            ph = checkNone(d['ph'])
            nh4 = checkNone(d['nh4'])
            tur = checkNone(d['turbid'])
            #print(sta_id, dt, tmp, con, tds, sal, deo, dep, ph, nh4, tur)
            print("Wrote st_code : " + sta_id + " successful.")

            # WRITE DATA
            f = open(filename, "a")
            f.write(sta_id + "," + dt + "," + str(tmp) + "," + str(con) + "," + str(tds) + "," + str(sal) + "," + str(deo) + "," + str(dep) + "," + str(ph) + "," + str(nh4) + "," + str(tur) + "\n")
 
f.close()