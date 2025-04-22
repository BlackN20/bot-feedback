import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd
import os
import threading

# Inicia o navegador com WebDriver Manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://web.whatsapp.com")
input("Escaneie o QR Code no navegador e pressione Enter aqui para continuar...")

def enviar_feedback(numero):
    try:
        link = f"https://web.whatsapp.com/send?phone={numero}&text=Olá! Como você avalia nosso atendimento de 0 a 10?"
        driver.get(link)
        time.sleep(15)
        botao_enviar = driver.find_element(By.XPATH, '//span[@data-icon="send"]')
        botao_enviar.click()
        print("Mensagem enviada.")
        resposta = esperar_resposta()
        responder_com_base_na_nota(resposta)
        salvar_feedback(numero, resposta)
        messagebox.showinfo("Sucesso", f"Feedback salvo com nota: {resposta}")
    except Exception as e:
        messagebox.showerror("Erro", str(e))

def esperar_resposta():
    print("Aguardando resposta...")
    ultima_msg = ""
    while True:
        try:
            mensagens = driver.find_elements(By.XPATH, '//div[contains(@class,"message-in")]//span[@dir="ltr"]')
            if mensagens:
                nova = mensagens[-1].text
                if nova != ultima_msg:
                    ultima_msg = nova
                    return nova
        except:
            pass
        time.sleep(5)

def responder_com_base_na_nota(nota):
    try:
        nota = int(nota)
        if nota >= 9:
            resposta = "Muito obrigado pelo seu feedback! 😊"
        elif nota <= 6:
            resposta = "Sentimos muito! Vamos trabalhar para melhorar. 🙏"
        else:
            resposta = "Obrigado pela sua nota! Qualquer sugestão é bem-vinda!"
    except:
        resposta = "Desculpe, não entendi sua resposta. Poderia enviar uma nota de 0 a 10?"
    caixa = driver.find_element(By.XPATH, '//div[@title="Digite uma mensagem"]')
    caixa.send_keys(resposta + Keys.ENTER)

def salvar_feedback(numero, nota):
    arquivo = "feedbacks.xlsx"
    df_novo = pd.DataFrame([{"Número": numero, "Nota": nota}])
    if os.path.exists(arquivo):
        df_existente = pd.read_excel(arquivo)
        df_total = pd.concat([df_existente, df_novo], ignore_index=True)
    else:
        df_total = df_novo
    df_total.to_excel(arquivo, index=False)

def iniciar_envio():
    numero = entrada_numero.get()
    if numero:
        thread = threading.Thread(target=enviar_feedback, args=(numero,))
        thread.start()
    else:
        messagebox.showwarning("Atenção", "Digite um número!")

# === Interface Gráfica ===
janela = tk.Tk()
janela.title("Bot de Feedback - WhatsApp")
janela.geometry("350x180")

tk.Label(janela, text="Número do cliente (com DDI):").pack(pady=10)
entrada_numero = tk.Entry(janela, width=30)
entrada_numero.pack()

botao_enviar = tk.Button(janela, text="Enviar Feedback", command=iniciar_envio)
botao_enviar.pack(pady=20)

janela.mainloop()
