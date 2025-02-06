import streamlit as st
import random

# Define a list of community member names
names = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Helen", "Ian", "Jack",
         "Karen", "Louis", "Mia", "Nathan", "Olivia", "Paul", "Quincy", "Rita", "Sam", "Tina",
         "Uma", "Vince", "Will", "Xena", "Yara", "Zack"]

# Define the interests for random assignment
interests = ["Sports", "Music", "Art", "Technology", "Travel", "Cooking", "Fitness", "Reading", "Gaming", "Photography"]

# Function to generate random profiles
def generate_member_data():
    return {
        "Name": random.choice(names),
        "Age": random.randint(18, 60),  # Random age between 18 and 60
        "Interest": random.choice(interests),  # Random interest
        "Profile": f"This is the profile of {random.choice(names)}"  # Random profile description
    }

# Generate random data for 25 members
members = [generate_member_data() for _ in range(25)]

# Convert list of member data to a pandas DataFrame
import pandas as pd
members_df = pd.DataFrame(members)

# Streamlit App
st.title("Community Members Management")

# Display a brief introduction
st.write("This app dynamically generates a list of community members with random profile data.")

# Sidebar for selecting a community member
member_name = st.sidebar.selectbox("Select a Member", members_df['Name'])

# Display the profile details of the selected member
selected_member = members_df[members_df['Name'] == member_name].iloc[0]
st.subheader(f"Profile of {selected_member['Name']}")
st.write(f"**Age:** {selected_member['Age']}")
st.write(f"**Interest:** {selected_member['Interest']}")
st.write(f"**Profile Description:** {selected_member['Profile']}")

# Display the full list of community members
st.subheader("Full List of Community Members")
st.dataframe(members_df)

# Adding a button for refreshing the member list or generating new members
if st.button('Refresh Members'):
    # Regenerate the member data and update the DataFrame
    members = [generate_member_data() for _ in range(25)]
    members_df = pd.DataFrame(members)
    st.experimental_rerun()  # Rerun the app to refresh the list
