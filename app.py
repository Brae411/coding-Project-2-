import streamlit as st

# Add custom CSS for gradient background
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #6a5acd 0%, #f7b2e6 100%) !important;
    }
    .stApp {
        background: linear-gradient(135deg, #6a5acd 0%, #f7b2e6 100%) !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Anime & Cartoon Character Quiz")
st.write("Think of a character from anime or a popular cartoon show, and I'll try to guess who it is!")

if 'step' not in st.session_state:
    st.session_state.step = 1
if 'answers' not in st.session_state:
    st.session_state.answers = {}

def reset_quiz():
    st.session_state.step = 1
    st.session_state.answers = {}

if st.button("Restart Quiz"):
    reset_quiz()

if st.session_state.step == 1:
    q1 = st.radio("Is your character from an anime or cartoon?", ["Anime", "Cartoon"])
    if st.button("Next", key="step1"):
        st.session_state.answers['q1'] = q1
        st.session_state.step = 2

elif st.session_state.step == 2:
    if st.session_state.answers['q1'] == "Anime":
        q2 = st.radio("Is your character a boy or a girl?", ["Boy", "Girl"])
        if st.button("Next", key="step2a"):
            st.session_state.answers['q2'] = q2
            st.session_state.step = 3
    else:
        q2 = st.radio("Is your character an animal?", ["Yes", "No"])
        if st.button("Next", key="step2b"):
            st.session_state.answers['q2'] = q2
            st.session_state.step = 3

elif st.session_state.step == 3:
    if st.session_state.answers['q1'] == "Anime":
        if st.session_state.answers['q2'] == "Boy":
            q3 = st.radio("Is your character from Demon Slayer?", ["Yes", "No"])
            if q3 == "Yes":
                q4 = st.radio("Does your character use water breathing?", ["Yes", "No"])
                if st.button("Get Result", key="step3a1"):
                    st.session_state.answers['q3'] = q3
                    st.session_state.answers['q4'] = q4
                    st.session_state.step = 4
            else:
                q4 = st.radio("Does your character have spiky hair?", ["Yes", "No"])
                if st.button("Get Result", key="step3a2"):
                    st.session_state.answers['q3'] = q3
                    st.session_state.answers['q4'] = q4
                    st.session_state.step = 4
        else:
            q3 = st.radio("Is your character a magical girl?", ["Yes", "No"])
            if q3 == "Yes":
                q4 = st.radio("Does your character fight with a wand?", ["Yes", "No"])
                if st.button("Get Result", key="step3b1"):
                    st.session_state.answers['q3'] = q3
                    st.session_state.answers['q4'] = q4
                    st.session_state.step = 4
            else:
                q4 = st.radio("Is your character from Attack on Titan?", ["Yes", "No"])
                if st.button("Get Result", key="step3b2"):
                    st.session_state.answers['q3'] = q3
                    st.session_state.answers['q4'] = q4
                    st.session_state.step = 4
    else:
        if st.session_state.answers['q2'] == "Yes":
            q3 = st.radio("Is your character a mouse?", ["Yes", "No"])
            if q3 == "Yes":
                if st.button("Get Result", key="step3c1"):
                    st.session_state.answers['q3'] = q3
                    st.session_state.step = 4
            else:
                q4 = st.radio("Is your character a dog?", ["Yes", "No"])
                if st.button("Get Result", key="step3c2"):
                    st.session_state.answers['q3'] = q3
                    st.session_state.answers['q4'] = q4
                    st.session_state.step = 4
        else:
            q3 = st.radio("Is your character yellow?", ["Yes", "No"])
            if q3 == "Yes":
                if st.button("Get Result", key="step3d1"):
                    st.session_state.answers['q3'] = q3
                    st.session_state.step = 4
            else:
                q4 = st.radio("Is your character a superhero?", ["Yes", "No"])
                if q4 == "Yes":
                    q5 = st.radio("Is your character a girl?", ["Yes", "No"])
                    if st.button("Get Result", key="step3d2"):
                        st.session_state.answers['q3'] = q3
                        st.session_state.answers['q4'] = q4
                        st.session_state.answers['q5'] = q5
                        st.session_state.step = 4
                else:
                    q5 = st.radio("Does your character wear a green shirt?", ["Yes", "No"])
                    if st.button("Get Result", key="step3d3"):
                        st.session_state.answers['q3'] = q3
                        st.session_state.answers['q4'] = q4
                        st.session_state.answers['q5'] = q5
                        st.session_state.step = 4

elif st.session_state.step == 4:
    ans = st.session_state.answers
    result = ""
    image_url = "https://upload.wikimedia.org/wikipedia/commons/6/65/No-Image-Placeholder.svg"  # Placeholder (always loads)
    if ans['q1'] == "Anime":
        if ans['q2'] == "Boy":
            if ans.get('q3') == "Yes":  # Demon Slayer branch
                if ans.get('q4') == "Yes":
                    result = "Are you thinking of Tanjiro Kamado from Demon Slayer?"
                    image_url = "Tanjiro.png"  # Local image file
                else:
                    result = "Are you thinking of Zenitsu Agatsuma from Demon Slayer?"
                    image_url = "image copy 3.png"  # Use the requested image file
            else:
                if ans.get('q4') == "Yes":
                    result = "Are you thinking of Goku from Dragon Ball?"
                    image_url = "image.png"  # Use the requested image file
                else:
                    result = "Are you thinking of Shinji Ikari from Evangelion?"
                    image_url = "image copy.png"  # Use the requested image file
        else:
            if ans.get('q3') == "Yes":
                if ans.get('q4') == "Yes":
                    result = "Are you thinking of Sailor Moon?"
                    image_url = "image copy 5.png"  # Use the requested image file
                else:
                    result = "Are you thinking of Sakura Kinomoto from Cardcaptor Sakura?"
                    image_url = "image copy 7.png"  # Use the requested image file
            else:
                if ans.get('q4') == "Yes":
                    result = "Are you thinking of Mikasa Ackerman from Attack on Titan?"
                    image_url = "image copy 8.png"  # Use the requested image file
                else:
                    result = "Are you thinking of Nezuko Kamado from Demon Slayer?"
                    image_url = "image copy 10.png"  # Use the requested image file
    else:
        if ans['q2'] == "Yes":
            if ans.get('q3') == "Yes":
                result = "Are you thinking of Mickey Mouse?"
                image_url = "https://upload.wikimedia.org/wikipedia/commons/d/d4/Mickey_Mouse.png"  # This one works
            else:
                if ans.get('q4') == "Yes":
                    result = "Are you thinking of Scooby-Doo?"
                    image_url = "image copy 14.png"  # Use the requested image file
                else:
                    result = "Are you thinking of Courage the Cowardly Dog?"
                    image_url = "image copy 12.png"  # Use the requested image file
        else:
            if ans.get('q3') == "Yes":
                result = "Are you thinking of SpongeBob SquarePants?"
                image_url = "image copy 15.png"  # Use the requested image file
            else:
                if ans.get('q4') == "Yes":
                    if ans.get('q5') == "Yes":
                        result = "Are you thinking of Blossom from The Powerpuff Girls?"
                        image_url = "image copy 17.png"  # Use the requested image file
                    else:
                        result = "Are you thinking of Ben Tennyson from Ben 10?"
                        image_url = "image copy 18.png"  # Use the requested image file
                else:
                    if ans.get('q5') == "Yes":
                        result = "Are you thinking of Finn the Human from Adventure Time?"
                        image_url = "image copy 20.png"  # Use the requested image file
                    else:
                        result = "Are you thinking of Dexter from Dexter's Laboratory?"
                        image_url = "image copy 22.png"  # Use the requested image file
    st.markdown(f"<span style='color:#1a237e; font-size:22px; font-weight:bold;'>{result}</span>", unsafe_allow_html=True)
    # Always show an image, use a default placeholder if image_url is empty
    if not image_url:
        image_url = "https://upload.wikimedia.org/wikipedia/commons/6/65/No-Image-Placeholder.svg"
    try:
        st.image(image_url, caption=result, width=200)
    except Exception:
        st.image("https://upload.wikimedia.org/wikipedia/commons/6/65/No-Image-Placeholder.svg", caption="Image not available", width=200)
    st.write("Thanks for playing!")
