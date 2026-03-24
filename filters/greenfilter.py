import geopandas as gpd

green = gpd.read_file("data/raw/green_spaces_vilnius.geojson")

# Filter Keep only polygon (ignore points like)
green_polygons = green[green.geometry.type == 'Polygon'].copy()
green_polygons = green_polygons[green_polygons.geometry.is_valid].copy()

# Metric system (EPSG:3035)
green_polygons_metric = green_polygons.to_crs(epsg=3035)

# Area in square meters and hectares
green_polygons_metric['area_m2'] = green_polygons_metric.geometry.area
green_polygons_metric['area_ha'] = green_polygons_metric['area_m2'] / 10000

print(f"Green spaces: {len(green_polygons_metric)} polygons kept")

green_polygons_metric.to_file("data/processed/green_vilnius_cleaned.geojson", driver="GeoJSON")
