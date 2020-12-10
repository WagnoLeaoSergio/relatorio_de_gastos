import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import seaborn as sns
import datetime

from models import Gasto

sns.set_style("whitegrid")

# @st.cache(suppress_st_warning=True)
def get_data(month='todos'):

    data = {
        "date": [],
        "price": [],
        "category": []
    }

    for gasto in Gasto.objects:
        data["date"].append(gasto.date)
        data["price"].append(gasto.price)
        data["category"].append(gasto.category)

    data = pd.DataFrame(data)

    if month != 'todos':
        start_date = datetime.datetime.strptime(f'2020-{month}-1', '%Y-%m-%d')
        end_date = datetime.datetime.strptime(
            f"2020-{month}-{'30' if month != 2 else '28'}", '%Y-%m-%d'
        )
        mask = (data['date'] > start_date) & (data['date'] < end_date)
        data = data.loc[mask]
        
        if data.empty:
            st.error("Mês selecionado não disponível")

    return data.sort_values(by="date")

def date_price_plot(data, show_others=True):

    fig ,ax = plt.subplots()

    if show_others:
        lp = sns.lineplot(
            data=data.groupby("date").sum().reset_index(),
            x='date',
            y='price'
        )
    else:
        lp = sns.lineplot(
            data=data.query("category != 'outros'").groupby("date").sum().reset_index(),
            x='date',
            y='price'
        )

    date_form = DateFormatter("%Y-%m-%d")
    ax.xaxis.set_major_formatter(date_form)

    plt.xticks(rotation=30)

    ax.set(
        xlabel="Data",
        ylabel="Valor gasto (R$)",
        title="Valor gasto em função do tempo"
    )

    return fig

def category_hist(data, show_others=True):
    fig ,ax = plt.subplots()

    if show_others:
        new_data = data
    else:
        new_data = data.query("category != 'outros'")
    
    sns.barplot(
        data=new_data.groupby(by='category').sum().reset_index(),
        x='category',
        y='price'
    )

    ax.set(
        xlabel="Categoria",
        ylabel="Valor gasto (R$)",
        title="Valor gasto por categoria"
    )

    return fig

def dashboard_page():

    st.title("Relatório de Gastos")

    month_selected = st.selectbox(
        "Selecione o mês desejado:", ['todos'] + [ i for i in range(1,13) ]
    )

    gastos = get_data(month=month_selected)

    if not gastos.empty:
        show_others = st.checkbox("Mostrar categoria 'outros'?")

        st.pyplot(date_price_plot(gastos, show_others=show_others))
        st.pyplot(category_hist(gastos, show_others=show_others))


        st.markdown(
            f"""
                <center>
                    <h2> Total gasto:  R$ {round(gastos['price'].sum(), 2)} </h2>
                    <h2> Média total:  R$ {round(gastos['price'].mean(), 2)} </h2>
                </center>
                <br>
            """
        , unsafe_allow_html=True)

        data_expander = st.beta_expander("Tabela de dados")

        data_expander.table(gastos)

    else:
        st.info("Sem dados disponiveis")