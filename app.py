import streamlit as st
import pandas as pd
import random
import time

# ------------------------------
# PAGE CONFIG & LOGIN
# ------------------------------
st.set_page_config(page_title="K8s Dashboard Simulator", layout="wide")

def show_earth_symbol(width=100):
    st.markdown(
        f"""
        <div style="display: flex; justify-content: center; margin-bottom: 1rem;">
            <span style="font-size: {width}px;">🌍</span>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.caption("GlobalInternet.py – Earth symbol")

# Authentication
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(135deg, #0b3d5f, #1a6d8f);
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.title("🔐 Login Required")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        show_earth_symbol(150)
        st.markdown("<h2 style='text-align: center;'>Kubernetes Dashboard Simulator</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>by GlobalInternet.py</p>", unsafe_allow_html=True)
        password_input = st.text_input("Enter password to access", type="password")
        if st.button("Login"):
            if password_input == "20082010":
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("Incorrect password. Access denied.")
    st.stop()

# ------------------------------
# AFTER LOGIN – MAIN APP (blue theme)
# ------------------------------
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #0b3d5f, #1a6d8f);
    }
    .main-header {
        background: rgba(255,255,255,0.1);
        padding: 1.5rem;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 1rem;
        backdrop-filter: blur(5px);
    }
    .main-header h1 { color: white; margin: 0; font-size: 2.5rem; }
    .main-header p { color: #FFD700; margin: 0; font-size: 1.1rem; }
    .card {
        background: rgba(255,255,255,0.15);
        border-radius: 15px;
        padding: 1rem;
        margin: 0.5rem 0;
        color: white;
    }
    .footer { text-align: center; color: #ccc; margin-top: 2rem; padding-top: 1rem; border-top: 1px solid #ccc; }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("""
<div class="main-header">
    <h1>🌍 Kubernetes Dashboard Simulator</h1>
    <p>Visualize pods, deployments, services, and nodes in a simulated cluster</p>
</div>
""", unsafe_allow_html=True)

col_flag, col_title = st.columns([1, 3])
with col_flag:
    show_earth_symbol(120)
with col_title:
    st.markdown("<p style='font-size:1.1rem; color:white;'>🔧 Simulated Kubernetes environment – learn container orchestration concepts.</p>", unsafe_allow_html=True)

# ------------------------------
# SIDEBAR – COMPANY INFO & LOGOUT
# ------------------------------
with st.sidebar:
    st.markdown("## 🌍 GlobalInternet.py")
    show_earth_symbol(80)
    st.markdown("### K8s Dashboard")
    st.markdown("---")
    st.markdown("**Founder & Developer:**")
    st.markdown("Gesner Deslandes")
    st.markdown("📞 **WhatsApp:** [509 4738-5663](https://wa.me/50947385663)")
    st.markdown("📧 **Email:** deslandes78@gmail.com")
    st.markdown("🌐 **Main website:** [globalinternetsitepy...](https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/)")
    st.markdown("---")
    st.markdown("### 💰 Price")
    st.markdown("**$1,200 USD** (one‑time license, includes source code, setup, and 1 year support)")
    st.markdown("---")
    st.markdown("### © 2025 GlobalInternet.py")
    st.markdown("All Rights Reserved")
    st.markdown("---")
    if st.button("🚪 Logout", use_container_width=True):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

# ------------------------------
# MULTI-LANGUAGE SUPPORT
# ------------------------------
LANGUAGES = {"English":"en","Español":"es","Français":"fr","Kreyòl Ayisyen":"ht"}
TEXTS = {
    "en": {
        "refresh_btn": "🔄 Refresh Simulated Data",
        "pods_title": "📦 Pods",
        "deployments_title": "⚙️ Deployments",
        "services_title": "🔗 Services",
        "nodes_title": "🖥️ Nodes",
        "pod_cols": ["Name", "Status", "Node", "Restarts", "Age"],
        "deploy_cols": ["Name", "Replicas", "Available", "Strategy"],
        "service_cols": ["Name", "Type", "Cluster IP", "Ports"],
        "node_cols": ["Name", "Status", "Role", "Age", "Version"]
    },
    "es": {
        "refresh_btn": "🔄 Actualizar datos simulados",
        "pods_title": "📦 Pods",
        "deployments_title": "⚙️ Despliegues",
        "services_title": "🔗 Servicios",
        "nodes_title": "🖥️ Nodos",
        "pod_cols": ["Nombre", "Estado", "Nodo", "Reinicios", "Edad"],
        "deploy_cols": ["Nombre", "Réplicas", "Disponibles", "Estrategia"],
        "service_cols": ["Nombre", "Tipo", "IP del clúster", "Puertos"],
        "node_cols": ["Nombre", "Estado", "Rol", "Edad", "Versión"]
    },
    "fr": {
        "refresh_btn": "🔄 Actualiser les données simulées",
        "pods_title": "📦 Pods",
        "deployments_title": "⚙️ Déploiements",
        "services_title": "🔗 Services",
        "nodes_title": "🖥️ Nœuds",
        "pod_cols": ["Nom", "Statut", "Nœud", "Redémarrages", "Âge"],
        "deploy_cols": ["Nom", "Réplicas", "Disponibles", "Stratégie"],
        "service_cols": ["Nom", "Type", "IP du cluster", "Ports"],
        "node_cols": ["Nom", "Statut", "Rôle", "Âge", "Version"]
    },
    "ht": {
        "refresh_btn": "🔄 Mete ajou done simile yo",
        "pods_title": "📦 Pods",
        "deployments_title": "⚙️ Deplwaman",
        "services_title": "🔗 Sèvis",
        "nodes_title": "🖥️ Nœuds",
        "pod_cols": ["Non", "Estati", "Nœud", "Redemare", "Laj"],
        "deploy_cols": ["Non", "Replik", "Disponib", "Estrateji"],
        "service_cols": ["Non", "Kalite", "IP cluster", "Pò"],
        "node_cols": ["Non", "Estati", "Wòl", "Laj", "Vèsyon"]
    }
}
def get_text(key):
    lang = st.session_state.get("language", "en")
    return TEXTS[lang].get(key, TEXTS["en"].get(key, key))

lang_choice = st.sidebar.selectbox("🌐 Language", list(LANGUAGES.keys()))
st.session_state["language"] = LANGUAGES[lang_choice]

# ------------------------------
# SIMULATED DATA GENERATION
# ------------------------------
def generate_pods():
    names = ["nginx-pod", "redis-pod", "api-pod", "worker-pod", "frontend-pod", "db-pod", "cache-pod", "monitor-pod"]
    statuses = ["Running", "Running", "Running", "Pending", "Running", "Running", "CrashLoopBackOff", "Running"]
    nodes = ["node-1", "node-2", "node-1", "node-3", "node-2", "node-3", "node-1", "node-2"]
    restarts = [0, 0, 1, 0, 2, 0, 5, 0]
    ages = ["2d", "3d", "1d", "5h", "2d", "4d", "1h", "2d"]
    data = []
    for i in range(8):
        data.append([names[i], statuses[i], nodes[i], restarts[i], ages[i]])
    return pd.DataFrame(data, columns=get_text("pod_cols"))

def generate_deployments():
    names = ["nginx-deploy", "redis-deploy", "api-deploy", "frontend-deploy"]
    replicas = [3, 1, 2, 2]
    available = [3, 1, 2, 1]
    strategies = ["RollingUpdate", "Recreate", "RollingUpdate", "RollingUpdate"]
    data = list(zip(names, replicas, available, strategies))
    return pd.DataFrame(data, columns=get_text("deploy_cols"))

def generate_services():
    names = ["nginx-svc", "redis-svc", "api-svc", "frontend-svc"]
    types = ["ClusterIP", "ClusterIP", "NodePort", "LoadBalancer"]
    cluster_ips = ["10.96.0.1", "10.96.0.2", "10.96.0.3", "10.96.0.4"]
    ports = ["80/TCP", "6379/TCP", "8080:30080/TCP", "80:30000/TCP"]
    data = list(zip(names, types, cluster_ips, ports))
    return pd.DataFrame(data, columns=get_text("service_cols"))

def generate_nodes():
    names = ["node-1", "node-2", "node-3"]
    statuses = ["Ready", "Ready", "NotReady"]
    roles = ["control-plane", "worker", "worker"]
    ages = ["30d", "30d", "15d"]
    versions = ["v1.28", "v1.28", "v1.27"]
    data = list(zip(names, statuses, roles, ages, versions))
    return pd.DataFrame(data, columns=get_text("node_cols"))

# ------------------------------
# MAIN DASHBOARD
# ------------------------------
st.markdown("---")
if st.button(get_text("refresh_btn"), use_container_width=True):
    st.rerun()

col1, col2 = st.columns(2)
with col1:
    st.markdown(f"<div class='card'><h3>{get_text('pods_title')}</h3></div>", unsafe_allow_html=True)
    st.dataframe(generate_pods(), use_container_width=True)
    
    st.markdown(f"<div class='card'><h3>{get_text('services_title')}</h3></div>", unsafe_allow_html=True)
    st.dataframe(generate_services(), use_container_width=True)

with col2:
    st.markdown(f"<div class='card'><h3>{get_text('deployments_title')}</h3></div>", unsafe_allow_html=True)
    st.dataframe(generate_deployments(), use_container_width=True)
    
    st.markdown(f"<div class='card'><h3>{get_text('nodes_title')}</h3></div>", unsafe_allow_html=True)
    st.dataframe(generate_nodes(), use_container_width=True)

st.markdown("---")
st.markdown("📘 **Simulated Kubernetes environment** – refresh to see random status changes. Perfect for learning Kubernetes concepts.")

# Footer
st.markdown('<div class="footer">🌍 *GlobalInternet.py – Kubernetes Dashboard Simulator* 🌍</div>', unsafe_allow_html=True)
