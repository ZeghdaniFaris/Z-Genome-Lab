import matplotlib.pyplot as plt

def visualize_dna(original, mutated):
    fig, ax = plt.subplots(figsize=(10, 5))

    # Plotting the DNA sequences
    ax.plot(range(len(original)), [ord(n) for n in original], label="Original DNA", linewidth=2)
    ax.plot(range(len(mutated)), [ord(n) for n in mutated], label="Mutated DNA", linestyle="--", linewidth=2)
    
    ax.set_title("🧬 DNA Z Transformation (Symbolic Transition Mutation)", fontsize=14)
    ax.set_xlabel("Position")
    ax.set_ylabel("Nucleotide (ASCII Code)")
    ax.legend()

    # Full scientific explanation text below the graph
    explanation = (
        "🔬 Symbolic Transition Mutation: Stability through Genomic Logic\n\n"
        "This phenomenon applies a symbolic mutation on DNA sequences where:\n"
        "- Adenine (A) → Guanine (G)\n"
        "- Thymine (T) → Cytosine (C)\n\n"
        "These substitutions respect purine-to-purine and pyrimidine-to-pyrimidine transitions, ensuring:\n"
        "• Minimal structural disruption of the double helix\n"
        "• Preservation of molecular weight and hydrogen bonding balance\n"
        "• Symbolic mutation stability for intelligent DNA processing\n\n"
        "🧬 This rule mimics biological transition mutations but implements them in a mathematically controlled symbolic form Symbolic Mutation."
    )

    # Position explanation below the plot using Axes coordinates
    plt.figtext(0.5, -0.35, explanation, wrap=True, horizontalalignment='center', fontsize=9)

    plt.tight_layout()
    return fig
