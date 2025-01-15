import streamlit as st
import asyncio
from services.brasilapi import *

def consultar_cep():
    cep = st.text_input("Digite um CEP:", "")
    if st.button("Consultar CEP") or cep:  
        if len(cep) == 8 and cep.isdigit():
            result_cep = asyncio.run(getCep(cep))
            st.write(result_cep)
        else:
            st.write("Por favor, insira um CEP válido.")

def consultar_ddd():
    ddd = st.text_input("Digite um DDD:", "")
    if st.button("Consultar DDD") or ddd:
        if len(ddd) == 2 and ddd.isdigit():
            result_ddd = asyncio.run(getDdd(ddd))
            st.write(result_ddd)
        else:
            st.write("Por favor, insira um DDD válido.")

def consultar_cnpj():
    cnpj = st.text_input("Digite um CNPJ:", "")
    if st.button("Consultar CNPJ") or cnpj:
        if len(cnpj) == 14 and cnpj.isdigit():
            result_cnpj = asyncio.run(getCnpj(cnpj))
            st.write(result_cnpj)
        else:
            st.write("Por favor, insira um CNPJ válido.")

def consultar_feriados():
    ano = st.text_input("Digite o ano para consultar os feriados:", "")
    if st.button("Consultar Feriados") or ano:
        if ano.isdigit() and len(ano) == 4:
            result_feriados = asyncio.run(getFeriados(ano))
            st.write(result_feriados)
        else:
            st.write("Por favor, insira um ano válido (ex: 2025).")

def main():
    st.title("Brasil 🇧🇷")
    pagina = st.selectbox("Escolha a consulta", ["CEP", "DDD", "CNPJ", "Feriados"])

    if pagina == "CEP":
        consultar_cep()
    elif pagina == "DDD":
        consultar_ddd()
    elif pagina == "CNPJ":
        consultar_cnpj()
    elif pagina == "Feriados":
        consultar_feriados()

if __name__ == "__main__":
    main()
