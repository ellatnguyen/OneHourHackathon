import tkinter as tk
from tkinter import messagebox
import time
import pygame
import random
from PIL import Image, ImageTk

# Initialize pygame mixer for sound effects
pygame.mixer.init()
explosion_sound = pygame.mixer.Sound('explosion.mp3')  # Ensure you have an explosion sound file

# Track the last click time
last_click_time = 0
click_delay_threshold = 0.2  # 1 second threshold for detecting fast clicks
counter=0

# List of local cat image file paths
cat_image_files = [
    'cats/cat1.jpg',
    'cats/cat2.jpg',
    'cats/cat3.jpg',
    'cats/cat4.jpg',
    'cats/cat5.jpg',
    'cats/cat6.jpg',
    'cats/cat7.jpg',
    'cats/cat8.jpg',
    'cats/cat9.jpg',
    'cats/cat10.jpg'
]

def get_random_cat_image():
    try:
        image_path = random.choice(cat_image_files)
        image = Image.open(image_path)
        return ImageTk.PhotoImage(image)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load cat image: {e}")
        return None

def show_explosion():
    if explosion_photo:
        explosion_label.config(image=explosion_photo)
        explosion_label.image = explosion_photo  # Keep a reference to avoid garbage collection
        root.after(500, hide_explosion)  # Hide explosion after 500 ms

def hide_explosion():
    explosion_label.config(image='')

def on_click():
    global last_click_time
    current_time = time.time()
    
    if current_time - last_click_time < click_delay_threshold:
        # User clicked too fast, play explosion sound and show explosion image
        explosion_sound.play()
        show_explosion()
    # Load and display a new cat image
    cat_image = get_random_cat_image()
    if cat_image:
        label.config(image=cat_image)
        label.image = cat_image  # Keep a reference to avoid garbage collection
    
    last_click_time = current_time

# Set up the Tkinter window
root = tk.Tk()
root.title("Cat Clicker App")
root.geometry("600x400")  # Optional: Set a fixed window size
root.configure(bg='white')  # Set the background color

# Load explosion PNG image after creating the Tkinter window
try:
    explosion_image = Image.open('cats/explosion.gif')  # Replace with your explosion PNG path
    explosion_photo = ImageTk.PhotoImage(explosion_image)
except Exception as e:
    messagebox.showerror("Error", f"Failed to load explosion image: {e}")
    explosion_photo = None

# Create a label to display the cat images, centered in the window
label = tk.Label(root, bg='white')  # Match the background to the root's background color
label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Create a lab-el for displaying the explosion image, with the same background color as the root
explosion_label = tk.Label(root, bg='white', borderwidth=0)  # Match root's background color
explosion_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Center overlay

# Create a button that triggers the on_click function
button = tk.Button(root, text="Click for Cat!", command=on_click)
button.pack(side=tk.BOTTOM, pady=20)  # Position button at the bottom with padding

# Start the Tkinter event loop
root.mainloop()