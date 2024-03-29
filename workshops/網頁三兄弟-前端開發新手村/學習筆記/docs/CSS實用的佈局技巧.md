# CSS實用的佈局技巧

我們前面有提到過容器，但是都沒有更詳細的介紹它的用法。是時候學習容器的真正用處了！

> 此章節的圖片來源於 `css-tricks.com` 的[這篇文章](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)。

## 容器的作用

容器是我們寫 CSS 時可以操縱多個元素佈局的重要基石。瀏覽器就是按照元素是 `inline` 或是 `block` 的預設定位來去安排每一個元素的順序。我們可以通過 CSS 屬性（例如 `flex`、`grid`），把一個容器內的所有元素都追隨著特定的佈局或是順序。

> 也就是說不管元素原本是 `inline` 或是 `block` 元素，只要它的父容器設定了上述提到的屬性就會按照你指定的方式來排佈。

## Flexbox 佈局

因為時長關係本次工作坊只會學習 `flex` 的用法。在佈局方面，`grid` 也是很好用的，可以排出更加有規律的佈局。

首先要把一個容器（容器其實就是元素，只不過用於形容裝著元素的元素）變成 flex，我們需要以下的聲明：

```css
.flex-container {
    display: flex;
}
```

這個時候就會發現容器內的元素已經被改變了預設的佈局方式，而全部元素都是預設往右邊一行來順序：

![flex-direction](./resources/flex-direction.png)

預設的語法是這樣的：

```css
.flex-container {
    flex-direction: row;
}
```

## 橫坐標 / Main Axis For flex-direction: row

這個時候我們就具備了改變 flex 元素佈局的能力，我們可以在接下來的環節中從縱坐標（Y軸）和橫坐標（X軸）控制元素的排佈。

![justify-content](./resources/justify-content.png)

`justify-content` 會通過容器最大的寬度去分配容器內元素的位置，我們可以通過圖片中的 6 種方式去控制。

## 橫坐標 / Cross Axis For flex-direction: row

橫坐標的屬性是 `align-content` 跟 `justify-content` 大致上都是一樣的，只是由主軸轉成橫軸和其中一個值不一樣。我們可以從下方的圖片看到他們的分別：

![align-content](./resources/align-content.png)

## 練習

我們可以通過一些網上的小遊戲去學習 `flexbox` 佈局的用法，這是一個挺有趣的遊戲（[網址](https://flexboxfroggy.com/)）。

還可以準備本次工作坊要實作的項目的 header 部分。