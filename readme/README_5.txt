1. Uruchomienie programu

Lista dostępnych parametrów wywołania:

usage: main5.py [-h] [-N LAYERS]

optional arguments:
  -h, --help            show this help message and exit
  -N LAYERS, --layers LAYERS
                        number of layers between source and target vertices


Wywołanie bezparametrowe "python main3.py" spowoduje tradycyjne uruchomienie się aplikacji konsolowej.

2. Dane wejściowe.

- wprowadzanie danych z konsoli:
	Zarówno w wersji konsolowej jak i w przypadku wywołania parametrowego, wymagane jest, aby użytkownik
	wprowadził liczbę warstw sieci (wprowadzenie łańcuchu znaków, liczb oddzielonych spacjiami, itp. spowoduje 
	wyświetlenie odpowiedniego komunikatu o błędzie).

3. Dane wyjściowe.

Po wprowadzeniu danych wygenerowana zostanie graficzna reprezentacja sieci przeplywu wraz z jej przepustowoscia, 
a w konsoli zostanie wyświetlona wartość maksymalnego przepływu w sieci.

	
