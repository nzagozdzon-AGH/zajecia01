if __name__ == "__main__": #Sprawia, ¿e program uruchomi siê tylko jeœli jest g³ównym programem
    import sys #Program dzia³a na u¿ytkowanym systemie operacyjnym
    from math import sqrt #mówisz, ¿e warto to importowaæ



    # ZADANIE 1
    def naj_wsp_dzielnik(A, B): #Tworzê funkcje dwóch liczb s³u¿¹cych do odnalezienia ich najwiêkszego wspólnego dzielnika
        
        
        while A!=B: 
            #Pierwszy krok algorytmu euklidesa
            if A>B: 
                #sprawdza co wiêksze
                A=A-B 
            else:
                B=B-A #Tak leci ten algorytym, nie wiem co tu pisaæ
        print('Najwiekszy wspolny dzielnik z podanych liczb to ', A) #drukuje odpowiedŸ

    naj_wsp_dzielnik(15, 10)
    naj_wsp_dzielnik(33, 11)
    naj_wsp_dzielnik(5436, 234) #Sprawdzam dzia³anie programu na trzech przyk³adach


    #ZADANIE 2
    def trojmian(A, B, C): #tworze funkcje trzech zmiennych odpowiadajacych Ax^2 + Bx + C
        delta = B*B - 4*A*C  #Liczy delte, aby pozniej wyliczyc pierwiastki
        if delta>0:
            x1 = (-B + delta) / (2*A)
            x2 = (-B - delta) / (2*A) #jak delta jest dodatnia to leci wzorami
            print('Trojmain ma dwa pierwistki, x1=',x1,'i x2=', x2) #wypisuje odpowiedzi
        elif delta==0:
            x1 = -B / (2*A)
            print('Trojmain ma jeden pierwiastek, x1=', x1) #tu te¿ wypisuje przypadek z delta rowna 0
        else:
            print('Trojmian nie ma pierwiastkow rzeczywistych') #przypadek z delta na minus

    trojmian(1, 4, 4)
    trojmian(1, -2, -3)
    trojmian(1, 1, 1) #sprawdzenie dzia³ania programu

    

    #ZADANIE 3
    def sumer(A): #definiuje funkcje jednej zmiennej, ciagu znakow, ktory bedzie skracany
        suma = 0 #deklaruje zmienna pozniej potrzebna
        A_str = str(A)
        for i in len(A_str): #Tworzy pêtle do iterowania ka¿dej liczby w ci¹gu znaków
            suma = suma + int(A_str[i]) #iteracja trwa
        if suma<10: #warunek podany w poleceniu
            print('Wynik tego co chcialem zrobic to:', suma) #drukuje odpowiedz
        else:
            sumer(suma) #to siê chyba nazywa rekurencja, ponowiam dzialanie programu, poki sie nie skroci to liczby mniejszej niz 10

    sumer(153)
    sumer(4358978)
    sumer(2) #sprawdzam dzialanie programu
