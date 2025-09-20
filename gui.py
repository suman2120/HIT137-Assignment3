import tkinter as tk

def run_ai_gui():
    root = tk.Tk()
    root.title("")  # set window title
    root.geometry("800x500")  # set window size
    

    # Add a title label inside the window
    title_label = tk.Label(root, text="Tkinter AI GUI", font=("Arial", 18, "bold"))
    title_label.pack(pady=10)  # pack with some vertical spacing
    title_label.config(anchor="center")  # make sure it's centere
    

    root.mainloop()
