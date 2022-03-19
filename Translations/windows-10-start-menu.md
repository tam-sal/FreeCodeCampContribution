6 نوفمبر 2020 / [#WINDOWS] (https://www.freecodecamp.org/news/tag/windows/)

# Windows 10 Start Menu Not Working (Solved)

! [Kris Koishigawa] (https://www.freecodecamp.org/news/content/images/size/w100/2021/04/kris-author-image-cropped.jpeg)

[Kris Koishigawa] (https://www.freecodecamp.org/news/author/kris/)

! [Windows 10 Start Menu Not Working (Solved)] (https://cdn-media-2.freecodecamp.org/w1280/5fa1226549c47664ed819287.jpg)

لقد قطع Windows 10 شوطًا طويلاً منذ إطلاقه لأول مرة في عام 2015. يجلب كل تحديث الكثير من الميزات (features) الجديدة ، وقد تبنت Microsoft مجتمع المصدر المفتوح بطريقة كان يُعتقد في السابق أنها مستحيلة.

لا يزال ، كما هو الحال مع أي نظام تشغيل ، هناك أخطاء (bugs). وأحد الأخطاء الأكثر شيوعًا التي واجهها الأشخاص الذين يستخدمون نظام التشغيل Windows 10 هو أن قائمة البدء (Start Menu) تتوقف فجأة عن العمل.

في بعض الأحيان تتجمد القائمة ولا تستجيب ، وفي أحيان أخرى لن تفتح على الإطلاق عند النقر على زر Start Menu.

مهما كانت المشكلة المحددة التي تواجهها مع القائمة في Windows 10 ، فسنستعرض بعض الإصلاحات السريعة وغيرها في هذه المقالة.

## كيفية إعادة تشغيل Windows Explorer

Windows Explorer ، والذي يسمى الآن File Explorer ، هو التطبيق الذي تستخدمه لتصفح نظام الملفات (file system) وفتح البرامج والملفات. ولكنه يتحكم أيضًا في أشياء أخرى مثل Start Menu وشريط المهام (taskbar) والتطبيقات الأخرى.

إذا كانت لديك مشكلة في Start Menu ، فإن أول شيء يمكنك القيام به هو إعادة تشغيل عملية "Windows Explorer" في شريط المهام (taskbar).

لفتح الـ taskbar ، اضغط على ** Ctrl + Alt + Delete ** ، ثم انقر على زر "إدارة المهام" (Task Manager).

انقر على "مزيد من التفاصيل" (More details) للاطلاع على قائمة كاملة بالبرامج المفتوحة والعمليات التي تدور في الخلفية التي تقوم بتشغيلها:

! [] (https://www.freecodecamp.org/news/content/images/2020/11/task-manager-more-details.jpg)

قم بالتمرير خلال القائمة حتى تجد "Windows Explorer". ثم انقر بزر الماوس الأيمن على "Windows Explorer" وقم باختيار "إعادة التشغيل" (Restart):

! [] (https://www.freecodecamp.org/news/content/images/2020/11/task-manager-restart-windows-explorer.jpg)

سترى وميض قصير أثناء إعادة تشغيل Windows Explorer / Finder ، جنبًا إلى جنب مع taskbar وStart Menu.

بعد ذلك ، حاول فتح Start Menu. إذا لم تحل هذه الطريقة الخطأ ، فجرّب أحد الحلول الأخرى أدناه.

## كيفية إصلاح ملفات نظام Windows التالفة أو المفقودة

في بعض الأحيان ، ينحرف التحديث ، أو يتم حذف ملفًا مهمًا عن طريق الخطأ أثناء التعامل مع في نظام الملفات (filesystem).

إذا لا زلت تعاني من بعض المشاكل في Start Menu ، أو إذا تعطلت تطبيقات النظام الأساسية الأخرى (Core Windows Apps) ، فيمكنك محاولة استعادة أي ملفات الـ Windows المفقودة أو التالفة.

للقيام بذلك ، ستحتاج إلى فتح نافذة الأوامر كمسؤول [open the Windows Command Prompt as an administrator] (https://www.freecodecamp.org/news/how-to-open-the-command-prompt-in-windows-10/#how-to-open-command-prompt-as-an-administrator) وقم بتشغيل برنامج System File Checker.

بمجرد فتح نافذة الأوامر كمسؤول ، قم بتشغيل الأمر `sfc / scannow`:

! [] (https://www.freecodecamp.org/news/content/images/2020/11/sfc-scannow.jpg)

سيبدأ مدقق ملفات النظام (System File Checker) في استعراض جميع ملفات النظام واستبدال أي ملفات تالفة أو مفقودة بنسخة محفوظة مسبقًا.

قد تستغرق هذه العملية بعض الوقت ، لذلك لا تتردد في القيام بأمر آخر لمدة 5-10 دقائق. فقط كن حريصًا على عدم إغلاق النافذة أثناء قيام "sfc" بعمله.

بمجرد انتهاء System File Checker من القيام بوظيفته، سترى إما تقريرًا بجميع الملفات التي تم استبدالها ، أو إذا كان كل شيء على ما يرام ، فسترى رسالة مثل هذه:

! [] (https://www.freecodecamp.org/news/content/images/2020/11/sfc-scan-complete.jpg)

إذا قام System File Checker باستبدال أي ملفات نظام تالفة أو مفقودة ، فاحفظ كل عملك المفتوح وأعد تشغيل الكمبيوتر. بمجرد تسجيل الدخول مرة أخرى ، حاول فتح Start Menu لمعرفة ما إذا كان ذلك قد أدى إلى حل مشكلاتك.

** ملاحظة: ** يمكنك أيضًا استخدام Powershell لتشغيل الأمر `sfc / scannow` ، ولكن تذكر أنك ستحتاج إلى فتح وحدة طرفية عليا (elevated terminal) من Powershell.

## كيفية إعادة تعيين (reset) Start Menu بتطبيقات Windows 10 الافتراضية

الشيء التالي الذي يمكنك تجربته هو إعادة تعيين القائمة بالكامل ، بالإضافة إلى جميع تطبيقات Windows 10 التي تم تثبيتها مسبقًا أو تثبيتها من متجر Microsoft.

للقيام بذلك ، ستحتاج إلى فتح PowerShell كمسؤول - لن تعمل نافذة الأوامر (Command Prompt) مع الأمر الذي ستقوم بتشغيله في هذه الحالة.

هناك العديد من الطرق لفتح PowerShell ، ولكن إحدى أسرع الطرق هي استخدام تشغيل برنامج (Run program).

استخدم الاختصار ** Windows Key + R ** لفتح Run program ، أدخل "powershell" ، ثم اضغط ضغطة مطوّلة على "Ctrl + Shift" وانقر على الزر "OK":

  

! [] (https://www.freecodecamp.org/news/content/images/2020/11/run-cmd-powershell.jpg)

يجب أن يؤدي هذا إلى فتح وحدة PowerShell بامتيازات إدارية.

في وحدة PowerShell ، قم بتشغيل الأمر التالي:

```
Get-AppXPackage -AllUsers | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}

```

سيحاول الأمر "Get-AppXPackage" إعادة تثبيت جميع تطبيقات Windows الافتراضية ، بما في ذلك Start Menu وشريط البحث (search bar).

سيقوم أيضًا بتسجيل ملف بيان لكل برنامج يقوم بإعادة تثبيته. لا داعي للقلق بشأن ملفات البيان ، رغم ذلك - إنه مجرد أمر يحتاجه Windows لتشغيل كل برنامج.

امنحه من 5 إلى 10 دقائق ، وتأكد من عدم إغلاق نافذة PowerShell حتى تنتهي من العمل.

** ملاحظة: ** قد ترى ظهور بعض الأخطاء المخيفة أثناء تشغيل الأمر "Get-AppXPackage". لا تقلق بشأنها - معظمها مجرد تحذيرات حول سبب عدم إمكانية إعادة تثبيت البرنامج:

! [] (https://www.freecodecamp.org/news/content/images/2020/11/powershell-get-appxpackage.jpg)

عند انتهاء الأمر "Get-AppXPackage" من القيام بعمله ، أعد تشغيل الكمبيوتر ، وسجل الدخول ، وحاول فتح Start Menu.

## كيفية إعادة تعيين (reset) تثبيت Windows 10 الخاص بك

إذا لم تقم أي من الطرق المذكورة أعلاه بإصلاح Start Menu ، فإن آخر شيء يمكنك تجربته هو إجراء إعادة ضبط إعدادات المصنع (factory reset) لتثبيت نظام التشغيل Windows 10. لكن ضع في اعتبارك أن هذه آخر طريقة تريدها ، ويجب استخدامها فقط كملاذ أخير.

يجب أن تحافظ إعادة تعيين تثبيت Windows 10 على جميع ملفاتك الشخصية كما هي (المستندات والصور ومقاطع الفيديو وما إلى ذلك) ، ولكنها ستؤدي إلى إلغاء تثبيت جميع برامج التشغيل والبرامج الأخرى التي قمت بتثبيتها. يؤدي هذا بشكل أساسي إلى إعادة جهاز الكمبيوتر الخاص بك إلى الحالة التي كان عليها عندما قمت بتشغيله لأول مرة.

قبل اتخاذ إجراءات أكثر صلابة ، قم بعمل نسخ احتياطية لجميع ملفاتك المهمة باستخدام flash drive أو HDD/SSD خارجية أو online file host مثل Google Drive أو Dropbox.

في الواقع ، قم بحفظ نسختين احتياطيتين. ربما لن تحتاجهم ، لكن هذا لا يضر.

عند الانتهاء من نسخ جميع ملفاتك الاحتياطية ، افتح وحدة PowerShell - استخدم الاختصار ** Windows Key + R ** ، أدخل "powershell" ، ثم انقر فوق الزر "OK".

في وحدة PowerShell ، قم بتشغيل الأمر "systemreset" لإحضار نافذة إعادة تعيين النظام (Windows reset wizard).

بعد ذلك ، انقر فوق الزر "الاحتفاظ بملفاتي" (Keep my files):

! [] (https://www.freecodecamp.org/news/content/images/2020/11/system-reset-keep-my-files.jpg)

انتظر لحظة بينما يقوم المعالج بتحليل نظامك. بعد ذلك ، سترى قائمة بجميع البرامج التي سيتم حذفها:

! [] (https://www.freecodecamp.org/news/content/images/2020/11/system-reset-programs-to-be-removed.jpg)

انقر فوق الزر "Next" ، واتبع الإرشادات لإعادة تعيين تثبيت Windows 10.

بمجرد الانتهاء من إعادة تعيين Windows وإنشاء مستخدم جديد ، يجب أن تعمل قائمة Start Menu مرة أخرى.

## "Cortana ، افتحي Start Menu"

هذه هي جميع الطرق لإصلاح قائمة Start Menu في نظام التشغيل Windows 10 ، مدرجة من الأسهل إلى الأصعب.

هل أي من هذه الأساليب تعمل من أجلك؟ هل هناك طريقة أخرى فاتتني لاصلاح القائمة؟ اسمحوا لي أن أعرف عنها على [Twitter] (https://twitter.com/kriskoishigawa).

----------

! [Kris Koishigawa] (https://www.freecodecamp.org/news/content/images/size/w100/2021/04/kris-author-image-cropped.jpeg)

[Kris Koishigawa] (https://www.freecodecamp.org/news/author/kris/)

اقرأ [المزيد من المشاركات] (https://www.freecodecamp.org/news/author/kris/) بواسطة هذا المؤلف.

----------

إذا كنت وصلت إلى هذا الحد من قراءة المقالة ، فغرد للمؤلف لتعبّر له باهتمامك. غرد تعبيرًا عن شكرك

تعلم البرمجة مجانا. ساعد منهج freeCodeCamp مفتوح المصدر أكثر من 40 ألف شخص في الحصول على وظائف كمطورين. [البدء] (https://www.freecodecamp.org/learn/)