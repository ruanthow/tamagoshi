import time

# statuts iniciais
fome = 10
sede = 15
sono = 40
nome = ''


# bixinho
# feliz = (*-*)
# com fome ou sede = (`o`)
# com sono = (-.-)Zzz
# morto (x_x)


def _startgame(new_fome, new_name, new_sede, new_sono):
    continuar_jogando = 1
    print("Ola sou seu novo bixinho virtaul (*-*).")
    new_name = input("Preciso de um nome, então me de um: \n")

    while (new_name == ''):
        new_name = input("Pow cara vai lá me de um nome: \n")
    print("Meu nome agora é: ", new_name, "\n")
    print("Esses são os meus status agora:\n fome: ", new_fome,
          "\n sede: ", new_sede, "\n sono: ", new_sono)
    print("Essas são as acções que poderá fazer para ajudar o seu bixinho virtual")

    while (continuar_jogando != 0):
        action = int(input(
            "digite '1': para alimentar, digite '2': para beber água, ou digite '3': para dormir, digite '0': para finalizar\n"))
        while (action != 0):
            if (action == 1):
                new_fome = _alimentar(new_fome)
                if (new_fome > 100):
                    print('Seu bixinho morreu engasgado (x_x)')
                    return
                print("fome esta em :", new_fome, "%")
                action = int(input(
                    "digite '1': para alimentar, digite '2': para beber água, ou digite '3': para dormir, digite '0': para finalizar\n"))

            elif (action == 2):
                new_sede = _beber_agua(new_sede)
                if (new_sede > 100):
                    print('Seu bixinho morreu engasgado (x_x)')
                    return
                print("sede esta em :", new_sede, "%")
                action = int(input(
                    "digite '1': para alimentar, digite '2': para beber água, ou digite '3': para dormir, digite '0': para finalizar\n"))

            elif (action == 3):
                new_sono = _dormir(new_sono)
                print(new_sono)
                action = int(input(
                    "digite '1': para alimentar, digite '2': para beber água, ou digite '3': para dormir, digite '0': para finalizar\n"))
            else:
                print("Escolha uma das opções abaixo")
                action = int(input(
                    "digite '1': para alimentar, digite '2': para beber água, ou digite '3': para dormir, digite '0': para finalizar\n"))
        countdown(new_fome, new_sede, new_sono)
        continuar_jogando = int(
            input("Digite 1 para continuar a jogar ou '0' para sair\n"))


def _alimentar(current_fome):

    if (current_fome < 100):
        print("humm.... que delícia (*-*)")
        return current_fome + 25


def _beber_agua(current_sede):
    if (current_sede < 100):
        print("humm.... me sinto hidratado! (*-*)")
        return current_sede + 25


def _dormir(current_sono):
    if (current_sono < 45):
        print("Vou dorm....ir um pouco (-.-)Zzz")
        return current_sono + 15

    elif (current_sono > 45 and current_sono < 80):
        print("Vou dorm....ir mais um pouquinho (-.-)Zzz")
        return current_sono + 15

    elif (current_sono > 80):
        print("Não quero dormir não tenho muita energia ainda (*-*)")
        return current_sono + 0


def countdown(current_fome, current_sede, current_sono):
    x = 180
    while (x > 1):
        mins, secs = divmod(x, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print("Tempo para mudar os status do tamagoshi, Aguarde...", timer, end="\r")
        time.sleep(1)
        x -= 1
    return print("fome: ", current_fome - 10, "\nsede: ", current_sede - 10, "\nsono: ", current_sono - 10)


_startgame(fome, nome, sede, sono)
