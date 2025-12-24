import streamlit as st

# Para que o Streamlit use 100% da largura da tela do celular (evitando margens brancas laterais):
st.set_page_config(layout="wide")

import streamlit as st

# Código para esconder o menu (hambúrguer) e o rodapé (Streamlit/GitHub)
hide_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """
st.markdown(hide_style, unsafe_allow_html=True)

st.title("Hello World!")
import streamlit as st
import numpy as np
import pandas as pd

# 1. CONFIGURAÇÃO DA PÁGINA E ESTILO (CSS para Projeção)
st.set_page_config(page_title="Apostila Magnética", layout="wide")

st.markdown("""
    <style>
    /* Aumenta o tamanho da fonte do corpo do texto */
    .stMarkdown p {
        font-size: 24px !important;
        line-height: 1.6;
    }
    /* Estiliza títulos */
    h1 { color: #1E88E5; font-size: 60px !important; }
    h2 { color: #0D47A1; font-size: 40px !important; margin-top: 30px; }
    /* Estiliza fórmulas matemáticas */
    .katex { font-size: 1.5em !important; }
    </style>
    """, unsafe_allow_html=True)

# 2. CABEÇALHO E INTRODUÇÃO
st.title("🧲 Circuitos Magnéticos: Módulo 1")
st.write("""
Bem-vindo à sua apostila interativa. Este ambiente combina interatividade entre teoria, simulação e 
cálculo em tempo real.

Vamos explorar circuitos magnéticos, entender como o fluxo magnético é conduzido através de materiais.
""")

# 3. CONTEÚDO TEÓRICO COM IMAGEM
col1, col2 = st.columns([1, 1])

with col1:
    st.header("1. A Analogia de Hopkinson")
    st.write("""
    Assim como a eletricidade flui através de condutores, o **fluxo magnético** procura caminhos de baixa resistência (chamada aqui de **Relutância**).
    
    A relação fundamental é dada pela Lei de Hopkinson:
    """)
    st.latex(r"\mathcal{F} = \Phi \cdot \mathcal{R}")
    st.write("Onde $\mathcal{F}$ é a Força Magnetomotriz ($N \cdot I$).")

with col2:
    # Espaço para uma imagem (exemplo de link público)
   st.image("CircuitoBasico01.png", 
             caption="Circuito Magnético SIMPLES: com Núcleo e Bobina")

# 4. AMBIENTE COMPUTACIONAL INTERATIVO
st.markdown("---")
st.header("2. Laboratório de Simulação")
st.write("Altere os parâmetros abaixo para observar o comportamento do fluxo no gráfico:")

# Sliders para controle em tempo real
c1, c2, c3 = st.columns(3)
with c1:
    n = st.slider("Número de Espiras (N)", 10, 1000, 500)
with c2:
    corrente = st.slider("Corrente Aplicada (I) em Amperes", 0.1, 10.0, 2.0)
with c3:
    ur = st.select_slider("Material (Permeabilidade Relativa)", options=[100, 500, 1000, 2000, 5000], value=2000)

# Cálculos em Background
u0 = 4 * np.pi * 1e-7
area = 0.01
comprimento = 0.5
fmm = n * corrente

# Criar dados para o gráfico (Fluxo vs Entreferro)
x_entreferro = np.linspace(0, 0.005, 100) # 0 a 5mm
relutancia_nucleo = comprimento / (ur * u0 * area)
relutancia_ar = x_entreferro / (u0 * area)
fluxo = fmm / (relutancia_nucleo + relutancia_ar)

# Exibição do Gráfico Dinâmico
df_grafico = pd.DataFrame({"Entreferro (m)": x_entreferro, "Fluxo (Wb)": fluxo})
st.line_chart(df_grafico.set_index("Entreferro (m)"))

st.info(f"💡 Com os valores atuais, a Força Magnetomotriz gerada é de {fmm:.1f} A.t.")

# 5. CONCLUSÃO E NOTAS
st.header("3. Conclusão para o PDF")
st.write("""
Ao imprimir este documento, os gráficos acima representarão o estado da sua última 
simulação. Utilize esta ferramenta para validar os exercícios da página 42 da apostila estática.
""")
