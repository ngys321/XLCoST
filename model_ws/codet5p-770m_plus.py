import sys
import time
def typewrite(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    print("\n")
# text = "def addASCII(S, N):\n    new_S = ""\n    for char_S, char_N in zip(S, N):\n        a = ord(char_N) - ord('0') \n        b = ord(char_S) + a\n        if b > 122:\n            b -= 26\n        new_S += chr(b)\n    return new_S \n\nif __name__ == \"__main__\":\n    S = \"sun\"\n    N = \"966\"\n    print(addASCII(S, N))"
# typewrite(text)

###

import itertools
import sys
import time

def spinner():
    symbols = itertools.cycle(
        ['-','/','|','\\'] # ['Thinking   ','Thinking.  ','Thinking.. ','Thinking...']
    )
    while True:
        sys.stdout.write(next(symbols))
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b') # sys.stdout.write('\b\b\b\b\b\b\b\b\b\b\b')
#spinner()

###











def model_running(input_, tokenizer, model, device, max_token_len):

    inputs = tokenizer.encode(input_+"<extra_id_0>", return_tensors="pt").to(device)
    outputs = model.generate(inputs, max_length=int(max_token_len))
    output_ = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return output_

###

def model_preparing():

    from transformers import T5ForConditionalGeneration, AutoTokenizer
    import torch

    checkpoint = "Salesforce/codet5p-770m"
    device = "cuda" # for GPU usage or "cpu" for CPU usage

    tokenizer = AutoTokenizer.from_pretrained(checkpoint)
    model = T5ForConditionalGeneration.from_pretrained(checkpoint).to(device)

    return tokenizer, model, device


###

if __name__ == "__main__":
    import threading

    typewrite("Preparing model...")
    
    tokenizer, model, device = model_preparing()

    typewrite("Model is ready!")

    ###

    while input != "quit()":
        typewrite("Input: ")
        max_token_len = input("Maximun token length: ")
        input_ = input("Partial Code: \n")
        total_len = len(input_.split())
        

        output_ = model_running(input_, tokenizer, model, device, max_token_len)
        typewrite(output_)




