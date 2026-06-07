import streamlit as st
import streamlit.components.v1 as components

# 1. Page Configuration
st.set_page_config(
    page_title="KingPro.Ai Clay Library",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom Theme: Cozy Antique Cyber-Library
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@600;800&family=Inter:wght@400;600&display=swap');
    
    .stApp {
        background: radial-gradient(circle at center, #1e140f 0%, #0a0705 100%);
        color: #e2d7cd;
    }
    h1 {
        color: #f5e6d3 !important;
        font-family: 'Cinzel', serif;
        font-weight: 800;
        text-align: center;
        text-shadow: 0 0 15px rgba(245, 230, 211, 0.2);
    }
    p, span, label {
        font-family: 'Inter', sans-serif !important;
    }
    .stTextInput div div input {
        background-color: #1a110b !important;
        color: #f5e6d3 !important;
        border: 2px solid #3d281a !important;
        border-radius: 12px !important;
        font-size: 18px !important;
        text-align: center;
    }
    .stTextInput div div input:focus {
        border-color: #d4af37 !important;
        box-shadow: 0 0 20px rgba(212, 175, 55, 0.3) !important;
    }
    .shelf-badge {
        background: #261a10;
        color: #d4af37;
        padding: 6px 12px;
        border-radius: 6px;
        font-size: 13px;
        font-family: monospace;
        border: 1px solid #4a3321;
        margin: 4px;
        display: inline-block;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>📚 KingPro.Ai // The Claymation Library</h1>", unsafe_allow_html=True)
st.caption("<p style='text-align: center; color: #8c7355;'>AMBIENT AUDIO: GOD MODE (KARUPPU) ACTIVE | RENDERING: MATTE CLAY CORES</p>", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# THE MATTE CLAY ASSET DIRECTORY
# Handpicked high-detail models that look beautiful with matte clay shaders
# ----------------------------------------------------------------------
CLAY_ARCHIVE = {
    "astronaut": "https://modelviewer.dev/shared-assets/models/Astronaut.glb",
    "spaceman": "https://modelviewer.dev/shared-assets/models/Astronaut.glb",
    "duck": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/Duck/glTF-Binary/Duck.glb",
    "fox": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/Fox/glTF-Binary/Fox.glb",
    "animal": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/Fox/glTF-Binary/Fox.glb",
    "helmet": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/DamagedHelmet/glTF-Binary/DamagedHelmet.glb",
    "scifi helmet": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/DamagedHelmet/glTF-Binary/DamagedHelmet.glb",
    "chair": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/SheenChair/glTF-Binary/SheenChair.glb",
    "armchair": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/SheenChair/glTF-Binary/SheenChair.glb",
    "car": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/ToyCar/glTF-Binary/ToyCar.glb",
    "racecar": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/ToyCar/glTF-Binary/ToyCar.glb",
    "plant": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/DiffuseTransmissionPlant/glTF-Binary/DiffuseTransmissionPlant.glb",
    "brain": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/BrainStem/glTF-Binary/BrainStem.glb",
    "camera": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/AntiqueCamera/glTF-Binary/AntiqueCamera.glb",
    "watch": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/ChronographWatch/glTF-Binary/ChronographWatch.glb",
    "shoe": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/MaterialsVariantsShoe/glTF-Binary/MaterialsVariantsShoe.glb",
    "sneaker": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/MaterialsVariantsShoe/glTF-Binary/MaterialsVariantsShoe.glb"
}

# 2. Input Architecture
user_input_raw = st.text_input("📖 Pull a clay model from the library shelves:", value="astronaut")

# Input Processing & Matching
processed_term = user_input_raw.strip().lower()
if processed_term not in CLAY_ARCHIVE and processed_term.endswith('s'):
    processed_term = processed_term[:-1]

isolated_key = None
if processed_term in CLAY_ARCHIVE:
    isolated_key = processed_term
else:
    for dict_key in CLAY_ARCHIVE.keys():
        if dict_key in processed_term or processed_term in dict_key:
            isolated_key = dict_key
            break

# 3. Execution Pipeline
if isolated_key:
    glb_target = CLAY_ARCHIVE[isolated_key]
    st.success(f"📜 Materializing Hand-Crafted Clay '{isolated_key.upper()}'...")
    
    # Advanced WebGL Block: Injects custom clay style shaders & Karuppu audio streams
    engine_html = f"""
    <script type="module" src="https://ajax.googleapis.com/ajax/libs/model-viewer/3.4.0/model-viewer.min.js"></script>
    <style>
        body, html {{ margin: 0; padding: 0; overflow: hidden; background-color: #0a0705; }}
        
        /* Library Viewport Box with warm wooden background */
        model-viewer {{
            width: 100vw;
            height: 75vh;
            background: radial-gradient(circle at center, #2e1f14 0%, #0a0705 100%);
            border-radius: 16px;
            border: 3px solid #3d281a;
            box-shadow: 0 10px 30px rgba(0,0,0,0.6);
        }}
    </style>
    
    <iframe src="https://www.youtube.com/embed/gH8U8D081zI?autoplay=1&loop=1&playlist=gH8U8D081zI&mute=0" 
            allow="autoplay" 
            style="display:none; width:0; height:0; border:0;">
    </iframe>

    <model-viewer 
        src="{glb_target}" 
        alt="Claymation Matrix Node" 
        camera-controls 
        auto-rotate 
        interaction-prompt="none"
        
        /* Clay Style Lighting Config: High ambient light with intense shadows */
        shadow-intensity="2.5"
        shadow-softness="0.3"
        exposure="0.85"
        environment-image="neutral"
        stage-light-intensity="0.5">
    </model-viewer>
    """
    components.html(engine_html, height=540)
    
else:
    st.error(f"❌ '{user_input_raw}' is missing from the Library Archives.")
    st.markdown("### 🗄️ Available Library Books/Vectors:")
    
    sorted_keywords = sorted(list(set(CLAY_ARCHIVE.keys())))
    badge_payload = "".join([f"<div class='shelf-badge'>{keyword}</div>" for keyword in sorted_keywords])
    st.markdown(badge_payload, unsafe_allow_html=True)

st.markdown("---")
st.markdown("<p style='text-align: center; color: #5c4731; font-family: monospace;'>KingPro Library Matrix Engine v7.0 • Audio Loop Enabled</p>", unsafe_allow_html=True)
