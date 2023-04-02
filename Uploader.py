import paramiko
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog


def update_alpha_hmi(host, user, password, localpath):
    port = 22

    transport = paramiko.Transport((host, port))
    transport.connect(hostname=host, username=user,
                      password=password, port=port)
    sftp = paramiko.SFTPClient.from_transport(transport)

    remotepath = '/home/Administrator/'
    sftp.put(localpath, remotepath)

    sftp.close()
    transport.close()


def select_hmi():
    filepath = filedialog.askdirectory()
    return filepath


def main():
    root = tk.Tk()
    root.title("AlphaHMIUpdater")

    tk.Label(root, text="Host 1 IP Address:").grid(row=0, column=0)
    host1_entry = tk.Entry(root)
    host1_entry.grid(row=0, column=1)

    tk.Label(root, text="Host 2 IP Address:").grid(row=1, column=0)
    host2_entry = tk.Entry(root)
    host2_entry.grid(row=1, column=1)

    tk.Label(root, text="Username:").grid(row=2, column=0)
    username_entry = tk.Entry(root)
    username_entry.grid(row=2, column=1)

    tk.Label(root, text="Password:").grid(row=3, column=0)
    password_entry = tk.Entry(root, show="*")
    password_entry.grid(row=3, column=1)

    tk.Label(root, text="HMI folder:").grid(row=4, column=0)
    hmi_file_var = tk.StringVar()
    tk.Entry(root, textvariable=hmi_file_var,
             state="readonly").grid(row=4, column=1)
    tk.Button(root, text="Select", command=lambda: hmi_file_var.set(
        select_hmi())).grid(row=4, column=2)

    tk.Button(root, text="Download", command=lambda: [
        update_alpha_hmi(host1_entry.get(), username_entry.get(
        ), password_entry.get(), hmi_file_var.get()),
        update_alpha_hmi(host2_entry.get(), username_entry.get(
        ), password_entry.get(), hmi_file_var.get())
    ]).grid(row=5, columnspan=3)

    root.mainloop()


if __name__ == "__main__":
    main()
