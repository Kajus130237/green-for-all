"""
Fetch green spaces (parks, forests, natural areas) from OpenStreetMap 
for a Lithuanian city. Saves to data/raw/green_spaces_{city}.geojson
"""

import osmnx as ox
import argparse
import os

def fetch_green_spaces(city: str):
    print(f"🌍 Fetching green spaces for {city}, Lithuania...")
    
    # Define OSM tags for green areas
    tags = {
        "leisure": "park",
        "landuse": ["forest", "grass"],
        "natural": ["wood", "tree"]
    }
    
    try:
        # Fetch geodata from OpenStreetMap
        gdf = ox.features_from_place(f"{city}, Lithuania", tags=tags)
        
        # Ensure output directory exists
        output_dir = "data/raw"
        os.makedirs(output_dir, exist_ok=True)
        
        # Save to GeoJSON
        filename = f"green_spaces_{city.lower()}.geojson"
        filepath = os.path.join(output_dir, filename)
        gdf.to_file(filepath, driver="GeoJSON")
        
        print(f"✅ Success! Saved {len(gdf)} green features to {filepath}")
        return filepath
        
    except Exception as e:
        print(f"❌ Error fetching data for {city}: {e}")
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch green spaces from OpenStreetMap")
    parser.add_argument("--city", type=str, default="Vilnius", 
                        help="City name (e.g., Vilnius, Kaunas, Klaipeda)")
    args = parser.parse_args()
    
    fetch_green_spaces(args.city)