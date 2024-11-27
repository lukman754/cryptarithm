import streamlit as st
from itertools import permutations
import time

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

def apply_mapping_to_words(words, mapping):
    """Apply mapping to convert words to numbers."""
    return [int("".join(str(mapping[char]) for char in word)) for word in words]

# Streamlit app
st.title("Cryptarithm Solver")
st.write("Masukkan persamaan cryptarithm seperti `SEND + MORE = MONEY`.")

# Input cryptarithm equation
word_equation = st.text_input("Masukkan persamaan cryptarithm:")

if word_equation:
    # Preprocessing input
    word_equation = word_equation.replace(" ", "")
    st.write("Sedang mencari solusi...")
    with st.spinner("Mencari solusi, mohon tunggu..."):
        time.sleep(1)  # Simulate loading animation
        solution = solve_cryptarithm(word_equation)

    if solution:
        # Sort the mapping alphabetically
        sorted_mapping = dict(sorted(solution.items()))
        
        # Split words from equation
        left_side, right_side = word_equation.split("=")
        left_words = left_side.split("+")
        
        # Convert words to their numeric forms
        left_numbers = apply_mapping_to_words(left_words, solution)
        right_number = apply_mapping_to_words([right_side], solution)[0]

        # Display results
        st.success("Solusi ditemukan!")
        st.write("Mapping huruf ke angka:")
        st.write(sorted_mapping)

        # Show numeric representation of the equation
        st.write("Persamaan numerik:")
        equation_numeric = " + ".join(map(str, left_numbers)) + f" = {right_number}"
        st.write(equation_numeric)
    else:
        st.error("Tidak ada solusi yang valid.")
