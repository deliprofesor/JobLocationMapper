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

pip install -r requirements.txt

## Running the Project

Clone the repository from GitHub:

- **git clone https://github.com/deliprofesor/JobLocationMapper.git**

After cloning, install the necessary dependencies:

- **pip install -r requirements.txt**

Prepare your job_dataset.csv file:

This file should contain necessary information about job listings, such as city, state, job titles, and other relevant data.

Run the job_locator.py script to generate the map:

- **python job_locator.py**

The map will be saved as india_job_location_map_with_categories.html. Open this file in a web browser to start exploring the job listings on the map.

## Usage
The project visualizes job listings on the map and categorizes them by profession:

Occupation Categories
Job listings are color-coded based on their occupation categories such as Software, Marketing, and Design. These colors help users easily identify different types of job opportunities:

Software (Developer) jobs are marked in blue
Marketing jobs are marked in green
Design jobs are marked in red
Job Listing Information
Clicking on a job listing on the map will display the job title and location information. Users can learn more about each job opportunity as they explore the map.

## Map Visualization
The map is designed to visualize job listings in India, but it can easily be adapted to display listings from other geographical regions.

## Contribution
If you'd like to contribute to this project, follow these steps:

Fork this repository on GitHub.
Add a new feature or fix a bug.
Submit a pull request with your changes.
If you have any questions, please feel free to reach out via the Issues section.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
