import socket
import tkinter as tk
from tkinter import ttk
from control_methods import generate_control

SERVER_HOST = "localhost"
SERVER_PORT = 5000

# ---------------- SEND FUNCTION ----------------
def send_packet():
    data = entry.get()
    method = method_var.get()

    if not data or not method:
        status.config(text="⚠ Please fill all fields", fg="#e74c3c")
        return

    control = generate_control(data, method)
    packet = f"{data}|{method}|{control}"

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((SERVER_HOST, SERVER_PORT))
        s.send(packet.encode())
        s.close()

        status.config(text="✅ Packet Sent Successfully", fg="#27ae60")
        log_box.insert(tk.END, packet + "\n")

    except:
        status.config(text="❌ Server not running", fg="#c0392b")

# ---------------- GUI ----------------
root = tk.Tk()
root.title("📡 Client 1 - Data Sender")
root.geometry("420x430")
root.configure(bg="#1e272e")

card = tk.Frame(root, bg="#f5f6fa")
card.place(relx=0.5, rely=0.5, anchor="center", width=360, height=380)

tk.Label(
    card,
    text="📡 Data Communication",
    bg="#f5f6fa",
    fg="#2f3640",
    font=("Segoe UI", 14, "bold")
).pack(pady=10)

tk.Label(card, text="Enter Data", bg="#f5f6fa").pack()
entry = tk.Entry(card, font=("Segoe UI", 11))
entry.pack(pady=5)

tk.Label(card, text="Error Detection Method", bg="#f5f6fa").pack()
method_var = tk.StringVar()
methods = ["PARITY", "CRC16", "2D_PARITY", "HAMMING"]
ttk.Combobox(
    card,
    textvariable=method_var,
    values=methods,
    state="readonly"
).pack(pady=5)

tk.Button(
    card,
    text="🚀 SEND PACKET",
    font=("Segoe UI", 11, "bold"),
    bg="#4cd137",
    fg="white",
    relief="flat",
    command=send_packet
).pack(pady=15)

status = tk.Label(card, text="", bg="#f5f6fa", font=("Segoe UI", 9))
status.pack()

tk.Label(card, text="Logs", bg="#f5f6fa", font=("Segoe UI", 10, "bold")).pack(pady=5)

log_box = tk.Text(card, height=6, width=38, font=("Consolas", 9))
log_box.pack()

root.mainloop()

