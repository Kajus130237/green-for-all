import geopandas as gpd

edu = gpd.read_file("data/raw/education_spaces_vilnius.geojson")

# Filter to keep schools and kindergartens, universities are city wide
edu_filtered = edu[
    edu['amenity'].isin(['school', 'kindergarten'])
].copy()


edu_clean = edu_filtered[edu_filtered.geometry.is_valid].copy()

print(f"Education: {len(edu_clean)} facilities kept")

edu_clean.to_file("data/processed/education_vilnius_cleaned.geojson", driver="GeoJSON")