# Talking Data Analysis | [![Athena Award Badge](https://img.shields.io/endpoint?url=https%3A%2F%2Faward.athena.hackclub.com%2Fapi%2Fbadge)](https://award.athena.hackclub.com?utm_source=readme)

A data analysis project analyzing romance movies from the Rotten Tomatoes dataset, comparing favorite movies against genre statistics and visualizing trends.

## Overview

This project analyzes movie ratings data to understand how a favorite romance movie compares against other films in the same genre using statistical measures and data visualizations.

## Features

- **Data Loading**: Reads and processes Rotten Tomatoes movie dataset
- **Genre Filtering**: Filters movies by genre (Romance)
- **Statistical Analysis**: Calculates min, max, mean, and median ratings
- **Data Visualizations**: 
  - Histogram showing distribution of audience ratings
  - Scatter plot comparing audience vs critic ratings
- **Interactive Graphs**: Matplotlib visualizations with proper labels and grids

## Installation

### Prerequisites
- Python 3.x
- Required packages:
  - pandas
  - matplotlib

### Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd GWC
   ```

2. **Install dependencies**
   ```bash
   pip install pandas matplotlib
   ```

3. **Download the dataset**
   - Ensure `rotten_tomatoes_movies.csv` is in the same directory as the script
   - The dataset should be available or downloaded separately

4. **Run the program**
   ```bash
   python "Talking Data Starter Code.py"
   ```

## Usage

1. The program will load the Rotten Tomatoes movie dataset
2. It will analyze romance movies and display statistics about audience ratings
3. Follow the on-screen prompts to view data visualizations
4. Close each graph window to proceed to the next visualization

## Building an Executable

To create a standalone executable for Windows:

1. **Install PyInstaller** (if not already installed)
   ```bash
   pip install pyinstaller
   ```

2. **Build the executable**
   ```bash
   python -m PyInstaller --onefile --name "TalkingDataAnalysis" "Talking Data Starter Code.py"
   ```

   The executable will be created in the `dist` folder.

## Analysis Details

The program analyzes:
- **Minimum/Maximum ratings** in the romance genre
- **Mean and median** ratings for comparison
- **Visual distribution** of ratings via histogram
- **Correlation** between audience and critic ratings

## Data Source

- Rotten Tomatoes Movies Dataset
- Contains movie titles, genres, audience ratings, and critic ratings

## Technologies Used

- Python
- pandas (DataFrame manipulation)
- matplotlib (Visualizations)

## Author

Girls Who Code Project

## License

This project is part of a Girls Who Code educational program.
