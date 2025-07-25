import customtkinter

app = customtkinter.CTk()
app.geometry("400x200")

# Create an entry widget with a default placeholder
entry1 = customtkinter.CTkEntry(master=app, placeholder_text="Default Placeholder")
entry1.pack(pady=10)

# Create an entry widget and change its placeholder color
entry2 = customtkinter.CTkEntry(master=app, placeholder_text="Blue Placeholder")
entry2.configure(placeholder_text_color="blue")
entry2.pack(pady=10)

# Create an entry widget and change its placeholder color using a hex code
entry3 = customtkinter.CTkEntry(master=app, placeholder_text="Custom Color Placeholder")
entry3.configure(placeholder_text_color="#FF5733") # An orange-ish color
entry3.pack(pady=10)

app.mainloop()
