import streamlit as st
import pandas as pd
import json
import matplotlib.pyplot as plt
from mplsoccer import VerticalPitch
import seaborn as sns

st.title("Euros 2024 Shot Map")
st.subheader("Compare shots taken by players from different nations!")

# Load and preprocess data
df = pd.read_csv('euros_2024_shot_map.csv')
df = df[df['type'] == 'Shot'].reset_index(drop=True)
df['location'] = df['location'].apply(json.loads)

def filter_data(df: pd.DataFrame, team: str, player: str):
    if team:
        df = df[df['team'] == team]
    if player:
        df = df[df['player'] == player]
    return df

def plot_shots(df, ax, pitch):
    for x in df.to_dict(orient='records'):
        pitch.scatter(
            x=float(x['location'][0]),
            y=float(x['location'][1]),
            ax=ax,
            s=1000 * x['shot_statsbomb_xg'],
            color='blue' if x['shot_outcome'] == 'Goal' else 'red',
            edgecolors='black',
            alpha=1 if x['shot_outcome'] == 'Goal' else .5,
            zorder=2 if x['shot_outcome'] == 'Goal' else 1
        )

# Select the plot type
plot_type = st.selectbox("Select the type of plot", ["Shot Map", "Bar Chart", "Heatmap"])

# Select nation and player
nation = st.selectbox("Select a nation", df['team'].sort_values().unique())
players = df[df['team'] == nation]['player'].sort_values().unique()
player = st.selectbox("Select a player", players)

# Filter data
filtered_df = filter_data(df, nation, player)

if plot_type == "Shot Map":
    # Create the pitch with classic colors
    pitch = VerticalPitch(
        pitch_type='statsbomb',
        pitch_color='green',
        line_color='white',
        line_zorder=2,
        half=True
    )
    fig, ax = pitch.draw(figsize=(10, 10))
    plot_shots(filtered_df, ax, pitch)
    st.pyplot(fig)

elif plot_type == "Bar Chart":
    # Prepare data for bar chart
    player_shots = df[df['team'] == nation].groupby('player').size().reset_index(name='shots')
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.barplot(data=player_shots, x='player', y='shots', ax=ax, palette='viridis')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
    ax.set_title(f"Shots per Player for {nation}")
    st.pyplot(fig)

elif plot_type == "Heatmap":
    # Prepare data for heatmap
    heatmap_data = df[df['team'] == nation].copy()
    heatmap_data['x'] = heatmap_data['location'].apply(lambda loc: loc[0])
    heatmap_data['y'] = heatmap_data['location'].apply(lambda loc: loc[1])
    fig, ax = plt.subplots(figsize=(12, 8))
    heatmap_pivot = heatmap_data.pivot_table(index='y', columns='x', values='shot_statsbomb_xg', aggfunc='sum', fill_value=0)
    sns.heatmap(heatmap_pivot, cmap='viridis', ax=ax, cbar=True)
    ax.set_title(f"Shot Density Heatmap for {nation}")
    st.pyplot(fig)

# Add color labels and explanation
st.write("### Color Legend")
st.markdown('<span style="color:blue;">● Goal</span>', unsafe_allow_html=True)
st.markdown('<span style="color:red;">● No Goal</span>', unsafe_allow_html=True)

st.write("### Explanation")
st.write("In the Shot Map, the size of the dots represents the expected goals (xG). In the Bar Chart, the height of the bars shows the number of shots taken by each player. In the Heatmap, the color intensity indicates the density of shots in different areas of the pitch.")
