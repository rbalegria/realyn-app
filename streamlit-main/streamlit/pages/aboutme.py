import streamlit as st
import os

# Page title
st.title("About Alegria")

# Header for self gallery
st.title("🖼️ Self Gallery")

# Define the base directory for images
base_dir = "streamlit-main/pic"

# List of image filenames
image_files = ["me.jpg"]

# Construct full paths and verify images exist
image_paths = [os.path.join(base_dir, filename) for filename in image_files]

# Display images in columns
cols = st.columns(len(image_paths))
for col, image_path in zip(cols, image_paths):
    if os.path.exists(image_path):
        try:
            col.image(image_path, use_column_width=True)
        except Exception as e:
            col.write(f"Error displaying image {image_path}: {e}")
    else:
        col.write(f"Image not found: {image_path}")

# Header for personal information
st.header("👨 Alegria, Rhealyn B.")

# Family members and overview
st.markdown("""
##### 👨‍👦‍👦 Family Members

* 🤱 Mother's Name: Alegria, Rolan 
* 👨 Father's Name: Alegria, Lorena
* 👧 Sister's Name: Alegria, Rolyn

### 🔎 Overview
""", unsafe_allow_html=True)

# Personal information
st.header("Personal Information")
st.write("**Name:** Alegria, Rhealyn B.")
st.write("**Age:** 21 years old")
st.write("**Education:** Currently studying at CARLOS HILADO MEMORIAL STATE UNIVERSITY")
st.write("**Year:** 3rd year Bachelor of Science in Information Systems Student")
st.write("**Location:** Zone 10, Talisay City")

# Expandable section for future vision
with st.expander("Who am I 10 years from now?"):
    st.markdown("""
    Ten years from now, after graduating college, 
    I envision myself established in a career that aligns with my passions in technology. 
    By then, I aim to have advanced to more senior roles, gaining valuable experience and possibly even starting 
    my own venture or leading impactful projects. Personally, I expect to have a deeper understanding of myself, 
    strong relationships, and a fulfilling balance between work and personal life. Overall, I see myself as a confident, 
    experienced individual making a positive impact and enjoying both professional success and personal growth.

    My Vision:
    I aim to apply the skills that I learned from college in real-world scenarios, 
    helping businesses and organizations operate more efficiently and effectively. 
    Beyond technical expertise, I envision developing strong problem-solving abilities and a knack for innovation. 
    Ultimately, I aspire to contribute meaningfully to the digital transformation of industries, 
    making a positive impact on how information is utilized and shared globally.

    As an information systems professional, I envision leveraging technical expertise 
    to drive innovation and enhance organizational efficiency. 
    Contributing to the digital transformation of industries, my goal is to make a positive impact 
    on how information is managed and utilized globally.
    """, unsafe_allow_html=True)

# Favorite quotes
st.header("Favorite Quotes")
st.write("1. \"Every day may not be a best day but there is always something good in every day.\"")
st.write("2. \"Calm seas do not create skilled sailors.\"")
st.write("3. \"Do not lean on your own understanding.\"")
st.write("4. \"Don't be pushed around by the fears in your mind. Be led by the dreams in your heart.\"")
st.write("5. \"Prepare!\"")

# Additional images
additional_images = [
    {"path": "us1.jpg", "caption": "Throughout my academic journey, the invaluable support of my classmates has been instrumental in shaping my growth and success. As I reflect on the myriad experiences shared with these individuals, it becomes evident that their contributions have enriched my learning, inspired me to persevere through challenges, and fostered a sense of camaraderie that transcends the classroom."},
]

st.title("🖼️ Gallery")

# Display additional images
for image in additional_images:
    full_path = os.path.join(base_dir, image["path"])
    if os.path.exists(full_path):
        try:
            st.image(full_path, caption=image["caption"], use_column_width=True)
        except Exception as e:
            st.write(f"Error displaying image {full_path}: {e}")
    else:
        st.write(f"Image not found: {full_path}")

# Custom CSS styling
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f0f0f0; /* Light gray background */
        padding: 2em;
    }
    h1, h2 {
        color: #4CAF50; /* Green color for headers */
    }
    .stText {
        font-size: 1.2em;
        color: #333; /* Dark gray text color */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Footer or additional sections (optional)
st.write("### Thank you for visiting my profile!")
st.write("Feel free to connect and reach out if you share similar interests or have any questions.")
