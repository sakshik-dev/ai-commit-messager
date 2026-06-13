import requests
import streamlit as st

BASE_URL = "https://ai-commit-messager.onrender.com/"

st.set_page_config(
    page_title="AI Git Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Git Assistant")
st.caption("Paste a git diff → get commit message, PR, review & secrets")
tab1, tab2 = st.tabs(
    ["📝 Commit Generator", "🔍 Code Review"]
)

# =====================================================
# COMMIT GENERATOR
# =====================================================

with tab1:

    diff = st.text_area(
        "Git Diff",
        height=350,
        placeholder="Paste git diff here...",
        key="commit_diff"
    )

    if st.button(
        "Generate Commit Artifacts",
        use_container_width=True
    ):

        if not diff.strip():
            st.warning("Please paste a git diff.")
            st.stop()

        with st.spinner("Analyzing diff..."):

            response = requests.post(
                f"{BASE_URL}/generate",
                json={"diff": diff}
            )

            if response.status_code != 200:
                st.error("Backend error.")
                st.stop()

            data = response.json()

        st.divider()

        left, right = st.columns([3, 1])

        with left:

            st.subheader("Commit Message")

            st.code(
                data.get("commit_message", ""),
                language=None
            )

            st.subheader("PR Description")

            st.markdown(
                data.get("pr_description", "")
            )

            st.subheader("Release Notes")

            st.markdown(
                data.get("release_notes", "")
            )

        with right:

            st.subheader("Statistics")

            stats = data.get(
                "statistics",
                {}
            )

            st.metric(
                "Files Changed",
                stats.get(
                    "files_changed",
                    0
                )
            )

            st.metric(
                "Insertions",
                stats.get(
                    "insertions",
                    0
                )
            )

            st.metric(
                "Deletions",
                stats.get(
                    "deletions",
                    0
                )
            )

            st.subheader("Secrets")

            secrets = data.get(
                "secrets",
                []
            )

            if secrets:

                for secret in secrets:
                    st.warning(secret)

            else:
                st.success(
                    "No secrets found"
                )

# =====================================================
# CODE REVIEW
# =====================================================

with tab2:

    review_diff = st.text_area(
        "Git Diff",
        height=350,
        placeholder="Paste git diff here...",
        key="review_diff"
    )

    if st.button(
        "Review Code",
        use_container_width=True
    ):

        if not review_diff.strip():
            st.warning("Please paste a git diff.")
            st.stop()

        with st.spinner("Reviewing code..."):

            response = requests.post(
                f"{BASE_URL}/review",
                json={
                    "diff": review_diff
                }
            )

            if response.status_code != 200:
                st.error("Backend error.")
                st.stop()

            data = response.json()

        st.divider()

        st.subheader(
            "Performance Observations"
        )

        perf = data.get(
            "performance_observations",
            []
        )

        if perf:
            for item in perf:
                st.info(item)
        else:
            st.success("No observations")

        st.subheader(
            "Security Observations"
        )

        security = data.get(
            "security_observations",
            []
        )

        if security:
            for item in security:
                st.warning(item)
        else:
            st.success("No observations")

        st.subheader(
            "Maintainability Feedback"
        )

        maintainability = data.get(
            "maintainability_feedback",
            []
        )

        if maintainability:
            for item in maintainability:
                st.info(item)
        else:
            st.success("No observations")

        st.subheader(
            "Transactional Risks"
        )

        risks = data.get(
            "transactional_risks",
            []
        )

        if risks:
            for item in risks:
                st.warning(item)
        else:
            st.success("No observations")

        st.subheader(
            "Testing Suggestions"
        )

        tests = data.get(
            "testing_suggestions",
            []
        )

        if tests:
            for item in tests:
                st.info(item)
        else:
            st.success("No suggestions")

        st.subheader(
            "Code Smells"
        )

        smells = data.get(
            "code_smells",
            []
        )

        if smells:
            for item in smells:
                st.warning(item)
        else:
            st.success("No code smells found")