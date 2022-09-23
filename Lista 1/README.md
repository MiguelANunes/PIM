# Lista de exercícios para prova 1

1. Para se descobrir o tamanho em pixels de uma imagem gerada na saída de um sesnor monocromático dada a sua área de amostragem, deve-se **multiplicar a área de amostragem pela resolução do sensor**. Por exemplo, se a área de amostragem for 1 cm² e a resolução do sensor for 1000 pixels/cm², então o tamanho da imagem gerada será de 1 cm² x 1000 pixels/cm² = 1000 pixels.

No exercício temos:

- Área de amostragem: 2 cm x 3 cm = 6 cm²
- 1 pixel: 0.1mm x 0.2mm = 0.02 mm² = 0,0002 cm²
- x - 6
- 1 - 0,0002
- x = 6 / 0,0002 = **30000 pixels**

---

2. Sim, é possível. Utilizanado um arquivo PPM (formato de texto para armazenar informações sobre uma determinada imagem), é possível notar o seguinte cabeçalho:

   > P6
   > i j
   > k

Onde i e j representam respectivamente a largura e a altura em pixels da imagem, e k representa o valor máximo da escala de tons. Abaixo do cabeçalho seguem valores que representam cada pixel. Cada tripla de valores representa um único pixel, e cada valor da tripla representa o intensidade de cada canal na ordem Vermelho, Verde e Azul.

Aplicando o método da combinação linear, é possível obter a cor de cada pixel. Para isso, basta multiplicar cada valor da tripla pelo valor máximo da escala de tons, e dividir o resultado por 255. O resultado será um valor entre 0 e 1, que representa a intensidade de cada canal. Para obter a cor final, basta somar os valores de cada canal e dividir o resultado por 3.

---

3. A profundidade de bits é o que quantifica quantas cores únicas estão disponíveis na paleta de cores de uma imagem em termos de número de 0's e 1's, ou 'bits', que são utilizados para especificar cada cor. Isso não significa que uma imagem necessariamente utiliza todas essas cores, mas sim que pode especificar suas cores usando esse nível de precisão. Para uma imagem em tons de cinza, a profundidade de bits quantifica quantas gradações únicas de cinza estão disponíveis. Imagens com profundidades de bit maiores podem representar mais tons ou cores já que há mais combinações de 0's e 1's disponíveis para representá-las.

A. Como só há dois valores de intensidades luminosas diferentes, a imagem é binária, ou seja, possui apenas duas cores. Logo, a profundidade de bits é 1.

B. Como há 18 valores de intensidades com pouquíssima variação entre si, utilizaria uma profundidade de bits de 8 para que todos os valores fossem bem representados.

---

4. As diferenças entre **sensores CCD** e **sensores CMOS** baseia-se no tipo de estrutura do sensor. Os sensores CCD são baseados em um cristal de silício, enquanto os sensores CMOS são baseados em um circuito integrado. Os sensores CCD são mais sensíveis à luz, mas são mais caros e mais difíceis de serem fabricados. Os sensores CMOS são mais baratos e mais fáceis de serem fabricados, mas são menos sensíveis à luz. Os sensores CCD são mais utilizados em câmeras de vídeo, enquanto os sensores CMOS são mais utilizados em câmeras digitais.

---

5. **Global Shutter Timing** é um método de captura de imagens que captura todas as linhas da imagem ao mesmo tempo. **Rolling Shutter Timing** é um método de captura de imagens que captura as linhas da imagem de forma sequencial, ou seja, uma linha por vez. Sabendo disso, é possível notar que o método Rolling Shutter Timing é mais adequado para capturar imagens de movimento, pois ele captura as linhas de forma sequencial, enquanto o método Global Shutter Timing captura todas as linhas ao mesmo tempo, o que pode gerar distorções na imagem.
   **A.** Rolling Shutter Timing
   **B.** Global Shutter Timing

---

6. A relação entre resolução espacial de uma imagem e o desemepnho computacional do processamento de imagens é que **quanto maior a resolução espacial da imagem, maior será o desempenho computacional necessário para processá-la**. Isso ocorre porque _quanto maior a resolução espacial da imagem, maior será o número de pixels que precisarão ser processados_. Por exemplo, uma imagem com resolução espacial de 1000 x 1000 pixels precisará de um desempenho computacional maior do que uma imagem com resolução espacial de 500 x 500 pixels.

---

7. Para estimar a distância do prédio em relação à câmera pelo modelo de câmera pinhole, deve-se **multiplicar a distância focal pela altura do prédio**. Por exemplo, se a distância focal for 50 mm e a altura do prédio for 10 m, então a distância do prédio em relação à câmera será de 50 mm x 10 m = 500 mm.

Portanto, 27 m \* 5 mm = 0.135 m = 13.5cm

---

8. Uma estratégia simples e barata para determinação automática da cor do carro baseada na aquisição de imagens é a seguinte: **determinar a cor predominante da imagem, e então comparar essa cor com as cores de referência**. Para isso, basta utilizar o método da combinação linear para obter a cor de cada pixel, e então contar quantas vezes cada cor aparece na imagem. A cor predominante será a cor que aparecer mais vezes na imagem.

---

9. **A.** area = lado_ac \* lado_ab: 14.46 pixels quadrados || 0.04cm \* 0.01cm = 0.0004cm² = 0.04mm²

   **B.**
   projeções dos pontos em mm
   a = [2.17, 6.67]
   b = [2.18, 6.67]
   c = [2.17, 6.63]
   d = [2.18, 6.63]
   e = [2.15, 1.67]
   f = [2.15, 1.67]
   g = [2.15, 1.67]
   h = [2.15, 1.67]

dist entre 'a' e 'b' em pixels [dist_horizontal, dist_vertical]=[1.00, 0.00]

dist entre 'a' e 'c' em pixels [dist_horizontal, dist_vertical]=[0.00, 4.00]

dist entre 'c' e 'd' em pixels [dist_horizontal, dist_vertical]=[1.00, 0.00]

dist entre 'e' e 'f' em pixels [dist_horizontal, dist_vertical]=[0.00, 0.00]

dist entre 'e' e 'g' em pixels [dist_horizontal, dist_vertical]=[0.00, 0.00]

**C.** A escolha seria o sensor **S1**, porque com um tamanho menor dos quadrados dos pixels, a resolução espacial da imagem será maior e portanto conseguiremos mais detalhes da imagem, que é o objetivo da análise.

---

10. As operações **ariméticas** entre imagens são operações de arranjo matricial; ou seja, são realizadas entre pares de pixels correspondentes.

**SOMA.** s(x,y) = f(x,y) **+** g(x,y)
**SUBTRAÇÃO.** t(x,y) = f(x,y) **-** g(x,y)
**MULTIPLICAÇÃO.** u(x,y) = f(x,y) **X** g(x,y)
**DIVISÃO.** v(x,y) = f(x,y) **/** g(x,y)

- Adição de imagens ruidosas para a redução de ruídos;
- Subtração de imagens para realce de diferenças;
- Multiplicação e divisão de imagens para correção de sombreamento;

As operações **lógicas** são utilizadas em imagens binárias, tratando pixels em grupos de frente (valor 1) e de fundo (valor 0). Ao lidar com imagens binárias, refere-se a união, interseção e complemento como as operações lógicas (or, and, not).

- Operações lógicas entre imagens são amplamente utilizadas em morfologia de imagens, que é uma área da processamento de imagens que visa a extração de informações de imagens binárias.

---

11. _11.py_

---

12. Os três métodos são utilizados para a escolha e localização de um limiar. O limiar de imagem, que extrai o objeto de seu fundo de uma imagem, é uma das aplicações mais comuns na análise de imagens. Em geral, o limiar está localizado no vale óbvio e profundo no histograma de frequências. No entanto, surgem problemas quando o vale não é tão óbvio ou quando o histograma é unimodal.

**Método manual:** Esta forma simples consiste em encontrar cada um dos picos do histograma de frequências e depois os vales entre eles.

**Algoritmo IsoData:** Esta técnica iterativa simples é feita por uma estimativa de um valor possível para o limiar. A partir disso, são calculados os valores médios dos pixels nas duas categorias (objetos e fundo) produzidos a partir desse limiar. O limiar é reposicionado para ficar exatamente na metade do caminho entre as duas médias. Os valores médios são calculados novamente e um novo limite é obtido, e assim por diante até que o limite pare de mudar de valor.

**Método de Otsu:** Ele é baseado em análise discriminante e maximiza a variância entre classes do histograma GL para fornecer a melhor separação de classes.
Deixe que os pixels de uma dada imagem sejam representados em L níveis de cinza [0,1,2,...,L - 1]. O número de pixels no nível i é denotado por h(i) e o número total de pixels por N. O histograma de nível de cinza é normalizado e considerado como uma distribuição de probabilidade.
