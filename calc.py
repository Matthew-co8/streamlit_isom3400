import streamlit as st
import math

# --- Math Helper Functions ---
def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def custom_log(x, base):
    if x <= 0:
        raise ValueError("Input number must be greater than 0.")
    if base <= 0 or base == 1:
        raise ValueError("Log base must be greater than 0 and not equal to 1.")
    return math.log(x, base)

def natural_log(x):
    if x <= 0:
        raise ValueError("Input number must be greater than 0.")
    return math.log(x)

# --- Operation Registry ---
# Maps the dropdown label to a (function, requires_second_number) tuple
OPERATIONS = {
    "Add": (lambda x, y: x + y, True),
    "Subtract": (lambda x, y: x - y, True),
    "Multiply": (lambda x, y: x * y, True),
    "Divide": (divide, True),
    "Sin()": (lambda x: math.sin(x), False),
    "ln()": (natural_log, False),
    "log()": (custom_log, True),
}

# --- Streamlit UI ---
def main():
    st.title("Basic Web Calculator")

    operation = st.selectbox("Choose operation", list(OPERATIONS.keys()))
    func, needs_num2 = OPERATIONS[operation]

    num1 = st.number_input("Enter first number", value=0.0)
    
    # Only render the second input if the selected operation uses it
    num2 = None
    if needs_num2:
        label = "Enter base" if operation == "log()" else "Enter second number"
        num2 = st.number_input(label, value=0.0)
    if st.button("Calculate"):
        try:
            result = func(num1, num2) if needs_num2 else func(num1)
            st.success(f"Result: {result}")
        except ValueError as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
