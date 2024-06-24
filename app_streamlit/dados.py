import streamlit as st
import pandas as pd

periodo_counts = pd.DataFrame({
    "Período": ["Madrugada", "Manhã", "Tarde", "Noite"],
    "Contagem": [520, 659, 599, 1012]
})
import pandas as pd

variaveis = [
    ('ID_DELEGACIA', 'Identificação da delegacia'),
    ('NOME_DEPARTAMENTO', 'Nome do departamento de polícia'),
    ('NOME_SECCIONAL', 'Nome da seccional de polícia'),
    ('NOME_DELEGACIA', 'Nome da delegacia'),
    ('NOME_MUNICIPIO', 'Nome do município onde ocorreu o incidente'),
    ('ANO_BO', 'Ano do Boletim de Ocorrência'),
    ('NUM_BO', 'Número do Boletim de Ocorrência'),
    ('VERSAO', 'Versão do Boletim de Ocorrência'),
    ('NOME_DEPARTAMENTO_CIRC', 'Nome do departamento de polícia da área circunscrita'),
    ('NOME_SECCIONAL_CIRC', 'Nome da seccional de polícia da área circunscrita'),
    ('NOME_DELEGACIA_CIRC', 'Nome da delegacia da área circunscrita'),
    ('NOME_MUNICIPIO_CIRC', 'Nome do município da área circunscrita'),
    ('DATA_OCORRENCIA_BO', 'Data da ocorrência registrada no Boletim de Ocorrência'),
    ('HORA_OCORRENCIA', 'Hora da ocorrência registrada no Boletim de Ocorrência'),
    ('DESCRICAO_APRESENTACAO', 'Descrição da apresentação do caso'),
    ('DATAHORA_REGISTRO_BO', 'Data e hora do registro do Boletim de Ocorrência'),
    ('DATA_COMUNICACAO_BO', 'Data da comunicação do Boletim de Ocorrência'),
    ('DATAHORA_IMPRESSAO_BO', 'Data e hora da impressão do Boletim de Ocorrência'),
    ('DESCR_PERIODO', 'Descrição do período da ocorrência'),
    ('AUTORIA_BO', 'Informações sobre a autoria do Boletim de Ocorrência'),
    ('FLAG_INTOLERANCIA', 'Indicador de intolerância envolvida no incidente'),
    ('TIPO_INTOLERANCIA', 'Tipo de intolerância envolvida no incidente'),
    ('FLAG_FLAGRANTE', 'Indicador de flagrante no incidente'),
    ('FLAG_STATUS', 'Status do Boletim de Ocorrência'),
    ('DESC_LEI', 'Descrição da lei aplicada'),
    ('FLAG_ATO_INFRACIONAL', 'Indicador de ato infracional'),
    ('RUBRICA', 'Rubrica do incidente'),
    ('DESCR_CONDUTA', 'Descrição da conduta no incidente'),
    ('DESDOBRAMENTO', 'Desdobramentos do incidente'),
    ('CIRCUNSTANCIA', 'Circunstâncias do incidente'),
    ('DESCR_TIPOLOCAL', 'Descrição do tipo de local do incidente'),
    ('DESCR_SUBTIPOLOCAL', 'Descrição do subtipo de local do incidente'),
    ('CIDADE', 'Cidade do incidente'),
    ('BAIRRO', 'Bairro do incidente'),
    ('CEP', 'Código postal do local do incidente'),
    ('LOGRADOURO_VERSAO', 'Versão do logradouro'),
    ('LOGRADOURO', 'Logradouro do incidente'),
    ('NUMERO_LOGRADOURO', 'Número do logradouro do incidente'),
    ('LATITUDE', 'Latitude do local do incidente'),
    ('LONGITUDE', 'Longitude do local do incidente'),
    ('CONT_OBJETO', 'Conteúdo do objeto envolvido no incidente'),
    ('DESCR_MODO_OBJETO', 'Descrição do modo do objeto envolvido no incidente'),
    ('DESCR_TIPO_OBJETO', 'Descrição do tipo de objeto envolvido no incidente'),
    ('DESCR_SUBTIPO_OBJETO', 'Descrição do subtipo de objeto envolvido no incidente'),
    ('DESCR_UNIDADE', 'Descrição da unidade do objeto envolvido no incidente'),
    ('QUANTIDADE_OBJETO', 'Quantidade de objetos envolvidos no incidente'),
    ('MARCA_OBJETO', 'Marca do objeto envolvido no incidente'),
    ('FLAG_BLOQUEIO', 'Indicador de bloqueio do objeto'),
    ('FLAG_DESBLOQUEIO', 'Indicador de desbloqueio do objeto'),
    ('MES', 'Mês do incidente'),
    ('ANO', 'Ano do incidente')
]

df_variaveis = pd.DataFrame(variaveis, columns=['Nome', 'Descrição'])



def app():
    st.title("Dados")
    
    st.header("Obtenção dos Dados")
    st.markdown(""" Utilizamos dados de crimes da cidade de Ribeirão Preto, estado de São Paulo, no período de janeiro de 2023 até abril de 2024, divulgados pela Secretaria de Segurança Pública do estado. O conjunto de dados e sua explicação podem ser encontrados a seguir:""")

    st.write(df_variaveis)
    
    st.header("Pré-processamento")

    st.subheader("Conversão de Horário")
    st.markdown(""" Geramos as colunas ANO_OCORRENCIA MES_OCORRENCIA e DIA_OCORRENCIA a partir de DATA_OCORRENCIA_BO
                Para compreender melhor a distribuição das ocorrências ao longo do dia, utilizamos a coluna de hora de ocorrência (`HORA_OCORRENCIA`) e a transformamos em `PERIODO_DO_DIA`. """)
    st.markdown("""
    Os dados foram categorizados nos seguintes períodos:
    - **Madrugada**: 0h - 5:59h
    - **Manhã**: 6h - 11:59h
    - **Tarde**: 12h - 17:59h
    - **Noite**: 18h - 23:59h
    """)
    st.markdown("Contamos o número de ocorrências em cada período do dia:")
    st.dataframe(periodo_counts.set_index(periodo_counts.columns[0]))
    
    st.markdown("""
    Com isso, podemos visualizar padrões temporais nas ocorrências nos períodos descritos.
    """)

    st.subheader("Nomes de Bairros")
    st.markdown(""" 
                
                No processo de pré-processamento dos dados, a coluna `BAIRRO` foi corrigida para garantir a consistência dos registros. Inicialmente, aplicamos uma função de normalização que removeu acentos e caracteres especiais, convertendo todos os textos para maiúsculas. Em seguida, utilizamos um mapeamento específico para corrigir nomes de bairros comuns que poderiam ter variações devido a erros de digitação ou formatos diferentes. 

                Por exemplo, normalizamos e corrigimos o nome "Campos Elíseos" para "CAMPOS ELISEOS". Também a escrita com erro de digitação "Campos Elisios" para "CAMPOS ELISEOS".
                
                Essa normalização e correção foram essenciais para agrupar corretamente os dados por bairros, permitindo uma análise das ocorrências registradas em cada região.
                """)
    
    
    
    
    
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col3:
        if st.button("Ir para Análises"):
            st.session_state["current_page"] = "analises"
            st.rerun()
if __name__ == "__main__":
    app()
