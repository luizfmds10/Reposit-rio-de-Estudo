# 📝 Anotações de HTML & CSS — Do Dia a Dia

---

## 🏗️ HTML

---

### `<div>` e `<span>`
- **`<div>`** → bloco genérico. Ocupa a linha inteira. Usa pra agrupar seções.
- **`<span>`** → embutido (inline). Ocupa só o espaço do conteúdo. Usa pra estilizar parte de um texto.

```html
<div class="card">
  <p>Olá, meu nome é <span style="color: red;">João</span></p>
</div>
```
> O `<div>` agrupa o card inteiro, o `<span>` só pinta a palavra "João" de vermelho.

---

### Atributo `class` e `id`
- **`class`** → pode repetir em vários elementos. Usado pra estilizar grupos.
- **`id`** → único por página. Usado pra identificar um elemento específico.

```html
<p class="texto-destaque">Parágrafo 1</p>
<p class="texto-destaque">Parágrafo 2</p>
<h1 id="titulo-principal">Título Único</h1>
```
> No CSS, `class` vira `.texto-destaque` e `id` vira `#titulo-principal`.

---

### Atributo `style` (inline)
Aplica CSS direto no elemento, sem precisar de arquivo externo. Útil pra ajustes rápidos, mas evite abusar.

```html
<p style="color: blue; font-size: 18px;">Texto azul e grande</p>
```

---

### `<a>` — Links
Cria um link. O `href` define o destino. O `target="_blank"` abre em nova aba.

```html
<a href="https://google.com" target="_blank">Ir pro Google</a>
```

---

### `<img>` — Imagens
Exibe uma imagem. `src` é o caminho, `alt` é o texto alternativo (acessibilidade + SEO).

```html
<img src="foto.jpg" alt="Foto de perfil" width="200">
```

---

### `<ul>`, `<ol>`, `<li>` — Listas
- **`<ul>`** → lista sem ordem (bolinhas)
- **`<ol>`** → lista ordenada (números)
- **`<li>`** → cada item da lista

```html
<ul>
  <li>HTML</li>
  <li>CSS</li>
</ul>

<ol>
  <li>Primeiro</li>
  <li>Segundo</li>
</ol>
```

---

### `<input>` e `<button>`
- **`<input>`** → campo de texto, checkbox, etc. O `type` define o tipo.
- **`<button>`** → botão clicável.

```html
<input type="text" placeholder="Digite seu nome">
<input type="checkbox"> Aceito os termos
<button>Enviar</button>
```

---

### `data-*` — Atributos personalizados
Guarda informação extra num elemento HTML. Muito usado com JavaScript.

```html
<button data-id="42" data-acao="deletar">Deletar</button>
```
> No JS: `btn.dataset.id` retorna `"42"`.

---

## 🎨 CSS

---

### Seletores básicos
- `.classe` → seleciona por classe
- `#id` → seleciona por ID
- `elemento` → seleciona a tag diretamente
- `pai filho` → seleciona filho dentro do pai

```css
p { color: gray; }           /* toda tag <p> */
.card { border: 1px solid; } /* todo elemento com class="card" */
#titulo { font-size: 32px; } /* o elemento com id="titulo" */
.card p { margin: 0; }       /* <p> que estiver dentro de .card */
```

---

### `display`
Define como o elemento se comporta no layout.

- `block` → ocupa a linha inteira
- `inline` → fica na mesma linha, sem aceitar width/height
- `inline-block` → fica na mesma linha, mas aceita width/height
- `none` → some da tela (e do fluxo)
- `flex` → ativa o Flexbox
- `grid` → ativa o Grid

```css
.menu-item {
  display: inline-block;
  width: 100px;
}
```

---

### `position`
Controla onde o elemento fica na página.

- `static` → padrão, segue o fluxo normal
- `relative` → se move em relação a onde estava
- `absolute` → se posiciona em relação ao pai com `position: relative`
- `fixed` → fica fixo na tela mesmo rolando a página
- `sticky` → fica no lugar até chegar num ponto de rolagem

```css
/* Botão flutuante no canto inferior direito */
.btn-flutuante {
  position: fixed;
  bottom: 20px;
  right: 20px;
}
```

---

### `flexbox` — Flex Container
Ativa com `display: flex` no pai. Organiza os filhos em linha ou coluna.

- `flex-direction` → `row` (padrão) ou `column`
- `justify-content` → alinha no eixo principal (horizontal no row)
- `align-items` → alinha no eixo cruzado (vertical no row)
- `gap` → espaço entre os filhos

```css
.container {
  display: flex;
  justify-content: center;  /* centraliza na horizontal */
  align-items: center;      /* centraliza na vertical */
  gap: 16px;
}
```
> Os filhos de `.container` ficam centralizados com 16px de espaço entre eles.

---

### `box model` — margin, padding, border
Todo elemento é uma caixa. Da fora pra dentro:

- **`margin`** → espaço fora do elemento
- **`border`** → borda do elemento
- **`padding`** → espaço interno (entre conteúdo e borda)

```css
.card {
  margin: 20px;           /* afasta de outros elementos */
  border: 2px solid #ccc; /* borda cinza */
  padding: 16px;          /* espaço interno */
}
```

---

### `box-sizing: border-box`
Faz o `width` incluir o padding e a borda. Muito mais previsível. Coloque no `*` do projeto.

```css
* {
  box-sizing: border-box;
}
```
> Sem isso, um elemento com `width: 200px` e `padding: 20px` ficaria com 240px de largura total.

---

### `:hover`
Aplica estilo quando o mouse passa por cima do elemento.

```css
.botao {
  background-color: blue;
  color: white;
}

.botao:hover {
  background-color: darkblue; /* escurece ao passar o mouse */
}
```

---

### `:focus`
Aplica estilo quando o elemento está selecionado (ex: campo de input clicado).

```css
input:focus {
  outline: none;
  border: 2px solid blue;
}
```

---

### `:nth-child()`
Seleciona um filho específico dentro do pai.

```css
li:nth-child(1)  { color: gold; }   /* primeiro item */
li:nth-child(2n) { color: gray; }   /* itens pares */
li:last-child    { font-weight: bold; } /* último item */
```

---

### `transition`
Suaviza a mudança de uma propriedade CSS. Formato: `propriedade duração timing`.

```css
.botao {
  background-color: blue;
  transition: background-color 0.3s ease;
}

.botao:hover {
  background-color: darkblue; /* muda suavemente em 0.3s */
}
```

---

## 🧩 HTML semântico

### Tag semântica básica
- **`<header>`** → cabeçalho da página ou seção
- **`<nav>`** → área de navegação
- **`<main>`** → conteúdo principal
- **`<section>`** → seção com tema próprio
- **`<article>`** → conteúdo independente
- **`<footer>`** → rodapé

```html
<header>
  <nav>Menu</nav>
</header>
<main>
  <section>Conteúdo principal</section>
</main>
<footer>Rodapé</footer>
```

> Usar tags semânticas deixa o HTML mais legível e melhora a acessibilidade.

---

## 🧾 Formulários importantes

- **`<label>`** deve sempre estar associado ao campo com `for="id"`
- **`type="email"`** e **`type="tel"`** ajudam o teclado do celular
- **`required`** obriga o preenchimento no navegador
- **`placeholder`** é uma dica, não substitui a label

```html
<label for="nome">Nome</label>
<input type="text" id="nome" name="nome" required>
<label for="email">Email</label>
<input type="email" id="email" name="email" placeholder="seu@email.com">
```

---

## 🎯 CSS que aparece no dia a dia

### CSS Variables
Permitem reutilizar valores e mudar tema com facilidade.

```css
:root {
  --cor-primaria: blueviolet;
  --espacamento: 16px;
}
.botao {
  background: var(--cor-primaria);
  padding: var(--espacamento);
}
```

### Responsividade com media query
Ajusta layout em telas menores.

```css
@media (max-width: 600px) {
  .container {
    flex-direction: column;
  }
}
```

### Cores e fundo
- `background-color` define cor
- `background-image` pode usar gradiente
- `background-size: cover` faz a imagem cobrir a área

```css
.hero {
  background: linear-gradient(135deg, #667eea, #764ba2);
  color: white;
}
```

### Posicionamento e `z-index`
- `position: relative` mantém no fluxo
- `position: absolute` remove do fluxo e posiciona dentro do pai relativo
- `z-index` controla sobreposição

```css
.card {
  position: relative;
  z-index: 1;
}
.dropdown {
  position: absolute;
  top: 100%;
  left: 0;
  z-index: 10;
}
```

### `overflow`
Controla o que acontece quando o conteúdo passa do tamanho do elemento.
- `visible` → mostra tudo
- `hidden` → esconde o que ultrapassa
- `scroll` / `auto` → adiciona scroll

```css
.caixa {
  width: 300px;
  height: 150px;
  overflow: auto;
}
```

### Atalhos úteis de CSS
- `margin: 0 auto;` centraliza horizontalmente quando há `width`
- `padding: 1rem 2rem;` define espaço vertical e horizontal
- `border-radius: 8px;` arredonda cantos
- `cursor: pointer;` em botões e links clicáveis

```css
.botao {
  cursor: pointer;
  border-radius: 10px;
}
```

---

## ✅ Dicas rápidas para o dia a dia

- prefira usar **classes** em vez de estilos inline
- coloque o `alt` em todas as imagens
- use `label` para melhorar a acessibilidade dos formulários
- mantenha um `reset` ou `normalize` básico para evitar diferenças entre navegadores
- teste sempre em celular e desktop


---

### `transform`
Aplica transformações visuais sem afetar o layout.

- `scale(1.1)` → aumenta 10%
- `translateX(10px)` → move pra direita
- `rotate(45deg)` → rotaciona

```css
.card:hover {
  transform: scale(1.05); /* cresce levemente ao hover */
}
```

---

### `opacity` e `visibility`
- **`opacity: 0`** → invisível, mas ainda ocupa espaço e pode receber clique
- **`visibility: hidden`** → invisível, ocupa espaço, mas não recebe clique
- **`display: none`** → some completamente

```css
.fantasma {
  opacity: 0.3; /* transparente mas presente */
}
```

---

### `overflow`
Controla o que acontece quando o conteúdo é maior que o elemento.

- `visible` → padrão, vaza pra fora
- `hidden` → corta o conteúdo que sobra
- `scroll` → sempre mostra a barra de rolagem
- `auto` → barra só quando necessário

```css
.caixa {
  width: 200px;
  height: 100px;
  overflow: hidden; /* texto longo é cortado */
}
```

---

### `z-index`
Define qual elemento fica na frente quando dois se sobrepõem. Só funciona em elementos com `position` diferente de `static`.

```css
.modal {
  position: fixed;
  z-index: 1000; /* fica na frente de tudo */
}

.overlay {
  position: fixed;
  z-index: 999; /* fica atrás do modal */
}
```

---

### `@media query` — Responsividade
Aplica estilos diferentes dependendo do tamanho da tela.

```css
/* Estilo padrão (desktop) */
.container {
  width: 1200px;
}

/* Quando a tela for menor que 768px (celular) */
@media (max-width: 768px) {
  .container {
    width: 100%;
    padding: 16px;
  }
}
```

---

### Variáveis CSS (`--variavel`)
Define valores reutilizáveis. Declaradas no `:root` pra serem globais.

```css
:root {
  --cor-primaria: #3b82f6;
  --espacamento: 16px;
}

.botao {
  background-color: var(--cor-primaria);
  padding: var(--espacamento);
}
```
> Mudar `--cor-primaria` no `:root` já atualiza em todos os lugares.

---

### `cursor`
Muda o ícone do mouse sobre o elemento.

```css
.botao  { cursor: pointer; }    /* mãozinha */
.loading { cursor: wait; }      /* ampulheta */
.proibido { cursor: not-allowed; } /* círculo riscado */
```

---

### `text-overflow: ellipsis`
Corta texto longo com `...`. Precisa de `overflow: hidden` e `white-space: nowrap` juntos.

```css
.titulo-curto {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  width: 200px;
}
```
> "Nome muito longo que não cabe" vira "Nome muito longo que..."

---

*Arquivo gerado como guia de consulta rápida — HTML & CSS do dia a dia.*
