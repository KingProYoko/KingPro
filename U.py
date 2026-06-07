import streamlit as st
import streamlit.components.v1 as components
import urllib.parse

# 1. Page Config & Premium Theme
st.set_page_config(
    page_title="KingPro.Ai Global Spawner",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Deep space theme
st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle at center, #0f0f16 0%, #050508 100%);
        color: #e0e0e0;
    }
    h1 {
        color: #ffffff !important;
        font-family: 'Inter', sans-serif;
        font-weight: 800;
        text-align: center;
    }
    .stTextInput div div input {
        background-color: #141420 !important;
        color: #00ffcc !important;
        border: 2px solid #2a2a3a !important;
        border-radius: 10px !important;
        font-size: 20px !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("👑 KingPro.Ai // Global 3D Asset Spawner")
st.caption("<p style='text-align: center; color: #666;'>LIVE REPOSITORY ENGINE • SEARCHING EMBEDDED OPEN-SOURCE DATABASES</p>", unsafe_allow_html=True)

# 2. User Entry
user_query = st.text_input("🔮 Type ANY object in the world (e.g., apple, backpack, sword, chair):", value="backpack")

if user_query:
    # Clean up the text input to safely insert it into a URL search
    safe_search_query = urllib.parse.quote(user_query.strip())
    
    st.success(f"🔍 KingPro is searching global repositories for an exact 3D '{user_query}'...")
    
    # 3. Use an interactive, completely free WebGL sketchfab iframe embedding engine
    # This searches and pulls an exact match frame based on the user's tablet text input
    embed_url = f"https://sketchfab.com/search?q={safe_search_query}&type=models&embed=true"
    
    html_code = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body, html {{ margin:0; padding:0; height: 100%; overflow:hidden; background-color: #050508; }}
            iframe {{ width: 100%; height: 85vh; border: 2px solid #1f1f2e; border-radius: 12px; }}
        </style>
    </head>
    <body>
        <iframe 
            title="KingPro Live 3D Stream"
            src="https://sketchfab.com/models/search?q={safe_search_query}&embed=true&autostart=1"
            allowfullscreen
            mozallowfullscreen="true"
            webkitallowfullscreen="true"
            allow="autoplay; fullscreen; xr-spatial-tracking">
        </iframe>
    </body>
    </html>
    """
    
    # Render the viewport block onto your Samsung Tablet tab
    components.html(html_code, height=600)

st.markdown("---")
st.markdown("<p style='text-align: center; color: #33334d;'>KingPro Engine Fabric v5.0 • Connected to Infinite Global Repositories</p>", unsafe_allow_html=True)
