# JobLocationMapper

![india2](https://github.com/user-attachments/assets/38c99525-f288-457b-9c5c-2c50f70fd3bb)

**JobLocationMapper** is a Python project that visualizes the geographical locations of job listings on a map. This tool visualizes job opportunities by mapping city and state information on an interactive map, making it more accessible and visually appealing. Additionally, each job listing is color-coded based on its occupation category, allowing users to easily distinguish between different fields of job opportunities.

## Features

- **Geographical Location Visualization**  
  Job listings are visualized on the map based on their city and state information. Each job listing is placed on the map at the correct geographical location.

- **Color-Coded Markers by Job Category**  
  Job listings are color-coded according to their occupation category:
  - **Software** jobs are marked with `blue`
  - **Marketing** jobs are marked with `green`
  - **Design** jobs are marked with `red`
  
- **Geocoding**  
  City and state information is converted into geographical coordinates (latitude, longitude) using a geocoding service, and placed on the map at the correct location.

- **Clustered Markers**  
  Job listings that appear in the same location are grouped together on the map, offering a more organized and cleaner appearance.

- **Interactive Map**  
  Users can click on markers on the map to view details such as job titles and location information.

## Requirements

To run this project, you'll need the following Python libraries:

- `pandas` : For data manipulation and processing
- `folium` : For map visualization
- `geopy` : For geocoding (location resolution)

### Install Dependencies

To install all the required Python libraries, run the following command:

```bash
pip install -r requirements.txt
