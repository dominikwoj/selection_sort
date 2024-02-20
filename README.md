1. Info about sort type 'selection sort' - algorythm:
 > https://www.home.umk.pl/~abak/wdimat/s/SelectSort.html
 
Jest to chyba najbardziej intuicyjny algorytm sortowania. Polega on na wielokrotnym wyborze minimalnego elementu z coraz krótszego podciągu danych. Dokładnie ma to następujący przebieg:
 - Wybierz minimum z ciągu elementów na pozycjach od 1 do n i zamień go z pierwszym elementem.
 - Wybierz minimum z ciągu elementów na pozycjach od 2 do n i zamień go z drugim elementem (po tym kroku elementy na pozycjach od 1 do 2 są uporządkowane).
 - ...
 - Wybierz minimum z ciągu elementów na pozycjach n-1 i n i zamień go z elementem na pozycji n-1 (po tej operacji elementy na pozycjach od 1 do n-1 są uporządkowane, a element na pozycji n jest maksymalny, czyli ciąg elementów na pozycjach od 1 do n jest uporządkowany)

Znalezienie minimum w ciągu wymaga m-1 porównań, gdzie m jest długością ciągu. Algorytm sortowania przez wybór wykonuje n-1 takich operacji, a długość ciągu, z którego wybierany jest element minimalny zmienia się od n do 2.

It has a time complexity of O(n^2).

2. install all requirements
 > py -m pip install -r requirements.txt

3. run pytest
 > py -m pytest .\test.py -s -vv

