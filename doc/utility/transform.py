
import pandas as pd
import time
#need to normalize the x and the y so that it fits on a step than map each x and y combination to a region
#split them up because longitude will always be negative
def normalize_lat(coord, step):
    if (coord % abs(step))==0:
        return coord
    return (int(coord /step) * step) - step
def normalize_lon(coord, step):
    return (int(coord /step) * step) 
def init_search():
    regions = pd.read_csv("regions.csv")
    #max_lat_idx = 2
    #for i in range(len(regions)):
    #    curr_max_lat = regions.iloc[i]['max_latitude']
    #    region_id = regions.iloc[i]['region_id']
    #    if curr_max_lat in lookup:
    #        lookup[curr_max_lat].append((regions.iloc[i]['max_longitude'],region_id))
    #    else:
    #        lookup[curr_max_lat] =[(regions.iloc[i]['max_longitude'],region_id)]
    #BY THE POWER OF CHAT GPT BECOME SOMETHING MORE PERFORMANT ON PYTHON
    lookup = (
        regions.groupby('max_latitude')
        .apply(lambda group: list(zip(group['max_longitude'], group['region_id'])))
        .to_dict()
    )
    return lookup
def find(lat, lon):
    if lat not in lookup:
        return 0
    arr = lookup[lat]
    for i in arr:
        if i[0] == lon:
            return i[1]
    return 0
def test():
    longitude_step = .5
    latitude_step = -.5
    test_latitude = 40.73030648138512
    test_logitude = -73.98640431222074
    n_lat = normalize_lat(test_latitude,latitude_step)
    n_lon =normalize_lon(test_logitude,longitude_step)
    print(n_lat)
    print(n_lon)
    test_region = find(n_lat,n_lon)
    print(test_region)
def anotate_file(file_name, lat_column_name, lon_column_name, longitude_step, latitude_step, chunksize, num_chunks, remove_zeros):
    #long files will take a while. it will also take a lot of memory
    final = []
    count =0
    for chunk in pd.read_csv(file_name, chunksize=chunksize):
        regions = []
        if count >= num_chunks: #its possible to run out of memory so this is necessary
            break
        count+=1
    
        for index, row in chunk.iterrows():
           n_lat = normalize_lat(row[lat_column_name], latitude_step)
           n_lon = normalize_lon(row[lon_column_name], longitude_step)
           regions.append(find(n_lat, n_lon))
        chunk.insert(0,'region_id',regions)
        if remove_zeros:
            chunk = chunk[chunk['region_id'] != 0]
        final.append(chunk)
    final_df = pd.concat(final, ignore_index=True)
    final_df.to_csv("annotated_"+file_name,index = False)
def convert_lon(lon):
    dir = lon[-1]
    if dir == "W":
        return float(lon[:-1])*-1.0
    return float(lon[:-1])
def convert_lat(lat):
    dir = lat[-1]
    if dir == "S":
        return float(lat[:-1])*-1.0
    return float(lat[:-1])
def convert_coords(file_name, lat_column_name, lon_column_name):
    file = pd.read_csv(file_name)
    file[lat_column_name] = file[lat_column_name].apply(convert_lat)
    file[lon_column_name] = file[lon_column_name].apply(convert_lon)
    file.to_csv("converted_"+file_name, index = False)
def combine_csv(file_name_1, file_name_2, col_left, col_right):
    df1 = pd.read_csv(file_name_1)
    df2 = pd.read_csv(file_name_2)
    merged_df = pd.merge(df1, df2, left_on=col_left,right_on=col_right)
    merged_df.to_csv("merged_"+file_name_2,index = False)

print("initing search data structure")
lookup = init_search()
combine_csv("weather_stations_lat_long.csv","daily_coastal_2000_2023_weather.csv","id","station_id")
print("anotating file")
anotate_file("merged_daily_coastal_2000_2023_weather.csv","latitude", "longitude",.5,-.5,50000,20, True)

#anotate_file("obis.csv","decimallatitude","decimallongitude",.5,-.5,50000,20, True) 
#convert_coords("atlantic.csv", "Latitude", "Longitude")
#anotate_file("converted_atlantic.csv","Latitude", "Longitude",.5,-.5,50000,20, True)

