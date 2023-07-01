import random

class Qiuqiu:

    pemain = ['Player1','Player2']
    kartu = [1,2,3,4,5,6,7,8,9,0]

    totalKartu = 4


    def __init__(self) -> None:
        pass

    def acakKartu():
        global kartuPlayer1,kartuPlayer2
        kartuPlayer1 = []
        kartuPlayer2 = []
        for i in range(Qiuqiu.totalKartu):
            acakKartu = random.choice(Qiuqiu.kartu)
            if not len(kartuPlayer1) == 2:
                kartuPlayer1.append(acakKartu)
            else:
                kartuPlayer2.append(acakKartu)
        
        Qiuqiu.pembagianKartu()
        
    def pembagianKartu():
        #global nilai1, nilai2
        kartuPlayer1.sort(reverse=True)
        kartuPlayer2.sort(reverse=True)
        print("")
        print(f'Kartu Player1 : {kartuPlayer1}')
        print(f'Kartu Player2 : {kartuPlayer2}')

        totalKartuPlayer1 = kartuPlayer1[0] + kartuPlayer1[1]
        totalKartuPlayer2 = kartuPlayer2[0] + kartuPlayer2[1]

        nilai1 = totalKartuPlayer1
        nilai2 = totalKartuPlayer2

        Qiuqiu.jika(nilai1,nilai2)

    def jika(nilai1,nilai2):
        if nilai1 == 10:
            nilai1 = 0

        elif nilai2 == 10:
            nilai2 = 0

        if nilai1 > nilai2:
            print('Player1 Menang')
        elif nilai1 == nilai2:
            print('Seri')
        else:
            print('Player2 Menang')
        
        print("")
    #     Qiuqiu.ulang()

    # def ulang():
    #     while loop:
    #         ulang = input('ulang? [y/n] \n> ').upper()
    #         if ulang == 'Y':
    #             print('')
    #             Qiuqiu.acakKartu()
    #         elif ulang == 'N':
    #             exit()
    #         else:
    #             print('Anda salah ketik')


# print(""" 

#             9-9 
        
# """)

loop = True
#Qiuqiu.acakKartu()
while loop:
    ingin = input('Apakah anda ingin lanjut bermain? [y/n] \n> ').upper()
    if ingin == 'Y':
        print('')
        Qiuqiu.acakKartu()
    elif ingin == 'N':
        exit()
    else:
        print('Anda salah ketik')
