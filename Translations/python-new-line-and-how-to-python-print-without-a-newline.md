[Estefania Cassingena Navone](https://www.freecodecamp.org/news/author/estefaniacn/)

![Python New Line and How to Python Print Without a Newline](https://www.freecodecamp.org/news/content/images/size/w2000/2020/06/New-Line.png)
**مرحبًا!**  يتم استخدام رمز سطر جديد (New Line Character) في Python لتحديد نهاية السطر وبداية سطر جديد. معرفة كيفية استخدامه أمر ضروري إذا كنت تريد طباعة الناتج إلى وحدة التحكم والعمل مع الملفات.

**ستتعلم التالي في هذا المقال :** 

- كيفية التعرف على رمز سطر جديد (New Line Character) في Python.
- كيف يمكن استخدام رمز سطر جديد (New Line Character) في السلسة النصية "String" وتعليمات الطباعة.
- كيف يمكنك كتابة تعليمات الطباعة التي لا تضيف رمز سطر جديد (New Line Character) إلى نهاية السلسة النصية "String".


**فلنبدأ !** ✨
## 🔹 رمز السطر الجديد (New Line Character) 

رمز السطر الجديد (New Line Character) في Python هو:

![](https://www.freecodecamp.org/news/content/images/2020/06/image-142.png)

**يتكوّن الرمز من حرفين:**

- شرطة مائلة للخلف (Backslash).
- الحرف `n`.

إذا رأيت هذا الرمز في سلسة نصية ما (String) ، فهذا يعني أن السطر الحالي ينتهي عند تلك النقطة ويبدأ سطر جديد بعدها مباشرةً:

![](https://www.freecodecamp.org/news/content/images/2020/06/image-224.png)

يمكنك أيضًا استخدام الرمز نفسه مع **f-strings**. 
```python
>>> print(f"Hello\nWorld!")
```

## 🔸 رمز سطر جديد (New Line Character) في تعليمات الطباعة

تقوم تعليمات الطباعة بإضافة رمز سطر جديد (New Line Character) بشكل تلقائي "خلف الكواليس" في نهاية السلسلة النصية (String).
على النحو التالي:

![](https://www.freecodecamp.org/news/content/images/2020/06/image-145.png)

وفقًا لـ  [Python Documentation](https://docs.python.org/3/library/functions.html#print) فإن السبب يرجع إلى:

إن القيمة التلقائية/الافتراضية (default value) لمعلمة `end` لأمر الطباعة (print) المدمج هي `\n` ، لذا فيتم إلحاق رمز سطر جديد (New Line Character) بنهاية السلسلة النصية (String).   


💡 **نصيحة.** يٌقصد بـ "إلحاق" الإضافة إلى آخر السطر.


هذا هو تعريف الوظيفة:

![](https://www.freecodecamp.org/news/content/images/2020/06/image-146.png)

لاحظ أن قيمة  `end` هي `\n` ، لذا فيتم إضافة `\n` إلى نهاية السلسلة النصية (String). 


إذا كنت تستخدم أمر طباعة واحد فقط (Print)، فلن تلاحظ ذلك لأنه سيتم طباعة سطر واحد فقط:

![](https://www.freecodecamp.org/news/content/images/2020/06/image-147.png)

لكن إذا استخدمت عدة تعليمات طباعة واحدة تلو الأخرى في نص برمجي بلغة Python:

![](https://www.freecodecamp.org/news/content/images/2020/06/image-214.png)

ستتم طباعة الناتج في سطور منفصلة نظرًا لإضافة `\ n` "خلف الكواليس" إلى نهاية كل سطر:


![](https://www.freecodecamp.org/news/content/images/2020/06/image-218.png)


## 🔹 كيفية الطباعة بدون إضافة سطر جديد
يمكننا تغيير هذا السلوك الافتراضي عن طريق تخصيص قيمة المعلمة `end` لوظيفة` print`.

إذا استخدمنا القيمة الافتراضية في هذا المثال:

![](https://www.freecodecamp.org/news/content/images/2020/06/image-219.png)

نرى الناتج مطبوعًا في سطرين:

![](https://www.freecodecamp.org/news/content/images/2020/06/image-221.png)

ولكن إذا قمنا بتخصيص قيمة `end` وضبطناها على `" "`

![](https://www.freecodecamp.org/news/content/images/2020/06/image-222.png)

ستتم إضافة مسافة إلى نهاية السلسلة النصية (String) بدلاً من رمز سطر جديد (New Line Character)  `\ n` ، لذلك سيتم عرض ناتج طباعة الجملتين في نفس السطر:

![](https://www.freecodecamp.org/news/content/images/2020/06/image-223.png)

يمكنك استخدام هذا لطباعة سلسلة من القيم في سطر واحد، كما في هذا المثال:

![](https://www.freecodecamp.org/news/content/images/2020/06/image-210.png)

الناتج هو:

![](https://www.freecodecamp.org/news/content/images/2020/06/image-211.png)

**💡 نصيحة.** نضيف عبارة شرطية للتأكد من عدم إضافة الفاصلة إلى الرقم الأخير من التسلسل.
	

وبالمثل، يمكننا استخدام هذا لطباعة قيم قابلة للتكرار في نفس السطر:

![](https://www.freecodecamp.org/news/content/images/2020/06/image-225.png)

الناتج هو:

![](https://www.freecodecamp.org/news/content/images/2020/06/image-213.png)

## 🔸 رمز سطر جديد (New Line Character) في الملفات

يوجد رمز سطر جديد (New Line Character) `\n` أيضًا في الملفات، ولكنه "مخفي". عندما ترى سطرًا جديدًا في ملف نصي ، فقد تم إدراج رمز سطر جديد `\n`.


![](https://www.freecodecamp.org/news/content/images/2020/06/image-150.png)

يمكنك الإطلاع على ذلك عن طريق قراءة الملف بإستخدام `()file>.readlines>`، على النحو التالي: 


```python
with open("names.txt", "r") as f:
    print(f.readlines())
```

الناتج هو:

![](https://www.freecodecamp.org/news/content/images/2020/06/image-207.png)

كما ترى ، تنتهي الأسطر الثلاثة الأولى من الملف النصي برمز سطر جديد (New Line Character)  `\n` يعمل "خلف الكواليس".

**💡 نصيحة.** لاحظ أن السطر الأخير فقط من الملف لا ينتهي برمز سطر جديد (New Line Character).


## 🔹 الخلاصة

-   رمز سطر جديد (New Line Character) في Python هو `\n`. يتم استخدامة للإشارة إلى نهاية سطر نصّي.
-  يمكنك طباعة السلاسل النصية (Strings) دون إضافة سطر جديد مع <`end = <character`، وهذا الرمز المُشار إليه character) سيتم استخدامه لفصل السطور.

**أتمنى حقًا أن تكون مقالتي قد أعجبتك ووجدتها مفيدة.**  الآن يمكنك العمل مع رمز سطر جديد (New Line Character) في Python.

[إطلع على دوراتي التعليمية أونلاين] (https://www.udemy.com/user/estefania-cn/)  تابعني على [Twitter](https://twitter.com/EstefaniaCassN). ⭐️ 


