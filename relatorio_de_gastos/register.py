
import streamlit as st
import datetime

from models import Gasto
import os

def register_page():

    st.title("Registro de Gasto")
    new_date = None
    set_date = st.checkbox("Inserir data diferente da atual?")

    if set_date:
        new_date = st.date_input("Selecione a data desejada:")


    new_category = st.selectbox(
        "Selecione a categoria:",
        os.getenv("choices").split(",")
    )

    new_price = round(
        st.number_input(
            "Digite o gasto realizado (R$)",
            min_value=0.0,
            step=1.0
        ),
        3
    )

    

    if st.button("Registrar"):
        if not new_price:
            st.warning("Por favor digite o valor do gasto.")
        else:
            with st.spinner("Salvando..."):
                today_date = datetime.datetime.today() if not new_date else new_date
                new_gasto = Gasto(
                    date=today_date,
                    price=new_price,
                    category=new_category
                )

                new_gasto.save()

                st.info("Valor registrado!")