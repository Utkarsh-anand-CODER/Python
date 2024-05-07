import tkinter as tk

def xor_cipher(text, key):
    if isinstance(text, str):
        text = text.encode()

    if len(key) < len(text):
        key = key * (len(text) // len(key) + 1)
        key = key[:len(text)]

    return bytes([x ^ y for x, y in zip(text, key)])

def encrypt_decrypt():
    original_text = text_entry.get()
    key = key_entry.get().encode()

    encrypted = xor_cipher(original_text, key)
    decrypted = xor_cipher(encrypted, key)

    result_label.config(text="Encrypted Text: {}\nDecrypted Text: {}".format(encrypted.decode(), decrypted.decode()))

# GUI Setup
root = tk.Tk()
root.title("XOR Cipher")

text_label = tk.Label(root, text="Enter Text:")
text_label.pack()

text_entry = tk.Entry(root)
text_entry.pack()

key_label = tk.Label(root, text="Enter Key:")
key_label.pack()

key_entry = tk.Entry(root)
key_entry.pack()

encrypt_button = tk.Button(root, text="Encrypt / Decrypt", command=encrypt_decrypt)
encrypt_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
