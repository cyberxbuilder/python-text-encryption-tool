import base64

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.'
}
MORSE_REVERSE = {v: k for k, v in MORSE_CODE_DICT.items()}

def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def rot13(text):
    return caesar_encrypt(text, 13)

def atbash(text):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr(90 - (ord(char) - 65))
            else:
                result += chr(122 - (ord(char) - 97))
        else:
            result += char
    return result

def reverse_cipher(text):
    return text[::-1]

def base64_encrypt(text):
    return base64.b64encode(text.encode()).decode()

def base64_decrypt(text):
    try:
        return base64.b64decode(text.encode()).decode()
    except Exception:
        return "[Error] Invalid Base64 string!"

def binary_encode(text):
    return " ".join(format(ord(c), "08b") for c in text)

def binary_decode(binary_str):
    try:
        return "".join(chr(int(b, 2)) for b in binary_str.split())
    except Exception:
        return "[Error] Invalid binary string!"

def hex_encode(text):
    return text.encode().hex()

def hex_decode(hex_str):
    try:
        return bytes.fromhex(hex_str).decode()
    except Exception:
        return "[Error] Invalid hex string!"

def morse_encode(text):
    return " ".join(MORSE_CODE_DICT.get(ch.upper(), "?") for ch in text)

def morse_decode(code):
    return "".join(MORSE_REVERSE.get(ch, "?") for ch in code.split())

def main():
    while True:
        print("\n=== Text Encrypt/Decrypt Tool ===")
        print("1. Caesar Cipher Encrypt")
        print("2. Caesar Cipher Decrypt")
        print("3. ROT13 Cipher")
        print("4. Atbash Cipher")
        print("5. Reverse Cipher")
        print("6. Base64 Encode")
        print("7. Base64 Decode")
        print("8. Binary Encode")
        print("9. Binary Decode")
        print("10. Hex Encode")
        print("11. Hex Decode")
        print("12. Morse Encode")
        print("13. Morse Decode")
        print("14. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            text = input("Enter text: ")
            shift = int(input("Enter shift (e.g. 3): "))
            print("Encrypted:", caesar_encrypt(text, shift))
        
        elif choice == "2":
            text = input("Enter text: ")
            shift = int(input("Enter shift (e.g. 3): "))
            print("Decrypted:", caesar_decrypt(text, shift))
        
        elif choice == "3":
            text = input("Enter text: ")
            print("ROT13:", rot13(text))
        
        elif choice == "4":
            text = input("Enter text: ")
            print("Atbash:", atbash(text))
        
        elif choice == "5":
            text = input("Enter text: ")
            print("Reversed:", reverse_cipher(text))
        
        elif choice == "6":
            text = input("Enter text: ")
            print("Encoded (Base64):", base64_encrypt(text))
        
        elif choice == "7":
            text = input("Enter Base64 string: ")
            print("Decoded:", base64_decrypt(text))
        
        elif choice == "8":
            text = input("Enter text: ")
            print("Binary:", binary_encode(text))
        
        elif choice == "9":
            text = input("Enter binary string (8-bit, space separated): ")
            print("Decoded:", binary_decode(text))
        
        elif choice == "10":
            text = input("Enter text: ")
            print("Hex:", hex_encode(text))
        
        elif choice == "11":
            text = input("Enter hex string: ")
            print("Decoded:", hex_decode(text))
        
        elif choice == "12":
            text = input("Enter text: ")
            print("Morse:", morse_encode(text))
        
        elif choice == "13":
            text = input("Enter Morse code (space separated): ")
            print("Decoded:", morse_decode(text))
        
        elif choice == "14":
            print("Goodbye 👋")
            break
        else:
            print("[Error] Invalid choice!")

if __name__ == "__main__":
    main()
