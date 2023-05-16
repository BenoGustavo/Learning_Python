import tkinter as tk

from crud_funcionario import create_funcionario, read_funcionario, update_funcionario, delete_funcionario, show_all_id_from_table


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

    medicos = tk.Button(window, text="Medicos")
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

    funcionario_create_tittle_label = tk.Label(
        window, text="Insert the information from the new funcionario")
    funcionario_create_tittle_label.config(relief="sunken", justify="center")
    funcionario_create_tittle_label.pack(pady=20, side="top")

    create_funcionario_tittle = tk.Label(
        window, text="Insert your CPF", width=25)
    create_funcionario_tittle.config(relief="ridge")
    create_funcionario_tittle.pack(pady=1, side="top")

    cpf_entry = tk.Entry(window, width=30)
    cpf_entry.pack(pady=10, side="top")

    create_funcionario_tittle = tk.Label(
        window, text="Insert your name", width=25)
    create_funcionario_tittle.config(relief="ridge")
    create_funcionario_tittle.pack(pady=1, side="top")

    nome_entry = tk.Entry(window, width=30)
    nome_entry.pack(pady=10, side="top")

    create_funcionario_tittle = tk.Label(
        window, text="Insert your email", width=25)
    create_funcionario_tittle.config(relief="ridge")
    create_funcionario_tittle.pack(pady=1, side="top")

    email = tk.Entry(window, width=30)
    email.pack(pady=10, side="top")

    create_funcionario_tittle = tk.Label(
        window, text="Insert your telefone number", width=25)
    create_funcionario_tittle.config(relief="ridge")
    create_funcionario_tittle.pack(pady=1, side="top")

    telefone = tk.Entry(window, width=30)
    telefone.pack(pady=10, side="top")

    create_funcionario_tittle = tk.Label(
        window, text="Insert your role", width=25)
    create_funcionario_tittle.config(relief="ridge")
    create_funcionario_tittle.pack(pady=1, side="top")

    funcao = tk.Entry(window, width=30)
    funcao.pack(pady=10, side="top")

    funcionario_create_tittle_label = tk.Label(
        window, text="Insert the endereco from the new funcionario")
    funcionario_create_tittle_label.config(relief="sunken", justify="center")
    funcionario_create_tittle_label.pack(pady=20, side="top")

    create_funcionario_tittle = tk.Label(
        window, text="Insert your logradouro", width=25)
    create_funcionario_tittle.config(relief="ridge")
    create_funcionario_tittle.pack(pady=1, side="top")

    logradouro_entry = tk.Entry(window, width=30)
    logradouro_entry.pack(pady=10, side="top")

    create_funcionario_tittle = tk.Label(
        window, text="Insert your cep", width=25)
    create_funcionario_tittle.config(relief="ridge")
    create_funcionario_tittle.pack(pady=1, side="top")

    cep_entry = tk.Entry(window, width=30)
    cep_entry.pack(pady=10, side="top")

    create_funcionario_tittle = tk.Label(
        window, text="Insert the number of ur house", width=25)
    create_funcionario_tittle.config(relief="ridge")
    create_funcionario_tittle.pack(pady=1, side="top")

    numero_casa_entry = tk.Entry(window, width=30)
    numero_casa_entry.pack(pady=10, side="top")

    create_funcionario_tittle = tk.Label(
        window, text="Insert your bairro", width=25)
    create_funcionario_tittle.config(relief="ridge")
    create_funcionario_tittle.pack(pady=1, side="top")

    bairro_entry = tk.Entry(window, width=30)
    bairro_entry.pack(pady=10, side="top")

    endereco_create_tittle_label = tk.Button(
        window, text="Create funcionario", width=25, command=on_click_create_funcionario)
    endereco_create_tittle_label.config(justify="center")
    endereco_create_tittle_label.pack(pady=30, side="top")

    voltar = tk.Button(window, text="Return", width=25,
                       command=funcionario_table)
    voltar.pack(side="bottom", pady=10)


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

    update_funcionario_label = tk.Label(
        window, text="Id's from the funcionarios")
    update_funcionario_label.pack(side="top", pady=10)

    id_funcionario = tk.StringVar()
    id_funcionario.set(list(show_all_id_from_table("funcionario")))

    id_funcionario_label = tk.Label(window, textvariable=id_funcionario,)
    id_funcionario_label.config(relief="sunken")
    id_funcionario_label.pack(padx=3, side="top")

# Update funcionario text boxes

    funcionario_create_tittle_label = tk.Label(
        window, text="Update funcionario")
    funcionario_create_tittle_label.config(relief="sunken", justify="center")
    funcionario_create_tittle_label.pack(pady=20, side="top")

    create_funcionario_tittle = tk.Label(
        window, text="Insert your ID", width=25)
    create_funcionario_tittle.config(relief="ridge")
    create_funcionario_tittle.pack(pady=1, side="top")

    id_entry = tk.Entry(window, width=30)
    id_entry.pack(pady=10, side="top")

    create_funcionario_tittle = tk.Label(
        window, text="Insert your CPF", width=25)
    create_funcionario_tittle.config(relief="ridge")
    create_funcionario_tittle.pack(pady=1, side="top")

    cpf_entry = tk.Entry(window, width=30)
    cpf_entry.pack(pady=10, side="top")

    create_funcionario_tittle = tk.Label(
        window, text="Insert your name", width=25)
    create_funcionario_tittle.config(relief="ridge")
    create_funcionario_tittle.pack(pady=1, side="top")

    nome_entry = tk.Entry(window, width=30)
    nome_entry.pack(pady=10, side="top")

    create_funcionario_tittle = tk.Label(
        window, text="Insert your email", width=25)
    create_funcionario_tittle.config(relief="ridge")
    create_funcionario_tittle.pack(pady=1, side="top")

    email = tk.Entry(window, width=30)
    email.pack(pady=10, side="top")

    create_funcionario_tittle = tk.Label(
        window, text="Insert your telefone number", width=25)
    create_funcionario_tittle.config(relief="ridge")
    create_funcionario_tittle.pack(pady=1, side="top")

    telefone = tk.Entry(window, width=30)
    telefone.pack(pady=10, side="top")

    create_funcionario_tittle = tk.Label(
        window, text="Insert your role", width=25)
    create_funcionario_tittle.config(relief="ridge")
    create_funcionario_tittle.pack(pady=1, side="top")

    funcao = tk.Entry(window, width=30)
    funcao.pack(pady=10, side="top")

    funcionario_create_tittle_label = tk.Label(
        window, text="Insert the endereco from the new funcionario")
    funcionario_create_tittle_label.config(relief="sunken", justify="center")
    funcionario_create_tittle_label.pack(pady=20, side="top")

    create_funcionario_tittle = tk.Label(
        window, text="Insert your logradouro", width=25)
    create_funcionario_tittle.config(relief="ridge")
    create_funcionario_tittle.pack(pady=1, side="top")

    logradouro_entry = tk.Entry(window, width=30)
    logradouro_entry.pack(pady=10, side="top")

    create_funcionario_tittle = tk.Label(
        window, text="Insert your cep", width=25)
    create_funcionario_tittle.config(relief="ridge")
    create_funcionario_tittle.pack(pady=1, side="top")

    cep_entry = tk.Entry(window, width=30)
    cep_entry.pack(pady=10, side="top")

    create_funcionario_tittle = tk.Label(
        window, text="Insert the number of ur house", width=25)
    create_funcionario_tittle.config(relief="ridge")
    create_funcionario_tittle.pack(pady=1, side="top")

    numero_casa_entry = tk.Entry(window, width=30)
    numero_casa_entry.pack(pady=10, side="top")

    create_funcionario_tittle = tk.Label(
        window, text="Insert your bairro", width=25)
    create_funcionario_tittle.config(relief="ridge")
    create_funcionario_tittle.pack(pady=1, side="top")

    bairro_entry = tk.Entry(window, width=30)
    bairro_entry.pack(pady=10, side="top")

    endereco_create_tittle_label = tk.Button(
        window, text="Update funcionario", width=25, command=on_click_updating_funcionario)
    endereco_create_tittle_label.config(justify="center")
    endereco_create_tittle_label.pack(pady=5, side="top")

    voltar = tk.Button(window, text="Return", width=25,
                       command=funcionario_table)
    voltar.pack(side="bottom", pady=5)


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
    # create_funcionario()


# Setting up the window
window = tk.Tk()
window.config(background="lightblue")
window.title("MySQL database crud for an hospital")
window.geometry("500x850")
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

medicos = tk.Button(window, text="Medicos")
medicos.config(width=20, height=3)
medicos.pack(side="top", pady=10)

paciente = tk.Button(window, text="Paciente")
paciente.config(width=20, height=3)
paciente.pack(side="top", pady=10)

prontuarios = tk.Button(window, text="Prontuarios")
prontuarios.config(width=20, height=3)
prontuarios.pack(side="top", pady=10)

window.mainloop()
