import folium

m = folium.Map(location=[28.6139, 77.2090], zoom_start=5)  # India

map_id = m.get_name()

js = f"""
<script>
function reverseGeocode(lat, lng) {{
    let url = `https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat=${{lat}}&lon=${{lng}}`;
    fetch(url)
        .then(response => response.json())
        .then(data => {{
            let address = data.display_name || "No address found";
            let marker = L.marker([lat, lng]).addTo({map_id});
            marker.bindPopup("<b>Address:</b><br>" + address).openPopup();
        }})
        .catch(error => {{
            alert("Geocoding failed.");
        }});
}}

{map_id}.on('click', function(e) {{
    let lat = e.latlng.lat;
    let lng = e.latlng.lng;
    reverseGeocode(lat, lng);
}});
</script>
"""

m.get_root().html.add_child(folium.Element(js))
m.save("clickable_map.html")
