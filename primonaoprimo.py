from time import sleep


def comp_print(text):
    for a in str(text):
        print(a, end="")
        sleep(0.1)


numofdivs = 0

comp_print("Digite o seu número: ")
num = int(input())

comp_print(f"Os números divisores de {num} são: ")

for i in range(num):
    if num % (i+1) == 0:
        print(f"{i+1},", end=" ")
        sleep(0.1)
        numofdivs += 1

print()
comp_print(f"{num} tem {numofdivs} divisores.")
print()
if numofdivs == 2:
    comp_print("Isto quer dizer que esse número é primo. Parabéns!")
else:
    comp_print("O seu número não é primo.")
