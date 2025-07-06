import streamlit as st

def calculator_page():
    st.title("Calculator Page")

    if st.button("Logout"):
        st.session_state["logged_in"] = False
        st.session_state["current_page"] = "login"
        st.rerun() # Rerun to go back to the login page

    st.write("---") # Separator for better UI

    st.header("Perform Calculation")

    # Input for two floating-point values
    num1 = st.number_input("Enter first number", format="%f", value=0.0)
    num2 = st.number_input("Enter second number", format="%f", value=0.0)

    operation = st.selectbox(
        "Select Operation",
        ("Add", "Subtract", "Multiply", "Divide")
    )

    if st.button("Predict"):
        result = None
        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 != 0:
                result = num1 / num2
            else:
                st.error("Error: Division by zero is not allowed.")
        
        if result is not None:
            st.success(f"Result: {result}")