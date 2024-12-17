import geopandas as gpd
import matplotlib.pyplot as plt
import folium
import pandas as pd


# Load the shapefile
shapefile_path = "pathToShapefile.shp"
shapefile_path = "./data/BOEM_Wind_Leases_06_06_2024.shp"

gdf = gpd.read_file(shapefile_path)

# Display basic info about the data
print(gdf.head())
print(gdf.crs)  # Check the coordinate reference system

gdf = gdf[gdf.geometry.notnull()]  # Remove rows with missing geometries

if gdf.crs != "EPSG:4326":
    # Convert to WGS84 if not already in that format
    gdf = gdf.to_crs("EPSG:4326")


# data from csv

solar_data_path = './data/uspvdb_v2_0_20240801.csv'
solar_data = pd.read_csv(solar_data_path)

print(solar_data.columns)

gdf_solar = gpd.GeoDataFrame(
    solar_data, geometry=gpd.points_from_xy(solar_data['xlong'], solar_data['ylat']))


if gdf_solar.crs is None:
    gdf_solar = gdf_solar.set_crs(epsg=4326)

print(gdf_solar.crs)



### Interactive Map with Folium

centroid = gdf.geometry.centroid
map_center_lat = centroid.y.mean()
map_center_lon = centroid.x.mean()


# Define a style function for points
def point_style_function(feature):
    return {
        'fillColor': 'yellow',
        'color': 'orange',
        'weight': 1,
        'radius': 6,  # Adjust point size
        'fillOpacity': 0.8
    }



# Define a style function for polygons
def style_function(feature):
    properties = feature.get("properties", {})
    value = properties.get("LEASE_TYPE", "default")
    color_map = {
        "Easement": "blue",
        "Right-of-Way": "green",
        "Commercial": "red",
        "Research": "purple"
    }
    return {
        "fillColor": color_map.get(value, "gray"),
        "color": "black",
        "weight": 2,
        "fillOpacity": 0.5
    }

# Add a layer for solar sites
solar_layer = folium.FeatureGroup(name="Solar Project Sites")

# Add points as CircleMarkers
for _, row in gdf_solar.iterrows():
    folium.CircleMarker(
        location=[row.geometry.y, row.geometry.x],  # Extract point coordinates
        radius=6,  # Adjust the size of the point marker
        color='orange',  # Outline color
        fill=True,
        fill_color='yellow',  # Fill color
        fill_opacity=0.8,
        popup=f"Project: {row['project_name']}" if 'project_name' in row else "Solar Project"
    ).add_to(solar_layer)

# Create a Folium map centered on the data
m = folium.Map(location=[map_center_lat, map_center_lon], zoom_start=6)

# Add polygons to the map
folium.GeoJson(
        data=gdf.to_json(),
        style_function=style_function,
        tooltip=folium.GeoJsonTooltip(fields=["LEASE_NUMB", "LEASE_TYPE"]),
        popup=folium.GeoJsonPopup(fields=["LEASE_NUMB", "LEASE_TYPE"]),
        name="Wind Leases"
    ).add_to(m)

solar_layer.add_to(m)


# Save map to an HTML file (optional)
m.save("interactive_map.html")


