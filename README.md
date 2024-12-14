# Euros 2024 Shots Map

This Streamlit app visualizes and compares shots taken by players during the Euros 2024 tournament. It provides three types of plots to analyze shot data:

<details>
  <summary>1. Shot Map</summary>

  Displays shot locations on a pitch map with varying sizes for expected goals (xG) and colors indicating goals or misses.
  
  eg : ![image](https://github.com/user-attachments/assets/eaf8fd94-27a9-4a0e-96a0-67a828ee90eb)
  
</details>

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<details>
  <summary>2. Bar Chart</summary>

  Compares the number of shots taken by each player in a selected nation.
  
  eg : ![image](https://github.com/user-attachments/assets/ae7771e6-d6d8-44fa-9fa2-507262fec660)
  
</details>

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<details>
  <summary>3. Heatmap</summary>

  Shows the density of shots across different areas of the pitch.
  
  eg : ![image](https://github.com/user-attachments/assets/412ea47f-f9db-49c7-be83-de74aa617c6f)
  
</details>

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Files

- `euros_2024_shot_map.csv`: Contains detailed shot data including player information, shot location, and outcomes.
- `main.py`: The Streamlit application script that loads data, allows user interaction, and generates visualizations based on selected filters.

To run the app, ensure you have the necessary libraries installed and execute `streamlit run main.py`.
Docker command to run this project : docker run -p 8501:8501 abhishekdocks/euros-2024-shotsmap:latest.
