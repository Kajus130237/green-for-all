import geopandas as gpd

health = gpd.read_file("data/raw/health_spaces_vilnius.geojson")


health_filtered = health[
    health['amenity'].isin(['hospital', 'clinic', 'doctors'])
].copy()


health_clean = health_filtered[health_filtered.geometry.is_valid].copy()

print(f"Healthcare: {len(health_clean)} facilities kept")

health_clean.to_file("data/processed/health_vilnius_cleaned.geojson", driver="GeoJSON")