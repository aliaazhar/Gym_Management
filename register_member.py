import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk
import os
import sys
from pathlib import Path

class App(ctk.CTk):
    def __init__(self):
        super().__init__()        # Set appearance mode and default color theme
        ctk.set_appearance_mode("dark")  # Options: "light", "dark", "system"
        ctk.set_default_color_theme("blue")  # Options: "blue", "green", "dark-blue"

        self.title("Registration Form")
        self.geometry("640x480")

        # Set background color
        self.configure(fg_color="#ffffff")

        # # Configure grid layout (4x4) for better responsiveness
        # self.grid_columnconfigure((0, 1, 2, 3), weight=1)
        # self.grid_rowconfigure((0, 1, 2, 3), weight=1)


        # Create all widgets and components
        self.create_widgets()

    def create_widgets(self):
        """Create and place all widgets"""
        self.entry1 = ctk.CTkEntry(self, width=200, height=40, corner_radius=8, fg_color="#15c5ea", text_color="#ffffff", border_width=2, border_color="#15c5ea", placeholder_text="Enter Name", font=("Trebuchet", 12, "normal"))
        self.entry1.place(x=238, y=97)
        self.entry1.configure(placeholder_text_color="#ffffff")
        self.entry2 = ctk.CTkEntry(self, width=200, height=40, corner_radius=8, fg_color="#15c5ea", text_color="#ffffff", border_width=2, border_color="#15c5ea", placeholder_text="Enter Phone", font=("Trebuchet", 12, "normal"))
        self.entry2.place(x=240, y=150)
        self.entry2.configure(placeholder_text_color="#ffffff")
        self.button1 = ctk.CTkButton(self, text="save", width=120, height=40, corner_radius=8, fg_color="#ffffff", hover_color="#15c5ea", text_color="#000000", border_width=1, border_color="#44D0EE", font=("Trebuchet", 12, "bold"))
        self.button1.place(x=280, y=250)
        self.label1 = ctk.CTkLabel(self, text="Registration Form", width=276, height=30, corner_radius=8, fg_color="white", text_color="#000000", font=("Georgia", 30, "bold"))
        self.label1.place(x=204, y=28)
        try:
            from tkcalendar import DateEntry
            # Create a frame to host the date picker
            self.datepicker1 = ctk.CTkFrame(self, width=200, height=40, corner_radius=8, fg_color="#ffffff", border_width=1, border_color="#e2e8f0")
            self.datepicker1.place(x=239, y=201)
            self.datepicker1 = DateEntry(self.datepicker1, width=40, background="#ffffff", foreground="#000000", borderwidth=1, date_pattern="dd-mm-yyyy")
            self.datepicker1.place(relx=0.5, rely=0.5, anchor="center")
        except ImportError:
            print("tkcalendar not installed. Install with: pip install tkcalendar")
            # Fallback to a button that could open a date selection dialog
            self.datepicker_calendar = ctk.CTkButton(self, text="Select Date", width=200, height=30, corner_radius=8, fg_color="#ffffff", hover_color="#", text_color="#15c5ea", font=("Arial", 12, "normal"))
            self.datepicker_calendar.place(x=239, y=201)


if __name__ == "__main__":
    try:
        app = App()
        app.mainloop()
    except Exception as e:
        print(f"Error running application: {e}")
        import traceback
        traceback.print_exc()
