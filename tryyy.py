import tkinter as tk
from ttkthemes import ThemedStyle

root = tk.Tk()
style = ThemedStyle(root)

print(style.theme_names())
style = ThemedStyle(root)
themes = ['black', 'blue', 'equilux', 'default', 'clearlooks']
chosen_theme = StringVar(value=themes[0])

def update_theme():
    theme = chosen_theme.get()
    style = ThemedStyle(root)
    style.set_theme(theme)
