# CSS選擇器

由於網頁元素在同一網站下大多都採取相同的樣式和佈局，所以我們並不需要把每一個元素都單獨進行 CSS 的修改或修飾。我們可以把相同的元素賦予相同的 class 屬性名稱，這樣就可以批量地修改多個元素。而且還不會修改到其他不相關的元素。

# 常見的選擇器

在前面的章節中，我們學到了屬性 `class` 和 `id`。而 `id` 是獨特的，每一個 HTML 檔案只能有一個 id。所以一般我們會使用 `class` 來修改多個元素的樣式，而 `id` 一般只會在 JS 裡使用，或是只寫一個元素的 CSS。

CSS 中總共有 6 種類型的選擇器，我們最主要會用到的是 1, 2, 3, 5。看似類型很多，但是其實形式和原理都是一樣的。下面我們就會來學習他們的用處和分別。

1. Class Selectors
2. Id Selectors
3. Element Selectors
4. Attribute Selectors
5. Pseudo-class Selectors
6. Global Selectors