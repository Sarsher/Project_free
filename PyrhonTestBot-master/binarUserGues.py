import random
def userguessing():
    ranint = random.randint(1, 1000)
    userguess = int(input("Ваша преположение"))
    if userguess == ranint:
        print('Вы правы!')
        return
    elif userguess>ranint:
        print('Ваше преположение слишком большое')
        userguessing()
    elif userguess<ranint:
        print('Ваше предположение меньше нужного')
        userguessing()
userguessing()