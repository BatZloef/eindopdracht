import geojson
import folium
import webbrowser


class web:
    def get_html():
         
        with open('velo.geojson', 'r') as f:
            geo_data = geojson.load(f)
    
        map = folium.Map(location=[51.22977828979492, 4.417099952697754], zoom_start=13)
    
        folium.GeoJson(geo_data).add_to(map)
    
        for feature in geo_data['features']:
            coordinates = feature['geometry']['coordinates']
            longitude, latitude = coordinates[0], coordinates[1]
            name = feature['properties']['Naam']
            slots = feature['properties']['Aantal_plaatsen']
            melding = f"Naam: {name} \nAantal plaatsen: {slots}"
            marker = folium.Marker(location=[latitude, longitude], popup=melding)
            marker.add_to(map)
    
        map.save('map.html')
        webbrowser.open('map.html')
    

    get_html()