# Green for All LT : Urban Equity Index for Vilnius

**Duration**: October – December 2025  

---

## Overview

Our aim - analyze **access to green, cultural spaces and academic, health establishments** in the Lithuanian capital **Vilnius**. Using open data and spatial analysis, we will identify neighborhoods that lack sufficient access to these locations. Our outputs will support urban planning, public health and EU City goals.

---

## Data Sources

| Type | Source | Description | Access |
|------|--------|-----------|--------|
| **Live API (Mandatory)** | **OSMnx** | Parks, forests, gardens, educational, cultural and academic spaces |
| **Static** | **Statistics Lithuania**<br>([stat.gov.lt](https://stat.gov.lt)) | Population and density by *eldership* (seniūnija) | CSV |
| **Static** | **Vilnius Data Portal**<br>([vplanas.lt](https://zemelapiai.vplanas.lt/)) | Official administrative boundaries (elderships) | GeoJSON/ |
| **xGreen Space Reference** | **WHO / Eurostat** | Benchmark: ≥0.5 ha green space per 1,000 residents | Public guidelines |

> 🔍 **Note**: All data is publicly available and compliant with open data licenses.

---

## Tech Stack

- **Languages**: Python (primary)
- **Core Libraries**:  
  - `geopandas`, `shapely` → spatial data  
  - `osmnx` → OSM network + POI extraction  
  - `pandas`, `numpy` → data processing  
  - `scikit-learn` → clustering/modeling
  - `folium` / `plotly` / `streamlit` → visualization & dashboard
- **Tools**: Jupyter Notebook, GitHub, VS Code
- **Output Format**: Interactive web app + static report

---

## Methodology

1. **Define study area**: Vilnius city (elderships as analysis units).
2. **Extract green spaces**: Use OSMnx to pull all parks/forests within city limits.
3. **Calculate accessibility**:
   - For each residential centroid (or grid cell), compute **walking distance** to nearest green space using OSM street network.
   - Compute **green area per capita** per eldership.
4. **Merge with demographics**: Join with income, age, and population density.
5. **Build composite score**:  
   `Green Access Score = (Accessible green area per capita) × (Proximity weight)`
6. **Identify priority zones**: Rank elderships; flag those with low score + high vulnerability.
7. **Visualize & communicate**: Interactive map + policy recommendations.

---

## Social Impact

- **Local relevance**: Addresses urban inequality in Lithuania using hyperlocal data.
- **Policy-ready**: Outputs can inform municipal green infrastructure investments.
- **EU alignment**: Supports **EU Green City Accord** and **Lithuania’s National Urban Policy**.

---

## Team Coordination

- Use **GitHub** for version control (create issues for each milestone).
- Store raw data in `/data/raw`, processed in `/data/processed`.
- Document everything in `README.md` and `docs/`.

---
