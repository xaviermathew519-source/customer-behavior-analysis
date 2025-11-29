import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

st.title("📊 CUSTOMER SHOPPING BEHAVIOUR - SIMPLE DASHBOARD")

# load data

df = pd.read_csv("new_df.csv")

st.subheader("Data Preview")
st.dataframe(df.head())


# 1️ Subscription Pie Chart

st.subheader("🟢 Subscription Status Pie Chart")

# if "subscription_status" in df.columns:
counts = df["subscription_status"].value_counts()

# Create figure
fig1, ax = plt.subplots(figsize=(5,5))


color = ['#66c2a5',"#ae1877"]
explode = (0,0.1)
ax.pie(counts,labels=counts.index,autopct="%1.1f%%",colors = color,explode=explode,startangle=90,shadow=True)

ax.set_title("Subscription Status")
st.pyplot(fig1)



#  Gender Bar Chart

st.subheader("👦👧 Gender Distribution")

fig2, ax = plt.subplots(figsize=(6,4))
sns.countplot(x=df["gender"].astype(str), palette="magma", ax=ax)
ax.set_title("Gender Distribution")
st.pyplot(fig2)



# review in histogram

st.subheader("⭐ Review Rating Distribution")
fig3, ax = plt.subplots(figsize=(6,4))
ax.hist(df["review_rating"], bins=10, edgecolor="black", color="#708ccc")
ax.set_title("Review Rating Distribution")
ax.set_xlabel("Rating")
st.pyplot(fig3)



#  Average Purchase Amount by Category

st.subheader("🛒 Average Purchase Amount by Category")

df["purchase_amount"] = pd.to_numeric(df["purchase_amount"], errors="coerce")
cat_avg = df.groupby("category")["purchase_amount"].mean().reset_index()

fig4, ax = plt.subplots(figsize=(8,4))
sns.barplot(data=cat_avg, x="category", y="purchase_amount", palette="magma")
ax.set_title("Avg Purchase Amount by Category")

st.pyplot(fig4)
