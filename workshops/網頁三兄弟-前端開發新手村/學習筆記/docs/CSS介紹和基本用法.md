# CSS 介紹和基本用法

CSS 的作用就是改變網頁元素的外觀，例如文字大小、顏色、邊框、粗幼度和字體類型，以及最重要的元素佈局。這裡會提及到如何使用 CSS，和正確的使用方式。

> 其中一個對我來說很重要的功能就是增加互動性，例如當游標懸掛在元素時，可以修改其元素的外觀，而游標離開後則回到原本的外觀狀態。

## CSS 聲明 - Declaration

我們可以通過一對屬性與值來去修改元素的樣式。中間會使用冒號 `:` 隔開屬性和值，最後會使用一個分號 `;` 來示意你的 CSS 聲明已經完結。

![css-declaration](./resources/css-declaration.png)

## 最直接的使用方法

還記得我們剛剛提過的元素屬性嗎？我們可以用屬性名稱 `style` 來去修改元素的樣式。例如我們想把指定的 `<p>` 元素的字體顏色改為紅色：

```html
...
    <p style="color: red">CPS Workshop</p>
...
```

又或者同時想把這句句子中的 CPS 改為藍色和粗體，我們可以用一個 `<span>` 元素去包著 CPS 然後單獨去做樣式修改：

```html
...
    <p style="color: red;"><span style="color: blue; font-weight: bold;">CPS</span> Workshop</p>
...
```

> 這樣的寫法稱為 `inline styles`，行內樣式。也就是直接在元素上利用屬性去修改 CSS。