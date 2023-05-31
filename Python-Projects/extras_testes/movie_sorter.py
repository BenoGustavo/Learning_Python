from random import shuffle
import tkinter as tk

movies = []
del_movies = []

#Movies functions
def add_movie(movie,list_movies = None):
    if list_movies is None:
        list_movies = []
    
    list_movies.append(movie)

    return list_movies

def sort_movie(list_movies = None):
    if list_movies is None:
        list_movies = []

def show_movies(list_movies = None):
    if list_movies is None:
        list_movies = []

#Functions from Front-end
def destroy_window(window):
    for widget in window.winfo_children():
        widget.destroy()

def main_window():
    destroy_window(window)

    #Setting up main window
    button_frame = tk.Frame(window, width=50, height=100)
    button_frame.config(relief="raised",border=2,bg="#313232")
    button_frame.pack(expand=True, fill='both', padx=50, pady=50,anchor='center')

    main_tittle = tk.Label(window, text="Movie sorter")
    main_tittle.config(font=("roboto",12,"bold"),bg="grey",fg="white",relief="raised",border=0.5,padx=10,pady=10)

    button_mp3 = tk.Button(button_frame,text="Add movie")
    button_mp3.config(font=("roboto",12,"bold"),width=25,height=3,anchor="center")

    button_mp4 = tk.Button(button_frame,text="Delete movie")
    button_mp4.config(font=("roboto",12,"bold"),width=25,height=3,anchor="center")

    button_mp4 = tk.Button(button_frame,text="Sort movie")
    button_mp4.config(font=("roboto",12,"bold"),width=25,height=3,anchor="center")

    #Packing itens
    main_tittle.pack(pady=20,side="top",anchor='n')
    button_mp3.pack(pady=30)
    button_mp4.pack(pady=25)

    window.mainloop()

# Setting up the window
window = tk.Tk()
window.config(background="#101111")
window.title("Movie sorter")
window.geometry("400x450")
#
    