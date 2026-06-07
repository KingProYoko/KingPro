import streamlit as st
import streamlit.components.v1 as components

# 1. High-Performance Page Configuration
st.set_page_config(
    page_title="KingPro.Ai Mega Spawner",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Premium Core Cinematic Dark UI Design
st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle at center, #0d0d14 0%, #040406 100%);
        color: #e2e8f0;
    }
    h1, h2, h3 {
        color: #ffffff !important;
        font-family: 'Inter', sans-serif;
        font-weight: 900;
        letter-spacing: -1.5px;
        text-shadow: 0 0 20px rgba(0, 255, 204, 0.2);
    }
    .stTextInput div div input {
        background-color: #11111c !important;
        color: #00ffcc !important;
        border: 2px solid #1f1f2e !important;
        border-radius: 12px !important;
        font-size: 20px !important;
        padding: 14px !important;
        font-family: monospace;
    }
    .stTextInput div div input:focus {
        border-color: #00ffcc !important;
        box-shadow: 0 0 25px rgba(0, 255, 204, 0.3) !important;
    }
    .badge {
        background: #161622;
        color: #94a3b8;
        padding: 6px 12px;
        border-radius: 6px;
        font-size: 12px;
        font-family: monospace;
        border: 1px solid #27273a;
        margin: 4px;
        display: inline-block;
    }
    </style>
""", unsafe_allow_html=True)

st.title("👑 KingPro.Ai // Ultimate Universal 3D Asset Spawner")
st.caption("SYSTEM STATE: OPTIMAL | DATA_ARRAY: EXPANDED MEGA-MATRIX | CLOUD NODE: ACTIVE")

# ----------------------------------------------------------------------
# THE MASSIVE UNIVERSAL 3D ASSET INDEX
# Hardcoding a massive library mapping keys & global variations to raw production GLBs
# ----------------------------------------------------------------------
UNIVERSAL_MATRIX = {
    # --- LIVING WORLD & BIOLOGY ---
    "duck": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/Duck/glTF-Binary/Duck.glb",
    "rubber duck": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/Duck/glTF-Binary/Duck.glb",
    "bird": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/Duck/glTF-Binary/Duck.glb",
    
    "fish": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/BarramundiFish/glTF-Binary/BarramundiFish.glb",
    "salmon": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/BarramundiFish/glTF-Binary/BarramundiFish.glb",
    "shark": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/BarramundiFish/glTF-Binary/BarramundiFish.glb",
    "seafood": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/BarramundiFish/glTF-Binary/BarramundiFish.glb",
    
    "fox": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/Fox/glTF-Binary/Fox.glb",
    "animal": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/Fox/glTF-Binary/Fox.glb",
    "dog": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/Fox/glTF-Binary/Fox.glb",
    
    "plant": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/DiffuseTransmissionPlant/glTF-Binary/DiffuseTransmissionPlant.glb",
    "flower": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/DiffuseTransmissionPlant/glTF-Binary/DiffuseTransmissionPlant.glb",
    "tree": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/DiffuseTransmissionPlant/glTF-Binary/DiffuseTransmissionPlant.glb",
    "leaf": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/DiffuseTransmissionPlant/glTF-Binary/DiffuseTransmissionPlant.glb",
    "pot": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/DiffuseTransmissionPlant/glTF-Binary/DiffuseTransmissionPlant.glb",
    
    "avocado": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/Avocado/glTF-Binary/Avocado.glb",
    "fruit": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/Avocado/glTF-Binary/Avocado.glb",
    "apple": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/Avocado/glTF-Binary/Avocado.glb",
    "pear": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/Avocado/glTF-Binary/Avocado.glb",
    "food": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/Avocado/glTF-Binary/Avocado.glb",

    # --- ARCHITECTURE, FURNITURE & HOUSEHOLD INTERIORS ---
    "chair": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/SheenChair/glTF-Binary/SheenChair.glb",
    "armchair": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/SheenChair/glTF-Binary/SheenChair.glb",
    "seat": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/SheenChair/glTF-Binary/SheenChair.glb",
    "furniture": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/SheenChair/glTF-Binary/SheenChair.glb",
    "stool": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/SheenChair/glTF-Binary/SheenChair.glb",
    
    "sofa": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/SheenWoodLeatherSofa/glTF-Binary/SheenWoodLeatherSofa.glb",
    "couch": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/SheenWoodLeatherSofa/glTF-Binary/SheenWoodLeatherSofa.glb",
    "bench": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/SheenWoodLeatherSofa/glTF-Binary/SheenWoodLeatherSofa.glb",
    "lounge": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/SheenWoodLeatherSofa/glTF-Binary/SheenWoodLeatherSofa.glb",
    
    "lamp": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/AnisotropyBarnLamp/glTF-Binary/AnisotropyBarnLamp.glb",
    "light": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/AnisotropyBarnLamp/glTF-Binary/AnisotropyBarnLamp.glb",
    "bulb": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/AnisotropyBarnLamp/glTF-Binary/AnisotropyBarnLamp.glb",
    "chandelier": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/AnisotropyBarnLamp/glTF-Binary/AnisotropyBarnLamp.glb",
    
    "lantern": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/LanternPole/glTF-Binary/LanternPole.glb",
    "torch": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/LanternPole/glTF-Binary/LanternPole.glb",
    "streetlamp": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/LanternPole/glTF-Binary/LanternPole.glb",
    "post": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/LanternPole/glTF-Binary/LanternPole.glb",
    
    "pillow": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/SpecularSilkPouf/glTF-Binary/SpecularSilkPouf.glb",
    "cushion": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/SpecularSilkPouf/glTF-Binary/SpecularSilkPouf.glb",
    "bedding": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/SpecularSilkPouf/glTF-Binary/SpecularSilkPouf.glb",
    "pouf": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/SpecularSilkPouf/glTF-Binary/SpecularSilkPouf.glb",
    
    "cup": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/DiffuseTransmissionTeacup/glTF-Binary/DiffuseTransmissionTeacup.glb",
    "teacup": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/DiffuseTransmissionTeacup/glTF-Binary/DiffuseTransmissionTeacup.glb",
    "mug": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/DiffuseTransmissionTeacup/glTF-Binary/DiffuseTransmissionTeacup.glb",
    "glass": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/DiffuseTransmissionTeacup/glTF-Binary/DiffuseTransmissionTeacup.glb",
    "coffee": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/DiffuseTransmissionTeacup/glTF-Binary/DiffuseTransmissionTeacup.glb",

    # --- VEHICLES, SCI-FI APPARATUS & WARFARE ---
    "car": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/ToyCar/glTF-Binary/ToyCar.glb",
    "racecar": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/ToyCar/glTF-Binary/ToyCar.glb",
    "sportscar": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/ToyCar/glTF-Binary/ToyCar.glb",
    "vehicle": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/ToyCar/glTF-Binary/ToyCar.glb",
    "automobile": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/ToyCar/glTF-Binary/ToyCar.glb",
    
    "truck": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/CesiumMilkTruck/glTF-Binary/CesiumMilkTruck.glb",
    "lorry": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/CesiumMilkTruck/glTF-Binary/CesiumMilkTruck.glb",
    "van": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/CesiumMilkTruck/glTF-Binary/CesiumMilkTruck.glb",
    "milktruck": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/CesiumMilkTruck/glTF-Binary/CesiumMilkTruck.glb",
    
    "helmet": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/DamagedHelmet/glTF-Binary/DamagedHelmet.glb",
    "cyber helmet": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/DamagedHelmet/glTF-Binary/DamagedHelmet.glb",
    "armor": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/DamagedHelmet/glTF-Binary/DamagedHelmet.glb",
    "scifi helmet": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/DamagedHelmet/glTF-Binary/DamagedHelmet.glb",
    
    "flight helmet": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/FlightHelmet/glTF-Binary/FlightHelmet.glb",
    "pilot helmet": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/FlightHelmet/glTF-Binary/FlightHelmet.glb",
    "jet helmet": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/FlightHelmet/glTF-Binary/FlightHelmet.glb",
    "aviation": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/FlightHelmet/glTF-Binary/FlightHelmet.glb",

    # --- CONSUMER ELECTRONICS & MECHANICAL HARDWARE ---
    "boombox": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/BoomBox/glTF-Binary/BoomBox.glb",
    "radio": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/BoomBox/glTF-Binary/BoomBox.glb",
    "stereo": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/BoomBox/glTF-Binary/BoomBox.glb",
    "speaker": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/BoomBox/glTF-Binary/BoomBox.glb",
    "player": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/BoomBox/glTF-Binary/BoomBox.glb",
    
    "watch": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/ChronographWatch/glTF-Binary/ChronographWatch.glb",
    "clock": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/ChronographWatch/glTF-Binary/ChronographWatch.glb",
    "timer": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/ChronographWatch/glTF-Binary/ChronographWatch.glb",
    "chronograph": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/ChronographWatch/glTF-Binary/ChronographWatch.glb",
    
    "camera": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/AntiqueCamera/glTF-Binary/AntiqueCamera.glb",
    "lens": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/AntiqueCamera/glTF-Binary/AntiqueCamera.glb",
    "photo": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/AntiqueCamera/glTF-Binary/AntiqueCamera.glb",
    "video": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/AntiqueCamera/glTF-Binary/AntiqueCamera.glb",
    
    "microphone": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/Microphone/glTF-Binary/Microphone.glb",
    "mic": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/Microphone/glTF-Binary/Microphone.glb",
    "audio": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/Microphone/glTF-Binary/Microphone.glb",
    "studio": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/Microphone/glTF-Binary/Microphone.glb",

    # --- APPAREL, LUXURY COUTURE & APPOINTMENTS ---
    "shoe": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/MaterialsVariantsShoe/glTF-Binary/MaterialsVariantsShoe.glb",
    "sneaker": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/MaterialsVariantsShoe/glTF-Binary/MaterialsVariantsShoe.glb",
    "boot": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/MaterialsVariantsShoe/glTF-Binary/MaterialsVariantsShoe.glb",
    "footwear": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/MaterialsVariantsShoe/glTF-Binary/MaterialsVariantsShoe.glb",
    
    "sunglasses": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/SunglassesKhronos/glTF-Binary/SunglassesKhronos.glb",
    "glasses": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/SunglassesKhronos/glTF-Binary/SunglassesKhronos.glb",
    "spectacles": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/SunglassesKhronos/glTF-Binary/SunglassesKhronos.glb",
    "shades": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/SunglassesKhronos/glTF-Binary/SunglassesKhronos.glb",

    # --- GAMES, MISC CONTAINERS & COMPLEX GEOMETRY ---
    "chess": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/ABeautifulGame/glTF-Binary/ABeautifulGame.glb",
    "game": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/ABeautifulGame/glTF-Binary/ABeautifulGame.glb",
    "chessboard": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/ABeautifulGame/glTF-Binary/ABeautifulGame.glb",
    "boardgame": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/ABeautifulGame/glTF-Binary/ABeautifulGame.glb",
    
    "bottle": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/WaterBottle/glTF-Binary/WaterBottle.glb",
    "flask": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/WaterBottle/glTF-Binary/WaterBottle.glb",
    "waterbottle": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/WaterBottle/glTF-Binary/WaterBottle.glb",
    "bag": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/WaterBottle/glTF-Binary/WaterBottle.glb",
    
    "cube": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/BoxTextured/glTF-Binary/BoxTextured.glb",
    "box": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/BoxTextured/glTF-Binary/BoxTextured.glb",
    "crate": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/BoxTextured/glTF-Binary/BoxTextured.glb",
    "block": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/BoxTextured/glTF-Binary/BoxTextured.glb",
    
    "brain": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/BrainStem/glTF-Binary/BrainStem.glb",
    "stem": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/BrainStem/glTF-Binary/BrainStem.glb",
    "anatomy": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/BrainStem/glTF-Binary/BrainStem.glb",
    
    "astronaut": "https://modelviewer.dev/shared-assets/models/Astronaut.glb",
    "cosmonaut": "https://modelviewer.dev/shared-assets/models/Astronaut.glb",
    "spaceman": "https://modelviewer.dev/shared-assets/models/Astronaut.glb",
    "space": "https://modelviewer.dev/shared-assets/models/Astronaut.glb"
}

# 3. Smart User Input Entry Bar
user_raw_input = st.text_input("🔮 Type any object name (e.g., racecar, plant, scifi helmet, couch):", value="astronaut")

# 4. Fuzzy Semantic Parsing Engine
# Standardizing entry string parameters to ignore plural forms and messy whitespace
processed_query = user_raw_input.strip().lower()

# Plural stripping engine (e.g., fixes "chairs" -> "chair")
if processed_query not in UNIVERSAL_MATRIX and processed_query.endswith('s'):
    processed_query = processed_query[:-1]

# Fallback match check (Looks if the word contains or is contained in an active core key)
matched_target_key = None
if processed_query in UNIVERSAL_MATRIX:
    matched_target_key = processed_query
else:
    for dictionary_key in UNIVERSAL_MATRIX.keys():
        if dictionary_key in processed_query or processed_query in dictionary_key:
            matched_target_key = dictionary_key
            break

# 5. Asset Compilation & Render Injection Pipeline
if matched_target_key:
    selected_glb_url = UNIVERSAL_MATRIX[matched_target_key]
    st.success(f"⚡ Synthesis Operational: Materialized '{matched_target_key.upper()}' Matrix Vector Node.")
    
    # Advanced WebGL HTML Framework utilizing Google's WebXR Engine
    html_rendering_block = f"""
    <script type="module" src="https://ajax.googleapis.com/ajax/libs/model-viewer/3.4.0/model-viewer.min.js"></script>
    <style>
        body {{ margin: 0; padding: 0; background-color: #040406; overflow: hidden; }}
        model-viewer {{
            width: 100vw;
            height: 85vh;
            background: radial-gradient(circle at center, #141424 0%, #040406 100%);
            border-radius: 16px;
            border: 1px solid #1e1e2f;
        }}
    </style>
    <model-viewer 
        src="{selected_glb_url}" 
        alt="KingPro Matrix node: {matched_target_key}" 
        ar 
        ar-modes="webxr scene-viewer quick-look" 
        camera-controls 
        auto-rotate 
        interaction-prompt="auto"
        shadow-intensity="2"
        shadow-softness="0.7"
        exposure="1.2">
    </model-viewer>
    """
    components.html(html_rendering_block, height=580)
    
else:
    # Error safety grid showing the extensive core matrix categories to choose from
    st.warning(f"⚠️ Vector string '{user_raw_input}' is currently out of structural bounds.")
    st.markdown("### 🗂️ Map an active Vector from the core inventory array:")
    
    # Render all active tracking keywords beautifully grouped into visual modules
    categorized_words = sorted(list(set(UNIVERSAL_MATRIX.keys())))
    
    badge_html = "".join([f"<div class='badge'>{word}</div>" for word in categorized_words])
    st.markdown(badge_html, unsafe_allow_html=True)

st.markdown("---")
st.markdown("<p style='text-align: center; color: #33334d; font-family: monospace;'>KingPro Core Engine Matrix Node v4.0.0 • Total Lines Compliant</p>", unsafe_allow_html=True)
