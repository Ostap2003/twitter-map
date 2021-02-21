""" Module that generates map (HTML page) with Twitter friends' locations """

import folium
from folium.plugins import MarkerCluster

def generate_map(locations: dict):
    """
    Generates HTML page with map
    The markers are users that given user is followig on Twitter
    """
    usr_map = folium.Map(tiles='cartodbdark_matter', zoom_start=30, min_zoom=1)

    layer = MarkerCluster(name='Friends', )

    for user in locations:
        location = locations[user]

        html = f'''
                <div>
                <b>{user}</b>
                </div>
                '''

        layer.add_child(folium.Marker(location=location,
                                   popup=html,
                                   icon=folium.Icon(icon='glyphicon glyphicon-map-marker',
                                                    color='blue')))

    usr_map.add_child(layer)
    return usr_map._repr_html_()
