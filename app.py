import streamlit as st
books = ["The Hobbit", "1984", "Pride and Prejudice", "To Kill a Mockingbird", "The Great Gatsby"]
st.title("Book Checker App")
st.write("Enter a book title to check if it exists in the database.")
user_input = st.text_input("Book Tile")
if st.button("Check Book"):
  if user_input.strip() == "":
    st.warning("Please enter a book title.")
  elif user_input in books:
    st.sucsess("The book exists in database!")
  else:
    st.error("The book is NOT in the database.")
st.subheader("Your Personal Library")
if "my_books" not in st.session_state:
    st.session_state.my_books = []
if st.button("Add Book to My Library"):
    if user_input.strip() == "":
        st.warning("Please enter a book title to add.")
    else:
        st.session_state.my_books.append(user_input)
        st.success("Book added to your personal library!")
if st.button("Check in My Library"):
    if user_input in st.session_state.my_books:
        st.success("The book is in your personal library!")
    else:
        st.error("The book is NOT in your personal library.")
st.write("My Books:")
for book in st.session_state.my_books:
    st.write("-", book)
