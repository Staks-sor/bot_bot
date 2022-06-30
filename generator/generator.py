import random


def for_man():
    boy_first = open("generator/mat_man.txt", encoding="UTF8").read().split()
    boy_two = open("generator/mat_man_prilog.txt", encoding="UTF8").read().split()
    mat_for_boy_first = random.choice(boy_first)
    mat_for_boy_two = random.choice(boy_two)

    mat = "Ты " + str.lower(mat_for_boy_first + " " + mat_for_boy_two)

    return mat


def for_women():
    girlfirst = open("generator/mat_women.txt", encoding="UTF8").read().split()

    girlsec = ["хуйня", "залупа", "манда", "шлюха", "лихохуярка", "блядь",
               "залупоеблогнойница", "выхухоль", "пидораска", "ебланка", "нервостенничка", "мозгоебка", "дермоблядунья",
               "низтроехериница", "приятельница червей"]

    mat_for_women_first = random.choice(girlfirst)
    mat_for_women_two = random.choice(girlsec)

    mat = "Ты " + str.lower(mat_for_women_first + " " + mat_for_women_two)
    return mat


if __name__ == '__main__':
    for_man()
    for_women()
