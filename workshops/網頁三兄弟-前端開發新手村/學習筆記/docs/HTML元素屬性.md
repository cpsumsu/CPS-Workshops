# HTML元素屬性

屬性是 HTML 元素中額外的信息，其作用就是更詳細地描述其元素。屬性的形式會以鍵值對來表示，也就是一個屬性的名稱和其數值。而每一個元素都可以擁有多於一個元素。

```html
<h1 class="heading" id="title">澳大電腦學會</h1>
```

`class` 和 `id` 屬性主要是用於 CSS 中指定特定元素進行樣色修改。除此之外，我們也可以通過這兩個元素的名稱在 JS 中獲取擁有相同 `class` 名稱的元素。我們可以在後續的 CSS 和 JS 環節中會看到他們作用。

另外一個我們現在可以理解的例子是連結和圖片：

```html
<a href="www.google.com">Google</a>
```

`href` 的全稱是 Hypertext Reference，翻譯大概是超文本鏈接。是用於把當前的元素連結到其他的頁面上。以上面的代碼為例，連結可以通往 Google 的頁面。

```html
<img src="google-icon.png" alt="A Google Icon" width="100px" height="100px">
```

`src` 的全稱是 Source，也就是圖片元素的資源路徑。我們需要把想展示的圖片的檔案路徑和名稱放在這裡。
`alt` 的全稱是 Alternate Text，當圖片路徑錯誤或以其他因素不能顯示時，頁面上就會顯示 `alt` 的值以代替圖片的空缺。
`width` 和 `height` 則是用於修改圖片的大小。`px` 這個單位我們後面會再提到的。