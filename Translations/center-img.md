30 ديسمبر 2019 / [CSS#](https://www.freecodecamp.org/news/tag/css/)

# How to Center an Image Using Text Align: Center

![How to Center an Image Using Text Align: Center](https://cdn-media-2.freecodecamp.org/w1280/5f9c9e5e740569d1a4ca3cbb.jpg)

عنصر الصورة `<img>` هو عنصر مدمج في نفس السطر (inline element) (قيمة العرض `inline-block`). يمكن توسيطها بسهولة عن طريق إضافة `;text-align: center` ، وهي خاصية الـ CSS التي تشير إلى العنصر الأب الذي يحوي الصورة.

لتوسيط صورة باستخدام `;text-align: center` يجب وضع `<img>` داخل عنصر شمولي (block-level element) مثل `div`. نظرًا لأن خاصية محاذاة النص `text-align` تنطبق فقط على العناصر الشمولية ، يمكنك تحديد `;text-align: center` في العنصر الشمولي الحاوي لكافة العناصر لتحقيق مركزًا أفقيًا للـ `<img>`.

### **مثال**

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Center an Image using text align center</title>
    <style>
      .img-container {
        text-align: center;
      }
    </style>
  </head>
  <body>
    <div class="img-container"> <!-- Block parent element -->
      <img src="user.png" alt="John Doe">
    </div>
  </body>
</html>
```

****ملاحظة:**** يجب أن يكون العنصر الأب عنصر شمولي (block element). غير ذلك ، فيجب إضافة خاصيتيّ `;display: block` و
`;text-align: center`  من CSS لتحقيق ذلك.

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Center an Image using text align center</title>
    <style>
      .img-container {
        text-align: center;
        display: block;
      }
    </style>
  </head>
  <body>
    <span class="img-container"> <!-- Inline parent element -->
      <img src="user.png" alt="">
    </span>
  </body>
</html>
```

****عرض توضيحي:**** [Codepen](https://codepen.io/aravindio/pen/PJMXbp)

## تناسب الكائن (Object Fit)

بمجرد توسيط صورتك ، قد ترغب في تغيير حجمها. تحدد الخاصية `object-fit` كيفية استجابة العنصر لعرض وارتفاع الصندوق الأب (parent box) المنتمي إليه.

يمكن استخدام هذه الخاصية للصور أو الفيديو أو أي وسائط أخرى. يمكن استخدامها أيضًا مع خاصية `object-position` للحصول على مزيد من التحكم في كيفية عرض الوسائط.

ببساطة تقوم خاصية `object-fit` بتحديد كيفية تمدد أو ضغط الوسائط المضمنة في نفس السطر (inline media).

### بناء النص البرمجي (Syntax)

```css
.element {
    object-fit: fill || contain || cover || none || scale-down;
}
```

### القيم (Values)

- `fill` : ****هذه هي القيمة الافتراضية****. تقوم بتغيير حجم المحتوى لمطابقة الصندوق الأب (parent box) بغض النظر عن نسبة العرض إلى الارتفاع (aspect-ratio).
- `contain` : تغيّر حجم المحتوى لملء الصندوق الأب (parent box) محافظًة على نسبة العرض إلى الارتفاع (aspect-ratio) الصحيحة.
- `cover` : مشابهة لـ `contain` ولكن غالبًا ما يتم اقتصاص المحتوى.
- `none` : تعرض الصورة بحجمها الأصلي.
- `scale-down` : تقارن الفرق بين `none` و `contain` للعثور على أصغر حجم ملموس للكائن.

### التوافق مع المتصفح (Browser Compatibility)

يتم دعم `object-fit` من قبل معظم المتصفحات الحديثة ، للحصول على أحدث المعلومات حول التوافق ، يمكنك التحقق من ذلك هنا [http://caniuse.com/#search=object-fit](http://caniuse.com/#search=object-fit).

## **التوثيق (Documentation)**

-   [****text-align****  - MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/text-align)
-   [**object-fit**  - MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/object-fit)
-   [****<img>****  - MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img)