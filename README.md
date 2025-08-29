# 🤖 Bot de Feedback - WhatsApp

Um bot desenvolvido em Python para coletar e gerenciar feedbacks de clientes via WhatsApp Web de forma automatizada.  
O bot envia mensagens, aguarda respostas, responde de acordo com a nota recebida e salva os dados em um arquivo Excel.

---

## Funcionalidades
- Envio automático de mensagens de feedback pelo WhatsApp.
- Aguardando resposta do cliente de forma automatizada.
- Resposta automática baseada na nota do cliente:
  - 9-10: "Muito obrigado pelo seu feedback! 😊"
  - 7-8: "Obrigado pela sua nota! Qualquer sugestão é bem-vinda!"
  - 0-6: "Sentimos muito! Vamos trabalhar para melhorar. 🙏"
- Armazena todos os feedbacks em um arquivo Excel (`feedbacks.xlsx`).
- Interface gráfica simples usando Tkinter.
- Suporte a múltiplos envios via threading para não travar a interface.

---

## Tecnologias e Bibliotecas Utilizadas
- Python 3.x
- **Tkinter** – interface gráfica
- **Selenium** – automação do WhatsApp Web
- **webdriver-manager** – gerenciamento automático do ChromeDriver
- **pandas** – manipulação e armazenamento de dados
- **openpyxl** – leitura e escrita de arquivos Excel
- Excel – armazenamento dos feedbacks

---

## Como Executar
1. Clone o repositório:
   ```bash
   git clone https://github.com/BlackN20/bot-feedback.git
   cd bot-feedback
