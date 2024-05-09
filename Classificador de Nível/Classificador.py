nome = input("Insira o nome do herói:")

while True:
  xp = input("Digite a quantidade de XP do herói: ")
  try:
    xp = int(xp)
    break
  except ValueError:
    print("Insira um número inteiro")

if xp <= 1000:
  nv = "Ferro"
elif 1001 <= xp < 2000:
  nv = "Bronze"
elif 2001 <= xp < 5000:
  nv = "Prata"
elif 5001 <= xp < 7000:
  nv = "Ouro"
elif 7001 <= xp < 8000:
  nv = "Platina"
elif 8001 <= xp < 9000:
  nv = "Ascedente"
elif 9001 <= xp < 10000:
  nv = "Imortal"
elif xp >= 10001:
  nv = "Radiante"

print("O Herói de nome",nome,"está no nível de",nv)