from langchain_community.tools import DuckDuckGoSearchRun
from datetime import datetime

# Busca na internet
search = DuckDuckGoSearchRun()

def buscar_web(pergunta: str) -> str:
    return search.run(pergunta)

def data_hora_atual() -> str:
    return datetime.now().strftime("%d/%m/%Y %H:%M")