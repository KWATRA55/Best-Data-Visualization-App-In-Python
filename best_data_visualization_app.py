# used libraries
from enum import auto
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
matplotlib.use("Agg")

# ML packages


# main

def main():
    st.title("Best Data Visualization App")
    st.text("With Streamlit")

    activities = ["EDA", "Plot", "Model Building", "About"]

    choice = st.sidebar.selectbox("Select Activity", activities)
     
    if choice== "EDA":
        st.subheader("Exploratory Data Analysis")

        data = st.file_uploader("Upload Dataset", type=["txt", "csv"])
        if data is not None:
            df = pd.read_csv(data)
            st.dataframe(df.head())

            if st.checkbox("Show Shape"):
                st.write(df.shape)

            if st.checkbox("Select Coloums To Show"):
                selected_columns = st.multiselect("Select Columns", df.columns)
                new_df = df[selected_columns]
                st.dataframe(new_df)

            if st.checkbox("Show All Coloums"):
                st.write(df.columns)

            if st.checkbox("Show Summary"):
                st.write(df.describe())

            if st.checkbox("Show Value Count"):
                st.write(df.iloc[:, -1].value_counts())
    


    elif choice== "Plot":
        st.subheader("Data Visualization")

        data = st.file_uploader("Upload Dataset", type=["txt", "csv"])
        if data is not None:
            df = pd.read_csv(data)
            st.dataframe(df.head())

        if st.checkbox("Correlation With Seaborn"):
            st.set_option('deprecation.showPyplotGlobalUse', False) # just to avoid any warning
            st.write( sns.heatmap(df.corr(), annot=True))
            st.pyplot()

        if st.checkbox("Pie Chart"):
            st.set_option('deprecation.showPyplotGlobalUse', False) # just to avoid any warning
            columns_to_plot = st.selectbox("Select Any Column", df.columns)
            pie_plot = df[columns_to_plot].value_counts().plot.pie(autopct = "%1.1f%%")
            st.write(pie_plot)
            st.pyplot()

        
        type_of_plot = st.selectbox("Select Type of Plot", ["area", "bar", "line", "hist", "box", "kde" ])
        selected_columns_names = st.multiselect("Select Columns to plot", df.columns)

        if st.button("Generate Plot"):
            st.success("Generating Customizable Plot of {} for {}".format(type_of_plot, selected_columns_names))

            #plot by streamli
            if type_of_plot == "area":
                custom_data = df[selected_columns_names]
                st.area_chart(custom_data)

            elif type_of_plot == "bar":
                custom_data = df[selected_columns_names]
                st.bar_chart(custom_data)

            elif type_of_plot == "line":
                custom_data = df[selected_columns_names]
                st.line_chart(custom_data)

            elif type_of_plot:
                custom_plot = df[selected_columns_names].plot(kind = type_of_plot)
                st.write(custom_plot)
                st.pyplot()


    elif choice== "Model Building":
        st.subheader("Building ML Models")
    


    elif choice== "About":
        st.subheader("About")
    

    




if __name__ == "__main__":
    main()
