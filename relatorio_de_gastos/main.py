import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

import dashboard
import register


PAGES = {
    "Visualizar gastos": dashboard.dashboard_page,
    "Registrar gasto": register.register_page
}

side_options = st.sidebar.selectbox(
    "Opções", ["Visualizar gastos", "Registrar gasto"]
)

page = PAGES[side_options]

page()