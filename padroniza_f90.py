#!/home/lufla/anaconda3/bin/python
import sys
import shutil
import os
import subprocess  # Para chamar comandos do sistema
from fprettify import run  # pragma: no cover

def limpa_brancos(nome_arquivo):
    source = open(nome_arquivo, 'r')
    lines = source.readlines()
    source.close()
    new_source = open(nome_arquivo, 'w')
    nlinha = 0
    for line in lines:
        nlinha = nlinha + 1
        new_line = line.strip() + "\n"
        new_source.write(new_line)
        if not new_line.startswith('!'):
            if ';' in new_line:
                print(f"[;][{nlinha}]{new_line}")

    new_source.close()

def makePretty(nome_arquivo):
    # Chama o comando fprettify no arquivo original com os argumentos especificados
    #print(f"Executando fprettify no arquivo '{nome_arquivo}' com os argumentos personalizados...")
    resultado = subprocess.run(
        [
            "fprettify",
            "--indent", "4",
            "--strict-indent",
            "--line-length", "132",
            "--case", "1", "1", "1", "1",
            "--enable-replacements",
            "--c-relations",
            nome_arquivo
        ],
        capture_output=True,
        text=True
    )

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python3 padroniza_f90.py <arquivo>")
    else:
        limpa_brancos(sys.argv[1])
        makePretty(sys.argv[1])
        #run()