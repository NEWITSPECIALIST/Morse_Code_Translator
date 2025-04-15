import tkinter as tk

# Морзе-словник
MORSE_CODE_DICT = {
    'A': '.-',     'B': '-...',   'C': '-.-.',
    'D': '-..',    'E': '.',      'F': '..-.',
    'G': '--.',    'H': '....',   'I': '..',
    'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',
    'P': '.--.',   'Q': '--.-',   'R': '.-.',
    'S': '...',    'T': '-',      'U': '..-',
    'V': '...-',   'W': '.--',    'X': '-..-',
    'Y': '-.--',   'Z': '--..',
    '0': '-----',  '1': '.----',  '2': '..---',
    '3': '...--',  '4': '....-',  '5': '.....',
    '6': '-....',  '7': '--...',  '8': '---..',
    '9': '----.',
    ' ': '/'
}
MORSE_TO_TEXT = {value: key for key, value in MORSE_CODE_DICT.items()}  #є "реверсом" (оберненням) словника MORSE_CODE_DICT.

# Функції
def encode_text():
    text = input_entry.get().upper()
    morse = []
    for char in text:
        if char in MORSE_CODE_DICT:
            morse.append(MORSE_CODE_DICT[char])
        else:
            morse.append('?')
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, ' '.join(morse))

def decode_morse():
    code = input_entry.get().strip()
    words = code.split(' ')
    decoded = []
    for symbol in words:
        if symbol in MORSE_TO_TEXT:
            decoded.append(MORSE_TO_TEXT[symbol])
        else:
            decoded.append('?')
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, ''.join(decoded))

# Створення вікна
root = tk.Tk()
root.title("Morse Code Translator")
root.geometry("400x300")

# Ввід
tk.Label(root, text="Enter text or Morse code:").pack(pady=5)
input_entry = tk.Entry(root, width=50)
input_entry.pack(pady=5)

# Кнопки
tk.Button(root, text="Encode to Morse", command=encode_text).pack(pady=5)
tk.Button(root, text="Decode to Text", command=decode_morse).pack(pady=5)

# Вивід
tk.Label(root, text="Result:").pack(pady=5)
output_text = tk.Text(root, height=6, width=50)
output_text.pack(pady=5)

# Старт
root.mainloop()