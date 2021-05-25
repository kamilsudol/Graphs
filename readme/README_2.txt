1. Uruchomienie programu

Lista dostępnych parametrów wywołania:

usage: main2.py [-h] [-t TASK] [-f FILENAME] [-o OUTPUT] [-s SHUFFLES] [-p PLOTS] [-v VERTICES] [-k REGULARITY] [-seq SEQUENCE] [--minv MINV] [--maxv MAXV]

optional arguments:
  -h, --help            show this help message and exit
  -t TASK, --task TASK  task number
  -f FILENAME, --filename FILENAME
                        input file name
  -o OUTPUT, --output OUTPUT
                        graph output format: list/inc/adj
  -s SHUFFLES, --shuffles SHUFFLES
                        number of edge randomizations
  -p PLOTS, --plots PLOTS
                        will it plot? y/n
  -v VERTICES, --vertices VERTICES
                        number of vertices
  -k REGULARITY, --regularity REGULARITY
                        degree of regularity
  -seq SEQUENCE, --sequence SEQUENCE
                        graphic sequence representation
  --minv MINV           minimum vertices
  --maxv MAXV           maximum vertices

Wywołanie bezparametrowe "python main2.py" spowoduje tradycyjne uruchomienie się aplikacji konsolowej.

2. Dostępne parametry wywoływania dla poszczególnych zadań.

ZADANIE 1 - czy ciag jest graficzny: -t 1 opcjonalnie(-f FILENAME -seq SEQUENCE -p PLOTS)

ZADANIE 2 - randomizacja grafu: -t 2 opcjonalnie(-f FILENAME -o OUTPUT -s SHUFFLES -p PLOTS)

ZADANIE 3 - najwieksze spojne skladowe na grafie: -t 3 opcjonalnie(-f FILENAME -p PLOTS)

ZADANIE 4 - cykl Eulera: -t 4 opcjonalnie(-f FILENAME --minv MINV --maxv MAXV -s SHUFFLES -p PLOTS)

ZADANIE 5 - generuj losowy graf k-spojny: -t 5 opcjonalnie(-v VERTICES -k REGULARITY)

ZADANIE 6 - cykl Hamiltona: -t 6 opcjonalnie(-f FILENAME -p PLOTS)

3. Dane wejściowe.

- podanie ścieżki do pliku:
	Plik o podanej lokalizacji powinien istnieć, w przeciwnym wypadku użytkownik zostanie poinformowany o błędzie.

- wczytywanie danych z pliku:
	W przypadku zadan 2, 3, 4 oraz 6, podany plik powinien zawierać graf dowolnej reprezentacji (macierz sąsiedztwa, macierz incydencji, lista sąsiedztwa).
	
	Wyjątkiem jest zadanie 1, które jako jedyne wczytuje z pliku tylko i wyłącznie ciąg graficzny.

	Przykłady reprezentacji akceptowalne przez program zostały załączone do projektu.

- wprowadzanie danych z konsoli:
	Zadanie 1:
	- w wersji konsolowej ciag graficzny musi być podany jako ciąg liczb oddzielony spacjami, np: 3 3 2 2 2 2 2 2 2
	- w przypadku wywołania parametrowego, ciąg musi być ograniczony apostrofami, np: python main2.py -t 1 -seq "3 3 2 2 2 2 2 2 2"
	
	Zadanie 5:
	- liczba wierzcholków oraz stopień k-regularności musi być podany jako ciąg liczb oddzielony spacjami, np: 7 5 (gdzie 7 oznacza l. wierzchołków, 5 - stopień regularności).
	
	W pozostałych zadaniach, tam, gdzie program prosi o podanie liczby, wprowadzenie ciągu znaków czy liczb oddzielonych spacjami spowoduje natychmiastowe wyświetlenie błędu.


