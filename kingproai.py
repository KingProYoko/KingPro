
import streamlit as st
import streamlit.components.v1 as components

# 1. Page Configuration & Theme
st.set_page_config(
    page_title="KingPro.Ai 3D Engine",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS to inject the KingPro dark, premium theme
st.markdown("""
    <style>
    /* Deep space background */
    .stApp {
        background: radial-gradient(circle at center, #111118 0%, #07070a 100%);
        color: #e0e0e0;
    }
    /* Sleek sidebar / headers */
    h1, h2, h3 {
        color: #ffffff !important;
        font-family: 'Inter', sans-serif;
        font-weight: 700;
        letter-spacing: -0.5px;
    }
    /* Custom input box styling */
    .stTextInput div div input {
        background-color: #1a1a26 !important;
        color: #00ffcc !important;
        border: 1px solid #33334d !important;
        border-radius: 8px !important;
        font-size: 18px !important;
    }
    .stTextInput div div input:focus {
        border-color: #00ffcc !important;
        box-shadow: 0 0 10px rgba(0, 255, 204, 0.5) !important;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Header Architecture
st.title("👑 KingPro.Ai // 3D Object Spawner")
st.caption("SYSTEM STATUS: ONLINE | CORE: THREE.JS WEBGL | ARCHITECTURE: PREMIUM")
st.write("Type an object name below (e.g., `cube`, `sphere`, `torus`, `cone`, `cylinder`) to generate it dynamically in 3D space.")

# 3. User Input
user_object = st.text_input("🔮 Enter Object Core Vector Name:", value="torus").strip().lower()

# Map user input to Three.js Geometries
geometry_mapping = {
    "cube": "THREE.BoxGeometry(2, 2, 2)",
    "box": "THREE.BoxGeometry(2, 2, 2)",
    "sphere": "THREE.SphereGeometry(1.5, 32, 32)",
    "torus": "THREE.TorusGeometry(1, 0.4, 16, 100)",
    "donut": "THREE.TorusGeometry(1, 0.4, 16, 100)",
    "cone": "THREE.ConeGeometry(1.5, 3, 32)",
    "cylinder": "THREE.CylinderGeometry(1, 1, 3, 32)"
}

# Default back to a cube if they type something unsupported natively
selected_geometry = geometry_mapping.get(user_object, "THREE.BoxGeometry(2, 2, 2)")

if user_object not in geometry_mapping and user_object != "":
    st.sidebar.warning(f"⚠️ '{user_object}' unknown. Defaulting to Core Cube Matrix.")

# 4. Embedded Three.js Engine (HTML/JS)
three_js_code = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        body {{
            margin: 0;
            overflow: hidden;
            background-color: #07070a;
            font-family: sans-serif;
        }}
        #canvas-container {{
            width: 100vw;
            height: 600px;
            position: relative;
        }}
        #overlay-ui {{
            position: absolute;
            top: 15px;
            left: 15px;
            color: #00ffcc;
            font-family: monospace;
            font-size: 12px;
            text-shadow: 0 0 5px rgba(0,255,204,0.8);
            pointer-events: none;
        }}
    </style>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
</head>
<body>

    <div id="canvas-container">
        <div id="overlay-ui">RENDER_TARGET: {user_object.upper()} // ACTIVE_GRID: TRUE</div>
    </div>

    <script>
        // Setup Scene, Camera, Renderer
        const container = document.getElementById('canvas-container');
        const scene = new THREE.Scene();
        scene.background = new THREE.Color(0x07070a);
        
        const camera = new THREE.PerspectiveCamera(45, container.clientWidth / 600, 0.1, 1000);
        camera.position.z = 6;
        camera.position.y = 2;
        camera.lookAt(0,0,0);

        const renderer = new THREE.WebGLRenderer({{ antialias: true }});
        renderer.setSize(container.clientWidth, 600);
        container.appendChild(renderer.domElement);

        // Add Premium Holographic Matrix Grid
        const gridHelper = new THREE.GridHelper(20, 20, 0x00ffcc, 0x222233);
        gridHelper.position.y = -2;
        scene.add(gridHelper);

        // Enhanced Studio Lighting
        const ambientLight = new THREE.AmbientLight(0xffffff, 0.2);
        scene.add(ambientLight);

        const cyanLight = new THREE.PointLight(0x00ffcc, 1.5, 50);
        cyanLight.position.set(5, 5, 5);
        scene.add(cyanLight);

        const magentaLight = new THREE.PointLight(0xff00ff, 1.2, 50);
        magentaLight.position.set(-5, 3, -5);
        scene.add(magentaLight);

        // Dynamically Spawn User Requested Geometry
        const geometry = new {selected_geometry};
        
        // Premium cyber-mesh material
        const material = new THREE.MeshStandardMaterial({{
            color: 0x111122,
            roughness: 0.1,
            metalness: 0.8,
            wireframe: false,
            flatShading: false
        }});

        const mesh = new THREE.Mesh(geometry, material);
        scene.add(mesh);

        // Add Glowing Wireframe Overlay
        const wireframeGeom = new THREE.WireframeGeometry(geometry);
        const wireframeMat = new THREE.LineBasicMaterial({{ color: 0x00ffcc, linewidth: 1.5 }});
        const wireframe = new THREE.LineSegments(wireframeGeom, wireframeMat);
        mesh.add(wireframe);

        // Animation Loop
        function animate() {{
            requestAnimationFrame(animate);
            
            // Kinetic rotation matrix
            mesh.rotation.x += 0.005;
            mesh.rotation.y += 0.01;
            
            // Subtle floating levitation effect
            mesh.position.y = Math.sin(Date.now() * 0.0015) * 0.15;

            renderer.render(scene, camera);
        }}

        // Handle Responsive Resize
        window.addEventListener('resize', () => {{
            const width = container.clientWidth;
            camera.aspect = width / 600;
            camera.updateProjectionMatrix();
            renderer.setSize(width, 600);
        }});

        animate();
    </script>
</body>
</html>
"""

# 5. Render Engine inside the tab
components.html(three_js_code, height=600)

# Footer Brand
st.markdown("---")
st.markdown("<p style='text-align: center; color: #444466;'>KingPro.Ai Core Engine Engine Node v1.0.1 • Powered by WebGL</p>", unsafe_allow_html=True)