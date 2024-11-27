import streamlit as st
from itertools import permutations

def is_valid_solution(word_equation, mapping):
    """Check if a given mapping solves the cryptarithm."""
    try:
        equation = word_equation
        for char, num in mapping.items():
            equation = equation.replace(char, str(num))
        # Evaluate the equation
        left, right = equation.split("=")
        return eval(left) == eval(right)
    except Exception:
        return False

def solve_cryptarithm(word_equation):
    """Solve the cryptarithm equation."""
    # Extract unique letters
    letters = set(c for c in word_equation if c.isalpha())
    if len(letters) > 10:
        return None  # Cannot map more than 10 unique letters to digits

    # Generate all permutations of digits for the letters
    for perm in permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))
        if is_valid_solution(word_equation, mapping):
            return mapping
    return None

# Streamlit app
st.title("Cryptarithm Solver")
st.write("Masukkan persamaan cryptarithm seperti `SEND + MORE = MONEY`.")

# Input cryptarithm equation
word_equation = st.text_input("Masukkan persamaan cryptarithm:")

if word_equation:
    # Solve the cryptarithm
    solution = solve_cryptarithm(word_equation.replace(" ", ""))
    if solution:
        st.write("Solusi ditemukan!")
        st.write(solution)
    else:
        st.write("Tidak ada solusi yang valid.")
