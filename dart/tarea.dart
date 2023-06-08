import 'dart:io';

void main() {
  // Solicitar el tamaño de la lista
  print("Ingrese el tamaño de la lista:");
  int size = int.parse(stdin.readLineSync()!);

  // Crear la lista vacía
  List<int> lista = [];

  // Solicitar los elementos de la lista
  for (int i = 0; i < size; i++) {
    int elemento;
    do {
      print("Ingrese el elemento ${i + 1}:");
      elemento = int.parse(stdin.readLineSync()!);
    } while (elemento <= 0); // Verificar que sea un número entero positivo

    lista.add(elemento);
  }

  // Ordenar la lista ascendente y descendentemente
  ordenarAscendente(lista);
  ordenarDescendente(lista);

  // Imprimir la lista ordenada
  print("Lista ordenada ascendentemente: $lista");
  lista = lista.reversed.toList();
  print("Lista ordenada descendentemente: $lista");
}

void ordenarAscendente(List<int> lista) {
  for (int i = 0; i < lista.length - 1; i++) {
    for (int j = 0; j < lista.length - i - 1; j++) {
      if (lista[j] > lista[j + 1]) {
        int temp = lista[j];
        lista[j] = lista[j + 1];
        lista[j + 1] = temp;
      }
    }
  }
}

void ordenarDescendente(List<int> lista) {
  for (int i = 0; i < lista.length - 1; i++) {
    for (int j = 0; j < lista.length - i - 1; j++) {
      if (lista[j] < lista[j + 1]) {
        int temp = lista[j];
        lista[j] = lista[j + 1];
        lista[j + 1] = temp;
      }
    }
  }
}
