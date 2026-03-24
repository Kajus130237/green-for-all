import geopandas as gpd

culture = gpd.read_file("data/raw/culture_spaces_vilnius.geojson")

# Filter
culture_filtered = culture[
    culture['amenity'].isin(['library', 'theatre', 'cinema', 'museum']) |
    (culture['tourism'] == 'museum')
].copy()

culture_clean = culture_filtered[culture_filtered.geometry.is_valid].copy()

print(f"Culture: {len(culture_clean)} venues kept")

culture_clean.to_file("data/processed/culture_vilnius_cleaned.geojson", driver="GeoJSON")