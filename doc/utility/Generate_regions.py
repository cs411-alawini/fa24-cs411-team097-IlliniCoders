import pandas as pd
import numpy
def float_range(start, stop, step):
    if (start < stop):
        while start < stop:
            yield round(start, 10)  # rounding to avoid floating point arithmetic issues
            start += step
    else :
        while stop < start:
            yield round(start, 10)  # rounding to avoid floating point arithmetic issues
            start += step
top_latitude = 37
top_longitude= -87
bottom_latitude =24
bottom_longitude =-73
longitude_step = .5
latitude_step = -.5


min_latitudes = [] #exclusive
min_longitudes = [] #exclusive
max_latitudes = []#inclusive
max_longitudes = []#inclusive
indexes = []

curr_latitude = top_latitude
curr_longitude = top_longitude
i=1
for j in numpy.arange(top_latitude,bottom_latitude-latitude_step,latitude_step):
    for k in numpy.arange(top_longitude,bottom_longitude-longitude_step,longitude_step):
        indexes.append(i) #longitudes are fliped because they are all negative
        max_latitudes.append(j)
        max_longitudes.append(k+longitude_step)
        min_latitudes.append(j+latitude_step)
        min_longitudes.append(k)
        i+=1
   

regions = pd.DataFrame({
    "region_id": indexes,
    "min_latitude": min_latitudes,
    "max_latitude": max_latitudes,
    "min_longitude": min_longitudes,
    "max_longitude": max_longitudes,
    })
regions.to_csv('regions.csv', index=False)