import matplotlib.pyplot as plt
def visualize_dna(original, mutated):
    fig, ax = plt.subplots()
    ax.plot(range(len(original)), [ord(n) for n in original], label="Original")
    ax.plot(range(len(mutated)), [ord(n) for n in mutated], label="Mutated", linestyle="--")
    ax.set_title("DNA Z Transformation")
    ax.legend()
    return fig