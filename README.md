# KML Path Extractor 📍

## Overview

Welcome to the **KML Path Extractor**, a Python script designed to seamlessly extract path data from KML files and convert it into a user-friendly Excel format. Whether you're a civil engineer, a data analyst, or just someone curious about geographic data, this tool will help you visualize your paths with calculated distances!

## Features 🚀

- **Path Extraction**: Parse KML files to extract path names, start and end coordinates.
- **Distance Calculation**: Automatically calculate the total route distance between points using the geodesic method.
- **Excel Output**: Export the extracted data into a neatly formatted Excel sheet for easy analysis and sharing.

## Requirements 📋

To run this script, ensure you have the following installed:

- Python 3.x
- `pandas` library
- `geopy` library (install via `pip install geopy`)

## How It Works 🔍

The script parses KML files to extract the following information for each path:

- **Path Name**
- **Start Latitude**
- **Start Longitude**
- **End Latitude**
- **End Longitude**
- **Route Distance (km)**

### Workflow

1. **Parse the KML File**: The script uses `xml.etree.ElementTree` to parse the KML structure.
2. **Extract Coordinates**: For each path, it extracts all coordinates and calculates the total distance.
3. **Export to Excel**: Finally, the extracted data is saved into an Excel file using `pandas`.

## Usage 📊

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/KML-Path-Extractor.git
   ```

2. Change directory into the project folder:

   ```bash
   cd KML-Path-Extractor
   ```

3. Install the required packages if you haven't done so:

   ```bash
   pip install pandas geopy openpyxl
   ```

4. Update the script with your KML file path:

   ```python
   kml_file = "your kml path"  # Replace with your KML file path
   output_excel = 'extracted_paths_with_total_distance.xlsx'
   ```

5. Run the script:

   ```bash
   python kml_path_extractor.py
   ```

6. Check the output Excel file named `extracted_paths_with_total_distance.xlsx` for your path data!

## Example Input

Here's an example of how your KML file might look:

```xml
<kml xmlns="http://www.opengis.net/kml/2.2">
  <Placemark>
    <name>My Path</name>
    <LineString>
      <coordinates>
        -122.084,37.422,0
        -122.085,37.423,0
        -122.086,37.424,0
      </coordinates>
    </LineString>
  </Placemark>
</kml>
```

## Contributing 🤝

If you'd like to contribute to this project, feel free to submit a pull request! Your enhancements, bug fixes, and suggestions are always welcome.

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments 🎉

- Thanks to the creators of the `geopy` and `pandas` libraries for their incredible work!
- Inspiration and help from the Python community!

---

Feel free to modify any sections or add more details as needed!
