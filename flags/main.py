import os
from flags import bandeira_brasileira, bandeira_japao, bandeira_alemanha, bandeira_franca

IMG_DIR = "img"

if __name__ == '__main__':
  # img, nome = bandeira_brasileira(1400)
  # img, nome = bandeira_japao(1400)
  # img, nome = bandeira_alemanha(1400)
  img, nome = bandeira_franca(1400)

  filename = os.path.join(IMG_DIR, nome)
  img.save(filename)



