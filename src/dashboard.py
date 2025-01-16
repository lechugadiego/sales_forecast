import streamlit as st
from analysis import load_and_analyze_data

def main():
    st.title('Sales Performance Dashboard')
    
    # Load data and create visualizations
    summary_stats, fig = load_and_analyze_data()
    
    # Display statistics
    st.subheader('Product Performance Statistics')
    st.dataframe(summary_stats)
    
    # Display visualization
    st.plotly_chart(fig)

if __name__ == "__main__":
    main() 