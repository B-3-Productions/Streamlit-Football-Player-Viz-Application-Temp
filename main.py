import streamlit as st
from utilities.utils import get_players_by_position, load_data
from visualizations.pizza_chart import create_pizza_chart
from visualizations.radar_chart import create_radar_chart
from visualizations.overall_rank import create_rank_visualization
from st_pages import show_pages_from_config

DATA_PATH = 'data/football_player_stats.csv'
show_pages_from_config()
st.set_page_config(
    page_title='Football Data Viz',
    page_icon='💹',
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title('Football Player Metrics Visualization')

with st.expander("Expand to view Pizza Chart", expanded=False):
    data_frame = load_data(DATA_PATH)
    position = st.selectbox('Select Playing Position:', data_frame['Primary Position'].unique(), index=0, key='pizza_positon')
    player_name = st.selectbox('Select Player:', get_players_by_position(data_frame, position), index=0, key='pizza_player')

    # Button to generate pizza chart
    if st.button('Generate Pizza Chart'):
        fig_pizza = create_pizza_chart(data_frame, player_name, position)
        if fig_pizza is not None:
            st.pyplot(fig_pizza)  # Display the pizza chart

with st.expander("Expand to view Radar Chart", expanded=False):
    data_frame = load_data(DATA_PATH)
    position = st.selectbox('Select Playing Position:', data_frame['Primary Position'].unique(), index=0, key='radar_positon')
    player_name = st.selectbox('Select Player:', get_players_by_position(data_frame, position), index=0, key='radar_player')

    # Button to generate pizza chart
    if st.button('Generate Radar Chart'):
        fig_radar = create_radar_chart(data_frame, player_name, position)
        if fig_radar is not None:
            st.pyplot(fig_radar)  # Display the pizza chart

with st.expander("Expand to view Player's Overall Rank", expanded=False):
    data_frame = load_data(DATA_PATH)
    league = st.selectbox('Select League:', ['DEFAULT'], index=0, key='overall_league')
    position = st.selectbox('Select Playing Position:', data_frame['Primary Position'].unique(), index=0, key='overall_position')
    player_name = st.selectbox('Select Player:', get_players_by_position(data_frame, position), index=0, key='overall_player')

    # Button to generate pizza chart
    if st.button('Computer Player Rank'):
        fig_roverall = create_rank_visualization(data_frame, league, player_name, position)
        if fig_roverall is not None:
            st.plotly_chart(fig_roverall,use_container_width=True)
