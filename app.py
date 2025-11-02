import streamlit as st

st.set_page_config(page_title="Shook Vendor Assistant", page_icon="💬", layout="centered")

st.markdown("""
    <style>
        body {
            background-color: #0E0E0E;
            color: #FFFFFF;
            font-family: 'Inter', sans-serif;
        }
        .stTextInput > div > div > input {
            background-color: #FFFFFF;
            color: #0E0E0E;
            border: 1px solid #05FF8E;
        }
        .stButton>button {
            background-color: #05FF8E;
            color: #0E0E0E;
            border-radius: 8px;
            font-weight: 600;
        }
        .stButton>button:hover {
            background-color: #007BFF;
            color: #FFFFFF;
        }
    </style>
""", unsafe_allow_html=True)

st.title("💬 Shook Vendor Assistant")
st.caption("Ask me common vendor or freelancer questions.")

faq = {
    ("invoice", "invoices", "invoicing", "bill"): "📄 Send invoices to finance@shook.digital with your PO number or project reference.",
    ("payment", "paid", "pay", "paycheck", "compensation"): "💰 Payments are processed on the 15th and 30th of each month.",
    ("feedback", "review", "comment"): "🗣️ Contact your project lead or ops@shook.digital.",
    ("project files", "files", "documents", "assets", "drive", "project briefs"): "📁 Access shared Drive folders per project, or contact ops if you're missing access.",
    ("update details", "update", "change", "modify"): "✏️ Submit company info changes through the provided form link.",
    ("turnaround", "timeline", "time", "how long", "duration"): "⏱️ Design: 3–5 days | Web: 5–10 days.",
    ("slack", "chat", "messaging"): "💬 Join our Partner Ops Slack workspace!"
}

if "user_q" not in st.session_state:
    st.session_state["user_q"] = ""

with st.form("qa_form"):
    user_q = st.text_input("Ask a question:")
    submitted = st.form_submit_button("Ask")

if submitted:
    user_q_lower = user_q.lower()
    response = next(
        (answer for keywords, answer in faq.items() if any(k in user_q_lower for k in keywords)),
        "🤔 Please email ops@shook.digital for that."
    )
    st.success(response)