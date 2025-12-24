import streamlit as st
import numpy as np
import pandas as pd

# --- 1. CONFIGURAÇÃO INICIAL (DEVE SER A PRIMEIRA) ---
st.set_page_config(page_title="Apostila Interativa", layout="wide")

# --- 2. ESTILO CSS UNIFICADO ---
st.markdown("""
    <style>
    /* 1. INTERFACE DO SITE */
    
    /* Esconde a raposinha e a barra superior */
    header[data-testid="stHeader"] {
        display: none !important;
    }
    
    /* Ajusta o espaçamento do topo */
    .main .block-container {
        padding-top: 1.5rem !important;
    }

    /* Estilo do texto do corpo */
    .stMarkdown p {
        font-size: 24px !important;
        line-height: 1.6;
    }

    /* Estilo dos títulos */
    h1 { color: #1E88E5; font-size: 55px !important; font-weight: bold; }
    h2 { color: #0D47A1; font-size: 38px !important; margin-top: 30px; border-bottom: 2px solid #1E88E5; }
    
    /* Fórmulas matemáticas maiores */
    .katex { font-size: 1.4em !important; }

    /* 2. CONFIGURAÇÃO PARA IMPRESSÃO (PDF) */
/* 2. CONFIGURAÇÃO PARA IMPRESSÃO (PDF) */
    @media print {
        /* Remove as travas de rolagem e altura que cortam a página */
        html, body, .stApp, .main, .block-container {
            display: block !important;
            height: auto !important;
            overflow: visible !important;
            position: static !important;
        }

        /* Esconde elementos desnecessários */
        header, footer, .stSidebar, [data-testid="stHeader"], .stInfo, .stButton, .stSlider {
            display: none !important;
        }
        
        /* Garante que o conteúdo ocupe a largura total e não tenha margens estranhas */
        .main .block-container {
            max-width: 100% !important;
            padding: 0 !important;
            margin: 0 !important;
        }

        /* Força a quebra de página antes de cada título de seção para não cortar o gráfico ao meio */
        h2 {
            page-break-before: always;
        }

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
Bem-vindo à sua apostila interativa. Este ambiente permite explorar a teoria e realizar simulações
de circuitos magnéticos em tempo real.
""")

# --- 4. CONTEÚDO TEÓRICO ---
col1, col2 = st.columns([1, 1])

with col1:
    st.header("1. A Analogia de Hopkinson")
    st.write("""
    Assim como a eletricidade flui através de condutores, o **fluxo magnético** ($\Phi$) percorre caminhos 
    de baixa oposição, característica chamada de **Relutância** ($\mathcal{R}$).
    """)
    st.latex(r"\mathcal{F} = \Phi \cdot \mathcal{R}")
    st.write(r"Onde $\mathcal{F}$ é a Força Magnetomotriz ($N \cdot I$).")

with col2:
    # Espaço para imagem didática
    try:
        st.image("CircuitoBasico01.png", 
                 caption="Figura 1: Circuito Magnético com Núcleo Ferromagnético e Bobina")
    except:
        st.info("ℹ️ (Imagem 'CircuitoBasico01.png' será exibida aqui após o upload no GitHub)")

# --- 5. AMBIENTE COMPUTACIONAL INTERATIVO ---
st.markdown("---")
st.header("2. Laboratório de Simulação")
st.write("Ajuste os parâmetros para recalcular o fluxo magnético no sistema:")

# Controles de simulação
c1, c2, c3 = st.columns(3)
with c1:
    n = st.slider("Número de Espiras (N)", 10, 1000, 500)
with c2:
    corrente = st.slider("Corrente (I) [Amperes]", 0.1, 10.0, 2.0)
with c3:
    ur = st.select_slider("Material ($\mu_r$)", options=[100, 500, 1000, 2000, 5000], value=2000)

# Lógica de Cálculo (Física)
u0 = 4 * np.pi * 1e-7  # Permeabilidade do vácuo
area = 0.01            # Área em m²
comprimento = 0.5      # Comprimento do núcleo em m
fmm = n * corrente     # Força Magnetomotriz

# Vetor de entreferro para o gráfico
x_entreferro = np.linspace(0, 0.005, 100) # De 0 a 5mm
relutancia_nucleo = comprimento / (ur * u0 * area)
relutancia_ar = x_entreferro / (u0 * area)
fluxo = fmm / (relutancia_nucleo + relutancia_ar)

# Exibição do Gráfico
df_grafico = pd.DataFrame({"Entreferro (m)": x_entreferro, "Fluxo (Wb)": fluxo})
st.line_chart(df_grafico.set_index("Entreferro (m)"))

st.success(f"✅ Resultado Atual: Força Magnetomotriz = **{fmm:.1f} A.t**")

# --- 6. CONCLUSÃO ---
st.header("3. Conclusão")
st.write("""
Utilize os dados gerados no gráfico acima para completar os exercícios propostos. 
Lembre-se que o aumento do entreferro eleva drasticamente a relutância total do circuito.
""")

# --- 7. INSTRUÇÃO DE PDF (RODAPÉ) ---
st.markdown("---")
st.info("""
### 📄 Como gerar o PDF da Apostila:
Para salvar os resultados desta simulação:

1. **No Computador:** Use **Ctrl + P**.
2. **No Android (Brave/Chrome):** Vá no Menu (⋮) ➔ **Compartilhar** ➔ **Imprimir**.
3. **No iPhone (Safari):** Ícone **Compartilhar** ➔ **Imprimir**.

*Selecione **'Salvar como PDF'** nas opções de impressora.*
""")
