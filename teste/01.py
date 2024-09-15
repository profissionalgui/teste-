function pertenceFibonacci(num) {
  let a = 0, b = 1;
  while (b < num) {
    [a, b] = [b, a + b];
  }
  return b === num;
}

// Entrada do número
const numero = parseInt(prompt("Digite um número: "));

if (pertenceFibonacci(numero)) {
  console.log(`O número ${numero} pertence à sequência de Fibonacci.`);
} else {
  console.log(`O número ${numero} não pertence à sequência de Fibonacci.`);   

}