# KML Path Extractor 📍✨

## Overview

Welcome to the **KML Path Extractor**, your go-to Python script for transforming KML path data into an organized Excel sheet! This tool is perfect for engineers, researchers, and geospatial enthusiasts who want to analyze geographic paths with ease.

## Features 🚀

- **Extract Path Information**: Efficiently parses KML files to retrieve essential path data.
- **Distance Calculation**: Calculates the total route distance between coordinates using geodesic measurements.
- **Excel Output**: Exports data into a structured Excel sheet, making it easy to review and share.

## How It Works 🔍

1. **Parse the KML File**: The script reads the KML file structure to find paths.
2. **Extract Coordinates**: It gathers coordinates and computes the distance of each path.
3. **Export to Excel**: The data is then neatly formatted into an Excel file for your convenience.

## Requirements 📋

To run this script, ensure you have the following installed:

- Python 3.x
- `pandas` library
- `geopy` library (install via `pip install geopy`)

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

6. Find your output Excel file named `extracted_paths_with_total_distance.xlsx` ready for analysis!

## Sample Output 📋

Here's a sneak peek at what the resulting Excel sheet will look like:

| Path Name       | Start Latitude | Start Longitude | End Latitude | End Longitude | Route Distance (km) |
|------------------|----------------|------------------|--------------|----------------|----------------------|
| My Path          | 37.422         | -122.084         | 37.424       | -122.086       | 0.2                  |
| Scenic Route     | 37.420         | -122.083         | 37.425       | -122.087       | 0.5                  |
| Coastal Path     | 37.415         | -122.081         | 37.430       | -122.090       | 1.2                  |

## Example KML Input

The script works with KML files like the following example:

```xml
<kml xmlns="http://www.opengis.net/kml/2.2">
  <Placemark>
    <name>My Path</name>
    <LineString>
      <coordinates>
        -122.084,37.422,0
        -122.086,37.424,0
      </coordinates>
    </LineString>
  </Placemark>
</kml>
```

## Contributing 🤝

We welcome contributions! If you have ideas for improvements, bug fixes, or features, please submit a pull request.

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments 🎉

- Special thanks to the creators of the `geopy` and `pandas` libraries for their invaluable contributions!
- Inspired by the collaborative spirit of the Python community!

---

Feel free to adapt any sections or add your own flair! This format includes a sample output table to illustrate the data extracted and calculated by your script.
