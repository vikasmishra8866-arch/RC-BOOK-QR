import streamlit as st
import segno
import io

# Page Configuration
st.set_page_config(
    page_title="QR Generator | Vikas Mishra",
    page_icon="🎯",
    layout="centered"
)

# Premium Custom CSS
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: white;
    }
    .stTextArea textarea {
        background-color: #1e293b !important;
        color: #38bdf8 !important;
        border: 2px solid #334155 !important;
        border-radius: 10px !important;
    }
    .stButton > button {
        width: 100%;
        background: linear-gradient(90deg, #38bdf8, #2563eb) !important;
        color: white !important;
        font-weight: bold !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 10px !important;
    }
    .dev-credit {
        text-align: center;
        margin-top: 50px;
        padding: 15px;
        border-top: 1px solid #334155;
    }
    .dev-name {
        color: #38bdf8 !important;
        font-weight: bold;
        text-decoration: underline !important;
        font-size: 1.2rem;
    }
    </style>
    """, unsafe_allow_html=True)

# App Header
st.markdown("<h1 style='text-align: center;'>🎯 Borderless QR Generator</h1>", unsafe_allow_html=True)
st.write("Apni detail niche fill karein aur borderless QR download karein.")

# Input Box
detail = st.text_area("Yahan Detail Fill Karein:", placeholder="Link ya Text likhein...", height=150)

if st.button("Generate QR Code"):
    if detail.strip() == "":
        st.error("Kripya pehle detail fill karein!")
    else:
        with st.spinner("QR ban raha hai..."):
            try:
                # Making QR with border=0 (No white space)
                qr = segno.make(detail, error='H')
                
                # Saving to buffer
                img_buf = io.BytesIO()
                qr.save(img_buf, kind='png', scale=10, border=0) 
                img_buf.seek(0)
                
                # Preview and Download
                st.markdown("---")
                st.image(img_buf, caption="Aapka Borderless QR", width=300)
                
                st.download_button(
                    label="📥 Download QR Code",
                    data=img_buf,
                    file_name="Vikas_Mishra_QR.png",
                    mime="image/png"
                )
                st.success("QR taiyar hai!")
            except Exception as e:
                st.error(f"Error: {e}")

# Footer Credit
st.markdown("""
    <div class='dev-credit'>
        <p style='color: #94a3b8; margin-bottom: 5px;'>Developed By</p>
        <p class='dev-name'>VIKAS MISHRA</p>
    </div>
    """, unsafe_allow_html=True)
