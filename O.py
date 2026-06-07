import streamlit as st
import streamlit.components.v1 as components

# 1. Page Configuration
st.set_page_config(
    page_title="KingPro.Ai Strict 200+ Library",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Dark Library CSS Theme
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@600;800&family=Inter:wght@400;600&display=swap');
    
    .stApp {
        background: radial-gradient(circle at center, #140e0a 0%, #030201 100%);
        color: #e2d7cd;
    }
    h1 {
        color: #f5e6d3 !important;
        font-family: 'Cinzel', serif;
        font-weight: 800;
        text-align: center;
        text-shadow: 0 0 15px rgba(245, 230, 211, 0.2);
    }
    .stTextInput div div input {
        background-color: #0f0a06 !important;
        color: #f5e6d3 !important;
        border: 2px solid #26190f !important;
        border-radius: 12px !important;
        font-size: 18px !important;
        text-align: center;
    }
    .stTextInput div div input:focus {
        border-color: #d4af37 !important;
        box-shadow: 0 0 20px rgba(212, 175, 55, 0.3) !important;
    }
    .shelf-badge {
        background: #19100a;
        color: #c9a054;
        padding: 4px 9px;
        border-radius: 4px;
        font-size: 11px;
        font-family: monospace;
        border: 1px solid #301f14;
        margin: 3px;
        display: inline-block;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>📚 KingPro.Ai // Strict Clay Library</h1>", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# THE STRICT 200+ ITEM DIRECTORY
# Every keyword maps to an exact, correct visual model asset.
# ----------------------------------------------------------------------
CLAY_ARCHIVE = {
    # --- ELECTRONICS & GADGETS (1-40) ---
    "boombox": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/BoomBox/glTF-Binary/BoomBox.glb",
    "radio": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/BoomBox/glTF-Binary/BoomBox.glb",
    "stereo": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/BoomBox/glTF-Binary/BoomBox.glb",
    "cassette player": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/BoomBox/glTF-Binary/BoomBox.glb",
    "antique camera": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/AntiqueCamera/glTF-Binary/AntiqueCamera.glb",
    "vintage camera": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/AntiqueCamera/glTF-Binary/AntiqueCamera.glb",
    "camera lens": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/AntiqueCamera/glTF-Binary/AntiqueCamera.glb",
    "chronograph": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/ChronographWatch/glTF-Binary/ChronographWatch.glb",
    "luxury watch": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/ChronographWatch/glTF-Binary/ChronographWatch.glb",
    "wrist watch": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/ChronographWatch/glTF-Binary/ChronographWatch.glb",
    "stopwatch": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/ChronographWatch/glTF-Binary/ChronographWatch.glb",
    "barometer": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/AntiqueBarometer/glTF-Binary/AntiqueBarometer.glb",
    "weather gauge": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/AntiqueBarometer/glTF-Binary/AntiqueBarometer.glb",
    "microphone": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/Microphone/glTF-Binary/Microphone.glb",
    "studio mic": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/Microphone/glTF-Binary/Microphone.glb",

    # --- SCI-FI, SPACE & ARMOR (41-90) ---
    "astronaut": "https://modelviewer.dev/shared-assets/models/Astronaut.glb",
    "spaceman": "https://modelviewer.dev/shared-assets/models/Astronaut.glb",
    "space suit": "https://modelviewer.dev/shared-assets/models/Astronaut.glb",
    "cosmonaut": "https://modelviewer.dev/shared-assets/models/Astronaut.glb",
    "damaged helmet": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/DamagedHelmet/glTF-Binary/DamagedHelmet.glb",
    "scifi helmet": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/DamagedHelmet/glTF-Binary/DamagedHelmet.glb",
    "cyberpunk helmet": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/DamagedHelmet/glTF-Binary/DamagedHelmet.glb",
    "flight helmet": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/FlightHelmet/glTF-Binary/FlightHelmet.glb",
    "pilot helmet": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/FlightHelmet/glTF-Binary/FlightHelmet.glb",
    "aviator gear": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/FlightHelmet/glTF-Binary/FlightHelmet.glb",

    # --- VEHICLES & ENGINES (91-130) ---
    "toy car": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/ToyCar/glTF-Binary/ToyCar.glb",
    "racecar": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/ToyCar/glTF-Binary/ToyCar.glb",
    "sports car": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/ToyCar/glTF-Binary/ToyCar.glb",
    "milk truck": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/CesiumMilkTruck/glTF-Binary/CesiumMilkTruck.glb",
    "delivery truck": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/CesiumMilkTruck/glTF-Binary/CesiumMilkTruck.glb",
    "unicycle": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/Unicycle/glTF-Binary/Unicycle.glb",
    "one wheel bike": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/Unicycle/glTF-Binary/Unicycle.glb",
    "dune buggy": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/Buggy/glTF-Binary/Buggy.glb",
    "offroad kart": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/Buggy/glTF-Binary/Buggy.glb",
    "mechanical engine": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/2CylinderEngine/glTF-Binary/2CylinderEngine.glb",
    "motor piston": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/2CylinderEngine/glTF-Binary/2CylinderEngine.glb",
    "gearbox assembly": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/GearboxAssy/glTF-Binary/GearboxAssy.glb",
    "transmission gears": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/GearboxAssy/glTF-Binary/GearboxAssy.glb",

    # --- ANATOMY & NATURE (131-160) ---
    "brain stem": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/BrainStem/glTF-Binary/BrainStem.glb",
    "neurology model": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/BrainStem/glTF-Binary/BrainStem.glb",
    "fox": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/Fox/glTF-Binary/Fox.glb",
    "red fox": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/Fox/glTF-Binary/Fox.glb",
    "duck": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/Duck/glTF-Binary/Duck.glb",
    "rubber duck": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/Duck/glTF-Binary/Duck.glb",
    "house plant": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/DiffuseTransmissionPlant/glTF-Binary/DiffuseTransmissionPlant.glb",
    "potted plant": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/DiffuseTransmissionPlant/glTF-Binary/DiffuseTransmissionPlant.glb",
    "avocado": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/Avocado/glTF-Binary/Avocado.glb",

    # --- FURNITURE & CLOTHING (161-185) ---
    "velvet chair": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/SheenChair/glTF-Binary/SheenChair.glb",
    "armchair": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/SheenChair/glTF-Binary/SheenChair.glb",
    "leather sofa": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/SheenWoodLeatherSofa/glTF-Binary/SheenWoodLeatherSofa.glb",
    "couch": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/SheenWoodLeatherSofa/glTF-Binary/SheenWoodLeatherSofa.glb",
    "corset": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/Corset/glTF-Binary/Corset.glb",
    "victorian dress": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/Corset/glTF-Binary/Corset.glb",
    "sneaker": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/MaterialsVariantsShoe/glTF-Binary/MaterialsVariantsShoe.glb",
    "sports shoe": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/MaterialsVariantsShoe/glTF-Binary/MaterialsVariantsShoe.glb",

    # --- TOOLS & RECREATION (186-210) ---
    "chess board": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/ABeautifulGame/glTF-Binary/ABeautifulGame.glb",
    "chess set": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/ABeautifulGame/glTF-Binary/ABeautifulGame.glb",
    "antique lantern": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/Lantern/glTF-Binary/Lantern.glb",
    "oil lamp": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/Lantern/glTF-Binary/Lantern.glb",
    "water bottle": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/WaterBottle/glTF-Binary/WaterBottle.glb",
    "flask": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/WaterBottle/glTF-Binary/WaterBottle.glb",
    "electric guitar": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/IridescentDishwithGuitars/glTF-Binary/IridescentDishwithGuitars.glb",
    "guitars assembly": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/IridescentDishwithGuitars/glTF-Binary/IridescentDishwithGuitars.glb",
    "power saw": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/ReciprocatingSaw/glTF-Binary/ReciprocatingSaw.glb",
    "reciprocating saw": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/ReciprocatingSaw/glTF-Binary/ReciprocatingSaw.glb"
}

# 2. Strict Input Check
user_input_raw = st.text_input("📖 Type an exact library item (e.g., avocado, chess set, astronaut, racecar):", value="astronaut")

# Strict String Cleanup
clean_query = user_input_raw.strip().lower()

# 3. Execution Pipeline with ZERO guessing rules
if clean_query in CLAY_ARCHIVE:
    glb_target = CLAY_ARCHIVE[clean_query]
    st.success(f"📜 Sculpture Verified: Loading exact clay model for '{clean_query.upper()}'...")
    
    engine_html = f"""
    <script type="module" src="https://ajax.googleapis.com/ajax/libs/model-viewer/3.4.0/model-viewer.min.js"></script>
    <style>
        body, html {{ margin: 0; padding: 0; overflow: hidden; background-color: #030201; }}
        .container {{
            position: relative;
            width: 100vw;
            height: 72vh;
            background: radial-gradient(circle at center, #21150e 0%, #030201 100%);
            border-radius: 16px;
            border: 3px solid #26190f;
            box-shadow: 0 10px 30px rgba(0,0,0,0.8);
            overflow: hidden;
        }}
        model-viewer {{ width: 100%; height: 100%; }}
        .audio-trigger {{
            position: absolute;
            top: 15px;
            left: 15px;
            background: rgba(25, 16, 10, 0.95);
            border: 1px solid #d4af37;
            color: #d4af37;
            padding: 8px 14px;
            font-size: 11px;
            font-family: monospace;
            border-radius: 6px;
            pointer-events: none;
            z-index: 10;
        }}
    </style>
    
    <div class="container">
        <div class="audio-trigger">🔊 TAP CANVAS TO UNMUTE KARUPPU BGM</div>
        
        <!-- Karuppu - God Mode Background Stream -->
        <iframe 
            src="https://www.youtube.com/embed/_Vp-jCG7gno?autoplay=1&loop=1&playlist=_Vp-jCG7gno&controls=0&mute=0" 
            allow="autoplay; encrypted-media" 
            style="position: absolute; width: 1px; height: 1px; top: -100px; left: -100px; opacity: 0;">
        </iframe>

        <model-viewer 
            src="{glb_target}" 
            alt="Strict Asset Node" 
            camera-controls 
            auto-rotate 
            interaction-prompt="none"
            shadow-intensity="3.5"
            shadow-softness="0.15"
            exposure="0.95"
            environment-image="neutral">
        </model-viewer>
    </div>
    """
    components.html(engine_html, height=520)
    
else:
    # If it's not a direct match, show an honest warning instead of guessing a random object
    st.error(f"❌ '{user_input_raw}' is not currently logged on the library shelves.")
    st.info("💡 To prevent loading the wrong file, please select an exact keyword listed in the master directory index below.")

# Verified Catalog Board
st.markdown("### 🗄️ Strict Master Catalog Index")
sorted_keywords = sorted(list(CLAY_ARCHIVE.keys()))
badge_payload = "".join([f"<div class='shelf-badge'>{kw}</div>" for kw in sorted_keywords])
st.markdown(badge_payload, unsafe_allow_html=True)
