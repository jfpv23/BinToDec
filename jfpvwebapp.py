import streamlit as st
import DTB as dtb
import BTD as btd
import time


def main():
    st.markdown("<h1 style='text-align: center; color: white;'>Decimal-Binary Converter</h1>", unsafe_allow_html=True)
    st.subheader("By: John Frank Valenzona")
    conversion_type = st.radio("Select conversion type:", ("Decimal to Binary", "Binary to Decimal"))
    number = st.text_input("Enter the number:")

    result = ""
    if st.button("Click to Convert"):
        with st.spinner('Converting...'):
            time.sleep(3)
            st.success('Converted!')

        if conversion_type == "Decimal to Binary":
            try:
                decimal_number = int(number)
                result = dtb.decimal_to_binary(decimal_number)
            except ValueError:
                result = "Invalid input. Please enter a valid decimal number."
        elif conversion_type == "Binary to Decimal":
            try:
                binary_number = str(number)
                result = btd.binary_to_decimal(binary_number)
            except ValueError:
                result = "Invalid input. Please enter a valid binary number."

    st.write("Result:", result)



if __name__ == "__main__":
    main()
