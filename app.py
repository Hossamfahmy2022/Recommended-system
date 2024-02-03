import streamlit as st
import pandas as pd

dataframe = pd.read_csv("Clustered_data.csv")

def Get_Recommendation(User , dataframe , num_of_recommendations):
    Cluster = dataframe[dataframe["customer_id"] == User].reset_index()["Cluster"][0]
    df_cluster = dataframe[dataframe["Cluster"] == Cluster]
    df_cluster = df_cluster.groupby("product_category_name")["Monetary"].sum().sort_values(ascending = False).head(int(num_of_recommendations))
    for index , name in enumerate(df_cluster.index) : 
        st.success(f"Recommendation number {index + 1} is {name}")
def main():
    st.title("Target Offers")
    User = st.text_input("User ID")
    num_of_recommendations = st.text_input("Num of Recommendations")
    if st.button("Recommend"):
        Get_Recommendation(User , dataframe , num_of_recommendations)

main()
