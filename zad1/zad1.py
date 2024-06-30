""" Błażej Kapkowski
Algorytm bierze pokolej każdą litere w stringu s (oprócz pierwszej) i sprawdza
czy kolejne litery oddalone o tą samą odległość od początkowo wybranej są takie same.
W taki sposób zostaną uwzględnione jedynie palindromy nieparzyste.
Po dojściu do liter które się nie zgadzaja aktualizuje maxymalną odległość
i przechodzi do sprawdzania kolejnej litery. W przypadku szczególnym gdy palindorm
kończy się na ostatniej literze stringa także aktualizuje maxymalną odległość, ponieważ
kolejna iteracja pętli by jej już nie uwzględniła. Algorytm ma złożoność N^2, ponieważ
posiada 2 zagnieżdżone pętle, jednak pętla while w znacznej większości przypadków przerwie
się po wykonaniu kilku iteracji.
"""

from zad1testy import runtests

def ceasar( s ):
    max_leng=1
    s_leng=len(s)
    for i in range(1,s_leng):
        leng=1
        j=1
        while (i-j>=0 and i+j<s_leng):
            if s[i-j]==s[i+j]:
                leng+=2
            else:
                if leng>max_leng:
                    max_leng=leng
                break
            j+=1
            if (i+j==s_leng and leng>max_leng):
                max_leng=leng
            
    return max_leng

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ceasar , all_tests = True )
