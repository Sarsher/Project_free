import random
# randomnumber = random.randint(1,100)
# print(f'{randomnumber} чило было загаданно')
def kostigame():
    kost1 = random.randint(1, 6)
    kost2 = random.randint(1, 6)
    print(f'Kost 1 = {kost1}, kost 2 = {kost2}')
    if kost1 == 1:
        result1 = ('''
⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬛️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️''')
    elif kost1 == 2:
        result1 = ('''
⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬛️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬛️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️
''')
    elif kost1 == 3:
        result1 = ('''
⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬛️⬜️
⬜️⬜️⬛️⬜️⬜️
⬜️⬛️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️
''')
    elif kost1 == 4:
        result1 = ('''
⬜️⬜️⬜️⬜️⬜️
⬜️⬛️⬜️⬛️⬜️
⬜️⬜️⬜️⬜️⬜️
⬜️⬛️⬜️⬛️⬜️
⬜️⬜️⬜️⬜️⬜️
''')
    elif kost1 == 5:
        result1 = ('''
⬜️⬜️⬜️⬜️⬜️
⬜️⬛️⬜️⬛️⬜️
⬜️⬜️⬛️⬜️⬜️
⬜️⬛️⬜️⬛️⬜️
⬜️⬜️⬜️⬜️⬜️
''')
    elif kost1 == 6:
        result1 = ('''
⬜️⬜️⬜️⬜️⬜️
⬜️⬛️⬛️⬛️⬜️
⬜️⬜️⬜️⬜️⬜️
⬜️⬛️⬛️⬛️⬜️
⬜️⬜️⬜️⬜️⬜️
''')

    if kost2 == 1:
        result2 = ('''
⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬛️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️
''')
    elif kost2 == 2:
        result2 = ('''
⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬛️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬛️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️
''')
    elif kost2 == 3:
        result2 = ('''
⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬛️⬜️
⬜️⬜️⬛️⬜️⬜️
⬜️⬛️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️
''')

    elif kost2 == 4:
        prinresult2 = ('''
⬜️⬜️⬜️⬜️⬜️
⬜️⬛️⬜️⬛️⬜️
⬜️⬜️⬜️⬜️⬜️
⬜️⬛️⬜️⬛️⬜️
⬜️⬜️⬜️⬜️⬜️
''')
    elif kost2 == 5:
        result2 = ('''
⬜️⬜️⬜️⬜️⬜️
⬜️⬛️⬜️⬛️⬜️
⬜️⬜️⬛️⬜️⬜️
⬜️⬛️⬜️⬛️⬜️
⬜️⬜️⬜️⬜️⬜️
''')
    elif kost2 == 6:
        result2 = ('''
⬜️⬜️⬜️⬜️⬜️
⬜️⬛️⬛️⬛️⬜️
⬜️⬜️⬜️⬜️⬜️
⬜️⬛️⬛️⬛️⬜️
⬜️⬜️⬜️⬜️⬜️
''')

    return result1, result2