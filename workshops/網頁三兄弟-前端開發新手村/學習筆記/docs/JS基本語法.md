# JavaScript 基本語法

學習每一個編程語言是都有學習它的基礎，而基礎的部分都不外乎是以下的幾個：

1. 變量的宣告與使用
2. 變量的數據類型和差別
3. 使用變量進行運算
4. 條件語句和循環語句

這裡我們會快速介紹他們，然後立馬進入實戰來掌握他們。

## 變量

變量是用於存放數值的，例如我們可以把從伺服器中獲取的資料放進變量裡，這樣就不會每次使用時都想伺服器請求一次了。

```js
let myAge = 20; // let 代表變量可以在後續被改動
const LEGAL_AGE_TO_DRINK = 18; // const(常量) 代表在程式運行的週期中不能被修改

myAge = 21; // 沒有問題
LEGAL_AGE_TO_DRINK = 19; // 程式會報錯，並提示 const 變量不能被修改
```

> 變量的名稱也有一些限制，例如不能使用 `$` 和 `_` 以外的符號、名稱一定要由英文字母開頭等。

### 命名慣例

一般我們幫變量改名時會使用小寫開頭，當名稱是由多個單字組成時，則會使用 `camel-case` 駝峰式的方式。例如由 `last name` 變成 `lastName`。

如果變量為常數（const）且數值是寫死不會改時，我們會慣例把整個名稱改為大寫。

## 數據類型

`JavaScript` 的數據類型會伴隨著一直內置的函數供我們使用，而且每一種數據類型的特性都未必相同。所以我們要學習它們不同的特性和內置函數。以下是主要的數據類型：

1. number - 數值
2. string - 字串
3. boolean - 布爾值（對於錯）
4. undefined - 還沒宣告或還沒賦值
5. null - 沒有值
6. bigint
7. symbol

在本次工作坊中主要會帶過的是1至5，另外兩個會比較少情況會用到。

```js
const age = 18;
console.log(age) // 輸出 18

const name = "KaLok";
console.log(name) // 輸出 KaLok

const isPressed = true;
console.log(isPressed) // 輸出 true

const x;
console.log(x) // 提示 x 的值為 undefined

const user = null;
console.log(user) // 輸出 null
```

> `JavaScript` 不像 `C` 或 `Java` 等的那些編程語言，`JS` 的變量可以忽略數據類型去重新賦值變量，這樣就會相對不算嚴謹。但是我們一般也不會把不同類型的變量重新賦值。