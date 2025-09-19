import streamlit as st
import pandas as pd

st.set_page_config(page_title="Client Lookup", layout="wide")

st.title("🔎 Tela Client Lookup Tool by Max")

# Custom CSS for dark theme styling
st.markdown("""
    <style>
        body, .stApp {
            background-color: #121212;
            color: #f0f0f0;
        }
        .client-card {
            padding: 15px;
            margin-bottom: 15px;
            border-radius: 10px;
            border: 1px solid #333;
            background-color: #1e1e1e;
            box-shadow: 2px 2px 6px rgba(0,0,0,0.6);
        }
        .client-card h4 {
            margin: 0;
            color: #4FC3F7;
        }
        .client-card p {
            margin: 4px 0;
            font-size: 14px;
            color: #e0e0e0;
        }
        .stTextInput>div>div>input {
            background-color: #2c2c2c;
            color: #f0f0f0;
            border: 1px solid #555;
        }
    </style>
""", unsafe_allow_html=True)

# @st.cache_data   👈 remove this during testing
def load_data():
    df = pd.read_csv("clients.csv", dtype=str).fillna("")
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    return df

df = load_data()

query = st.text_input("Enter client name", placeholder="Type a client name...")

if query:
    mask = df["client_name"].str.contains(query, case=False, na=False)
    results = df[mask]

    if results.empty:
        st.warning("⚠️ No clients found. Try another search.")
    else:
        for _, row in results.iterrows():
            st.markdown(
                f"""
                <div class="client-card">
                    <h4>🏢 {row['client_name']}</h4>
                    <p><b>📂 Group:</b> {row['group'] or "—"}</p>
                    <p><b>📍 Location:</b> {row['location'] or "—"}</p>
                    <p><b>👨‍💼 Specialist:</b> {row['specialist'] or "—"}</p>
                    <p><b>📦 Assets:</b> {"None" if not row['assets'].strip().startswith(tuple("0123456789")) else row['assets']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
else:
    st.info("💡 Start typing a client name above to see results.")
