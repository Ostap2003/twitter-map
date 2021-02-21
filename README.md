# Twitter-friends-map-project
### What is it?
This is **Flask** project that uses **Twitter API** to get spesific user's friends list (in .json format). The user should enter random Twitter's user nickname and then the map with friends' locations _(each friend is a separate marker on the map)_ will be generated as a separate page. If the input is invalid, then the user will be warned that his/her input is invalid. The map is generated with the help of **Folium**.

The app is currently hosted on [pythonanywhere](https://www.pythonanywhere.com/) platform.<br>
**Here is a link to the web-app: http://optd.pythonanywhere.com/**
<hr>

### Modules:
- **application.py** is the main module.
- **get_location.py** gets information about the given user friends (location, Twitter nickname)
- **map_generator.py** module that generates a map (HTML page) with friends' locations
