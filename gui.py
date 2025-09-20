import tkinter as tk
from tkinter import ttk 

def run_ai_gui():
    root = tk.Tk()
    root.title("Tkinter AI GUI")
    root.geometry("800x500")

    # --- Title label ---
    title_label = tk.Label(root, text="Tkinter AI GUI", font=("Arial", 18, "bold"))
    title_label.pack(pady=5)

    # --- Top row with File, Models, Help ---
    top_frame = tk.Frame(root, relief="groove", bd=1)
    top_frame.pack(fill="x", padx=10, pady=2)

    file_btn = tk.Button(top_frame, text="File")
    file_btn.pack(side="left", padx=5, pady=2)

    models_btn = tk.Button(top_frame, text="Models")
    models_btn.pack(side="left", padx=5, pady=2)

    help_btn = tk.Button(top_frame, text="Help")
    help_btn.pack(side="left", padx=5, pady=2)
    
    model_frame = tk.Frame(root, relief="groove", bd=1)
    model_frame.pack(fill="x", padx=10, pady=5)
    
    model_label = tk.Label(model_frame, text="Model Selection:")
    model_label.pack(side="left", padx=5)

    # Dropdown for selecting models
    model_var = tk.StringVar()
    model_dropdown = ttk.Combobox(model_frame, textvariable=model_var, state="readonly")
    model_dropdown['values'] = ("Image Classification", "Text Sentiment")
    model_dropdown.current(0)  # default selection
    model_dropdown.pack(side="left", padx=5)

    # Load Model button
    load_btn = tk.Button(model_frame, text="Load Model")
    load_btn.pack(side="left", padx=5)
    
    

    root.mainloop()
