import tkinter as tk

# Morse Code Dictionary: Maps letters and numbers to Morse code
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.',
    ' ': '/'  # Space character is represented by '/'
}

# Reverse the MORSE_CODE_DICT to map Morse code back to letters and numbers
MORSE_TO_TEXT = {value: key for key, value in MORSE_CODE_DICT.items()}


# Function to encode text into Morse code
def encode_text():
    # Get the text input from the user, convert to uppercase
    text = input_entry.get().upper()
    morse = []  # List to hold Morse code characters

    # Convert each character in the input text to Morse code
    for char in text:
        if char in MORSE_CODE_DICT:
            morse.append(MORSE_CODE_DICT[char])
        else:
            morse.append('?')  # If character is not in the dictionary, append a '?'

    # Clear the output text box and display the Morse code
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, ' '.join(morse))  # Join Morse code with spaces


# Function to decode Morse code into text
def decode_morse():
    # Get the Morse code input from the user, strip any extra spaces
    code = input_entry.get().strip()
    words = code.split(' ')  # Split the Morse code into individual words (separated by spaces)
    decoded = []  # List to hold decoded characters

    # Decode each Morse code symbol to text
    for symbol in words:
        if symbol in MORSE_TO_TEXT:
            decoded.append(MORSE_TO_TEXT[symbol])  # Get corresponding letter from Morse code
        else:
            decoded.append('?')  # If symbol is not recognized, append a '?'

    # Clear the output text box and display the decoded text
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, ''.join(decoded))  # Join decoded characters into a string


# Create the main window using Tkinter
root = tk.Tk()
root.title("Morse Code Translator")  # Set the title of the window
root.geometry("400x300")  # Set the window size to 400x300 pixels

# Label to prompt the user to enter text or Morse code
tk.Label(root, text="Enter text or Morse code:").pack(pady=5)

# Input field for the user to enter text or Morse code
input_entry = tk.Entry(root, width=50)
input_entry.pack(pady=5)

# Button to encode text to Morse code
tk.Button(root, text="Encode to Morse", command=encode_text).pack(pady=5)

# Button to decode Morse code to text
tk.Button(root, text="Decode to Text", command=decode_morse).pack(pady=5)

# Label for the result
tk.Label(root, text="Result:").pack(pady=5)

# Text box to display the output (either Morse code or decoded text)
output_text = tk.Text(root, height=6, width=50)
output_text.pack(pady=5)

# Start the Tkinter event loop to make the window interactive
root.mainloop()