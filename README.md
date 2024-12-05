# Info_viz_movies

To Run
```bash 
streamlit run streamlit_app.py --server.enableCORS false --server.enableXsrfProtection false
```
* only run once

Update UI when you make changes to code: ctrl/cmd + R

# InfoViz Project Visualization

This repository contains the **InfoViz Project Visualization** code, which creates interactive visualizations to analyze trends in the movie industry using the IMDb dataset. These visualizations include:

1. **Choropleth Map of Global Movie Revenue**: Displays the distribution of movie revenues across countries.
2. **Animated Choropleth Map**: Visualizes year-wise movie revenue trends across the globe.
3. **Box Plot of IMDb Ratings by Country**: Explores IMDb rating distributions for movies from different countries.

## Requirements
To run this project, ensure you have the following installed:

- Python 3.7+
- Libraries:
  - `plotly`
  - `pandas`
  - `numpy`
  - `matplotlib`
  - `geopandas`
  - `nbformat`
  - `jupyter`

Install the required libraries using the following command:
```bash
pip install plotly pandas numpy matplotlib geopandas jupyter
```

## How to Run
Follow these steps to run the visualization:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/<your-username>/InfoViz_Project_Visualization.git
   cd InfoViz_Project_Visualization
   ```

2. **Upload Dataset**:
   - Add the IMDb dataset (`imdb_data.csv` or the relevant dataset) to the google drive directory.

3. **Open Google Colab**:
   - Upload the `InfoViz_Project_Visualization.ipynb` file to Google Colab.

4. **Run the Notebook**:
   - Open the `.ipynb` file in Google Colab.
   - Ensure the dataset is uploaded to the same directory as the notebook.
   - Execute all cells sequentially to generate the visualizations.

