import os

PASTA = os.path.join(os.path.abspath('.'), 'data')

def cria_diretorio(nome_dir):
  OUTPUR_DIR = os.path.join(PASTA, nome_dir)
  if not os.path.exists(OUTPUR_DIR):
    os.makedirs(OUTPUR_DIR)

def move_arquivo(arquivo, nome_pasta):
  caminho_antigo = os.path.join(PASTA, arquivo)
  caminho_novo = os.path.join(PASTA, nome_pasta, arquivo)

  try:
    os.rename(caminho_antigo, caminho_novo)
  except FileNotFoundError:
    print("O arquivo não foi encontrado")
  except Exception as e:
    print(f"Ocorreu um erro: {e}")

cria_diretorio("IMAGENS") # JPG, PNG
cria_diretorio("VIDEOS") # MP4
cria_diretorio("MUSICAS") # MP3
cria_diretorio("TEXTOS") # TXT, PDF, DOCX

if __name__ == '__main__':
  for nome in os.listdir(PASTA):
    if nome.endswith(".jpg") or nome.endswith(".png"):
      move_arquivo(nome, 'IMAGENS')
    elif nome.endswith(".mp4"):
      move_arquivo(nome, 'VIDEOS')
    elif nome.endswith(".mp3"):
      move_arquivo(nome, 'MUSICAS')
    elif nome.endswith(".txt") or nome.endswith(".pdf") or nome.endswith(".docx"):
      move_arquivo(nome, 'TEXTOS')