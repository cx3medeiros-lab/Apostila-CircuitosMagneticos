import streamlit as st
import numpy as np
import pandas as pd

# --- 1. CONFIGURAÇÃO INICIAL ---
st.set_page_config(page_title="Apostila Interativa", layout="wide")

# --- 2. ESTILO CSS (Sua versão original com ajuste de limpeza) ---
st.markdown("""
    <style>
    /* Esconde a barra superior (raposinha) */
    header[data-testid="stHeader"] {
        display: none !important;
    }
    
    /* Remove o espaço em branco no topo */
    .main .block-container {
        padding-top: 1rem !important;
    }

    /* Aumenta o tamanho da fonte para projeção e leitura no celular */
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

# --- 3. CABEÇALHO E INTRODUÇÃO (RESTAURADO) ---
st.title("🧲 Circuitos Magnéticos: Módulo 1")
st.write("""
Bem-vindo à sua apostila interativa. Este ambiente combina interatividade entre teoria, simulação e 
cálculo em tempo real.

Vamos explorar circuitos magnéticos, entender como o fluxo magnético é conduzido através de materiais.
""")

# --- 4. CONTEÚDO TEÓRICO COM IMAGEM (RESTAURADO) ---
col1, col2 = st.columns([1, 1])

with col1:
    st.header("1. A Analogia de Hopkinson")
    st.write("""
    Assim como a eletricidade flui através de condutores, o **fluxo magnético** procura caminhos de baixa resistência (chamada aqui de **Relutância**).
    
    A relação fundamental é dada pela Lei de Hopkinson:
    """)
    st.latex(r"\mathcal{F} = \Phi \cdot \mathcal{R}")
    st.write(r"Onde $\mathcal{F}$ é a Força Magnetomotriz ($N \cdot I$).")

with col2:
    # Espaço para sua imagem
    try:
        st.image("CircuitoBasico01.png", 
                 caption="Circuito Magnético SIMPLES: com Núcleo e Bobina")
    except:
        st.warning("Arquivo de imagem 'CircuitoBasico01.png' não encontrado no repositório.")

# --- 5. AMBIENTE COMPUTACIONAL INTERATIVO (RESTAURADO) ---
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

# --- 6. CONCLUSÃO E NOTAS (RESTAURADO) ---
st.header("3. Conclusão para o PDF")
st.write("""
Ao imprimir este documento, os gráficos acima representarão o estado da sua última 
simulação. Utilize esta ferramenta para validar os exercícios da página 42 da apostila estática.
""")

# --- 7. INSTRUÇÃO DE IMPRESSÃO ---
st.markdown("---")
st.info("""
### 📄 Como salvar ou imprimir esta Apostila:
Para guardar os resultados das suas simulações em PDF:

1. **No Computador:** Pressione **Ctrl + P**.
2. **No Android (Brave/Chrome):** Menu (⋮) ➔ **Compartilhar** ➔ **Imprimir**.
3. **No iPhone (Safari):** Ícone **Compartilhar** ➔ **Imprimir**.

*Certifique-se de selecionar **'Salvar como PDF'** e, se necessário, ajuste a escala (zoom) na prévia.*
""")
