import cv2
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import customtkinter as ctk


# ---------------- APPLICATION CONFIGURATION ----------------
def resize_images(input_folder, output_folder, width, height):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.tif', '.tiff')):
            image = cv2.imread(input_path)
            if image is None:
                continue
            resized_image = cv2.resize(image, (width, height))
            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, resized_image)
            print(f"Rescaled: {filename} -> {output_path}")

    messagebox.showinfo("Ready", "Scaling images completed!")


# ---------------- BACKGROUND APPEARANCE ----------------
def select_input_folder():
    folder = filedialog.askdirectory(title="Select input folder")
    input_entry.delete(0, tk.END)
    input_entry.insert(0, folder)


def select_output_folder():
    folder = filedialog.askdirectory(title="Select output folder")
    output_entry.delete(0, tk.END)
    output_entry.insert(0, folder)


def start_processing():
    input_folder = input_entry.get()
    output_folder = output_entry.get()
    width = width_entry.get()
    height = height_entry.get()

    if not input_folder or not output_folder:
        messagebox.showerror("Error", "Select input and output folders")
        return


    if not width or not height:
        messagebox.showerror("Error", "Specify the scaling width and height")
        return

    try:
        width = int(width)
        height = int(height)
        resize_images(input_folder, output_folder, width, height)
    except ValueError:
        messagebox.showerror("Error", "Scaling dimensions must be whole numbers")
    except Exception as e:
        messagebox.showerror("Error", f"There was a problem: {e}")


# ---------------- APPLICATION CONFIGURATION ----------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("PiranhaPix")
app.geometry("800x600")

# Application Icon Setting
app.iconbitmap(r"C:\Users\topgu\Desktop\Splotowe Sieci Neuronowe\piranha.ico")

# ---------------- BACKGROUND APPEARANCE ----------------
background_image = Image.open(r"C:\Users\topgu\Desktop\Splotowe Sieci Neuronowe\piranhapix.png")
background_photo = ImageTk.PhotoImage(background_image)

background_label = tk.Label(app, image=background_photo)
background_label.place(relwidth=1, relheight=1)


font = ("Orbitron", 14)


offset_y = 330

# ---------------- TEXT FIELDS + BUTTONS ----------------
# Entries (Input/Output Folder
input_entry = ctk.CTkEntry(
    master=app,
    width=300,
    placeholder_text="Input folder",
    fg_color="black",
    text_color="white",
    bg_color="transparent",
    font=font
)
input_entry.place(x=250, y=offset_y + 0)

# Input folder selection button
input_button = ctk.CTkButton(
    master=app,
    text="Select",
    command=select_input_folder,
    fg_color="#8A2BE2",
    text_color="white",
    hover_color="#7A1BBE",
    corner_radius=0,
    border_width=2,
    border_color="#7A1BBE",
    bg_color="transparent",
    font=("Orbitron", 14, "bold")
)
input_button.place(x=560, y=offset_y + 0)

# Output folder selection box
output_entry = ctk.CTkEntry(
    master=app,
    width=300,
    placeholder_text="Output folder",
    fg_color="black",
    text_color="white",
    bg_color="transparent",
    font=font
)
output_entry.place(x=250, y=offset_y + 50)

# Output folder selection button
output_button = ctk.CTkButton(
    master=app,
    text="Select",
    command=select_output_folder,
    fg_color="#8A2BE2",
    text_color="white",
    hover_color="#7A1BBE",
    corner_radius=0,
    border_width=2,
    border_color="#7A1BBE",
    bg_color="transparent",
    font=("Orbitron", 14, "bold")
)
output_button.place(x=560, y=offset_y + 50)

# Width and height fields
width_entry = ctk.CTkEntry(
    master=app,
    width=100,
    placeholder_text="Width",
    fg_color="black",
    text_color="white",
    bg_color="transparent",
    font=font
)
width_entry.place(x=250, y=offset_y + 100)

height_entry = ctk.CTkEntry(
    master=app,
    width=100,
    placeholder_text="Height",
    fg_color="black",
    text_color="white",
    bg_color="transparent",
    font=font
)
height_entry.place(x=360, y=offset_y + 100)

# Button to start scaling
start_button = ctk.CTkButton(
    master=app,
    text="Start scaling",
    command=start_processing,
    fg_color="cyan",
    text_color="black",
    hover_color="#00AAAA",
    corner_radius=0,
    border_width=2,
    border_color="#00AAAA",
    bg_color="transparent",
    font=("Orbitron", 14, "bold")
)
start_button.place(x=250, y=offset_y + 150)

# ---------------- LAUNCHING THE APPLICATION ----------------
app.mainloop()
