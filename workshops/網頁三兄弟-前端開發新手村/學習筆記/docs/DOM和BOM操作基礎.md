# DOM和BOM操作基礎

DOM（Document Object Model）和 BOM（Browser Object Model）是兩個非常重要的概念，我們會在這個環節中介紹他們的作用以及相關的操作方法。

## DOM - Document Object Model

`DOM` 是一個以 `JavaScript Object` 來表示 `HTML` 樹狀文件結構的模型，它是我們可以利用 JavaScript 來操控 HTML 元素的關鍵。可以想像整個文檔是一個物件變量，當中的每一的元素都視為一個物件。而每一個元素物件都有內置的屬性和函數讓我們使用，這樣我們就可以通過這種方式去修改元素物件的屬性、樣式等的數值。

> 例如我們可以通過 `DOM` 去獲取指定的容器元素，再去添加子元素進去這個容器。這就是大部分利用網絡獲取後，顯示這些資料在螢幕上的方式。

`document` 物件就是我們上述提到 DOM 在 JS 中的變量名稱，這是一個全局的變量。意思就是我們可以在不同的 JS 文檔、函數、所有的區域都可以使用這個變量。我們可以通過 `(.) dot notation` 的方式去使用這個物件變量的屬性和函數。

### 使用方式

我們可以先試一下獲取一個 `<h1>` 元素，然後去修改它展示的值。要去獲取一個元素甚至是多個元素，我們可以通過以下比較常見的方式去獲取：

```js
const title = document.getElementById("title"); // 通過元素的 id 屬性去獲取指定元素（一個）
const pTag = document.querySelector("p"); // 通過元素的標籤名去獲取元素（按文檔順序的第一個）
const card = document.querySelector(".card"); // 通過元素的 class 屬性去獲取指定元素（按文檔順序的第一個）

const pTags = document.querySelectorAll("p"); // 通過元素的標籤名去獲取元素（把文檔中所有的 p 元素獲取）
const cards = document.querySelectorAll(".card"); // 通過元素的 class 屬性去獲取指定元素（把文檔中所有含有 .card class 的元素獲取）
```

> `document.querySelectorAll()` 就是利用 CSS Selector 的機制去獲取元素。

獲取一個 `<h1>` 元素，然後去修改它展示的值：

```html
<h1>Testing</h1>
```

```js
const h1Element = document.getElementById("title");
h1Element.innerHTML = "H1 Changed By JS";
```

我們會在瀏覽器中看到 `<h1>` 元素的值已經被 JS 改為 `"H1 Changed By JS"`。這個大概就是我們可以通過 DOM 去修改 HTML 文檔中的元素的效果。

## BOM - Browser Object Model

`BOM` 是一組由瀏覽器提供的接口，由不同個別的物件變量提供瀏覽器的服務。例如我們一直在使用開發者工具中的 `console` 頁面，這個也是 `BOM` 的一種、還有向伺服器發送網絡請求的功能、取得瀏覽器目前網址等等。另外還有很多的 API（接口、也就是不同的物件變量）供我們使用。

### 進行網絡請求

我們將會在這個部分學習如何通過 `BOM API / Web API` 向我們電腦學會的伺服器進行網絡請求，這些資料將會用於我們後面實作的項目。

我們會使用內置的 `fetch()` 函數去進行獲取資料的動作。由於 `fetch()` 函數主要可使用兩種方式，我們會使用較容易的方案去做，因為較難的方式牽涉到同步於非同步的概念，可能需要有一定基礎才容易理解。

```js
// fetch() 函數的第一個參數是 url，想要請求的網址。
// 由於網絡請求需要時間來處理，JS 引擎會跳過並先執行後續的指令。
// 這樣就可以在等待伺服器回應的過程中做其他事情，
// 然後我們需要通過 .then() 的鏈式函數去利用請求回來的數據。

fetch("https://catfact.ninja/fact") 
    .then(function(res) {
        return res.json();
    })
    .then(function(result) {
        console.log(result);
        console.log("Fact: ", result.fact);
        console.log("Length: ", result.length)
    });
```

> 如果出現報錯時可以先在瀏覽器中前往 API 的網址看看有沒有回應先。

```js
const API_URL = "https://backend.cpsumsu.org/api/events";

fetch(API_URL)
    .then(function(res) {
        return res.json();
    })
    .then(function(result) {
        console.log(result);
        console.log(result.data);
    })
```