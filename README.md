# Generating Geographical Heatmap Project

## BrainyBeam Internship Submission

**Author**: \Pawan Kumar Barnawal
**Date**: August 24, 2025

This project creates a continuous temperature heatmap using the `Basemap` library. The code generates a sample dataset to simulate temperature variations.

## Requirements

- Python 3.9
- Conda environment manager

## Installation

1. Clone or download this repository.
2. Navigate to the project directory:

   ```bash
   cd Generating_Geographical_Heatmap
   ```
3. Create the Conda environment:

   ```bash
   conda env create -f environment.yml
   ```
4. Activate the environment:

   ```bash
   conda activate heatmap_env
   ```

## Usage

1. Run the main script:

   ```bash
   python src/app.py
   ```
2. Check the output file `output/basemap_heatmap.png` in the project directory.

## Project Structure

```
generating-geographical-heatmap/
├── src/
│   └── app.py               # Directory contain main Python script
├── environment.yml     # Conda environment configuration file
├── README.md          # Project documentation
├── report/
│   └── Task_1_Report.docx        # Report of the project
└── output/
   └── basemap_heatmap.png     # Geographical Headmap

```
## Notes

- The script uses a fixed random seed for reproducibility.
- If `basemap` installation fails, use the fallback: `conda install geos proj4` followed by `pip install basemap==1.2.2`.

### Contact
For questions or issues, contact at connectspawan@gmail.com.
