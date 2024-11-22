from time import sleep


def comp_print(text, skips):
    for a in str(text):
        print(a, end="")
        sleep(0.1)
    if skips > 0:
        for b in range(int(skips)):
            print()


numofdivs = 0

comp_print("Digite o seu número: ", 0)
num = int(input())

comp_print(f"Os números divisores de {num} são: ", 0)

for i in range(num):
    if num % (i+1) == 0:
        print(f"{i+1},", end=" ")
        sleep(0.1)
        numofdivs += 1

print()
comp_print(f"{num} tem {numofdivs} divisores.", 1)
if numofdivs == 2:
    comp_print("Isto quer dizer que esse número é primo. Parabéns!", 0)
else:
    comp_print("O seu número não é primo.", 0)
