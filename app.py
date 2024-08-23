import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Título do site
st.title("Demonstração de Capacidades do Streamlit")

# Texto introdutório
st.write("""
Este é um exemplo básico de um site criado com Streamlit.
Ele demonstra algumas funcionalidades básicas como:
- Exibição de texto e Markdown
- Gráficos
- Exibição de dados em tabelas
- Interatividade com o usuário
""")

# Exibindo texto em Markdown
st.markdown("### Exemplo de Markdown")
st.markdown("**Streamlit** é uma ferramenta poderosa para criar *aplicações web* de forma rápida e simples.")

# Gráfico de exemplo
st.markdown("### Exemplo de Gráfico")
data = np.random.randn(100)
fig, ax = plt.subplots()
ax.hist(data, bins=20)
st.pyplot(fig)

# Tabela de dados
st.markdown("### Exemplo de Tabela de Dados")
df = pd.DataFrame({
    'Coluna A': np.random.rand(10),
    'Coluna B': np.random.rand(10),
    'Coluna C': np.random.rand(10)
})
st.dataframe(df)

# Interatividade com o usuário
st.markdown("### Exemplo de Interatividade")
nome = st.text_input("Digite seu nome")
if nome:
    st.write(f"Olá, {nome}! Obrigado por testar este exemplo de site.")

# Slider para selecionar um valor
valor = st.slider("Selecione um valor", 0, 100, 50)
st.write(f"Você selecionou: {valor}")

# Rodapé
st.markdown("### Rodapé")
st.write("Este é um exemplo básico para demonstrar como criar um site com Streamlit.")

