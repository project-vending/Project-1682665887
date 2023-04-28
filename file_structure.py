
import os

# Define the project directory
project_dir = "Developing Analytical Reports with Tableau and Power BI"

# Define the top-level directories
data_dir = os.path.join(project_dir, "data")
reports_dir = os.path.join(project_dir, "reports")

# Create the top-level directories
os.makedirs(data_dir, exist_ok=True)
os.makedirs(reports_dir, exist_ok=True)

# Define the subdirectories within the data directory
raw_data_dir = os.path.join(data_dir, "raw")
processed_data_dir = os.path.join(data_dir, "processed")

# Create the subdirectories within the data directory
os.makedirs(raw_data_dir, exist_ok=True)
os.makedirs(processed_data_dir, exist_ok=True)

# Define the names of the empty files to create
raw_data_file = "raw_data.csv"
processed_data_file = "processed_data.csv"
dashboard_file = "dashboard.twb"

# Create the empty files
open(os.path.join(raw_data_dir, raw_data_file), "a").close()
open(os.path.join(processed_data_dir, processed_data_file), "a").close()
open(os.path.join(reports_dir, dashboard_file), "a").close()
