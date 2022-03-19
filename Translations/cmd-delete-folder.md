### في بعض الأحيان يكون من الأسرع القيام بالأمور باستخدام (Command Line).

في هذا البرنامج التعليمي السريع، سنتعرف على كيفية فتح (Command Line)، وبعض الأوامر والعلامات الأساسية، وكيفية حذف الملفات والمجلدات في (Command Line).

إذا كانت أوامر DOS الأساسية مألوفة بالنسبة إليك، فلا تتردد في [التخطي للأسفل] (https://www.freecodecamp.org/news/cmd-delete-folder-how-to-remove-files-and-folders-in -Windows / # how-to-delete-files-with-the-del-command).

## كيفية فتح (Command Line)

لفتح (Command Line) ، اضغط على مفتاح Windows ، واكتب "cmd".

ثم انقر فوق "تشغيل كمسؤول" (Run as Administrator):

![Screenshot showing how to open Command Prompt as an administrator](https://www.freecodecamp.org/news/content/images/2020/12/run-command-prompt-as-administrator.jpg)

بعد ذلك، سترى نافذة (Command Prompt) بامتيازات إدارية:

![](https://www.freecodecamp.org/news/content/images/2020/12/command-prompt-new-window.jpg)

لقطة شاشة لنافذة (Command Prompt)

إذا لم تتمكن من فتح (Command Prompt) كمسؤول، فلا داعي للقلق. يمكنك فتح نافذة (Command Prompt) عادية بالنقر فوق "فتح" (Open) بدلاً من "تشغيل كمسؤول" (Run as Administrator).

الاختلاف الوحيد هو أنك قد لا تتمكن من حذف بعض الملفات المحمية، وهو ما لا ينبغي أن يكون مشكلة في معظم الحالات.

## كيفية حذف الملفات باستخدام الأمر `del`

الآن بعد أن تم فتح (Command Prompt) ، استخدم `cd` لتغيير الدلائل (directories) إلى حيث توجد ملفاتك.

لقد أعددت دليلاً على سطح المكتب يسمى Test Folder. يمكنك استخدام الأمر `tree /f` لرؤية شجرة لجميع الملفات والمجلدات المتداخلة:

![Screenshot after running tree /f in target directory](https://www.freecodecamp.org/news/content/images/2020/12/command-prompt-tree.jpg)

لحذف ملف، استخدم الأمر التالي: `"<del "<filename`.

على سبيل المثال، لحذف `Test file.txt` ، ما عليك سوى كتابة `"del "Test File.txt` والضغط على (Enter). 

قد تكون هناك مطالبة تسألك عما إذا كنت تريد حذف الملف. إذا كان الأمر كذلك ، فاكتب "y" واضغط على (Enter).

** ملاحظة: ** لا يمكن استعادة أي ملفات تم حذفها باستخدام الأمر `del`. كن حذرًا جدًا في مكان وكيفية استخدام هذا الأمر.

بعد ذلك ، يمكنك كتابة `tree /f`  والضغط على (Enter) لتأكيد حذف ملفك:

![Screenshot after deleting file with del command](https://www.freecodecamp.org/news/content/images/2020/12/del-tree-check.jpg)

أيضًا ، نصيحة إضافية - يحتوي (Command Prompt) على خاصية إكمال تلقائي أساسي. لذلك يمكنك فقط كتابة `del test` ، والضغط على مفتاح (tab) ، وسيقوم (Command Prompt) بتغييره إلى `"del "Test File.txt`.

### كيفية فرض حذف الملفات باستخدام الأمر `del`

في بعض الأحيان يتم تحديد خاصية الملفات كمقروءة فقط (read only)، وسترى الخطأ التالي عند محاولة استخدام الأمر `del`:

![Screenshot of error after trying to delete a read only file](https://www.freecodecamp.org/news/content/images/2020/12/read-only-error.jpg)

للتغلب على ذلك، استخدم العلامة `f/` لفرض حذف الملف. على سبيل المثال، `"del /f "Read Only Test File.txt`:

![Screenshot after deleting file with the force flag](https://www.freecodecamp.org/news/content/images/2020/12/del-force-flag.jpg)

## كيفية حذف المجلدات باستخدام الأمر `rmdir`
لحذف الدلائل / المجلدات (directories/folders)، ستحتاج إلى استخدام الأمر `rmdir` أو`rd`. كلا الأمرين يعملان بنفس الطريقة ، لكن دعنا نلتزم بـ "rmdir" لأنه أكثر تعبيرًا إلى حد ما.

أيضًا، سأستخدم المصطلحين الدليل والمجلد (directory and folder) بالتبادل لبقية البرنامج التعليمي. "المجلد" هو مصطلح جديد أصبح شائعًا مع واجهات المستخدم لسطح المكتب (Desktop GUIs)، ولكن ببساطة المجلد والدليل يعنيان نفس الشيء.

لحذف دليل، ما عليك سوى استخدام الأمر <`rmdir <directory name`.

** ملاحظة: ** لا يمكن استرداد أي دلائل (directories) تم حذفها باستخدام الأمر `rmdir`. كن حذرًا جدًا في مكان وكيفية استخدام هذا الأمر.

في هذه الحالة أرغب في إزالة دليل باسم Subfolder ، لذلك سأستخدم الأمر `rmdir Subfolder`:

![Screenshot of a directory not empty error](https://www.freecodecamp.org/news/content/images/2020/12/directory-not-empty.jpg)

ولكن، إذا كنت تتذكر سابقًا، فإن Subfolder يحتوي على ملف يسمى Nested Test File.

يمكنك استخدام أمر "cd" في دليل Subfolder وإزالة الملف، ثم العودة مع `.. cd` وكتابة الأمر`rmdir Subfolder` مرة أخرى، لكن ذلك سيصبح أمرًا مجهدًا. وتخيل لو كانت هناك المزيد من الملفات والدلائل المتداخلة الأخرى!

كما هو الحال مع الأمر `del` ، هناك علامة مفيدة يمكننا استخدامها لجعل الأمور أسرع وأسهل بكثير.

### كيفية استخدام علامة ` s/ ` مع `rmdir`

لإزالة دليل، بما في ذلك جميع الملفات والأدلة الفرعية المتداخلة ، ما عليك سوى استخدام علامة `s/`:

![Screenshot after running rmdir with the /s flag](https://www.freecodecamp.org/news/content/images/2020/12/rmdir-s-flag.jpg)

من المحتمل أن تكون هناك مطالبة تسألك عما إذا كنت تريدحذف هذا الدليل. إذا كان الأمر كذلك، فما عليك سوى كتابة "y" واضغط على (Enter).

وهذا كل شيء! يجب أن يكون هذا كل ما تحتاج إلى معرفته لحذف الملفات والمجلدات في (Windows Command Prompt).

يجب أن تعمل كل هذه الأوامر في (PowerShell) ، وهو  الإصدار 2.0 لـ (Windows Command Prompt) أيضًا، يحتوي (PowerShell) على مجموعة من الأسماء المستعارة (aliases) الرائعة مثل `ls` و `clear` والتي يجب أن تكون سهلة تمامًا إذا كنت معتادًا على أوامر (Mac/Linux command line).

هل ساعدتك هذه الأوامر؟ هل هناك أي أوامر أخرى تجدها مفيدة؟ في كلتا الحالتين ، اسمحوا لي أن أعرف أكثر على Twitter.

----------


![Kris Koishigawa](https://www.freecodecamp.org/news/content/images/size/w100/2021/04/kris-author-image-cropped.jpeg)


[Kris Koishigawa](https://www.freecodecamp.org/news/author/kris/)

اقرأ [المزيد من المشاركات] (https://www.freecodecamp.org/news/author/kris/) بواسطة هذا المؤلف.











