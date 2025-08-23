import streamlit as st
from utils.extractor import extract_resume_text
from utils.preprocessing import preprocess_text
from utils.similarity import calculate_similarity
from utils.keywords import missing_keywords
from config.styles import custom_css
from config.settings import nlp, stop_words
from streamlit_extras.metric_cards import style_metric_cards

# Page config
st.set_page_config(page_title="Resume Matcher", page_icon="📄", layout="centered")

# Inject CSS
st.markdown(custom_css, unsafe_allow_html=True)

# --- Title ---
st.markdown('<div class="header">📄 Resume Classifier & Job Matcher</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">🧾 Upload your resume & 📋 paste job description to get started</div>', unsafe_allow_html=True)

# --- File Upload ---
uploaded_file = st.file_uploader("📎 Upload Resume (PDF only)", type=["pdf"])

# --- Job Description Input ---
job_desc = st.text_area("🧾 Paste Job Description Here", height=180)

# --- Main Logic ---
if uploaded_file and job_desc:
    with st.spinner("🔍 Analyzing your resume... Please wait..."):
        resume_text = extract_resume_text(uploaded_file)
        cleaned_resume = preprocess_text(resume_text)
        cleaned_job_desc = preprocess_text(job_desc)

        # Similarity Score
        score = calculate_similarity(cleaned_resume, cleaned_job_desc)
        percentage = round(score * 100, 2)

        st.markdown("## 📊 Match Results")
        col1, col2 = st.columns([1, 2])

        with col1:
            col1.metric(label="💡 Similarity Score", value=f"{percentage} %")
        style_metric_cards(background_color="#ffffff", border_left_color="#1f77b4", border_color="#E0E0E0")

        with col2:
            if score > 0.75:
                st.success("✅ Excellent Match! Your resume aligns well with the job description.")
            elif score > 0.5:
                st.warning("⚠️ Moderate Match. You might want to improve your resume alignment.")
            else:
                st.error("❌ Low Match. Consider tailoring your resume for better fit.")

        # Resume preview
        with st.expander("📄 View Extracted Resume Text"):
            st.markdown(resume_text)

        # Keyword suggestion
        keywords_missing = missing_keywords(cleaned_resume, cleaned_job_desc)
        if keywords_missing:
            with st.expander("🧠 Suggested Keywords to Add"):
                keyword_tags = ''.join(
                    [f'<span class="keyword-tag">{word}</span>' for word in keywords_missing]
                )
                st.markdown(f"<div style='display: flex; flex-wrap: wrap; gap: 6px;'>{keyword_tags}</div>", unsafe_allow_html=True)
        else:
            st.success("🎯 Your resume contains all major keywords from the job description!")

# Footer
st.markdown("---")
st.markdown("🛠️ Built with ❤️ using Python, Streamlit, SpaCy, and Scikit-learn")
