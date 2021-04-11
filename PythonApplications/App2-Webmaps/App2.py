import folium

location=[20.5937, 78.9629]
map= folium.Map(location, zoom_start=7)
fg=folium.FeatureGroup(name="My Map")

for i in [[19.249197,73.1412416], [20.249197,75.1412416]]:
    fg.add_child(folium.Marker(location=i, popup="Hello I'm Here", icon= folium.Icon(color="green")))
    fg.add_child(folium.CircleMarker(location=i, radius=8, popup="Hello I'm Here", color="Red"))

fgp=folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open("world.json", 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green'if x['properties']['POP2005']>20000000 else 'red'}))


map.add_child(fgp)
map.add_child(fg)
map.add_child(folium.LayerControl())
map.save("Map1.html")
