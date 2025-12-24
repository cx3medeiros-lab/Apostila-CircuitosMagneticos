import streamlit as st
import numpy as np
import pandas as pd

# --- 1. CONFIGURAÇÃO INICIAL (DEVE SER A PRIMEIRA) ---
st.set_page_config(page_title="Apostila Interativa", layout="wide")

# --- 2. ESTILO CSS UNIFICADO ---
st.markdown("""
    <style>
    /* Esconde a raposinha e a barra superior */
    header[data-testid="stHeader"] {
        display: none !important;
    }
    
    /* Remove o espaço em branco no topo */
    .main .block-container {
        padding-top: 1rem !important;
    }

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

    /* Isso prepara a página para quando o usuário mandar imprimir pelo menu do navegador */
    @media print {
        /* Esconde elementos desnecessários na impressão */
        header, footer, .stSidebar, [data-testid="stHeader"] {
            display: none !important;
        }
        /* Garante que o conteúdo ocupe a largura total do papel */
        .main .block-container {
            max-width: 100% !important;
            padding: 0 !important;
            margin: 0 !important;
        }
        /* Força a quebra de página antes de cada título grande, se desejar */
        h1, h2 {
            page-break-before: always;
        }
        /* Mantém as cores e gráficos nítidos */
        * {
            -webkit-print-color-adjust: exact !important;
            print-color-adjust: exact !important;
        }
    }
    </style>
    """, unsafe_allow_html=True)
    
# --- 3. CABEÇALHO E INTRODUÇÃO ---
st.title("🧲 Circuitos Magnéticos: Módulo 1")
st.write("""
Bem-vindo à sua apostila interativa. Este ambiente combina interatividade entre teoria, simulação e 
cálculo em tempo real.
""")

# --- 4. CONTEÚDO TEÓRICO ---
col1, col2 = st.columns([1, 1])

with col1:
    st.header("1. A Analogia de Hopkinson")
    st.write("""
    Assim como a eletricidade flui através de condutores, o **fluxo magnético** procura caminhos de baixa resistência (chamada aqui de **Relutância**).
    """)
    st.latex(r"\mathcal{F} = \Phi \cdot \mathcal{R}")
    st.write(r"Onde $\mathcal{F}$ é a Força Magnetomotriz ($N \cdot I$).")

with col2:
    # Nota: Certifique-se de que o arquivo "CircuitoBasico01.png" está no seu GitHub
    try:
        st.image("CircuitoBasico01.png", 
                 caption="Circuito Magnético SIMPLES: com Núcleo e Bobina")
    except:
        st.warning("Arquivo de imagem 'CircuitoBasico01.png' não encontrado no repositório.")

# --- 5. AMBIENTE COMPUTACIONAL INTERATIVO ---
st.markdown("---")
st.header("2. Laboratório de Simulação")
st.write("Altere os parâmetros abaixo para observar o comportamento do fluxo no gráfico:")

c1, c2, c3 = st.columns(3)
with c1:
    n = st.slider("Número de Espiras (N)", 10, 1000, 500)
with c2:
    corrente = st.slider("Corrente Aplicada (I) em Amperes", 0.1, 10.0, 2.0)
with c3:
    ur = st.select_slider("Material (Permeabilidade Relativa)", options=[100, 500, 1000, 2000, 5000], value=2000)

# Cálculos
u0 = 4 * np.pi * 1e-7
area = 0.01
comprimento = 0.5
fmm = n * corrente

x_entreferro = np.linspace(0, 0.005, 100) # 0 a 5mm
relutancia_nucleo = comprimento / (ur * u0 * area)
relutancia_ar = x_entreferro / (u0 * area)
fluxo = fmm / (relutancia_nucleo + relutancia_ar)

# Gráfico
df_grafico = pd.DataFrame({"Entreferro (m)": x_entreferro, "Fluxo (Wb)": fluxo})
st.line_chart(df_grafico.set_index("Entreferro (m)"))

st.info(f"💡 Com os valores atuais, a Força Magnetomotriz gerada é de {fmm:.1f} A.t.")

# --- 6. CONCLUSÃO ---
st.header("3. Conclusão")
st.write("Utilize esta ferramenta para validar os exercícios da sua apostila.")

# --- INSTRUÇÃO DE IMPRESSÃO NO RODAPÉ ---
st.markdown("---")
st.info("""
### 📄 Como salvar ou imprimir esta Apostila:
Para guardar os resultados das suas simulações em PDF ou imprimir o material:

1. **No Computador:** Pressione **Ctrl + P** (ou Cmd + P no Mac).
2. **No Android (Brave/Chrome):** Toque nos **três pontinhos** no canto superior ➔ **Compartilhar** ➔ **Imprimir**.
3. **No iPhone (Safari):** Toque no ícone de **Compartilhar** (quadrado com seta) ➔ **Imprimir**.

*Certifique-se de selecionar **"Salvar como PDF"** na lista de impressoras.*
""")
