import random

class Qiuqiu:

    pemain = ['Player1','Player2']
    kartu = [1,2,3,4,5,6,7,8,9,0]

    totalKartu = 4


    def __init__(self) -> None:
        pass

    def acakKartu(self):
        global kartuPlayer1,kartuPlayer2
        kartuPlayer1 = []
        kartuPlayer2 = []
        for i in range(self.totalKartu):
            acakKartu = random.choice(self.kartu)
            if not len(kartuPlayer1) == 2:
                kartuPlayer1.append(acakKartu)
            else:
                kartuPlayer2.append(acakKartu)
        self.pembagianKartu()
        
    def pembagianKartu(self):
        kartuPlayer1.sort(reverse=True)
        kartuPlayer2.sort(reverse=True)
        print("")
        print(f'Kartu Player1 : {kartuPlayer1}')
        print(f'Kartu Player2 : {kartuPlayer2}')
        totalKartuPlayer1 = kartuPlayer1[0] + kartuPlayer1[1]
        totalKartuPlayer2 = kartuPlayer2[0] + kartuPlayer2[1]
        nilai1 = totalKartuPlayer1
        nilai2 = totalKartuPlayer2
        self.jika(nilai1,nilai2)

    def jika(self,nilai1,nilai2):
        if nilai1 >= 10:
            nilai1 -= 10
        elif nilai2 >= 10:
            nilai2 -= 10

        if nilai1 > nilai2:
            print('Player1 Menang')
        elif nilai1 == nilai2:
            print('Seri')
        else:
            print('Player2 Menang')
        print("")

Qiuqiu().acakKartu()
# loop = True
# #Qiuqiu.acakKartu()
# while loop:
#     ingin = input('Apakah anda ingin lanjut bermain? [y/n] \n> ').upper()
#     if ingin == 'Y':
#         print('')
#         Qiuqiu().acakKartu()
#     elif ingin == 'N':
#         exit()
#     else:
#         print('Anda salah ketik')
