import streamlit as st
from zgl_input import load_dna_sequence
from zgl_symbolic_mutation import apply_symbolic_mutation
from zgl_predict import predict_next_mutation
from zgl_viewer import visualize_dna
from zgl_export import export_result

st.set_page_config(page_title="Z Genome Lab Lite", page_icon="🧬")
st.title("🧬 Z Genome Lab Lite – Symbolic Mutation Engine")

st.markdown("Enter a DNA sequence to apply a symbolic Z mutation and visualize the result.")

dna_input = st.text_input("🔤 DNA Sequence:", load_dna_sequence())

if st.button("🔁 Apply Z Mutation"):
    mutated_dna = apply_symbolic_mutation(dna_input)
    prediction = predict_next_mutation(dna_input)

    st.success("Mutation Applied!")
    st.code(f"Original : {dna_input}", language="text")
    st.code(f"Mutated  : {mutated_dna}", language="text")

    st.markdown(f"🧠 **AI Prediction:** _{prediction}_")

    st.pyplot(visualize_dna(dna_input, mutated_dna))

    if st.download_button("📄 Download Result", data=f"Original: {dna_input}\nMutated: {mutated_dna}", file_name="zgl_result.txt"):
        st.success("Result downloaded successfully!")