# you will need to install folium via pip

neighborhoods = ['Palermo', 'Ricoleta', 'Santelmo', 'Puerto Madero', 'Belgrano', 'La Boca']

palermo = neighborhoods[0]

la_boca = neighborhoods[-1]

coordinates = [-34.6037, -58.3816]

ba_latitude = coordinates[0]  # to assign latitude, the first item in coordinates
ba_longitude = coordinates[1]


import folium
buenos_map = folium.Map([ba_latitude, ba_longitude])
buenos_map

'''Folium is a mapping library built on Python. 
We created a representation of a map, by referencing the folium.Map function and passing through a list. 
That list represents the latitude and longitude, just like we saw previously. 
The map object is stored as the variable buenos. Since buenos_map is the last line of a cell, the map is displayed
'''

#adding a marker to the map
# start by adding a marker for the Buenos Aires coordinates
buenos_marker = folium.Marker([ba_latitude, ba_longitude])
buenos_marker.add_to(buenos_map)

''' So we used the folium library to create a marker. We specified the coordinates 
of the marker as a list. Finally, we added the marker to our map with the add_to function.
'''

# check the updated map
buenos_map

# NOTE: both map object and map marker are stored as variables
buenos_marker

# we can also generate them as a list
buenos_markers = [buenos_marker]

#set the coordinates for all the neighborhoods
neighborhoods = ['Palermo', 'Ricoleta', 'Santelmo', 'Puerto Madero', 'Belgrano', 'La Boca']
marker_one = folium.Marker([-34.5711, -58.4233])
marker_two = folium.Marker([-34.5895, -58.3974])
marker_three = folium.Marker([-34.6212, -58.3731])
marker_four = folium.Marker([-34.6177, -58.3621])
marker_five = folium.Marker([-34.603722,  -58.381592])
marker_six = folium.Marker([-34.6345, -58.3631])
neighborhood_markers = [marker_one, marker_two, marker_three, marker_four, marker_five, marker_six]

la_boca_marker = folium.Marker([-34.6345, -58.3631])

# Then we rewrite the buenos_map variable and add the la_boca_marker to the map and zoom in using the zoom_start attribute
import folium
buenos_map = folium.Map([ba_latitude, ba_longitude], zoom_start = 12)
la_boca_marker.add_to(buenos_map)
buenos_map


