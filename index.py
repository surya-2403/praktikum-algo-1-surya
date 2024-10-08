import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")  # Format waktu 24 jam
    label.config(text=current_time)  # Update label dengan waktu baru
    label.after(1000, update_time)  # Panggil fungsi ini lagi setelah 1000 ms (1 detik)

# Membuat jendela utama
root = tk.Tk()
root.title("Jam Digital")

# Membuat label untuk menampilkan waktu
label = tk.Label(root, font=("Arial", 50), fg="black")
label.pack()

update_time()  # Panggil fungsi untuk mengupdate waktu
root.mainloop()  # Jalankan loop utama aplikasi

