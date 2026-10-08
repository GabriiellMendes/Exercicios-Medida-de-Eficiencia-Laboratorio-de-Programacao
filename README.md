# Laboratório de Programação - Python

Lista com 80 exercícios de Python da disciplina Laboratório de Programação (Profª Ma. Layse Souza).
Cada questão está na pasta `ME Python`, em um arquivo com o número dela (`ATV01.py` até `ATV80.py`).

Para rodar uma questão:

```
python "ME Python/ATV01.py"
```

## Resumo das questões

### Entrada, saída e cálculos básicos
1. Guardar em uma variável a quantidade de livros lidos pela turma vencedora e exibir uma mensagem.
2. Ler o nome do estudante e exibir uma mensagem de boas-vindas personalizada.
3. Ler a produção de hortaliças de dois setores e exibir o total do dia.
4. Ler duas notas e calcular a média do estudante.

### Condicionais
5. Ler o valor da compra e informar se o cliente tem direito ao desconto (compras a partir de R$ 500,00).
6. Ler o código de um equipamento e informar se é par ou ímpar.

### Repetição
7. Exibir os assentos de um ônibus, de 1 a 20.
8. Ler as quantidades arrecadadas por 5 voluntários e calcular o total.

### Listas e tuplas
9. Ler três títulos de livros, guardar em uma lista e exibir.
10. Criar uma tupla com os dias da semana e exibir o primeiro.

### Mais condicionais
11. Ler a média final do estudante e informar se pode participar da seleção de bolsas (média a partir de 8,0).
12. Ler a velocidade de um veículo e informar se ultrapassou o limite de 80 km/h.
13. Ler o consumo de energia de dois setores e informar o maior.

### Laços de repetição
14. Exibir os números de 1 até 50.
15. Exibir os números de 1 a 15.
16. Exibir a contagem regressiva de 10 até 1.
17. Ler as quantidades de cestas básicas de 10 voluntários e informar o total.
18. Ler as vendas de 7 dias e apresentar o faturamento da semana.
19. Ler um inteiro positivo e calcular o fatorial.
20. Somar os valores digitados até o usuário digitar 0.

### Listas
21. Receber o nome de 5 produtos, guardar em uma lista e exibir a lista completa.
22. Guardar notas em uma lista e exibir a maior.
23. Calcular a soma dos valores de uma lista de gastos.
24. Inverter uma lista.
25. Determinar a quantidade de elementos de uma lista.
26. Verificar se um código está presente em uma lista.

### Tuplas
27. Criar uma tupla com os meses do ano e exibir todos os elementos.
28. Guardar 4 temperaturas em uma tupla e calcular a soma.
29. Guardar vendas em uma tupla e exibir o maior valor.
30. Exibir o último elemento de uma tupla com os dias letivos.

### Dicionários
31. Criar um dicionário com nome, idade e setor de um funcionário e exibir os dados.
32. Criar um dicionário só com o nome do paciente e depois adicionar a idade.
33. Exibir todas as chaves de um dicionário de livro.
34. Consultar a nota de um estudante a partir do nome informado.
35. Cadastrar 3 produtos com suas quantidades em um dicionário e exibir o conteúdo.

### Números aleatórios
36. Gerar um número aleatório entre 1 e 50.
37. Simular o lançamento de um dado de seis faces.
38. Escolher um livro aleatoriamente em uma lista.
39. Sortear um número entre 1 e 10 e informar se o usuário acertou.
40. Jogo de adivinhação em que o sistema diz se o número procurado é maior ou menor após cada erro.

### Matrizes
41. Construir uma matriz 2x2 e exibir seus valores.
42. Calcular a soma de todos os valores de uma matriz.
43. Encontrar o maior valor de uma matriz.
44. Encontrar o menor valor de uma matriz.
45. Exibir os elementos da diagonal principal de uma matriz quadrada.
46. Calcular a soma dos elementos da diagonal principal.
47. Contar quantos valores positivos existem em uma matriz.
48. Gerar a matriz identidade de ordem 3.

### Problemas combinados
49. Cadastrar 5 alunos (nome e nota) em um dicionário e exibir todos os registros.
50. Cadastrar 5 alunos e notas, exibir a média da turma e os alunos aprovados (nota a partir de 7,0).
51. Ler 5 temperaturas de uma estufa, calcular a média, informar se está na faixa ideal (18°C a 28°C) e exibir as temperaturas.
52. Cadastrar 5 medicamentos com a quantidade em estoque e consultar um medicamento informado.
53. Sortear o líder de uma equipe entre Ana, Carlos, Pedro, Beatriz e Maria.
54. Analisar uma matriz 3x3 de vagas de estacionamento e contar as ocupadas e as livres.
55. Guardar as disciplinas em uma tupla e os alunos (nome, nota de Matemática e de Português) em um dicionário; calcular a média, informar Aprovado ou Reprovado (média a partir de 7,0) e exibir as disciplinas.
56. Calcular quantos grãos de trigo o monge esperava receber no tabuleiro de xadrez de 64 casas, dobrando a cada casa.

### Funções
57. Função que recebe uma string e um caractere e mostra quantas vezes o caractere aparece.
58. Função que calcula e exibe a gorjeta de 10% do valor da conta.
59. Função que retorna o menor de dois números se ambos forem pares e o maior se um ou ambos forem ímpares.
60. Função que converte temperatura de ºF para ºC.
61. Função que inverte cinco strings dadas.
62. Função que verifica se um número é perfeito.
63. Programa com três funções: ler 5 números reais, retornar o maior e retornar o menor.
64. Função que soma três inteiros entre 1 e 11 com as regras do limite de 21 (reduz 10 se houver 11 e retorna -1 se ainda passar de 21).
65. Funções `calcularCubo` e `calcularDivisaoCubo` (só calcula o cubo se o número for divisível por 3).
66. Função que descobre quantas galinhas e quantos coelhos Seu Chico tem, sabendo que são 35 cabeças e 94 pernas.

### Tratamento de exceções
67. Ler a idade com `while True` e `try/except`, repetindo até receber um valor válido.
68. Dividir o lucro entre N acionistas tratando `ZeroDivisionError` e `ValueError`.
69. Abrir o arquivo `relatorio_vendas.txt` tratando `FileNotFoundError` e usando `finally`.
70. Função que busca a permissão de um perfil tratando `KeyError` e `IndexError`, retornando `acesso_restrito`.
71. Criar a exceção `SaldoInsuficienteError` e lançá-la em um saque acima do saldo.
72. Função `parse_cpf` que lança `ValueError` e deixa o erro chegar até a função `main`.
73. Aplicar 10% de desconto em preços lidos como texto, usando o bloco `else` do `try`.
74. Simular a rota `/produto/<id>` retornando status 404 (não encontrado) e 500 (erro inesperado).
75. Simular uma conexão instável com até 3 tentativas em caso de `ConnectionError`.
76. Processar uma lista tratando `TypeError` e `ValueError` no mesmo `except` e registrando o erro com `traceback`.
77. Função `realizar_saque` com validação de valor e de saldo.
78. Função `calcular_media` com notas de 0 a 10, tratamento de entradas inválidas e situação do aluno.
79. Função `cadastrar_produto` validando nome, preço e quantidade.
80. Sistema de vendas de uma loja virtual com exceções próprias, validação, relatório (total de vendas, produto mais vendido, faturamento e ticket médio) e gravação em `vendas.txt` e `log_erros.txt`.
