import random
import time

# Função para mostrar texto devagar (efeito RPG)
def slow(text):
    for c in text:
        print(c, end='', flush=True)
        time.sleep(0.015)
    print()

# Criar personagem
slow("Bem-vindo ao RPG da Floresta Sombria!")
nome = input("Digite o nome do seu herói: ")

jogador = {
    "nome": nome,
    "vida": 100,
    "ataque": 15,
    "defesa": 5,
    "poções": 3,
    "xp": 0,
    "level": 1
}

inimigos = [
    {"nome": "Goblin", "vida": 40, "ataque": 10},
    {"nome": "Lobo Selvagem", "vida": 55, "ataque": 12},
    {"nome": "Esqueleto", "vida": 60, "ataque": 14},
    {"nome": "Ogro", "vida": 85, "ataque": 18}
]

def batalha():
    inimigo = random.choice(inimigos)
    inimigo_vida = inimigo["vida"]
    slow(f"\n⚔️ Um {inimigo['nome']} apareceu!\n")

    while inimigo_vida > 0 and jogador["vida"] > 0:
        print(f"\n{jogador['nome']} - Vida: {jogador['vida']} | Poções: {jogador['poções']}")
        print(f"{inimigo['nome']} - Vida: {inimigo_vida}")
        print("\n1 - Atacar")
        print("2 - Usar poção")
        print("3 - Fugir")

        escolha = input("Escolha: ")

        if escolha == "1":
            dano = jogador["ataque"] + random.randint(-3, 3)
            inimigo_vida -= dano
            slow(f"💥 Você causou {dano} de dano!")
        elif escolha == "2":
            if jogador["poções"] > 0:
                jogador["poções"] -= 1
                jogador["vida"] += 30
                slow("🧪 Você usou uma poção e recuperou 30 de vida!")
            else:
                slow("❌ Você não tem poções!")
                continue
        elif escolha == "3":
            slow("🏃 Você fugiu da batalha!")
            return False
        else:
            slow("Opção inválida!")
            continue

        if inimigo_vida > 0:
            dano_inimigo = inimigo["ataque"] + random.randint(-4, 4) - jogador["defesa"]
            dano_inimigo = max(0, dano_inimigo)
            jogador["vida"] -= dano_inimigo
            slow(f"⚔️ {inimigo['nome']} te atacou causando {dano_inimigo} de dano!")

    if jogador["vida"] <= 0:
        slow("💀 Você foi derrotado…")
        return "morto"

    slow(f"🎉 Você derrotou o {inimigo['nome']}!")
    xp_ganho = random.randint(15, 30)
    jogador["xp"] += xp_ganho
    slow(f"⭐ Você ganhou {xp_ganho} XP!")

    level_up()
    return True

def level_up():
    if jogador["xp"] >= jogador["level"] * 50:
        jogador["level"] += 1
        jogador["ataque"] += 3
        jogador["defesa"] += 2
        jogador["vida"] += 20
        slow(f"\n⬆️ LEVEL UP! Você agora é nível {jogador['level']}!")
        slow("Seus atributos aumentaram!")

# Loop principal
while True:
    print("\n==============================")
    print("1 - Explorar a floresta")
    print("2 - Ver status")
    print("3 - Sair do jogo")
    print("==============================")

    escolha = input("O que deseja fazer? ")

    if escolha == "1":
        resultado = batalha()
        if resultado == "morto":
            break
    elif escolha == "2":
        print("\n=== STATUS DO JOGADOR ===")
        for k, v in jogador.items():
            print(f"{k.capitalize()}: {v}")
    elif escolha == "3":
        slow("Saindo do jogo... Até a próxima aventura!")
        break
    else:
        slow("Escolha inválida!")