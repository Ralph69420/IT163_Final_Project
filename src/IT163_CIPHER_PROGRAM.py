import tkinter as tk
from tkinter import scrolledtext  # Scrollbar support
import base64

# Atbash cipher function
def atbash_cipher(text, mode):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    reverse_alphabet = 'zyxwvutsrqponmlkjihgfedcba'
    result = ''

    for char in text.lower():
        if char in alphabet:
            index = alphabet.index(char)
            if mode == 1:   # Encryption mode
                result += reverse_alphabet[index]
            elif mode == 2: # Decryption mode
                result += alphabet[reverse_alphabet.index(char)]
        else:
            result += char
    
    return result

# Base64 encrypt function
def base64_encrypt(text):
    encoded_bytes = base64.b64encode(text.encode('utf-8'))
    return encoded_bytes.decode('utf-8')

# Base64 decrypt function
def base64_decrypt(text):
    try:
        decoded_bytes = base64.b64decode(text.encode('utf-8'))
        return decoded_bytes.decode('utf-8')
    except Exception as e:
        return str(e)

# Caesar cipher function
def caesar_cipher(text, shift, direction, mode):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ''

    for char in text.lower():
        if char in alphabet:
            index = alphabet.index(char)
            if mode == 1:   # Encryption mode
                if direction == 'right':
                    result += alphabet[(index + shift) % 26]
                elif direction == 'left':
                    result += alphabet[(index - shift) % 26]
            elif mode == 2: # Decryption mode
                if direction == 'right':
                    result += alphabet[(index - shift) % 26]
                elif direction == 'left':
                    result += alphabet[(index + shift) % 26]
        else:
            result += char
    
    return result

# Caesar cipher decryption results function
def brute_force_caesar(text):
    results = []
    for shift in range(1, 26):
        decrypted_right = caesar_cipher(text, shift, 'right', 2)  # Decrypt mode with right shift
        decrypted_left = caesar_cipher(text, shift, 'left', 2)  # Decrypt mode with left shift
        results.append(f"Shift {shift} (Right): {decrypted_right}\nShift {shift} (Left): {decrypted_left}")
    return '\n'.join(results)

# Encrypt/Decrypt function
def encrypt_decrypt():
    choice = cipher_choice.get()    # Cipher choice
    input_text = text_entry.get("1.0", tk.END).strip()  # Text input
    direction = direction_choice.get()  # Shift direction
    mode = mode_choice.get()    # Encrypt or Decrypt mode
    

    if choice == 1: # Atbash Cipher
        output_text = atbash_cipher(input_text, mode)
    
    elif choice == 2:   # Base64 Encryption
        if mode == 1:       # Encryption mode
            output_text = base64_encrypt(input_text)
        elif mode == 2:     # Decryption mode
            output_text = base64_decrypt(input_text)
    
    elif choice == 3:   # Caesar Cipher
        if mode == 1:       # Encryption mode
            shift = int(shift_entry.get())
            output_text = caesar_cipher(input_text, shift, direction, mode)
        elif mode == 2:     # Decryption mode
            output_text = brute_force_caesar(input_text)
    
    else:   # Error output
        output_text = "Invalid choice or mode."

    # Update the result label with the encrypted or decrypted text
    result_text.config(state=tk.NORMAL)     # Enable editing state
    result_text.delete(1.0, tk.END)         # Clear previous content
    result_text.insert(tk.END, output_text) # Insert new content
    result_text.config(state=tk.DISABLED)   # Disable editing state

# Create the Main Window and Frames
window = tk.Tk()
window.title("Cipher Program")
window.eval('tk::PlaceWindow . center')
frame1 = tk.Frame(window)
frame1.pack(side=tk.TOP, fill=tk.X, expand=True)
frame2 = tk.Frame(window)
frame2.pack(side=tk.TOP, fill=None, expand=True)
frame3 = tk.Frame(window)
frame3.pack(side=tk.TOP, fill=None, expand=True)
frame4 = tk.Frame(window)
frame4.pack(side=tk.TOP, fill=None, expand=True)
frame5 = tk.Frame(window)
frame5.pack(side=tk.TOP, fill=None, expand=True)

# Text Input Frame
text_entry = tk.Text(frame1, height=2, width=40)
text_entry.pack(fill=tk.X, padx=10, pady=10)

# Cipher options
cipher_choice = tk.IntVar()
cipher_choice.set(1)  # Default to Atbash Cipher
atbash_radio = tk.Radiobutton(frame2, text="Atbash Cipher", variable=cipher_choice, value=1)
atbash_radio.pack(side=tk.LEFT, padx=5, pady=5)
base64_radio = tk.Radiobutton(frame3, text="Base64 Format", variable=cipher_choice, value=2)
base64_radio.pack(side=tk.LEFT, padx=5, pady=5)
caesar_radio = tk.Radiobutton(frame4, text="Caesar Cipher", variable=cipher_choice, value=3)
caesar_radio.pack(side=tk.LEFT, padx=5, pady=5)

# Shift amount input
shift_label = tk.Label(frame4, text="Shift(1-25):")
shift_label.pack(side=tk.LEFT, anchor=tk.CENTER)
shift_entry = tk.Entry(frame4, width=4)
shift_entry.pack(side=tk.LEFT, anchor=tk.CENTER)

# Direction options
direction_choice = tk.StringVar()
direction_choice.set('right')  # Default direction to right
left_radio = tk.Radiobutton(frame4, text="Left", variable=direction_choice, value='left')
left_radio.pack(side=tk.LEFT, anchor=tk.CENTER)
right_radio = tk.Radiobutton(frame4, text="Right", variable=direction_choice, value='right')
right_radio.pack(side=tk.LEFT, anchor=tk.CENTER)

# Encrypt or Decrypt mode options
mode_choice = tk.IntVar()
mode_choice.set(1)  # Default to Encryption
encrypt_radio = tk.Radiobutton(frame5, text="Encrypt", variable=mode_choice, value=1)
encrypt_radio.pack(side=tk.LEFT, padx=5, pady=5)
decrypt_radio = tk.Radiobutton(frame5, text="Decrypt", variable=mode_choice, value=2)
decrypt_radio.pack(side=tk.LEFT, padx=5, pady=5)

# Submit button for encrypt_decrypt function
encrypt_button = tk.Button(window, text="Submit", command=encrypt_decrypt)
encrypt_button.pack(pady=10)

# Create a scrolled text widget for the result label
result_text = scrolledtext.ScrolledText(window, height=10, width=40, wrap=tk.WORD)
result_text.pack(fill=tk.X)

# Run the GUI
window.mainloop()