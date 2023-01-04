"""
    Made By: Marwan Alhindi
    Created On: 27 July 2022
    From: Python Crash Course
    This file purpose was to learn how to import,read and write json files. You learned how to extract specific information from json data type. Since they are usually nested lists and dictionaries, you need to use for loop to extract each object and then use object['key'] to get a specific value you want.

    The Data Visualization project starts in Chapter 15, in which you'll learn to generate data and create a series of functional and beautiful visualizations of that data using Matplotlib and Plotly. Chapter 16 teaches you to access data from online sources and feed it into a visualization package to create plots of weather data and a map of global earthquake activity. Finally, Chapter 17 shows you how to write a program to automatically download and visualize data. Learning to make visualizations allows you to explore the field of data mining, which is a highly sought-after skill in the world today.
"""
import json
from plotly.graph_objects import Scattergeo, Layout
from plotly import offline

#opening world json data type
filename= 'data/eq_data_30_day_m1.json'
with open(filename) as f:
    content= json.load(f)
#writing a more formated json file of the same data that has been opened
filename= 'data/formated_data.json'
with open(filename,'w') as f:
    json.dump(content,f,indent=4)

#extracting just the earthquakes features
all_earthquakes= content['features']

#writing to a new json file all the earthquake features
filename= 'data/eathquake_features.json'
with open(filename,'w') as f:
    json.dump(all_earthquakes,f,indent=4)

#extracing all the magnitude of each earthquake
mags= []
for object in all_earthquakes:
    single_mag= object["properties"]["mag"]
    mags.append(single_mag)

#extracting longtitude and latitude of each earthquake
longitude,latitude,hover_texts= [],[],[]
for object in all_earthquakes:
    each_coordinate= object["geometry"]["coordinates"]
    each_latitude= each_coordinate[0]
    each_longitude= each_coordinate[1]
    latitude.append(each_latitude)
    longitude.append(each_longitude)
    title = object['properties']['title']
    hover_texts.append(title)

#you can either plot and represent the data this way:
# data = [Scattergeo(lon=longitude, lat=latitude)]
#or this way:
plotted_data= [{
    'type':'scattergeo',
    'lon':longitude,
    'lat':latitude,
    'text': hover_texts,
    'marker':{
        'size':[5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    }
}]
my_layout= Layout(title='Global earthquake magnitude')
fig= {'data':plotted_data,'layout':my_layout}
offline.plot(fig,filename= 'data/Earthquake_data.png')