import streamlit as st
from zgl_input import load_dna_sequence
from zgl_symbolic_mutation import apply_symbolic_mutation
from zgl_predict import predict_next_mutation
from zgl_viewer import visualize_dna
from zgl_export import export_result

st.set_page_config(page_title="Z Genome Lab Lite", page_icon="🧬")
st.title("🧬 Z Genome Lab Lite – Symbolic Mutation Engine")

st.markdown("Enter a DNA sequence to apply a symbolic Z mutation and visualize the result.")

# Load initial sequence (or placeholder)
dna_input = st.text_input("🔤 DNA Sequence:", load_dna_sequence())

if st.button("🔁 Apply Z Mutation"):
    mutated_dna = apply_symbolic_mutation(dna_input)
    prediction = predict_next_mutation(dna_input)

    st.success("Mutation Applied!")
    st.code(f"Original : {dna_input}", language="text")
    st.code(f"Mutated  : {mutated_dna}", language="text")

    st.markdown(f"🧠 **AI Prediction:** _{prediction}_")

    # Display chart
    st.pyplot(visualize_dna(dna_input, mutated_dna))

    # Export button
    if st.download_button("📄 Download Result", data=f"Original: {dna_input}\nMutated: {mutated_dna}", file_name="zgl_result.txt"):
        st.success("Result downloaded successfully!")

# Symbolic Explanation (appears under chart)
st.markdown("""
---
🔬 **Symbolic Transition Mutation: Stability through Genomic Logic**

This phenomenon applies a symbolic mutation on DNA sequences where:  
- **Adenine (A)** → **Guanine (G)**  
- **Thymine (T)** → **Cytosine (C)**  

These substitutions respect **purine-to-purine** and **pyrimidine-to-pyrimidine** transitions, ensuring:  
- ✅ Minimal structural disruption of the double helix  
- ✅ Preservation of molecular weight and hydrogen bonding balance  
- ✅ Symbolic mutation stability for intelligent DNA processing  
 ✒️ i name it Symbolic Stable Mutation (SSM)
🧬 This rule mimics biological transition mutations but implements them in a **mathematically controlled symbolic form**: **Symbolic Mutation**
""")
