function contarA(texto) {
    const textoMinusculo = texto.toLowerCase();
  
    const contagem = textoMinusculo.split('a').length - 1;
  
    return contagem;
  }
  
  // Exemplo
  const frase = "Olá, mundo! Como você está hoje?";
  const resultado = contarA(frase);
  console.log(`A letra 'a' aparece ${resultado} vezes na frase.`);