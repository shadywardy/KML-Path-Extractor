import xml.etree.ElementTree as ET
import pandas as pd
from geopy.distance import geodesic  # Requires geopy library

def extract_paths_from_kml(kml_file):
    # Parse the KML file
    tree = ET.parse(kml_file)
    root = tree.getroot()
    
    # Define the KML namespace
    namespaces = {'kml': 'http://www.opengis.net/kml/2.2'}
    
    # List to store path data
    paths = []
    
    # Loop through each Placemark in the KML file
    for placemark in root.findall('.//kml:Placemark', namespaces):
        name = placemark.find('kml:name', namespaces)
        name_text = name.text if name is not None else "Unnamed Path"
        
        # Find LineString element to get the path coordinates
        linestring = placemark.find('kml:LineString', namespaces)
        if linestring is not None:
            # Get coordinates text
            coordinates = linestring.find('kml:coordinates', namespaces).text.strip()
            # Split into coordinate pairs and remove empty items
            coord_pairs = [coord.strip() for coord in coordinates.split() if coord.strip()]
            
            # Extract all coordinates
            coords = [(float(coord.split(',')[1]), float(coord.split(',')[0])) for coord in coord_pairs]
            
            # Append path data to list
            paths.append({
                'Path Name': name_text,
                'Start Latitude': coords[0][0],
                'Start Longitude': coords[0][1],
                'End Latitude': coords[-1][0],
                'End Longitude': coords[-1][1],
                'Coordinates': coords  # Store all coordinates for distance calculation
            })
    
    return paths

def calculate_total_route_distance(coords):
    total_distance = 0.0
    for i in range(len(coords) - 1):
        total_distance += geodesic(coords[i], coords[i + 1]).kilometers
    return total_distance

def save_paths_to_excel(paths, output_file):
    # Convert path data to a pandas DataFrame
    df = pd.DataFrame(paths)
    
    # Calculate total route distance and add it as a new column
    df['Route Distance (km)'] = df['Coordinates'].apply(calculate_total_route_distance)
    
    # Write DataFrame to an Excel file
    df.drop(columns='Coordinates', inplace=True)  # Remove the Coordinates column from the output
    df.to_excel(output_file, index=False)
    print(f"Data saved to {output_file}")

# Input and output files
kml_file = "your kml path"  # Replace with your KML file path
output_excel = 'extracted_paths_with_total_distance.xlsx'

# Extract paths and save to Excel
paths = extract_paths_from_kml(kml_file)
save_paths_to_excel(paths, output_excel)
