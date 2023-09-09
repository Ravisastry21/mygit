import streamlit as st
import google.generativeai as palm

# Set up the Streamlit app
st.title("Q&A Prompt with PALM-2")

# Input for the prompt
prompt = st.text_area("Enter your question or prompt:")

if st.button("Generate Response"):
    # Configure PALM-2 with your API key
    palm.configure(api_key="AIzaSyCErWP745eisoPx6lzk9kwxaLWYtCY0Zx4")  # Replace with your actual API key

    # Default settings
    defaults = {
        'model': 'models/text-bison-001',
        'temperature': 0.7,
        'candidate_count': 1,
        'top_k': 40,
        'top_p': 0.95,
        'max_output_tokens': 1024,
        'stop_sequences': [],
        'safety_settings': [
            {"category": "HARM_CATEGORY_DEROGATORY", "threshold": 1},
            {"category": "HARM_CATEGORY_TOXICITY", "threshold": 1},
            {"category": "HARM_CATEGORY_VIOLENCE", "threshold": 2},
            {"category": "HARM_CATEGORY_SEXUAL", "threshold": 2},
            {"category": "HARM_CATEGORY_MEDICAL", "threshold": 2},
            {"category": "HARM_CATEGORY_DANGEROUS", "threshold": 2},
        ],
    }

    # Generate text based on the user's prompt
    response = palm.generate_text(**defaults, prompt=prompt)

    # Display the generated response
    st.subheader("Generated Response:")
    st.write(response.result)
