import streamlit as st
import streamlit.components.v1 as components

# Set up the look and feel of your app
st.set_page_config(page_title="KingPro 3D Engine", layout="centered")

st.markdown("<h1 style='text-align: center; color: #4F46E5;'>👑 KingPro 3D Asset Engine</h1>", unsafe_safe=True)
st.markdown("<p style='text-align: center;'>Type an object name below to load and view its 3D model instantly on your tablet.</p>", unsafe_safe=True)

# -------------------------------------------------------------
# THE MEGA 3D ASSET DICTIONARY
# Maps user search terms to open-source, production-ready GLB files
# -------------------------------------------------------------
ASSET_DATABASE = {
    # Animals & Nature
    "duck": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/Duck/glTF-Binary/Duck.glb",
    "fish": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/BarramundiFish/glTF-Binary/BarramundiFish.glb",
    "avocado": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/Avocado/glTF-Binary/Avocado.glb",
    "plant": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/DiffuseTransmissionPlant/glTF-Binary/DiffuseTransmissionPlant.glb",
    "fox": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/Fox/glTF-Binary/Fox.glb",
    
    # Furniture & Home
    "chair": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/SheenChair/glTF-Binary/SheenChair.glb",
    "sofa": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/SheenWoodLeatherSofa/glTF-Binary/SheenWoodLeatherSofa.glb",
    "couch": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/SheenWoodLeatherSofa/glTF-Binary/SheenWoodLeatherSofa.glb",
    "lamp": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/AnisotropyBarnLamp/glTF-Binary/AnisotropyBarnLamp.glb",
    "lantern": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/LanternPole/glTF-Binary/LanternPole.glb",
    "cushion": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/SpecularSilkPouf/glTF-Binary/SpecularSilkPouf.glb",
    "pillow": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/SpecularSilkPouf/glTF-Binary/SpecularSilkPouf.glb",
    "teacup": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/DiffuseTransmissionTeacup/glTF-Binary/DiffuseTransmissionTeacup.glb",
    "cup": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/DiffuseTransmissionTeacup/glTF-Binary/DiffuseTransmissionTeacup.glb",
    
    # Vehicles & Sci-Fi / Gear
    "car": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/ToyCar/glTF-Binary/ToyCar.glb",
    "truck": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/CesiumMilkTruck/glTF-Binary/CesiumMilkTruck.glb",
    "helmet": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/DamagedHelmet/glTF-Binary/DamagedHelmet.glb",
    "flight helmet": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/FlightHelmet/glTF-Binary/FlightHelmet.glb",
    "scifi helmet": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/DamagedHelmet/glTF-Binary/DamagedHelmet.glb",
    
    # Electronics & Tools
    "boombox": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/BoomBox/glTF-Binary/BoomBox.glb",
    "radio": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/BoomBox/glTF-Binary/BoomBox.glb",
    "watch": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/ChronographWatch/glTF-Binary/ChronographWatch.glb",
    "clock": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/ChronographWatch/glTF-Binary/ChronographWatch.glb",
    "camera": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/AntiqueCamera/glTF-Binary/AntiqueCamera.glb",
    "microphone": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/Microphone/glTF-Binary/Microphone.glb",
    
    # Clothes & Accessories
    "shoe": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/MaterialsVariantsShoe/glTF-Binary/MaterialsVariantsShoe.glb",
    "sneaker": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/MaterialsVariantsShoe/glTF-Binary/MaterialsVariantsShoe.glb",
    "sunglasses": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/SunglassesKhronos/glTF-Binary/SunglassesKhronos.glb",
    "glasses": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/SunglassesKhronos/glTF-Binary/SunglassesKhronos.glb",
    "bag": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/WaterBottle/glTF-Binary/WaterBottle.glb",
    
    # Miscellaneous / Games
    "chess": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/ABeautifulGame/glTF-Binary/ABeautifulGame.glb",
    "game": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/ABeautifulGame/glTF-Binary/ABeautifulGame.glb",
    "bottle": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/WaterBottle/glTF-Binary/WaterBottle.glb",
    "cube": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/BoxTextured/glTF-Binary/BoxTextured.glb",
    "box": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/BoxTextured/glTF-Binary/BoxTextured.glb",
    "brain": "https://raw.githubusercontent.com/KhronosGroup/glTF-Sample-Assets/main/Models/BrainStem/glTF-Binary/BrainStem.glb",
    "astronaut": "https://modelviewer.dev/shared-assets/models/Astronaut.glb"
}

# -------------------------------------------------------------
# USER INPUT HANDLING & SMART CLEANING
# -------------------------------------------------------------
user_query = st.text_input("Enter what you want to see:", value="astronaut")

# Clean the search term so it matches dictionary keys seamlessly
clean_query = user_query.strip().lower()

# Quick check to automatically handle plurals (e.g., matching "cars" to "car")
if clean_query not in ASSET_DATABASE and clean_query.endswith('s'):
    clean_query = clean_query[:-1]

# -------------------------------------------------------------
# 3D RENDER ENGINE (Google <model-viewer> Integration)
# -------------------------------------------------------------
if clean_query in ASSET_DATABASE:
    selected_model_url = ASSET_DATABASE[clean_query]
    st.success(f"Success! Rendering the 3D model for: '{user_query}'")
    
    # This raw HTML piece injects Google's ultra-smooth web renderer 
    html_code = f"""
    <script type="module" src="https://ajax.googleapis.com/ajax/libs/model-viewer/3.4.0/model-viewer.min.js"></script>
    <style>
        body {{ margin: 0; padding: 0; background-color: #f8fafc; }}
        model-viewer {{
            width: 100vw;
            height: 90vh;
            background-color: #f1f5f9;
            border-radius: 12px;
            box-shadow: inset 0 2px 4px 0 rgba(0, 0, 0, 0.06);
        }}
    </style>
    <model-viewer 
        src="{selected_model_url}" 
        alt="A 3D model of a {clean_query}" 
        ar 
        ar-modes="webxr scene-viewer quick-look" 
        camera-controls 
        auto-rotate 
        shadow-intensity="1.5"
        shadow-softness="1">
    </model-viewer>
    """
    # Render component safely sized for standard tablet screen orientations
    components.html(html_code, height=550)

else:
    # If they typed something we haven't mapped yet, show them what is available
    st.warning(f"Sorry, we don't have a free 3D model for '{user_query}' mapped yet.")
    st.markdown("### Try searching for one of these words:")
    
    # Generate clean, clickable suggestion blocks grouped for readability
    available_words = sorted(list(ASSET_DATABASE.keys()))
    st.info(", ".join(available_words))

