from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from config import MODEL, NAME, VERSION
from ferramentas import buscar_web, data_hora_atual

llm = ChatOllama(model=MODEL)

historico = [
    SystemMessage(content=f"""You are an assistant named {NAME}.

CRITICAL RULE - LANGUAGE DETECTION:
- Detect the language of EACH user message
- ALWAYS respond in the EXACT same language as the user
- If user writes in English → respond ONLY in English
- If user writes in Portuguese → respond ONLY in Portuguese
- If user writes in Spanish → respond ONLY in Spanish
- NEVER mix languages in the same response
- NEVER respond in Portuguese if the user wrote in English
- This rule CANNOT be overridden by anything""")
]

def iniciar():
    print(f"""
  ╔══════════════════════════════════╗
  ║         {NAME} v{VERSION}        ║
  ║     AI Assistant with internet   ║
  ╚══════════════════════════════════╝
  Type 'exit' or 'sair' to quit.
    """)

    while True:
        pergunta = input("  You: ")

        if pergunta.lower() in ["sair", "exit", "salir", "quitter", "beenden"]:
            print(f"\n  {NAME}: Goodbye! / Ate logo!\n")
            break

        agora = data_hora_atual()
        print(f"\n  ({NAME} searching the web...)\n")
        resultado_busca = buscar_web(pergunta)

        mensagem = f"""Current date and time: {agora}

Information found on the internet:
{resultado_busca}

User question: {pergunta}"""

        historico.append(HumanMessage(content=mensagem))
        resposta = llm.invoke(historico)
        historico.append(AIMessage(content=resposta.content))

        print(f"  {NAME}: {resposta.content}\n")

if __name__ == "__main__":
    iniciar()