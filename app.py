import streamlit as st
import numpy as np
import pandas as pd

# --- 1. CONFIGURAÇÃO INICIAL ---
st.set_page_config(page_title="Apostila Interativa", layout="wide")

# --- 2. ESTILO CSS SIMPLIFICADO ---
st.markdown("""
    <style>
    /* Esconde a barra superior (raposinha) para o site ficar limpo */
    header[data-testid="stHeader"] {
        display: none !important;
    }
    
    /* Ajusta o texto para ficar legível em telas de celular e projeção */
    .stMarkdown p {
        font-size: 22px !important;
        line-height: 1.5;
    }

    h1 { color: #1E88E5; font-size: 50px !important; }
    h2 { color: #0D47A1; font-size: 35px !important; }
    
    /* Fórmulas matemáticas em tamanho bom */
    .katex { font-size: 1.3em !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. CABEÇALHO E INTRODUÇÃO ---
st.title("🧲 Circuitos Magnéticos: Módulo 1")
st.write("Bem-vindo à sua apostila interativa de engenharia.")

# --- 4. CONTEÚDO TEÓRICO ---
col1, col2 = st.columns([1, 1])

with col1:
    st.header("1. A Analogia de Hopkinson")
    st.write("""
    O fluxo magnético ($\Phi$) percorre o caminho de menor **Relutância** ($\mathcal{R}$).
    """)
    st.latex(r"\mathcal{F} = \Phi \cdot \mathcal{R}")
    st.write(r"Onde $\mathcal{F} = N \cdot I$")

with col2:
    try:
        st.image("CircuitoBasico01.png", caption="Circuito Magnético Simples")
    except:
        st.info("Imagem ilustrativa aqui.")

# --- 5. LABORATÓRIO INTERATIVO ---
st.markdown("---")
st.header("2. Simulação de Fluxo")

c1, c2, c3 = st.columns(3)
with c1:
    n = st.slider("Espiras (N)", 10, 1000, 500)
with c2:
    corrente = st.slider("Corrente (I) [A]", 0.1, 10.0, 2.0)
with c3:
    ur = st.select_slider("Material (µr)", options=[100, 1000, 5000], value=1000)

# Cálculos Físicos
u0 = 4 * np.pi * 1e-7
area, comp = 0.01, 0.5
fmm = n * corrente
x_gap = np.linspace(0, 0.005, 100)
rel_n = comp / (ur * u0 * area)
rel_a = x_gap / (u0 * area)
fluxo = fmm / (rel_n + rel_a)

# Gráfico
df = pd.DataFrame({"Entreferro (m)": x_gap, "Fluxo (Wb)": fluxo})
st.line_chart(df.set_index("Entreferro (m)"))

st.success(f"FMM Gerada: {fmm:.1f} A.t")

# --- 6. CONCLUSÃO E INSTRUÇÕES ---
st.header("3. Conclusão")
st.write("Salve os resultados abaixo para o seu relatório.")

st.markdown("---")
st.warning("""
**Dica para PDF:** Para salvar esta apostila, use a função **Imprimir** do seu navegador (no celular fica em 'Compartilhar' -> 'Imprimir'). 
Na tela que abrir, você pode ajustar o zoom e as páginas manualmente antes de salvar.
""")
