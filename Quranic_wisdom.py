import streamlit as st
import random

# Set page configuration
st.set_page_config(
    page_title="Spiritual Reflection - Quranic Wisdom",
    page_icon="☪️",
    layout="centered"
)

# Dictionary of Quran quotes organized by emotion
quran_quotes = {
    "Happy": [
        {"verse": "So remember Me; I will remember you.", "reference": "Quran 2:152"},
        {"verse": "Indeed, with hardship [will be] ease.", "reference": "Quran 94:6"},
        {"verse": "And He found you lost and guided [you].", "reference": "Quran 93:7"}
    ],
    "Sad": [
        {"verse": "And We will surely test you with something of fear and hunger and a loss of wealth and lives and fruits, but give good tidings to the patient.", "reference": "Quran 2:155"},
        {"verse": "And whoever relies upon Allah - then He is sufficient for him.", "reference": "Quran 65:3"},
        {"verse": "Do not lose hope, nor be sad. You will surely be victorious if you are true believers.", "reference": "Quran 3:139"}
    ],
    "Angry": [
        {"verse": "Those who spend [in the cause of Allah] during ease and hardship and who restrain anger and who pardon the people - and Allah loves the doers of good.", "reference": "Quran 3:134"},
        {"verse": "And when you are angry, be silent.", "reference": "Based on Hadith"},
        {"verse": "So pardon them and ask forgiveness for them and consult them in the matter.", "reference": "Quran 3:159"}
    ],
    "Helpless": [
        {"verse": "Allah does not burden a soul beyond that it can bear.", "reference": "Quran 2:286"},
        {"verse": "Is not Allah sufficient for His Servant?", "reference": "Quran 39:36"},
        {"verse": "And when My servants ask you concerning Me - indeed I am near. I respond to the invocation of the supplicant when he calls upon Me.", "reference": "Quran 2:186"}
    ],
    "Regret": [
        {"verse": "Say, 'O My servants who have transgressed against themselves [by sinning], do not despair of the mercy of Allah. Indeed, Allah forgives all sins. Indeed, it is He who is the Forgiving, the Merciful.'", "reference": "Quran 39:53"},
        {"verse": "But whoever repents after his wrongdoing and reforms, indeed, Allah will turn to him in forgiveness. Indeed, Allah is Forgiving and Merciful.", "reference": "Quran 5:39"},
        {"verse": "And it is He who accepts repentance from his servants and pardons misdeeds, and He knows what you do.", "reference": "Quran 42:25"}
    ],
    "Jealous": [
        {"verse": "And do not wish for that which Allah has made some of you exceed others.", "reference": "Quran 4:32"},
        {"verse": "Or do they envy people for what Allah has given them of His bounty?", "reference": "Quran 4:54"},
        {"verse": "And from the evil of the envier when he envies.", "reference": "Quran 113:5"}
    ],
    "Grateful": [
        {"verse": "And [remember] when your Lord proclaimed, 'If you are grateful, I will surely increase you [in favor].'", "reference": "Quran 14:7"},
        {"verse": "So remember Me; I will remember you. And be grateful to Me and do not deny Me.", "reference": "Quran 2:152"},
        {"verse": "And Allah has extracted you from the wombs of your mothers not knowing a thing, and He made for you hearing and vision and hearts [intellect] that perhaps you would be grateful.", "reference": "Quran 16:78"}
    ],
    "Fearful": [
        {"verse": "Those to whom people said, 'Indeed, the people have gathered against you, so fear them.' But it [merely] increased them in faith, and they said, 'Sufficient for us is Allah, and [He is] the best Disposer of affairs.'", "reference": "Quran 3:173"},
        {"verse": "And whoever fears Allah - He will make for him a way out. And will provide for him from where he does not expect.", "reference": "Quran 65:2-3"},
        {"verse": "So fear not the people but fear Me.", "reference": "Quran 5:44"}
    ],
    "Anxious": [
        {"verse": "Unquestionably, by the remembrance of Allah hearts are assured.", "reference": "Quran 13:28"},
        {"verse": "And seek help through patience and prayer, and indeed, it is difficult except for the humbly submissive [to Allah].", "reference": "Quran 2:45"},
        {"verse": "Say, 'Never will we be struck except by what Allah has decreed for us; He is our protector.' And upon Allah let the believers rely.", "reference": "Quran 9:51"}
    ],
    "Hopeful": [
        {"verse": "Indeed, with hardship [will be] ease. Indeed, with hardship [will be] ease.", "reference": "Quran 94:5-6"},
        {"verse": "And my success is not but through Allah. Upon Him I have relied, and to Him I return.", "reference": "Quran 11:88"},
        {"verse": "Do not despair of relief from Allah. Indeed, no one despairs of relief from Allah except the disbelieving people.", "reference": "Quran 12:87"}
    ]
}

# Add custom CSS without external image dependency
def add_custom_styling():
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        }
        .title {
            color: white;
            text-align: center;
            font-size: 3rem;
            text-shadow: 2px 2px 4px #000000;
            padding: 20px;
        }
        .subtitle {
            color: white;
            text-align: center;
            font-size: 1.5rem;
            text-shadow: 1px 1px 2px #000000;
            margin-bottom: 30px;
        }
        .quote-box {
            background-color: rgba(255, 255, 255, 0.8);
            border-radius: 10px;
            padding: 20px;
            margin: 30px 0;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        .verse {
            font-size: 1.5rem;
            font-style: italic;
            margin-bottom: 10px;
            color: #2c3e50;
            text-align: center;
        }
        .reference {
            font-size: 1.2rem;
            color: #7f8c8d;
            text-align: right;
        }
        div[data-baseweb="select"] {
            margin-bottom: 20px;
        }
        div[data-baseweb="select"] > div {
            background-color: rgba(255, 255, 255, 0.2);
            border-color: white;
        }
        .stSelectbox label {
            color: white !important;
            font-size: 1.2rem !important;
            text-shadow: 1px 1px 2px #000000;
        }
        .stButton button {
            background-color: #27ae60;
            color: white;
            font-weight: bold;
            padding: 0.5em 1em;
            border-radius: 5px;
            border: none;
            width: 100%;
        }
        .stButton button:hover {
            background-color: #2ecc71;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Main function to build the app
def main():
    add_custom_styling()
    
    # Title
    st.markdown('<div class="title">Quranic Wisdom for the Heart</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Find spiritual guidance based on your emotional state</div>', unsafe_allow_html=True)
    
    # Emotion selector
    emotion = st.selectbox(
        "What emotion are you experiencing?",
        options=list(quran_quotes.keys()),
        key="emotion_selector"
    )
    
    # Display quote when a selection is made
    if emotion:
        if st.button("Seek Guidance", key="seek_guidance"):
            selected_quote = random.choice(quran_quotes[emotion])
            
            st.markdown(
                f"""
                <div class="quote-box">
                    <div class="verse">"{selected_quote['verse']}"</div>
                    <div class="reference">{selected_quote['reference']}</div>
                </div>
                """,
                unsafe_allow_html=True
            )
            
            # Additional guidance based on emotion
            st.markdown(
                f"""
                <div style="color: white; background-color: rgba(0, 0, 0, 0.6); padding: 15px; border-radius: 10px; margin-top: 20px;">
                    <p style="font-size: 1.1rem; text-align: center;">Reflection: Take a moment to contemplate this verse. How might it apply to your current situation?</p>
                </div>
                """,
                unsafe_allow_html=True
            )

# Run the app
if __name__ == "__main__":
    main()