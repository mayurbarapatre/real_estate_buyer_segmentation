import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# -------------------------------
# Page Settings
# -------------------------------

st.set_page_config(
    page_title="Real Estate Market Intelligence",
    page_icon="🏠",
    layout="wide"
)


# -------------------------------
# Title
# -------------------------------

st.title("🏠 Real Estate Market Intelligence")

st.subheader(
    "Machine Learning Based Buyer Segmentation "
    "and Investment Profiling"
)

st.write(
    "This application helps analyze real estate "
    "buyers and their investment behavior."
)
try:
    df = pd.read_csv("clients.csv")
except FileNotFoundError:
    st.error("clients.csv file not found.")
    st.stop()
    

# -------------------------------
# Sidebar
# -------------------------------

st.sidebar.title("Navigation")

page = st.sidebar.selectbox(
    "Select Page",
    [
        "Dashboard",
        "Buyer Segmentation",
        "Investment Profiling",
        "Market Intelligence"
    ]
)


# -------------------------------
# Dashboard
# -------------------------------

if page == "Dashboard":

    st.header("📊 Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Buyers", len(df))

    with col2:
        st.metric("Total Properties", df["client_id"].nunique())

    with col3:
        st.metric("Total Records",df.shape[0])

    st.success(
        "Real Estate ML Dashboard is working successfully!"
    )


# -------------------------------
# Buyer Segmentation
# -------------------------------

elif page == "Buyer Segmentation":

    st.header("👥 Buyer Segmentation")

    st.write(
        "Select numeric features for analysis."
    )

    numeric_columns= df.select_dtypes(
        include="number").columns.tolist()
    
    if len(numeric_columns)==0:
        st.warning("No numeric cloumns found.")
    else:
        selected_column = st.selectbox("Select numeric",
            numeric_columns
        )
        st.subheader(" Features Distribution")
        st.bar_chart(
            df[selected_column].value_counts()
        )
        

# -------------------------------
# Investment Profiling
# -------------------------------

elif page == "Investment Profiling":

    st.header("💰 Investment Profiling")
    
    numeric_columns= df.select_dtypes(
            include="number").columns.tolist()
    if len(numeric_columns)==0:
        st.warning("No numeric data available.")
    else:
        selected_column = st.selectbox("Select Investment Feature",
            numeric_columns
        )
        st.metric("Maximum Value",
            f"{df[selected_column].max():,.2f}"
        )
        st.metric("Minimum Value",
            f"{df[selected_column].min():,.2f}"
        )
    

# -------------------------------
# Market Intelligence
# -------------------------------

elif page == "Market Intelligence":

    st.header("📈 Market Intelligence")
    numeric_columns= df.select_dtypes(
            include="number").columns.tolist()
    
    if len(numeric_columns)<2:
        st.warning("At least two numeric columns are required."
        )
    else:
        col1, col2 = st.columns(2)
        
        with col1:
            x_column = st.selectbox(
                "Select X-axis",
                numeric_columns,
                index=0
            )
        
        with col2:
            y_column = st.selectbox(
                "Select Y-axis",
                numeric_columns,
                index=1
            )
        
        st.subheader("Relationship between selected features")
        
        fig, ax = plt.subplots(figsize=(8, 5))
        
        ax.scatter(
            df[x_column],
            df[y_column],
        )
        
        ax.set_xlabel(x_column)
        ax.set_ylabel(y_column)
        ax.set_title(f"{x_column} vs {y_column}")
        
        st.pyplot(fig)
        
        st.subheader("Distribution")
        
        selected = st.selectbox(
            "Select Feature for Histogram",
            numeric_columns
        )
        fig, ax = plt.subplots(figsize=(8, 5))
        
        ax.hist(df[selected].dropna(), 
                bins=20,
        )
        
        ax.set_title(f"Distribution of {selected}")
        
        ax.set_xlabel(selected)
        ax.set_ylabel("Frequency")  
        
        st.pyplot(fig)

    