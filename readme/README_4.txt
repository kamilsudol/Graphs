1. Uruchomienie programu

Lista dostępnych parametrów wywołania:

usage: main4.py [-h] [-t TASK] [-f FILENAME] [-o OUTPUT] [-s SHUFFLES] [-p PLOTS] [-v VERTICES] [-k REGULARITY] [-seq SEQUENCE] [--minv MINV] [--maxv MAXV]

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


Wywołanie bezparametrowe "python main4.py" spowoduje tradycyjne uruchomienie się aplikacji konsolowej.

2. Dostępne parametry wywoływania dla poszczególnych zadań.

ZADANIE 1 - generuj losowy graf skierowany: -t 1 opcjonalnie(-p PLOTS)
	wejście:
		aplikacja pyta o parametry losowania w postaci "[liczba_wierzchołków] [prawdopodbieństwo_krawędzi]"
	wyjście:
		wygenerowany graf skierowany w reprezentacji macierzy sąsiedztwa
		oraz jego reprezentacja graficzna.

ZADANIE 2 - znajdz najwieksza silnie spojna skladowa: -t 2 opcjonalnie(-f FILENAME -p PLOTS)
	wejście:
		aplikacja pyta o parametry losowania w postaci "[liczba_wierzchołków] [prawdopodbieństwo_krawędzi]"
	wyjście:
		lista silnych spójnych składowych oraz ich wizualizacja na graficznej reprezentacji grafu
		oraz reprezentacja graficzna digrafu.
	W PRZYPADKU WYWOŁANIA Z KONSOLI:
		jeśli digraf bedzie dostarczony z pliku losowanie jest pomijane

ZADANIE 3 - znajdz najkrotsze sciezki od danego wierzcholka: -t 3 opcjonalnie(-f FILENAME -v VERTICES -p PLOTS)
	wejście:
		aplikacja pyta o parametry losowania w postaci "[liczba_wierzchołków] [prawdopodbieństwo_krawędzi]",
		a po wygenerowaniu digrafu, o wybranie wierzchołka z którego ma liczyć koszta
	wyjście:
		wektor kosztów dojścia do poszczególnych wierzchołków od tego podanego
		oraz reprezentacja graficzna digrafu.
	W PRZYPADKU WYWOŁANIA Z KONSOLI:
		jeśli digraf bedzie dostarczony z pliku losowanie jest pomijane,
		jeśli wierzchołek, od którego mają być liczone koszta dojścia, nie będzie dostarczony, wówczas funkcja będzie liczyła koszta dla pierwszego wierzchołka.

ZADANIE 4 - odleglosci pomiedzy wszystkimi parami wierzcholkow: -t 4 opcjonalnie(-f FILENAME -p PLOTS)
	wejście:
		aplikacja pyta o parametry losowania w postaci "[liczba_wierzchołków] [prawdopodbieństwo_krawędzi]"
	wyjście:
		macierz kosztów dojścia pomiędzy wszystkimi wierzchołków
		oraz reprezentacja graficzna digrafu.
	W PRZYPADKU WYWOŁANIA Z KONSOLI:
		jeśli digraf bedzie dostarczony z pliku losowanie jest pomijane

3. Dane wejściowe.

- podanie ścieżki do pliku:
	Plik o podanej lokalizacji powinien istnieć, w przeciwnym wypadku użytkownik zostanie poinformowany o błędzie.

- wczytywanie danych z pliku:
	W przypadku zadan 2, 3 oraz 4, podany plik powinien zawierać graf w reprezentacji macierzy sąsiedztwa.
	
	Przykłady reprezentacji akceptowalnych przez program zostały załączone do projektu.

- wprowadzanie danych z konsoli:
	
	Tam, gdzie program prosi o podanie liczby, wprowadzenie ciągu znaków czy liczb oddzielonych spacjami spowoduje natychmiastowe wyświetlenie błędu.
	W przypadku, gdy program prosi o wprowadzenie danych w celu wygenerowania losowego grafu skierowanego, liczba wierzcholków oraz wartość prawdopodobieństwa istnienia krawędzi musi być podany jako ciąg liczb oddzielony spacjami, np: 7 0.3 (gdzie 7 oznacza l. wierzchołków, 0.3 - prawdopodobieństwo).
	Wszelkie wagi połączeń są generowane automatycznie.
	
	W pozostałych zadaniach, tam, gdzie program prosi o podanie liczby, wprowadzenie ciągu znaków czy liczb oddzielonych spacjami spowoduje natychmiastowe wyświetlenie błędu.


