# DIAGNOSIS-GPT

Este é um mini-projeto educativo, realizado durante a disciplina ECOM031 - INTELIGÊNCIA ARTIFICIAL
que simula um sistema de diagnóstico médico com interface gráfica em Python. O sistema interage com o usuário por meio de linguagem natural (via chatbot), coleta sintomas descritos e tenta fornecer um diagnóstico baseado em regras simples.

---

## Como clonar e executar

1. **Clone o repositório:**

   ```bash
   git clone https://KauaLessa/DIAGNOSIS-GPT
   cd diagnosis-chatbot
   ```

2. **(Opcional) Crie um ambiente virtual:**

   ```bash
   python -m venv venv
   source venv/bin/activate   # No Windows: venv\Scripts\activate
   ```

3. **Execute o chatbot:**

   ```bash
   python chatbot.py
   ```

Certifique-se de estar em um ambiente com suporte a interface gráfica (GUI).

---

## Como funciona

* O sistema utiliza uma interface feita com `Tkinter`.
* O usuário descreve seus sintomas em linguagem natural no campo de entrada.
* O sistema analisa a entrada, extrai sintomas relevantes e tenta compará-los com um conjunto de **regras pré-definidas**.
* Quando uma combinação de sintomas é suficiente, o chatbot fornece um possível diagnóstico e explica a lógica usada.
* A conversa reinicia após cada diagnóstico.

---

## Exemplo de uso

```
Você: Estou com febre e dor de garganta.
Bot: Entendi que você relata: febre, dor de garganta.
Bot: Possível diagnóstico: Amigdalite.
Explicação: Dor de garganta com febre pode indicar uma inflamação nas amígdalas.
```

---

## Tecnologias utilizadas

* Python 3.x
* Interface gráfica com **Tkinter** (padrão da biblioteca do Python)

---

## Observações

* Este projeto é **educativo** e não deve ser usado para diagnóstico médico real.
* O sistema utiliza uma abordagem simples baseada em palavras-chave e regras fixas.
* A extração de sintomas ignora diferenças de caixa (maiúsculas/minúsculas) e acentuação.

---

