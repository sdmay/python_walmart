import folium
import pandas

# retrieve data using pandas to read the csv file
data = pandas.read_csv('1962_2006_walmart_store_openings.csv')
# print(data)
lat = list(data['LAT'])
lon = list(data['LON'])
open_date = list(data['OPENDATE'])
super_date = list(data['date_super'])
# print(super_date)

# color code the store location based on open date
def open_date_color(opendate):
    year = opendate[-2:]
    # print(year)
    y = int(year)
    if 15 < y < 70:
        return 'green'
    elif 70 < y < 80:
        return 'orange'
    elif 80 < y < 90:
        return 'red'
    elif 90 < y <= 99:
        return 'blue'
    elif 0 < y < 7:
        return 'yellow'

# set map location at center of US at nice zoom level to start
map = folium.Map(location=[36, -102], zoom_start=4, tiles='Mapbox Bright')

# set featured group for ease of extrapolation
# TO DO: set a feature group based on their opening date to add as layers
fg = folium.FeatureGroup('Supercenter')
fg60 = folium.FeatureGroup("1960's")
fg70 = folium.FeatureGroup("1970's")
fg80 = folium.FeatureGroup("1980's")
fg90 = folium.FeatureGroup("1990's")
fg00 = folium.FeatureGroup("2000's")


# loop and zip the info together and have it displayed on the map with a circle marker
for lt, ln, od in zip(lat, lon, open_date):
    year = str(od)[-2:]
    y = int(year)
    if 15 < y < 69:
        fg60.add_child(folium.CircleMarker(location=[lt, ln], radius=2, fill=True, fill_color=open_date_color(od), color=open_date_color(od)))
    elif 70 < y < 80:
        fg70.add_child(folium.CircleMarker(location=[lt, ln], radius=2, fill=True, fill_color=open_date_color(od), color=open_date_color(od)))
    elif 80 < y < 90:
        fg80.add_child(folium.CircleMarker(location=[lt, ln], radius=2, fill=True, fill_color=open_date_color(od), color=open_date_color(od)))
    elif 90 < y <= 99:
        fg90.add_child(folium.CircleMarker(location=[lt, ln], radius=2, fill=True, fill_color=open_date_color(od), color=open_date_color(od)))
    elif 0 < y < 7:
        fg00.add_child(folium.CircleMarker(location=[lt, ln], radius=2, fill=True, fill_color=open_date_color(od), color=open_date_color(od)))

# append child to map object
map.add_child(fg60)
map.add_child(fg70)
map.add_child(fg80)
map.add_child(fg90)
map.add_child(fg00)
map.add_child(folium.LayerControl())
# save map
map.save('supercenter.html')
