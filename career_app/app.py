import streamlit as st
import pandas as pd

# Load career data
career_data = pd.read_csv('career_data.csv')

st.title("🎓 Student Career Guidance Tool")
st.image("career.jpg",use_container_width=True)
st.markdown("""Welcome to our Student Career Guidance tool!! Our tool aims to simplify the process of career exploration by providing personalized recommendations based on your unique profile. Many students struggle with choosing a path for their career in the future. Our tool helps such students to explore options based on their interests and skills. We also provide cited sources from where they can start learning for their preferred career.""")

# Sidebar Inputs
st.sidebar.title("🔷Team D³")
st.sidebar.header("Your Profile")
name = st.sidebar.text_input("Name")
#grade = st.sidebar.selectbox("Current Grade", ["9th", "10th", "11th", "12th"])
interests = st.sidebar.multiselect("Your Interests", ["Technology", "Arts", "Business", "Science", "Healthcare", "Social Work", "Engineering"])
skills = st.sidebar.multiselect("Your Skills", ["Frontend","SQL","Attention to detail","Problem-solving", "Creativity", "Communication", "Coding", "Design", "Empathy", "Leadership","Knowledge of anatomy","Knowledge of fitness","Leadership","Mathematics","Motivation","Organisation","Planning","Research","Writing","Field work","Decision-making","Focus"])

# Rule-based filter
def filter_careers(interests, skills):
    if not interests or not skills:
        return pd.DataFrame()

    matches = career_data[
        career_data['Suitable Interests'].apply(lambda x: any(i in x for i in interests)) &
        career_data['Suitable Skills'].apply(lambda x: any(s in x for s in skills))
    ]
    return matches

if st.sidebar.button("Get Recommendations"):
    results = filter_careers(interests, skills)

    if not results.empty:
        st.subheader(f"Hi {name}, here are some careers you might like:")
        for _, row in results.iterrows():
            st.markdown(f"### 🎯 {row['Career']}")
            st.write(f"About: {row['Description']}")
            st.write(f"Average Salary: {row['Avg Salary']} | Growth Outlook: {row['Growth Outlook']}")
            st.markdown(f"[Learn More]({row['Resource']})")
            st.markdown("---")
    else:
        st.warning("No matches found. Try selecting more interests or skills.")
