import socket
import tkinter as tk
from control_methods import generate_control

HOST = "localhost"
PORT = 6000

# ---------------- CHECK FUNCTION ----------------
def check_packet(packet):
    parts = packet.split("|")
    data = parts[0]
    received_control = parts[2]
    method = parts[1]
    error_type = parts[3]

    computed_control = generate_control(data, method)

    data_label.config(text=data)
    method_label.config(text=method)
    sent_label.config(text=received_control)
    computed_label.config(text=computed_control)
    error_label.config(text=error_type)


    if received_control == computed_control:
        status_label.config(text="DATA CORRECT", fg="#27ae60")
    else:
        status_label.config(text="DATA CORRUPTED", fg="#c0392b")


# ---------------- SERVER LISTENER ----------------
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(1)

    status_label.config(text="Waiting for data...", fg="#2980b9")

    while True:
        conn, addr = server.accept()
        packet = conn.recv(1024).decode()
        print("Received:", packet)
        check_packet(packet)
        conn.close()


# ---------------- GUI ----------------
root = tk.Tk()
root.title("📥 Client 2 - Receiver")
root.geometry("450x420")
root.configure(bg="#1e272e")

card = tk.Frame(root, bg="#f5f6fa")
card.place(relx=0.5, rely=0.5, anchor="center", width=380, height=360)

tk.Label(
    card,
    text="📥 Data Receiver",
    bg="#f5f6fa",
    fg="#2f3640",
    font=("Segoe UI", 14, "bold")
).pack(pady=10)

def field(title):
    tk.Label(card, text=title, bg="#f5f6fa", font=("Segoe UI", 9, "bold")).pack()
    lbl = tk.Label(card, text="-", bg="#f5f6fa", font=("Consolas", 10))
    lbl.pack(pady=2)
    return lbl


data_label = field("Received Data")
method_label = field("Method")
sent_label = field("Sent Control Bits")
computed_label = field("Computed Control Bits")
error_label = field("Injected Error Type")

status_label = tk.Label(
    card,
    text="Server not started",
    bg="#f5f6fa",
    font=("Segoe UI", 11, "bold")
)
status_label.pack(pady=10)

import threading
threading.Thread(target=start_server, daemon=True).start()

root.mainloop()



