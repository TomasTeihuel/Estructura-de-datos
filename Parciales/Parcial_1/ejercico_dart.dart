import 'dart:math';

void main() {
  List<int> numerosr = List.generate(5, (_) => Random().nextInt(10) + 1);
  print(numerosr);
}
