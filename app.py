import streamlit as st
import segno
import io

# Page Config for Professional Look
st.set_page_config(
    page_title="Pro QR Generator | Vikas Mishra",
    page_icon="🎯",
    layout="centered"
)

# Custom CSS for Premium Styling
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        color: white;
    }
    .stTextInput > div > div > input {
        background-color: #1e293b;
        color: white;
        border: 2px solid #38bdf8;
        border-radius: 10px;
    }
    .stButton > button {
        width: 100%;
        background: linear-gradient(90deg, #38bdf8, #2563eb);
        color: white;
        font-weight: bold;
        border: none;
        border-radius: 10px;
        padding: 10px;
        transition: 0.3s;
    }
    .stButton > button:hover {
        transform: scale(1.02);
        box-shadow: 0px 0px 15px rgba(56, 189, 248, 0.5);
    }
    /* Vikas Mishra Credit Styling */
    .dev-credit {
        text-align: center;
        margin-top: 50px;
        padding: 10px;
    }
    .dev-name {
        color: #38bdf8 !important;
        font-weight: bold;
        text-decoration: underline !important;
        font-size: 1.1rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Main Dashboard UI
st.title("🎯 Borderless QR Generator")
st.write("Apni details niche diye gaye box mein bhariye aur turant professional QR code payiye.")

# Input Area
detail = st.text_area("Yahan Detail Fill Karein:", placeholder="URL, Text, ya koi bhi jankari likhein...", height=150)

if st.button("Generate QR Code"):
    if detail.strip() == "":
        st.error("Kripya pehle detail fill karein!")
    else:
        with st.spinner("QR Code generate ho raha hai..."):
            # Creating Borderless QR using Segno
            # border=0 se safed border puri tarah hat jata hai
            qr = segno.make(detail, error='H')
            
            # Saving to memory buffer
            img_buf = io.BytesIO()
            qr.save(img_buf, kind='png', scale=10, border=0) 
            img_buf.seek(0)
            
            # Displaying QR
            st.markdown("### ✅ Aapka QR Code Ready Hai")
            st.image(img_buf, caption="Preview (Borderless)", width=300)
            
            # Download Button
            st.download_button(
                label="📥 Download QR Code",
                data=img_buf,
                file_name="Vikas_Mishra_QR.png",
                mime="image/png"
            )
            st.success("QR Code download ke liye taiyar hai!")

# Sidebar/Footer for Credit
st.markdown("<div class='dev-credit'>", unsafe_allow_html=True)
st.markdown("<p style='color: #94a3b8; margin-bottom: 2px;'>Developed By</p>", unsafe_allow_html=True)
st.markdown("<p class='dev-name'>VIKAS MISHRA</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
