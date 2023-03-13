# JavaScript物件概念

除了前面提到的數據類型外，`JavaScript` 中有一個較複雜的數據結構 `Object`（物件）。我們可以利用物件去組成一個單獨並包含多個鍵值對的變量。簡而言之，我們可以組成一個變量集合，一個變量裝著不同數據類型的變量。

## 為什麼要使用物件

我們從痛點中上手會比較能夠理解，為什麼大部分開發者都傾向於用物件。試想一下我們需要管理一個用戶的相關資訊，例如名稱、住址、電話號碼、年齡等。

```js
const name = "KaLok";
const address = "UMAC";
const contactNumber = "1234567890";
const age = 20;
```

可能這樣看其實還好，不會覺得有很大的問題。但是當需要存放用戶的資料越多，我們的數據就會越散開。更好的做法是使用 `Object` 的寫法：

```js
const user = {
    name: "KaLok",
    address: "UMAC",
    contactNumber: "1234567890";
    age: 20,
};

console.log(user.name) // 輸出：KaLok
console.log(user.age) // 輸出：UMAC
```

可以看到這樣的寫法會把相關的數據或變量都放在一起，通過這樣的數據結構就可以更好的使用和管理我們的代碼。而且我們等一下就會進行網絡請求去獲取活動資料，而基本上所有的 API（網絡接口）的數據都是以 `Object` 的形式返回的。所以要學會 `JavaScript`，`Object` 是一個不可忽略的知識點。