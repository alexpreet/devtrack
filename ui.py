import customtkinter as ctk
from tkinter import messagebox
import matplotlib.pyplot as plt

from storage import add_entry, reset_data
from analytics import (
    total_hours,
    unique_skills,
    skill_distribution,
    daily_trend,
    productivity_score
)
from testdata import generate_test_data


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class DevTrackApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("DevTrack ")
        self.geometry("700x600")

        self.build_layout()
        self.update_stats()

    def build_layout(self):

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)

        # Left Panel
        self.left_frame = ctk.CTkFrame(self)
        self.left_frame.grid(row=0, column=0, sticky="nswe", padx=20, pady=20)

        self.title_label = ctk.CTkLabel(
            self.left_frame, text="DevTrack Pro", font=("Arial", 24, "bold")
        )
        self.title_label.pack(pady=20)

        self.hours_entry = ctk.CTkEntry(
            self.left_frame, placeholder_text="Hours"
        )
        self.hours_entry.pack(pady=10)

        self.skill_entry = ctk.CTkEntry(
            self.left_frame, placeholder_text="Skill"
        )
        self.skill_entry.pack(pady=10)

        self.project_entry = ctk.CTkEntry(
            self.left_frame, placeholder_text="Project"
        )
        self.project_entry.pack(pady=10)

        self.add_button = ctk.CTkButton(
            self.left_frame, text="Add Entry", command=self.add_data
        )
        self.add_button.pack(pady=10)

        self.test_button = ctk.CTkButton(
            self.left_frame, text="Generate Test Data",
            command=self.generate_data
        )
        self.test_button.pack(pady=10)

        self.reset_button = ctk.CTkButton(
            self.left_frame, text="Reset Data",
            command=self.reset_all
        )
        self.reset_button.pack(pady=10)

        # Right Panel
        self.right_frame = ctk.CTkFrame(self)
        self.right_frame.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        self.stats_label = ctk.CTkLabel(
            self.right_frame, text="", font=("Arial", 18)
        )
        self.stats_label.pack(pady=20)

        self.pie_button = ctk.CTkButton(
            self.right_frame, text="Skill Distribution",
            command=self.show_pie
        )
        self.pie_button.pack(pady=10)

        self.line_button = ctk.CTkButton(
            self.right_frame, text="Daily Trend",
            command=self.show_line
        )
        self.line_button.pack(pady=10)

    def add_data(self):
        try:
            hours = float(self.hours_entry.get())
            skill = self.skill_entry.get()
            project = self.project_entry.get()

            add_entry(hours, skill, project)
            self.update_stats()
            messagebox.showinfo("Success", "Entry Added")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_stats(self):
        text = (
            f"Total Hours: {total_hours()}\n"
            f"Unique Skills: {unique_skills()}\n"
            f"Productivity Score: {productivity_score()}"
        )
        self.stats_label.configure(text=text)

    def show_pie(self):
        skills, hours = skill_distribution()

        if not skills:
            messagebox.showinfo("No Data", "No data available.")
            return

        plt.figure()
        plt.pie(hours, labels=skills, autopct="%1.1f%%")
        plt.title("Skill Distribution")
        plt.show()

    def show_line(self):
        dates, hours = daily_trend()

        if not dates:
            messagebox.showinfo("No Data", "No data available.")
            return

        plt.figure()
        plt.plot(dates, hours, marker="o")
        plt.xticks(rotation=45)
        plt.title("Daily Coding Hours")
        plt.tight_layout()
        plt.show()

    def generate_data(self):
        generate_test_data()
        self.update_stats()
        messagebox.showinfo("Done", "Test Data Generated")

    def reset_all(self):
        reset_data()
        self.update_stats()
        messagebox.showinfo("Reset", "Data Cleared")

