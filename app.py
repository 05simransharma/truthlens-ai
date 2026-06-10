import streamlit as st

from utils.pdf_loader import extract_text
from modules.contract_analyzer import analyze_contract
from modules.news_analyzer import analyze_news

st.set_page_config(
    page_title="TruthLens AI",
    page_icon="🔍",
    layout="wide"
)

# ---------- CUSTOM STYLING ----------

st.markdown("""
<style>
.main {
    padding-top: 1rem;
}

.big-title {
    text-align: center;
    font-size: 3rem;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: gray;
    margin-bottom: 2rem;
}

.feature-box {
    padding: 20px;
    border-radius: 10px;
    border: 1px solid #ddd;
    margin-top: 10px;
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------

st.markdown(
    '<div class="big-title">🔍 TruthLens AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Trust & Risk Intelligence Platform</div>',
    unsafe_allow_html=True
)

# ---------- SIDEBAR ----------

with st.sidebar:

    st.title("TruthLens AI")

    st.markdown("---")

    st.markdown("### Features")

    st.markdown("""
    ✅ Contract Risk Analysis

    ✅ News Credibility Analysis

    ✅ AI-Powered Summarization

    ✅ Risk Detection

    ✅ Bias Identification
    """)

    st.markdown("---")

    st.info(
        "TruthLens AI helps users evaluate "
        "contracts and news articles using "
        "AI-powered risk and credibility analysis."
    )

# ---------- TABS ----------

tab1, tab2 = st.tabs(
    ["📄 Contract Risk Analyzer", "📰 News Credibility Analyzer"]
)

# ==================================================
# CONTRACT ANALYZER
# ==================================================

with tab1:

    st.subheader("Upload and Analyze Contracts")

    uploaded_pdf = st.file_uploader(
        "Upload a PDF Contract",
        type=["pdf"],
        key="contract_pdf"
    )

    if uploaded_pdf:

        st.success("PDF uploaded successfully.")

        if st.button(
            "🔍 Analyze Contract",
            use_container_width=True
        ):

            with st.spinner("Analyzing contract..."):

                contract_text = extract_text(uploaded_pdf)

                result = analyze_contract(contract_text)

                st.markdown("## 📋 Analysis Report")

                st.markdown(result)

# ==================================================
# NEWS ANALYZER
# ==================================================

with tab2:

    st.subheader("Analyze News Credibility")

    article = st.text_area(
        "Paste News Article",
        height=300,
        placeholder="Paste the article content here..."
    )

    if st.button(
        "📰 Analyze News",
        use_container_width=True
    ):

        if not article.strip():

            st.warning(
                "Please enter an article."
            )

        else:

            with st.spinner("Analyzing article..."):

                result = analyze_news(article)

                st.markdown("## 📊 Credibility Report")

                st.markdown(result)

# ---------- FOOTER ----------

st.divider()

st.caption(
    "TruthLens AI • Hackathon Prototype • Powered by Gemini"
)