# Euros 2024 Shots Map

This Streamlit app visualizes and compares shots taken by players during the Euros 2024 tournament. It provides three types of plots to analyze shot data:

1. **Shot Map**: Displays shot locations on a pitch map with varying sizes for expected goals (xG) and colors indicating goals or misses.
   eg : ![image](https://github.com/user-attachments/assets/eaf8fd94-27a9-4a0e-96a0-67a828ee90eb)
   -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

2. **Bar Chart**: Compares the number of shots taken by each player in a selected nation.
   eg : ![image](https://github.com/user-attachments/assets/ae7771e6-d6d8-44fa-9fa2-507262fec660)
   -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

3. **Heatmap**: Shows the density of shots across different areas of the pitch.
   eg : ![image](https://github.com/user-attachments/assets/412ea47f-f9db-49c7-be83-de74aa617c6f)
   -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------


## Files

- `euros_2024_shot_map.csv`: Contains detailed shot data including player information, shot location, and outcomes.
- `main.py`: The Streamlit application script that loads data, allows user interaction, and generates visualizations based on selected filters.

To run the app, ensure you have the necessary libraries installed and execute `streamlit run app.py`.
