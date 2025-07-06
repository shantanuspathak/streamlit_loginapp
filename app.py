   import streamlit as st
   import time

   def check_login(username, password):
       # Replace with your authentication logic (e.g., checking against a database)
       if username == "test" and password == "test":
           return True
       else:
           return False

   def login_page():
       st.title("Login")
       username = st.text_input("Username")
       password = st.text_input("Password", type="password")
       if st.button("Login"):
           if check_login(username, password):
               st.session_state.logged_in = True
               st.session_state.username = username
               st.success("Login successful!")
               time.sleep(0.5)
               st.switch_page("pages/page1.py")  # Redirect to a protected page
           else:
               st.error("Invalid username or password")

   def main_page():
       st.title("Main Page (Protected)")
       st.write(f"Welcome, {st.session_state.username}!")
       if st.button("Logout"):
           st.session_state.logged_in = False
           st.session_state.username = None
           st.success("Logged out!")
           time.sleep(0.5)
           st.switch_page("app.py")  # Redirect back to login

   if __name__ == "__main__":
       if not st.session_state.get("logged_in", False):
           login_page()
       else:
           main_page()