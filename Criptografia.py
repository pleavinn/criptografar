def criptografar(texto, deslocamento):
    resultado = ''
    for char in texto:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            resultado += chr((ord(char) - base + deslocamento) % 26 + base)
        else:
            resultado += char
    return resultado

def main():
    textoo = input("digite a palavra/frase a ser criptografada: ")
    deslocamento = int(input("deslocamento: "))

    textocrip = criptografar(textoo, deslocamento)

    print(f"Texto criptografado: {textocrip}")

if __name__ == "__main__":
    main()