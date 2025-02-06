import streamlit as st
import random
import pandas as pd

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
def generate_members(count=25):
    return [generate_member_data() for _ in range(count)]

# Convert list of member data to a pandas DataFrame
members = generate_members()
members_df = pd.DataFrame(members)

# Streamlit App
st.title("Community Members Management")

# Display a brief introduction
st.write("This app dynamically generates a list of community members with random profile data.")

# Sidebar for navigation between pages
page = st.sidebar.radio("Select Page", ["Home", "Member List", "Filters", "Stats"])

if page == "Home":
    st.subheader("Welcome to the Community Members Management App!")
    st.write("""
    This application helps you explore community members' profiles, view lists, and filter members based on various criteria. You can also check out community statistics.
    """)
elif page == "Member List":
    # Display the full list of community members
    st.subheader("Full List of Community Members")
    st.dataframe(members_df)

    # Adding pagination
    rows_per_page = 10
    total_pages = len(members_df) // rows_per_page + 1
    page_number = st.number_input("Select Page", min_value=1, max_value=total_pages, value=1)

    start_idx = (page_number - 1) * rows_per_page
    end_idx = start_idx + rows_per_page
    st.dataframe(members_df[start_idx:end_idx])

elif page == "Filters":
    st.subheader("Filter Members")

    # Filter by age
    age_filter = st.slider("Select Age Range", 18, 60, (18, 60))
    filtered_members = members_df[(members_df['Age'] >= age_filter[0]) & (members_df['Age'] <= age_filter[1])]
    
    # Filter by interest
    interest_filter = st.selectbox("Select Interest", ["All"] + interests)
    if interest_filter != "All":
        filtered_members = filtered_members[filtered_members['Interest'] == interest_filter]

    st.dataframe(filtered_members)

elif page == "Stats":
    st.subheader("Community Statistics")

    # Average Age of Members
    avg_age = members_df['Age'].mean()
    st.write(f"**Average Age:** {avg_age:.2f}")

    # Most Common Interest
    most_common_interest = members_df['Interest'].mode()[0]
    st.write(f"**Most Common Interest:** {most_common_interest}")

    # Distribution of Interests
    st.subheader("Interest Distribution")
    interest_counts = members_df['Interest'].value_counts()
    st.bar_chart(interest_counts)

# Sidebar for selecting a community member
member_name = st.sidebar.selectbox("Select a Member", members_df['Name'])

# Display the profile details of the selected member
selected_member = members_df[members_df['Name'] == member_name].iloc[0]
st.subheader(f"Profile of {selected_member['Name']}")
st.write(f"**Age:** {selected_member['Age']}")
st.write(f"**Interest:** {selected_member['Interest']}")
st.write(f"**Profile Description:** {selected_member['Profile']}")

# Adding a button for refreshing the member list or generating new members
if st.button('Refresh Members'):
    # Regenerate the member data and update the DataFrame
    members = generate_members()
    members_df = pd.DataFrame(members)
    st.experimental_rerun()  # Rerun the app to refresh the list
