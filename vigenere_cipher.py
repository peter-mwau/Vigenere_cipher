import gradio as gr

def vigenere_cipher(message, key, mode):
    alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key = key.upper().replace(" ", "")
    message = message.upper().replace(" ", "")
    key_length = len(key)
    message_length = len(message)
    
    result = []
    for i in range(message_length):
        if mode == 'Encrypt':
            result.append(alphabets[(alphabets.index(message[i]) + alphabets.index(key[i % key_length])) % 26])
        elif mode == 'Decrypt':
            result.append(alphabets[(alphabets.index(message[i]) - alphabets.index(key[i % key_length])) % 26])
    
    return "".join(result)


# Create the Gradio interface
inputs = [
    gr.inputs.Textbox(label="Message"),
    gr.inputs.Textbox(label="Key"),
    gr.inputs.Radio(['Encrypt', 'Decrypt'], label="Mode")
]
output = gr.outputs.Textbox(label="Result")

interface = gr.Interface(fn=vigenere_cipher, inputs=inputs, outputs=output, title="Vigenère Cipher")
interface.launch()
