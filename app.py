import streamlit as st

from utils.pdf_loader import extract_text
from modules.contract_analyzer import analyze_contract
from modules.news_analyzer import analyze_news
from utils.translations import translations

st.set_page_config(
    page_title="TruthLens AI",
    page_icon="🔍",
    layout="wide"
)

# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    language = st.selectbox(
        "🌐 Language",
        ["English", "Hindi", "Telugu"],
        key="language_selector"
    )

    t = translations[language]

    st.title(t["title"])

    st.caption(
        "AI-powered risk & credibility analysis"
    )

    st.markdown("---")

    provider = st.selectbox(
        "🤖 AI Provider",
        [
            "Gemini (Cloud)",
            "Ollama (Local)"
        ],
        key="provider"
    )

    if provider == "Gemini (Cloud)":

        st.header(f'🔑 {t["api_configuration"]}')

        api_key = st.text_input(
            t["api_key"],
            type="password"
        )

    else:

        api_key = ""

        st.success(
            "Using local Ollama model (Qwen 2.5)"
        )

    st.markdown("---")

    st.markdown(
        f"### {t['features']}"
    )

    st.markdown(
        t["feature_list"]
    )

    st.markdown("---")

    st.info(
        t["sidebar_info"]
    )

# ==================================================
# CUSTOM STYLING
# ==================================================

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
</style>
""", unsafe_allow_html=True)

# ==================================================
# HEADER
# ==================================================

st.markdown(
    f'<div class="big-title">🔍 {t["title"]}</div>',
    unsafe_allow_html=True
)

st.markdown(
    f'<div class="subtitle">{t["subtitle"]}</div>',
    unsafe_allow_html=True
)

# ==================================================
# TABS
# ==================================================

tab1, tab2 = st.tabs(
    [
        t["contract_tab"],
        t["news_tab"]
    ]
)

# ==================================================
# CONTRACT ANALYZER
# ==================================================

with tab1:

    st.subheader(
        t["contract_header"]
    )

    uploaded_pdf = st.file_uploader(
        t["upload_pdf"],
        type=["pdf"],
        key="contract_pdf"
    )

    if uploaded_pdf:

        st.success(
            "PDF uploaded successfully."
        )

        if st.button(
            t["analyze_contract"],
            use_container_width=True
        ):

            if (
                provider == "Gemini (Cloud)"
                and not api_key
            ):

                st.warning(
                    "Please enter your Gemini API Key in the sidebar."
                )

            else:

                with st.spinner(
                    "Analyzing contract..."
                ):

                    contract_text = extract_text(
                        uploaded_pdf
                    )

                    result = analyze_contract(
                        contract_text,
                        api_key,
                        language,
                        provider
                    )

                    st.markdown(
                        t["analysis_report"]
                    )

                    st.markdown(
                        result
                    )

# ==================================================
# NEWS ANALYZER
# ==================================================

with tab2:

    st.subheader(
        t["news_header"]
    )

    article = st.text_area(
        "Paste News Article",
        height=300,
        placeholder="Paste the article content here..."
    )

    if st.button(
        t["analyze_news"],
        use_container_width=True
    ):

        if not article.strip():

            st.warning(
                "Please enter an article."
            )

        elif (
            provider == "Gemini (Cloud)"
            and not api_key
        ):

            st.warning(
                "Please enter your Gemini API Key in the sidebar."
            )

        else:

            with st.spinner(
                "Analyzing article..."
            ):

                result = analyze_news(
                    article,
                    api_key,
                    language,
                    provider
                )

                st.markdown(
                    t["credibility_report"]
                )

                st.markdown(
                    result
                )

# ==================================================
# FOOTER
# ==================================================

st.divider()

st.caption(
    "TruthLens AI • Powered by Gemini & Ollama • BYOK Enabled • Multilingual Support"
)