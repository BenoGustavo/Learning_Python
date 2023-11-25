#ENVIANDO EMAILS SMTP COM PYTHON
import os

#CARREGAR VARIAVEIS DE AMBIENTE
from dotenv import load_dotenv

#CRIAR CAMINHO DO ARQUIVO
from pathlib import Path

#SUBSTITUIR TEXTO
from string import Template

#IMPORTS FROM EMAIL
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#IMPORTS FROM SMTP
import smtplib

load_dotenv()

#Caminho para o arquivo html
ROOT_DIR = Path(__file__).parent
HTML_PATH = ROOT_DIR / 'email.html'

#Dados do remetente e destinatário
remetente = os.getenv('FROM-EMAIL',"")
destinatario = remetente

#Configurações do servidor SMTP
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = os.getenv('FROM-EMAIL',"")
smtp_password = os.getenv('FROM-PASSWORD',"")

#Mensagem de texto
with open(HTML_PATH, 'r') as html:
    texto_do_arquivo = html.read()
    Template = Template(texto_do_arquivo)
    texto_email = Template.substitute(nome='Fulano', idade='20',link='https://www.google.com')

# tranformar mensagem em MIMEMultipart
mime_multiplart = MIMEMultipart()
mime_multiplart["from"]  = remetente
mime_multiplart["to"] = destinatario
mime_multiplart["subject"] = "Assunto do email"

corpo_email = MIMEText(texto_email, "html","utf-8")
mime_multiplart.attach(corpo_email)

with smtplib.SMTP(smtp_server, smtp_port) as server:
    #manda um hello
    server.ehlo()
    #inicia o servidor
    server.starttls()
    #manda as credenciais
    server.login(smtp_username, smtp_password)
    #envia o email
    server.sendmail(remetente, destinatario, mime_multiplart.as_string())
    #finaliza a conexão
    server.quit()