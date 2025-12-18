import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Tkinter Test Window")

# Add a label
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

# Run the GUI event loop
root.mainloop()
