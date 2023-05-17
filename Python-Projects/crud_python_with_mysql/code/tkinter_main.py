import tkinter as tk

from crud_funcionario import create_funcionario, read_funcionario, update_funcionario, delete_funcionario, show_all_id_from_table
from crud_medico import create_medicos,read_medicos,update_medicos,delete_medicos

def clear_window(window):
    for widget in window.winfo_children():
        widget.destroy()


def main_menu():
    clear_window(window)

    escolher = tk.Label(window, text="What table do you want o work with?")
    escolher.pack(pady=10)

    clinica = tk.Button(window, text="Clinica")
    clinica.config(width=20, height=3)
    clinica.pack(side="top", pady=10,)

    doencas = tk.Button(window, text="Doencas")
    doencas.config(width=20, height=3)
    doencas.pack(side="top", pady=10)

    funcionario = tk.Button(window, text="Funcionarios",
                            command=funcionario_table)
    funcionario.config(width=20, height=3)
    funcionario.pack(side="top", pady=10)

    hospital = tk.Button(window, text="Hospital")
    hospital.config(width=20, height=3)
    hospital.pack(side="top", pady=10)

    medicos = tk.Button(window, text="Medicos",command=medico_table)
    medicos.config(width=20, height=3)
    medicos.pack(side="top", pady=10)

    paciente = tk.Button(window, text="Paciente")
    paciente.config(width=20, height=3)
    paciente.pack(side="top", pady=10)

    prontuarios = tk.Button(window, text="Prontuarios")
    prontuarios.config(width=20, height=3)
    prontuarios.pack(side="top", pady=10)


def funcionario_id_read():
    def on_click_read_funcionario():
        ids = insert_id_for_read.get()
        dados_funcionario = read_funcionario(int(ids))

        funcionario_id_read()
        for item in dados_funcionario:
            rotulo_dados = tk.Label(
                window, text=f"{item.capitalize()} - {dados_funcionario[item]}")
            rotulo_dados.config(relief=("sunken"), width=40, justify="center")
            rotulo_dados.pack(side="top", pady=3)

    clear_window(window)

    funcionario_read_tittle_label = tk.Label(
        window, text="Id's from funcionarios")
    funcionario_read_tittle_label.pack(pady=10, side="top")

    # lista_de_ids = show_all_id_from_table("funcionario")

    id_funcionario = tk.StringVar()
    id_funcionario.set(list(show_all_id_from_table("funcionario")))

    id_funcionario_label = tk.Label(window, textvariable=id_funcionario,)
    id_funcionario_label.config(relief="sunken")
    id_funcionario_label.pack(padx=3, side="top")

    insert_id_for_read = tk.Entry(window)
    insert_id_for_read.pack(pady=10, side="top")

    botao = tk.Button(window, text="Search for funcionario",
                      command=on_click_read_funcionario)
    botao.pack(pady=10)

    voltar = tk.Button(window, text="Return", width=25,
                       command=funcionario_table)
    voltar.pack(side="bottom", pady=10)

def on_click_creating_funcionario():
    def on_click_create_funcionario():
        try:
            cpf_value = cpf_entry.get()
            nome_value = nome_entry.get()
            email_value = email.get()
            telefone_value = telefone.get()
            funcao_value = funcao.get()
            logradouro_value = logradouro_entry.get()
            cep_value = cep_entry.get()
            numero_casa_value = numero_casa_entry.get()
            bairro_value = bairro_entry.get()

            create_funcionario(cpf_value, nome_value, email_value, telefone_value,
                               logradouro_value, funcao_value, cep_value, numero_casa_value, bairro_value)

            on_click_creating_funcionario()

            funcionario_created = tk.Label(
                window, text=f"Funcionario {nome_value.capitalize()} criado com sucesso")
            funcionario_created.config(fg="green")
            funcionario_created.pack(side="top")

        except Exception as error:
            print(error)
            on_click_creating_funcionario()
            funcionario_not_created = tk.Label(
                window, text="Error ao criar o usuario")
            funcionario_not_created.config(fg="red")
            funcionario_not_created.pack(side="top")

    clear_window(window)

    frame_right = tk.Frame(window)
    frame_right.config(bg="lightblue",relief="sunken")
    frame_right.pack(padx=15,pady=15,anchor='nw',side="right")

    frame_left = tk.Frame(window)
    frame_left.config(bg="lightblue",relief="sunken")
    frame_left.pack(padx=15,pady=15,anchor="ne",side="left")

    funcionario_create_tittle_label = tk.Label(
        frame_left, text="Insert the information from the new funcionario")
    funcionario_create_tittle_label.config(relief="sunken",)
    funcionario_create_tittle_label.pack(pady=20, side="top")

    create_funcionario_tittle = tk.Label(
        frame_left, text="Insert your CPF", width=25)
    create_funcionario_tittle.config(relief="ridge")
    create_funcionario_tittle.pack(pady=1,padx=10, side="top")

    cpf_entry = tk.Entry(frame_left, width=30)
    cpf_entry.pack(pady=10,padx=10, side="top")

    create_funcionario_tittle = tk.Label(
        frame_left, text="Insert your name", width=25)
    create_funcionario_tittle.config(relief="ridge")
    create_funcionario_tittle.pack(pady=1,padx=10, side="top")

    nome_entry = tk.Entry(frame_left, width=30)
    nome_entry.pack(pady=10,padx=10, side="top")

    create_funcionario_tittle = tk.Label(
        frame_left, text="Insert your email", width=25)
    create_funcionario_tittle.config(relief="ridge")
    create_funcionario_tittle.pack(pady=1,padx=10, side="top")

    email = tk.Entry(frame_left, width=30)
    email.pack(pady=10,padx=10, side="top")

    create_funcionario_tittle = tk.Label(
        frame_left, text="Insert your telefone number", width=25)
    create_funcionario_tittle.config(relief="ridge")
    create_funcionario_tittle.pack(pady=1,padx=10, side="top")

    telefone = tk.Entry(frame_left, width=30)
    telefone.pack(pady=10,padx=10, side="top")

    create_funcionario_tittle = tk.Label(
        frame_left, text="Insert your role", width=25)
    create_funcionario_tittle.config(relief="ridge")
    create_funcionario_tittle.pack(pady=1,padx=10, side="top")

    funcao = tk.Entry(frame_left, width=30)
    funcao.pack(pady=10,padx=10, side="top")

    funcionario_create_tittle_label = tk.Label(
        frame_right, text="Insert the endereco from the new funcionario")
    funcionario_create_tittle_label.config(relief="sunken", justify="center")
    funcionario_create_tittle_label.pack(pady=20,padx=10, side="top")

    create_funcionario_tittle = tk.Label(
        frame_right, text="Insert your logradouro", width=25)
    create_funcionario_tittle.config(relief="ridge")
    create_funcionario_tittle.pack(pady=1,padx=10, side="top")

    logradouro_entry = tk.Entry(frame_right, width=30)
    logradouro_entry.pack(pady=10,padx=10, side="top")

    create_funcionario_tittle = tk.Label(
        frame_right, text="Insert your cep", width=25)
    create_funcionario_tittle.config(relief="ridge")
    create_funcionario_tittle.pack(pady=1, side="top")

    cep_entry = tk.Entry(frame_right, width=30)
    cep_entry.pack(pady=10,padx=10,side="top")

    create_funcionario_tittle = tk.Label(
        frame_right, text="Insert the number of ur house", width=25)
    create_funcionario_tittle.config(relief="ridge")
    create_funcionario_tittle.pack(pady=1,padx=10,side="top")

    numero_casa_entry = tk.Entry(frame_right, width=30)
    numero_casa_entry.pack(pady=10,padx=10,side="top")

    create_funcionario_tittle = tk.Label(
        frame_right, text="Insert your bairro", width=25)
    create_funcionario_tittle.config(relief="ridge")
    create_funcionario_tittle.pack(pady=1,padx=10,side="top")

    bairro_entry = tk.Entry(frame_right, width=30)
    bairro_entry.pack(pady=10,padx=10, side="top")

    endereco_create_tittle_label = tk.Button(
        frame_right, text="Create funcionario", width=25, command=on_click_create_funcionario)
    endereco_create_tittle_label.pack(pady=5, side="bottom",anchor='s')

    voltar = tk.Button(frame_right, text="Return", width=25,
                       command=funcionario_table)
    voltar.pack(side="bottom", pady=25,anchor='s')

def on_click_delete_funcionario():
    def on_click_delete_funcionario_function():
        id_to_delete_funcionario = insert_id_for_delete.get()
        try:
            delete_funcionario(int(id_to_delete_funcionario))

            on_click_delete_funcionario()

            deletado_com_sucesso = tk.Label(
                window, text="Funcionario deletado com sucesso")
            deletado_com_sucesso.config(relief="sunken", bg="green")
            deletado_com_sucesso.pack(padx=3, side="top")

        except Exception as error:
            print(error)

            on_click_delete_funcionario()
            
            deletado_com_sucesso = tk.Label(
                window, text="Falha ao deletar o funcionario")
            deletado_com_sucesso.config(relief="sunken", bg="red")
            deletado_com_sucesso.pack(padx=3, side="top")

    clear_window(window)

    delete_funcionario_label = tk.Label(
        window, text="Id's from the funcionarios")
    delete_funcionario_label.pack(side="top", pady=10)

    id_funcionario = tk.StringVar()
    id_funcionario.set(list(show_all_id_from_table("funcionario")))

    id_funcionario_label = tk.Label(window, textvariable=id_funcionario,)
    id_funcionario_label.config(relief="sunken")
    id_funcionario_label.pack(padx=3, side="top")

    insert_id_for_delete = tk.Entry(window)
    insert_id_for_delete.pack(pady=10, side="top")

    botao = tk.Button(window, text="Delete funcionario",
                      command=on_click_delete_funcionario_function)
    botao.pack(pady=10)

    voltar = tk.Button(window, text="Return", width=25,
                       command=funcionario_table)
    voltar.pack(side="bottom", pady=10)

def on_click_update_funcionario():
    def on_click_updating_funcionario():
        try:
            id_value = id_entry.get()
            cpf_value = cpf_entry.get()
            nome_value = nome_entry.get()
            email_value = email.get()
            telefone_value = telefone.get()
            funcao_value = funcao.get()
            logradouro_value = logradouro_entry.get()
            cep_value = cep_entry.get()
            numero_casa_value = numero_casa_entry.get()
            bairro_value = bairro_entry.get()

            update_funcionario(int(id_value), cpf_value, nome_value, email_value, telefone_value,
                               logradouro_value, funcao_value, cep_value, numero_casa_value, bairro_value)

            on_click_update_funcionario()

            funcionario_created = tk.Label(
                window, text=f"Funcionario {nome_value.capitalize()} atualizado com sucesso")
            funcionario_created.config(fg="green")
            funcionario_created.pack(side="top")

        except Exception as error:
            print(error)

            on_click_update_funcionario()

            funcionario_not_created = tk.Label(
                window, text="Error ao atualizar o usuario")
            funcionario_not_created.config(fg="red")
            funcionario_not_created.pack(side="top")

    clear_window(window)

    frame_right = tk.Frame(window)
    frame_right.config(bg="lightblue",relief="sunken")
    frame_right.pack(padx=15,pady=15,anchor='nw',side="right")

    frame_left = tk.Frame(window)
    frame_left.config(bg="lightblue",relief="sunken")
    frame_left.pack(padx=15,pady=15,anchor="ne",side="left")

    frame_middle = tk.Frame(window)
    frame_middle.config(bg="lightblue",relief="sunken")
    frame_middle.pack(padx=15,pady=15,anchor="n",side="top")

    update_funcionario_label = tk.Label(
        frame_middle, text="Id's from the funcionarios")
    update_funcionario_label.pack(side="top", pady=5)

    id_funcionario = tk.StringVar()
    id_funcionario.set(list(show_all_id_from_table("funcionario")))

    id_funcionario_label = tk.Label(frame_middle, textvariable=id_funcionario,)
    id_funcionario_label.config(relief="sunken")
    id_funcionario_label.pack(padx=3, side="top")

# Update funcionario text boxes

    funcionario_create_tittle_label = tk.Label(
        frame_left, text="Update funcionario")
    funcionario_create_tittle_label.config(relief="sunken", justify="center")
    funcionario_create_tittle_label.pack(pady=5, side="top")

    create_funcionario_tittle = tk.Label(
        frame_left, text="Insert your ID", width=25)
    create_funcionario_tittle.config(relief="ridge")
    create_funcionario_tittle.pack(pady=1, side="top")

    id_entry = tk.Entry(frame_left, width=30)
    id_entry.pack(pady=10, side="top")

    create_funcionario_tittle = tk.Label(
        frame_left, text="Insert your CPF", width=25)
    create_funcionario_tittle.config(relief="ridge")
    create_funcionario_tittle.pack(pady=1, side="top")

    cpf_entry = tk.Entry(frame_left, width=30)
    cpf_entry.pack(pady=10, side="top")

    create_funcionario_tittle = tk.Label(
        frame_left, text="Insert your name", width=25)
    create_funcionario_tittle.config(relief="ridge")
    create_funcionario_tittle.pack(pady=1, side="top")

    nome_entry = tk.Entry(frame_left, width=30)
    nome_entry.pack(pady=10, side="top")

    create_funcionario_tittle = tk.Label(
        frame_left, text="Insert your email", width=25)
    create_funcionario_tittle.config(relief="ridge")
    create_funcionario_tittle.pack(pady=1, side="top")

    email = tk.Entry(frame_left, width=30)
    email.pack(pady=10, side="top")

    create_funcionario_tittle = tk.Label(
        frame_left, text="Insert your telefone number", width=25)
    create_funcionario_tittle.config(relief="ridge")
    create_funcionario_tittle.pack(pady=1, side="top")

    telefone = tk.Entry(frame_left, width=30)
    telefone.pack(pady=10, side="top")

    create_funcionario_tittle = tk.Label(
        frame_left, text="Insert your role", width=25)
    create_funcionario_tittle.config(relief="ridge")
    create_funcionario_tittle.pack(pady=1, side="top")

    funcao = tk.Entry(frame_left, width=30)
    funcao.pack(pady=10, side="top")

    funcionario_create_tittle_label = tk.Label(
        frame_right, text="Funcionario endereco")
    funcionario_create_tittle_label.config(relief="sunken",)
    funcionario_create_tittle_label.pack(pady=20, side="top")

    create_funcionario_tittle = tk.Label(
        frame_right, text="Insert your logradouro", width=25)
    create_funcionario_tittle.config(relief="ridge")
    create_funcionario_tittle.pack(pady=1, side="top")

    logradouro_entry = tk.Entry(frame_right, width=30)
    logradouro_entry.pack(pady=10, side="top")

    create_funcionario_tittle = tk.Label(
        frame_right, text="Insert your cep", width=25)
    create_funcionario_tittle.config(relief="ridge")
    create_funcionario_tittle.pack(pady=1, side="top")

    cep_entry = tk.Entry(frame_right, width=30)
    cep_entry.pack(pady=10, side="top")

    create_funcionario_tittle = tk.Label(
        frame_right, text="Insert the number of ur house", width=25)
    create_funcionario_tittle.config(relief="ridge")
    create_funcionario_tittle.pack(pady=1, side="top")

    numero_casa_entry = tk.Entry(frame_right, width=30)
    numero_casa_entry.pack(pady=10, side="top")

    create_funcionario_tittle = tk.Label(
        frame_right, text="Insert your bairro", width=25)
    create_funcionario_tittle.config(relief="ridge")
    create_funcionario_tittle.pack(pady=1, side="top")

    bairro_entry = tk.Entry(frame_right, width=30)
    bairro_entry.pack(pady=10, side="top")

    endereco_create_tittle_label = tk.Button(
        window, text="Update funcionario", width=25, command=on_click_updating_funcionario)
    endereco_create_tittle_label.pack(pady=5, side="bottom",anchor='s')

    voltar = tk.Button(window, text="Return", width=25,
                       command=funcionario_table)
    voltar.pack(side="bottom", pady=5,anchor='s')

def funcionario_table():

    clear_window(window)

    funcionario_main_tittle_label = tk.Label(
        window, text="Choose a function [Table: Funcionario]")
    funcionario_main_tittle_label.config()
    funcionario_main_tittle_label.pack(pady=10)

    ler_funcionario = tk.Button(
        window, text="Read funcionario table", width=25, command=funcionario_id_read)
    ler_funcionario.config(width=20, height=3)
    ler_funcionario.pack(side="top", pady=10)

    criar_funcionario = tk.Button(
        window, text="Create a funcionario", width=25, command=on_click_creating_funcionario)
    criar_funcionario.config(width=20, height=3)
    criar_funcionario.pack(side="top", pady=10)

    atualizar_funcionario = tk.Button(
        window, text="Update a funcionario", width=25, command=on_click_update_funcionario)
    atualizar_funcionario.config(width=20, height=3)
    atualizar_funcionario.pack(side="top", pady=10)

    deletar_funcionario = tk.Button(
        window, text="Delete a funcionario", width=25, command=on_click_delete_funcionario)
    deletar_funcionario.config(width=20, height=3)
    deletar_funcionario.pack(side="top", pady=10)

    voltar = tk.Button(window, text="Return", width=25, command=main_menu)
    voltar.pack(side="bottom", pady=10)

def reading_medico():
    def on_click_read_medico():
        ids = insert_id_for_read.get()
        dados_medico = read_medicos(int(ids))
        
        reading_medico()

        for item in dados_medico:
            rotulo_dados = tk.Label(
                window, text=f"{item.capitalize()} - {dados_medico[item]}")
            rotulo_dados.config(relief=("sunken"), width=40, justify="center")
            rotulo_dados.pack(side="top", pady=3)

    clear_window(window)

    medico_read_tittle_label = tk.Label(
        window, text="Id's from medicos")
    medico_read_tittle_label.pack(pady=10, side="top")

    # lista_de_ids = show_all_id_from_table("funcionario")

    id_medico = tk.StringVar()
    id_medico.set(list(show_all_id_from_table("medicos")))

    id_medico_label = tk.Label(window, textvariable=id_medico,)
    id_medico_label.config(relief="sunken")
    id_medico_label.pack(padx=3, side="top")

    insert_id_for_read = tk.Entry(window)
    insert_id_for_read.pack(pady=10, side="top")

    botao = tk.Button(window, text="Search for medico",
                      command=on_click_read_medico)
    botao.pack(pady=10)

    voltar = tk.Button(window, text="Return", width=25,
                       command=medico_table)
    voltar.pack(side="bottom", pady=10)
#on_click_delete_medicos não atualiza conforme vamos dando deletando
def on_click_delete_medicos():

    def on_click_delete_medicos_function():
        id_to_delete_medicos = insert_id_for_delete.get()
        try:
            delete_medicos(int(id_to_delete_medicos))

            on_click_delete_medicos()

            deletado_com_sucesso = tk.Label(
                window, text="medicos deletado com sucesso")
            deletado_com_sucesso.config(relief="sunken", bg="green")
            deletado_com_sucesso.pack(padx=3, side="top")

        except Exception as error:
            print(error)

            on_click_delete_medicos()

            deletado_com_sucesso = tk.Label(
                window, text="Falha ao deletar o medicos")
            deletado_com_sucesso.config(relief="sunken", bg="red")
            deletado_com_sucesso.pack(padx=3, side="top")

    clear_window(window)

    delete_medicos_label = tk.Label(
        window, text="Id's from the medicos")
    delete_medicos_label.pack(side="top", pady=10)

    id_medicos = tk.StringVar()
    id_medicos.set(list(show_all_id_from_table("medicos")))

    id_medicos_label = tk.Label(window, textvariable=id_medicos,)
    id_medicos_label.config(relief="sunken")
    id_medicos_label.pack(padx=3, side="top")

    insert_id_for_delete = tk.Entry(window)
    insert_id_for_delete.pack(pady=10, side="top")

    botao = tk.Button(window, text="Delete medicos",
                      command=on_click_delete_medicos_function)
    botao.pack(pady=10)

    voltar = tk.Button(window, text="Return", width=25,
                       command=medico_table)
    voltar.pack(side="bottom", pady=10)

def creating_medico():  
    def on_click_create_medico():
        try:
            cpf_value = cpf_entry.get()
            nome_value = nome_entry.get()
            email_value = email.get()
            telefone_value = telefone.get()
            especialidade_value = especialidade.get()
            logradouro_value = logradouro_entry.get()
            cep_value = cep_entry.get()
            numero_casa_value = numero_casa_entry.get()
            bairro_value = bairro_entry.get()

            create_medicos(cpf_value, nome_value, email_value, telefone_value,
                               logradouro_value, especialidade_value, cep_value, numero_casa_value, bairro_value)

            creating_medico()

            medico_created = tk.Label(
                window, text=f"medico {nome_value.capitalize()} criado com sucesso")
            medico_created.config(fg="green")
            medico_created.pack(side="bottom")

        except Exception as error:
            print(error)

            creating_medico()

            medico_not_created = tk.Label(
                window, text="Error ao criar o usuario")
            medico_not_created.config(fg="red")
            medico_not_created.pack(side="bottom")

    clear_window(window)

    medico_create_tittle_label = tk.Label(
        window, text="Insert the information from the new medico")
    medico_create_tittle_label.config(relief="sunken", justify="center")
    medico_create_tittle_label.pack(pady=20, side="top")

    create_medico_tittle = tk.Label(
        window, text="Insert your CPF", width=25)
    create_medico_tittle.config(relief="ridge")
    create_medico_tittle.pack(pady=1, side="top")

    cpf_entry = tk.Entry(window, width=30)
    cpf_entry.pack(pady=10, side="top")

    create_medico_tittle = tk.Label(
        window, text="Insert your name", width=25)
    create_medico_tittle.config(relief="ridge")
    create_medico_tittle.pack(pady=1, side="top")

    nome_entry = tk.Entry(window, width=30)
    nome_entry.pack(pady=10, side="top")

    create_medico_tittle = tk.Label(
        window, text="Insert your email", width=25)
    create_medico_tittle.config(relief="ridge")
    create_medico_tittle.pack(pady=1, side="top")

    email = tk.Entry(window, width=30)
    email.pack(pady=10, side="top")

    create_medico_tittle = tk.Label(
        window, text="Insert your telefone number", width=25)
    create_medico_tittle.config(relief="ridge")
    create_medico_tittle.pack(pady=1, side="top")

    telefone = tk.Entry(window, width=30)
    telefone.pack(pady=10, side="top")

    create_medico_tittle = tk.Label(
        window, text="Insert your especialidade", width=25)
    create_medico_tittle.config(relief="ridge")
    create_medico_tittle.pack(pady=1, side="top")

    especialidade = tk.Entry(window, width=30)
    especialidade.pack(pady=10, side="top")

    medico_create_tittle_label = tk.Label(
        window, text="Insert the endereco from the new medico")
    medico_create_tittle_label.config(relief="sunken", justify="center")
    medico_create_tittle_label.pack(pady=20, side="top")

    create_medico_tittle = tk.Label(
        window, text="Insert your logradouro", width=25)
    create_medico_tittle.config(relief="ridge")
    create_medico_tittle.pack(pady=1, side="top")

    logradouro_entry = tk.Entry(window, width=30)
    logradouro_entry.pack(pady=10, side="top")

    create_medico_tittle = tk.Label(
        window, text="Insert your cep", width=25)
    create_medico_tittle.config(relief="ridge")
    create_medico_tittle.pack(pady=1, side="top")

    cep_entry = tk.Entry(window, width=30)
    cep_entry.pack(pady=10, side="top")

    create_medico_tittle = tk.Label(
        window, text="Insert the number of ur house", width=25)
    create_medico_tittle.config(relief="ridge")
    create_medico_tittle.pack(pady=1, side="top")

    numero_casa_entry = tk.Entry(window, width=30)
    numero_casa_entry.pack(pady=10, side="top")

    create_medico_tittle = tk.Label(
        window, text="Insert your bairro", width=25)
    create_medico_tittle.config(relief="ridge")
    create_medico_tittle.pack(pady=1, side="top")

    bairro_entry = tk.Entry(window, width=30)
    bairro_entry.pack(pady=10, side="top")

    endereco_create_tittle_label = tk.Button(
        window, text="Create medico", width=25, command=on_click_create_medico)
    endereco_create_tittle_label.config(justify="center")
    endereco_create_tittle_label.pack(pady=30, side="top")

    voltar = tk.Button(window, text="Return", width=25,
                       command=medico_table)
    voltar.pack(side="bottom", pady=10)

def updating_medico():
    def on_click_updating_medico():
        try:
            id_value = id_entry.get()
            cpf_value = cpf_entry.get()
            nome_value = nome_entry.get()
            email_value = email.get()
            telefone_value = telefone.get()
            especialidade_value = especialidade.get()
            logradouro_value = logradouro_entry.get()
            cep_value = cep_entry.get()
            numero_casa_value = numero_casa_entry.get()
            bairro_value = bairro_entry.get()

            update_medicos(int(id_value), cpf_value, nome_value, email_value, telefone_value,
                               logradouro_value, especialidade_value, cep_value, numero_casa_value, bairro_value)

            updating_medico()

            medico_created = tk.Label(
                window, text=f"medico {nome_value.capitalize()} atualizado com sucesso")
            medico_created.config(fg="green")
            medico_created.pack(side="top")

        except Exception as error:
            print(error)

            updating_medico()

            medico_not_created = tk.Label(
                window, text="Error ao atualizar o usuario")
            medico_not_created.config(fg="red")
            medico_not_created.pack(side="top")

    clear_window(window)

    update_medico_label = tk.Label(
        window, text="Id's from the medicos")
    update_medico_label.pack(side="top", pady=5)
    
    id_medico = tk.StringVar()
    id_medico.set(list(show_all_id_from_table("medicos")))

    id_medico_label = tk.Label(window, textvariable=id_medico,)
    id_medico_label.config(relief="sunken")
    id_medico_label.pack(padx=3, side="top")

# Update medico text boxes

    medico_create_tittle_label = tk.Label(
        window, text="Update medico")
    medico_create_tittle_label.config(relief="sunken", justify="center")
    medico_create_tittle_label.pack(pady=5, side="top")

    create_medico_tittle = tk.Label(
        window, text="Insert your ID", width=25)
    create_medico_tittle.config(relief="ridge")
    create_medico_tittle.pack(pady=1, side="top")

    id_entry = tk.Entry(window, width=30)
    id_entry.pack(pady=10, side="top")

    create_medico_tittle = tk.Label(
        window, text="Insert your CPF", width=25)
    create_medico_tittle.config(relief="ridge")
    create_medico_tittle.pack(pady=1, side="top")

    cpf_entry = tk.Entry(window, width=30)
    cpf_entry.pack(pady=10, side="top")

    create_medico_tittle = tk.Label(
        window, text="Insert your name", width=25)
    create_medico_tittle.config(relief="ridge")
    create_medico_tittle.pack(pady=1, side="top")

    nome_entry = tk.Entry(window, width=30)
    nome_entry.pack(pady=10, side="top")

    create_medico_tittle = tk.Label(
        window, text="Insert your email", width=25)
    create_medico_tittle.config(relief="ridge")
    create_medico_tittle.pack(pady=1, side="top")

    email = tk.Entry(window, width=30)
    email.pack(pady=10, side="top")

    create_medico_tittle = tk.Label(
        window, text="Insert your telefone number", width=25)
    create_medico_tittle.config(relief="ridge")
    create_medico_tittle.pack(pady=1, side="top")

    telefone = tk.Entry(window, width=30)
    telefone.pack(pady=10, side="top")

    create_medico_tittle = tk.Label(
        window, text="Insert your role", width=25)
    create_medico_tittle.config(relief="ridge")
    create_medico_tittle.pack(pady=1, side="top")

    especialidade = tk.Entry(window, width=30)
    especialidade.pack(pady=10, side="top")

    medico_create_tittle_label = tk.Label(
        window, text="Insert the endereco from the new medico")
    medico_create_tittle_label.config(relief="sunken", justify="center")
    medico_create_tittle_label.pack(pady=20, side="top")

    create_medico_tittle = tk.Label(
        window, text="Insert your logradouro", width=25)
    create_medico_tittle.config(relief="ridge")
    create_medico_tittle.pack(pady=1, side="top")

    logradouro_entry = tk.Entry(window, width=30)
    logradouro_entry.pack(pady=10, side="top")

    create_medico_tittle = tk.Label(
        window, text="Insert your cep", width=25)
    create_medico_tittle.config(relief="ridge")
    create_medico_tittle.pack(pady=1, side="top")

    cep_entry = tk.Entry(window, width=30)
    cep_entry.pack(pady=10, side="top")

    create_medico_tittle = tk.Label(
        window, text="Insert the number of ur house", width=25)
    create_medico_tittle.config(relief="ridge")
    create_medico_tittle.pack(pady=1, side="top")

    numero_casa_entry = tk.Entry(window, width=30)
    numero_casa_entry.pack(pady=10, side="top")

    create_medico_tittle = tk.Label(
        window, text="Insert your bairro", width=25)
    create_medico_tittle.config(relief="ridge")
    create_medico_tittle.pack(pady=1, side="top")

    bairro_entry = tk.Entry(window, width=30)
    bairro_entry.pack(pady=10, side="top")

    endereco_create_tittle_label = tk.Button(
        window, text="Update medico", width=25, command=on_click_updating_medico)
    endereco_create_tittle_label.config(justify="center")
    endereco_create_tittle_label.pack(pady=5, side="top")

    voltar = tk.Button(window, text="Return", width=25,
                       command=medico_table)
    voltar.pack(side="bottom", pady=5)

def medico_table():
    clear_window(window)

    medico_main_tittle_label = tk.Label(
        window, text="Choose a function [Table: Medico]")
    medico_main_tittle_label.config()
    medico_main_tittle_label.pack(pady=10)

    ler_medico_ = tk.Button(
        window, text="Read medico table", width=25, command=reading_medico)
    ler_medico_.config(width=20, height=3)
    ler_medico_.pack(side="top", pady=10)

    criar_medico = tk.Button(
        window, text="Create a medico", width=25, command=creating_medico)
    criar_medico.config(width=20, height=3)
    criar_medico.pack(side="top", pady=10)

    atualizar_medico = tk.Button(
        window, text="Update a medico", width=25, command=updating_medico)
    atualizar_medico.config(width=20, height=3)
    atualizar_medico.pack(side="top", pady=10)

    deletar_medico = tk.Button(
        window, text="Delete a medico", width=25, command=on_click_delete_medicos)
    deletar_medico.config(width=20, height=3)
    deletar_medico.pack(side="top", pady=10)

    voltar = tk.Button(window, text="Return", width=25, command=main_menu)
    voltar.pack(side="bottom", pady=10)

# Setting up the window
window = tk.Tk()
window.config(background="lightblue")
window.title("MySQL database crud for an hospital")
window.geometry("600x500")
#

# Building the main menu
escolher = tk.Label(window, text="What table do you want o work with?")
escolher.pack(pady=10)

clinica = tk.Button(window, text="Clinica")
clinica.config(width=20, height=3)
clinica.pack(side="top", pady=10,)

doencas = tk.Button(window, text="Doencas")
doencas.config(width=20, height=3)
doencas.pack(side="top", pady=10)

funcionario = tk.Button(window, text="Funcionarios", command=funcionario_table)
funcionario.config(width=20, height=3)
funcionario.pack(side="top", pady=10)

hospital = tk.Button(window, text="Hospital")
hospital.config(width=20, height=3)
hospital.pack(side="top", pady=10)

medicos = tk.Button(window, text="Medicos", command=medico_table)
medicos.config(width=20, height=3)
medicos.pack(side="top", pady=10)

paciente = tk.Button(window, text="Paciente")
paciente.config(width=20, height=3)
paciente.pack(side="top", pady=10)

prontuarios = tk.Button(window, text="Prontuarios")
prontuarios.config(width=20, height=3)
prontuarios.pack(side="top", pady=10)

window.mainloop()
