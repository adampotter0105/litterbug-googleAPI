# Import google_streetview for the api module
import google_streetview.api
import math
import os
import time
steps = 8
from matplotlib import pyplot as plt

nodes= [    (40.819283, -73.910595),
            (40.821256, -73.909943), 
            (40.821497, -73.911144),
            (40.820281, -73.911885), 
            (40.818023, -73.913214),
            (40.816310, -73.914167),
            (40.816180, -73.911897),
            ]
streets=[]
for i in range(len(nodes)-1):
    streets.append([nodes[i],nodes[i+1]])
print(streets)
coordx=[]
coordy=[]
def get_image(lat, lon, head):
    # Define parameters for street view api
    coordx.append(lat)
    coordy.append(lon)
    params = [{
    	'size': '640x640', # max 640x640 pixels
    	'location':  str(lat)+","+str(lon),
    	'heading': str(head),
    	'pitch': '-0.76',
    	'key': 'AIzaSyDhPefszM5msxfXW6XM9FwxqmbjQ-MVLN4'
    }]
    # Create a results object
    results = google_streetview.api.results(params)
    # Download images to directory 'downloads'
    results.download_links('downloads')
    #rename file
    time.sleep(0.05)
    name = str(round(lat*10000))+"_"+str(round(lon*10000))
    dst = name + ".jpg"
    src ='downloads/'+ 'gsv_0.jpg' 
    dst ='downloads/'+ dst 
    try:
        os.rename(src, dst) 
        print("Success")
    except:
        print("Failed to rename")
    
def scan():
    for i in streets:
        m = (i[1][0]-i[0][0]), (i[1][1]-i[0][1])
        head = math.atan( m[1]/ m[0] )*(180/math.pi)+90
        get_image(i[0][0],i[0][1], head)
        
        for l in range(1, steps-1):
            get_image(i[0][0]+m[0]*(l/(steps-1)), i[0][1]+m[1]*(l/(steps-1)), head)
            
        get_image(i[1][0],i[1][1], head)
        
        
#Run once
scan()
    
plt.scatter(coordx,coordy)
plt.show()