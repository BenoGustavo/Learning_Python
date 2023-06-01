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
    button_frame.config(relief="flat",border=2,bg="white")
    button_frame.pack(expand=True, fill='both', padx=50, pady=30,anchor='center')

    main_tittle = tk.Label(window, text="Movie sorter")
    main_tittle.config(font=("roboto",12,"bold"),bg="#222222",fg="white",relief="raised",border=0.5,padx=10,pady=10)

    button_add_movie = tk.Button(button_frame,text="Add movie")
    button_add_movie.config(font=("roboto",12,"bold"),bg="#222222",fg="white",width=25,height=3,anchor="center")

    button_del_movie = tk.Button(button_frame,text="Delete movie")
    button_del_movie.config(font=("roboto",12,"bold"),bg="#222222",fg="white",width=25,height=3,anchor="center")

    button_sort_movie = tk.Button(button_frame,text="Sort movie")
    button_sort_movie.config(font=("roboto",12,"bold"),bg="#222222",fg="white",width=25,height=3,anchor="center")

    #Packing itens
    main_tittle.pack(pady=20,side="top",anchor='n')
    button_add_movie.pack(pady=15,anchor="center")
    button_del_movie.pack(pady=10,anchor="center")
    button_sort_movie.pack(pady=15,anchor="center")

    window.mainloop()

def add_movie_window():
    pass

def del_movie_window():
    pass

def sort_movie_window():
    pass

# Setting up the window
window = tk.Tk()
window.config(background="#334464")
window.title("Movie sorter")
window.geometry("400x450")
#

main_window()