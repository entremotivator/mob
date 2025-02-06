import streamlit as st
import pandas as pd
import random

# Create a sample of 25 community members with basic profiles
names = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Helen", "Ian", "Jack",
         "Karen", "Louis", "Mia", "Nathan", "Olivia", "Paul", "Quincy", "Rita", "Sam", "Tina",
         "Uma", "Vince", "Will", "Xena", "Yara", "Zack"]

ages = [random.randint(18, 60) for _ in range(25)]
interests = ["Sports", "Music", "Art", "Technology", "Travel", "Cooking", "Fitness", "Reading", "Gaming", "Photography"]

# Create a dataframe of community members
members = pd.DataFrame({
    "Name": names,
    "Age": ages,
    "Interest": [random.choice(interests) for _ in range(25)],
    "Profile": [f"Profile of {name}" for name in names]
})

# Streamlit App
st.title("Community Members Management")

# Display a brief introduction
st.write("This app manages a list of community members, displaying their basic profile information.")

# Sidebar for selecting a community member
member_name = st.sidebar.selectbox("Select a Member", members['Name'])

# Display the profile details of the selected member
selected_member = members[members['Name'] == member_name].iloc[0]
st.subheader(f"Profile of {selected_member['Name']}")
st.write(f"**Age:** {selected_member['Age']}")
st.write(f"**Interest:** {selected_member['Interest']}")
st.write(f"**Profile Description:** {selected_member['Profile']}")

# Display the full list of community members
st.subheader("Full List of Community Members")
st.dataframe(members)

# Adding a button for refreshing the member list or generating new members
if st.button('Refresh Members'):
    # Create random member profiles again
    members['Age'] = [random.randint(18, 60) for _ in range(25)]
    members['Interest'] = [random.choice(interests) for _ in range(25)]
    st.experimental_rerun()
