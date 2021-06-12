1. Uruchomienie programu

Lista dostępnych parametrów wywołania:

usage: main3.py [-h] [-t TASK] [-f FILENAME] [-o OUTPUT] [-s SHUFFLES] [-p PLOTS] [-v VERTICES] [-k REGULARITY] [-seq SEQUENCE] [--minv MINV] [--maxv MAXV]

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


Wywołanie bezparametrowe "python main3.py" spowoduje tradycyjne uruchomienie się aplikacji konsolowej.

2. Dostępne parametry wywoływania dla poszczególnych zadań.

ZADANIE 1 - generowanie spojnego grafu losowego z krawedziami o losowych wagach: -t 1 opcjonalnie(-f FILENAME -p PLOTS)
	wejście:
		aplikacja pyta o sposób generacji grafu losowego, oraz odpowiednie parametry losowania
		opcjonalnie można wprowadzić graf w postaci macierzy sasiedztwa za pomocą flagi wywołania konsolowego
	wyjście:
		graficzna reprezentacja wygenerowanego grafu.
        jeśli wygenerowany graf nie jest spójny, wynikiem będzie jego największa spójna składowa
	W PRZYPADKU WYWOŁANIA Z APLIKACJI:
		wygenerowany graf losowy z wagami jest wykorzystywany w wywołaniach kolejnych zadań

ZADANIE 2 - najkrótsze ścieżki w grafie (alg. Dijkstry): -t 2 opcjonalnie(-f FILENAME -p PLOTS)
	wejście:
		graf wygenerowany w zadaniu 1 jest automatycznie pobierany
		opcjonalnie można wprowadzić graf w postaci macierzy sasiedztwa za pomocą flagi wywołania konsolowego
	wyjście:
		lista nakrótszych ścieżek od pierwszego do pozostałych wierzchołków wraz z kosztami dojścia.
	W PRZYPADKU WYWOŁANIA Z APLIKACJI:
		zadanie wymaga wygenerowania grafu losowego z wagami za pomocą zadania 1
	W PRZYPADKU WYWOŁANIA Z KONSOLI:
		jeśli graf nie został podany z pliku użytkownik zostanie poproszony o podanie sposobu i parametrów generacji

ZADANIE 3 - macierz odleglosci miedzy wszystkimi parami wierzcholkow: -t 3 opcjonalnie(-f FILENAME -p PLOTS)
	wejście:
		graf wygenerowany w zadaniu 1 jest automatycznie pobierany
		opcjonalnie można wprowadzić graf w postaci macierzy sasiedztwa za pomocą flagi wywołania konsolowego
	wyjście:
		macierz kosztów dojścia pomiędzy wszystkimi parami wierzchołków.
	W PRZYPADKU WYWOŁANIA Z APLIKACJI:
		zadanie wymaga wygenerowania grafu losowego z wagami za pomocą zadania 1
	W PRZYPADKU WYWOŁANIA Z KONSOLI:
		jeśli graf nie został podany z pliku użytkownik zostanie poproszony o podanie sposobu i parametrów generacji

ZADANIE 4 - centrum i centrum minmax grafu: -t 4 opcjonalnie(-f FILENAME -p PLOTS)
	wejście:
		graf wygenerowany w zadaniu 1 jest automatycznie pobierany
		opcjonalnie można wprowadzić graf w postaci macierzy sasiedztwa za pomocą flagi wywołania konsolowego
	wyjście:
		informacja o centrum grafu wraz z sumą odległości
		oraz o centrum minmax grafu wraz z odległością od najdalszego wierzchołka.
	W PRZYPADKU WYWOŁANIA Z APLIKACJI:
		zadanie wymaga wygenerowania grafu losowego z wagami za pomocą zadania 1
	W PRZYPADKU WYWOŁANIA Z KONSOLI:
		jeśli graf nie został podany z pliku użytkownik zostanie poproszony o podanie sposobu i parametrów generacji

ZADANIE 5 - minimalne drzewo rozpinajace: -t 5 opcjonalnie(-f FILENAME -p PLOTS)
	wejście:
		graf wygenerowany w zadaniu 1 jest automatycznie pobierany
		opcjonalnie można wprowadzić graf w postaci macierzy sasiedztwa za pomocą flagi wywołania konsolowego
	wyjście:
		graficzne porownanie podanego grafu oraz minimalnego drzewa rozpinającego powstałego z podanego grafu.
	W PRZYPADKU WYWOŁANIA Z APLIKACJI:
		zadanie wymaga wygenerowania grafu losowego z wagami za pomocą zadania 1
	W PRZYPADKU WYWOŁANIA Z KONSOLI:
		jeśli graf nie został podany z pliku użytkownik zostanie poproszony o podanie sposobu i parametrów generacji

3. Dane wejściowe.

- podanie ścieżki do pliku:
	Plik o podanej lokalizacji powinien istnieć, w przeciwnym wypadku użytkownik zostanie poinformowany o błędzie.

- wczytywanie danych z pliku:
	W przypadku wszystkich zadan, podany plik powinien zawierać graf w reprezentacji macierzy sąsiedztwa.
	
	Przykłady reprezentacji akceptowalnych przez program zostały załączone do projektu.

- wprowadzanie danych z konsoli:
	
	Tam, gdzie program prosi o podanie liczby, wprowadzenie ciągu znaków czy liczb oddzielonych spacjami spowoduje natychmiastowe wyświetlenie błędu.


