import osmnx as ox
import argparse
import os

def fetch_education_spaces(city: str):
    print(f"🌍 Fetching health spaces for {city}, Lithuania...")
    
   
    # src/data/fetch_healthcare.py
    tags = {
        "amenity": ["hospital", "clinic", "doctors", "pharmacy"]
    }
    
    try:
        # Fetch geodata from OpenStreetMap
        gdf = ox.features_from_place(f"{city}, Lithuania", tags=tags)
        
        # Ensure output directory exists
        output_dir = "data/raw"
        os.makedirs(output_dir, exist_ok=True)
        
        # Save to GeoJSON
        filename = f"health_spaces_{city.lower()}.geojson"
        filepath = os.path.join(output_dir, filename)
        gdf.to_file(filepath, driver="GeoJSON")
        
        print(f"✅ Success! Saved {len(gdf)} health features to {filepath}")
        return filepath
        
    except Exception as e:
        print(f"❌ Error fetching data for {city}: {e}")
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch health spaces from OpenStreetMap")
    parser.add_argument("--city", type=str, default="Vilnius", 
                        help="City name (e.g., Vilnius, Kaunas, Klaipeda)")
    args = parser.parse_args()
    
    fetch_education_spaces(args.city)