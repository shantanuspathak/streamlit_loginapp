import streamlit as st

def login_page():
    st.title("Login Page")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        # Simple authentication (replace with more secure method in production)
        if username == "user" and password == "password":
            st.session_state["logged_in"] = True
            st.session_state["current_page"] = "calc"
            st.success("Logged in successfully!")
            st.rerun() # Rerun to switch to the calculator page
        else:
            st.error("Invalid username or password")

def main():
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False
        st.session_state["current_page"] = "login"

    if st.session_state["logged_in"] and st.session_state["current_page"] == "calc":
        # Import and run the calculator app
        import calc
        calc.calculator_page()
    else:
        login_page()

if __name__ == "__main__":
    main()