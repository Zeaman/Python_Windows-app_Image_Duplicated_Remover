"""
Author: Amanuel Mihiret (MSc. in Mechatronics Engineering)
"""
# Import required dependencies
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, UnidentifiedImageError


# Remove duplicated images inside each class
def dhash(image, hash_size=8):
    return hash(str(image.tobytes()))


def find_duplicates(folder):
    duplicates = []
    hash_keys = []

    try:
        for filename in os.listdir(folder):
            image_path = os.path.join(folder, filename)

            try:
                with Image.open(image_path) as img:
                    h = dhash(img)

                if h in hash_keys:
                    duplicates.append(image_path)
                else:
                    hash_keys.append(h)

            except UnidentifiedImageError:
                print(f"Skipping non-image file: {image_path}")

    except FileNotFoundError:
        print(f"Folder not found: {folder}")

    return duplicates


def delete_duplicates(duplicates):
    if not duplicates:
        print("No duplicate files found.")
    else:
        for duplicate_path in duplicates:
            # Delete duplicate files
            os.remove(duplicate_path)
            print(f"Deleted duplicate: {duplicate_path}")

    # Display a notice when all files are resized
    messagebox.showinfo("Success!",
                        "All files have been successfully checked for duplicated files.")


def process_folder(folder_path):
    duplicates = find_duplicates(folder_path)
    delete_duplicates(duplicates)


def browse_directory(entry_widget):
    directory = filedialog.askdirectory()

    if directory:
        entry_widget.delete(0, tk.END)  # Clear the entry widget
        entry_widget.insert(0, directory)  # Insert the selected directory into the entry widget
        process_folder(directory)  # Automatically process the selected folder


def submit_action(entry_widget):
    folder_path = entry_widget.get()
    process_folder(folder_path)


def cancel_action(root):
    root.destroy()  # Close the Tkinter window


def get_user_input():
    root = tk.Tk()
    root.title("Duplicate Image Remover")

    # Set the size of the window
    root.geometry("400x200")  # Width x Height

    # Entry for source folder
    source_folder_label = tk.Label(root, text="Source Folder:")
    source_folder_label.pack()
    source_folder_entry = tk.Entry(root)
    source_folder_entry.pack(pady=5)

    # Button to browse source directory
    browse_source_button = tk.Button(root, text="Browse Source", command=lambda: browse_directory(source_folder_entry))
    browse_source_button.pack(pady=10)  # vertical spacing

    # Submit and Cancel Buttons
    submit_button = tk.Button(root, text="Submit", command=lambda: submit_action(source_folder_entry))
    submit_button.pack(side=tk.LEFT, padx=10)  # horizontal spacing

    cancel_button = tk.Button(root, text="Cancel", command=lambda: cancel_action(root))
    cancel_button.pack(side=tk.RIGHT, padx=10)  # horizontal spacing

    root.mainloop()


# Get user input using Tkinter GUI
get_user_input()
