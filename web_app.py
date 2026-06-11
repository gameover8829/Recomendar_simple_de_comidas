import streamlit as st
from app import recomendar_comida

st.set_page_config(
    page_title="RECOMENDADOR SIMPLE DE COMIDAS",
    layout="centered"
)

st.title("RECOMENDADOR SIMPLE DE COMIDAS")
st.write(
    "Escribe los ingredientes que tienes disponibles y el sistema recomendará "
)

ingredientes = st.text_input(
    "Ingredientes disponibles",
    placeholder="Ejemplo huevo, tortilla, queso"
)

if st.button("Recomendar comida"):
    if not ingredientes.strip():
        st.warning("Ingresa al menos un ingrediente.")
    else:
        try:
            resultado = recomendar_comida(ingredientes)

            st.subheader("Resultado")
            st.write(f"**Comida recomendada:** {resultado['nombre']}")
            st.write(f"**Tipo:** {resultado['tipo']}")
            st.write(f"**Tiempo estimado:** {resultado['tiempo_estimado']}")
            st.write(f"**Coincidencia:** {resultado['score']}%")

            if resultado["matches"]:
                st.write(f"**Ingredientes relacionados:** {', '.join(resultado['matches'])}")
            else:
                st.write("**Ingredientes relacionados:** No hubo coincidencias exactas.")

            st.write(f"**Ingredientes de la comida:** {resultado['ingredientes']}")

        except Exception as error:
            st.error(f"Ocurrió un error: {error}")