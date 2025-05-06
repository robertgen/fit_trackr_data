FitTrackr Data Processing and Analysis
This project involves preprocessing and analyzing user activity data from the FitTrackr application to extract insights that can inform business and marketing decisions.

Files Overview
dataprocessing.py
This module contains functions to clean and prepare the raw data:
- convert_to_numeric(df): Extracts numeric values from text fields like "30 min" or "120 kcal" and converts them to integers.
- data_standardatization(df): Standardizes activity names (e.g., "swim", "swimm" → "swimming") to ensure consistency.
- deduplicated_data(df): Removes duplicate and incomplete rows (i.e., containing NaN values).
- prepare_data(df): A pipeline that applies all the steps above to prepare the data for analysis.

finalproject_popescu_robert_stefan.py
This script:
1. Loads the dataset (fit_trackr_data.csv)
2. Cleans it using prepare_data() from the dataprocessing module
3. Performs multiple analyses, including:
   - Average activity duration
   - Most frequent activity and mood
   - Calorie variation by activity type
   - Age distribution comparison
   - Activity types most associated with happiness
   - Whether longer activity duration correlates with better mood

All outputs are printed to the console, and the cleaned dataset is saved back to fit_trackr_data.csv.

How to Run
1. Ensure both .py files and fit_trackr_data.csv are in the same directory.
2. Run the main script:
   python finalproject_popescu_robert_stefan.py
3. The results will be displayed in the terminal, and the cleaned CSV will be updated.

Requirements
- Python 3.x
- pandas

You can install pandas via:
   pip install pandas
