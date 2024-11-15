import streamlit as st

import streamlit.components.v1 as components
def inject_google_analytics():
    # Google Analytics tag with your Measurement ID
    ga_tag = """
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-D09LB5TCTL"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());

      gtag('config', 'G-D09LB5TCTL');
    </script>
    """
    # Inject the tag into the Streamlit app's head section
    st.components.v1.html(ga_tag, height=0)


inject_google_analytics()

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.write('hello')
