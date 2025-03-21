---
title: تهيئة wis2box
---

# تهيئة wis2box

!!! abstract "نتائج التعلم"

    بنهاية هذه الجلسة العملية، ستكون قادرًا على:

    - تشغيل السكربت `wis2box-create-config.py` لإنشاء التكوين الأولي
    - بدء تشغيل wis2box والتحقق من حالة مكوناته
    - الوصول إلى **wis2box-webapp**، وAPI، وواجهة MinIO ولوحة معلومات Grafana في المتصفح
    - الاتصال بـ **wis2box-broker** المحلي باستخدام MQTT Explorer

!!! note

    المواد التدريبية الحالية تستخدم wis2box-1.0.0rc1.
    
    انظر [accessing-your-student-vm](accessing-your-student-vm.md) للحصول على تعليمات حول كيفية تنزيل وتثبيت حزمة برامج wis2box إذا كنت تقوم بتشغيل هذا التدريب خارج جلسة تدريب محلية.

## التحضير

قم بتسجيل الدخول إلى VM المخصص لك باستخدام اسم المستخدم وكلمة المرور الخاصة بك وتأكد من أنك في دليل `wis2box-1.0.0rc1`:

```bash
cd ~/wis2box-1.0.0rc1
```

## إنشاء التكوين الأولي

التكوين الأولي لـ wis2box يتطلب:

- ملف بيئة `wis2box.env` يحتوي على معاملات التكوين
- دليل على الجهاز المضيف للمشاركة بين الجهاز المضيف وحاويات wis2box المحددة بمتغير البيئة `WIS2BOX_HOST_DATADIR`

يمكن استخدام السكربت `wis2box-create-config.py` لإنشاء التكوين الأولي لـ wis2box.

سيطرح عليك مجموعة من الأسئلة لمساعدتك في إعداد التكوين الخاص بك.

سيكون بإمكانك مراجعة وتحديث ملفات التكوين بعد اكتمال السكربت.

قم بتشغيل السكربت كما يلي:

```bash
python3 wis2box-create-config.py
```

### دليل بيانات المضيف wis2box

سيطلب منك السكربت إدخال الدليل الذي سيتم استخدامه لمتغير البيئة `WIS2BOX_HOST_DATADIR`.

لاحظ أنك بحاجة إلى تحديد المسار الكامل لهذا الدليل.

على سبيل المثال، إذا كان اسم المستخدم الخاص بك هو `username`، فإن المسار الكامل للدليل هو `/home/username/wis2box-data`:

```{.copy}
username@student-vm-username:~/wis2box-1.0.0rc1$ python3 wis2box-create-config.py
يرجى إدخال الدليل الذي سيتم استخدامه لـ WIS2BOX_HOST_DATADIR:
/home/username/wis2box-data
سيتم تعيين الدليل الذي سيتم استخدامه لـ WIS2BOX_HOST_DATADIR على:
    /home/username/wis2box-data
هل هذا صحيح؟ (y/n/exit)
y
تم إنشاء الدليل /home/username/wis2box-data.
```

### عنوان URL لـ wis2box

بعد ذلك، سيُطلب منك إدخال عنوان URL لـ wis2box. هذا هو العنوان URL الذي سيتم استخدامه للوصول إلى تطبيق ويب wis2box وAPI وUI.

يرجى استخدام `http://<your-hostname-or-ip>` كعنوان URL.

```{.copy}
يرجى إدخال عنوان URL لـ wis2box:
 للاختبار المحلي، العنوان هو http://localhost
 لتمكين الوصول عن بُعد، يجب أن يشير العنوان إلى عنوان IP العام أو اسم النطاق للخادم الذي يستضيف wis2box.
http://username.wis2.training
سيتم تعيين عنوان URL لـ wis2box على:
  http://username.wis2.training
هل هذا صحيح؟ (y/n/exit)
```

### كلمات مرور WEBAPP، STORAGE و BROKER

يمكنك استخدام خيار توليد كلمة مرور عشوائية عندما يُطلب منك ذلك و`WIS2BOX_WEBAPP_PASSWORD`، `WIS2BOX_STORAGE_PASSWORD`، `WIS2BOX_BROKER_PASSWORD` وتحديد كلمة المرور الخاصة بك.

لا تقلق بشأن تذكر هذه الكلمات، سيتم تخزينها في ملف `wis2box.env` في دليل wis2box-1.0.0rc1 الخاص بك.

### مراجعة `wis2box.env`

بمجرد اكتمال السكربتات، تحقق من محتويات ملف `wis2box.env` في دليلك الحالي:

```bash
cat ~/wis2box-1.0.0rc1/wis2box.env
```

أو تحقق من محتوى الملف عبر WinSCP.

!!! question

    ما هي قيمة WISBOX_BASEMAP_URL في ملف wis2box.env؟

??? success "انقر للكشف عن الإجابة"

    القيمة الافتراضية لـ WIS2BOX_BASEMAP_URL هي `https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png`.

    يشير هذا العنوان إلى خادم البلاط OpenStreetMap. إذا كنت ترغب في استخدام مزود خرائط مختلف، يمكنك تغيير هذا العنوان ليشير إلى خادم بلاط مختلف.

!!! question 

    ما هي قيمة متغير البيئة WIS2BOX_STORAGE_DATA_RETENTION_DAYS في ملف wis2box.env؟

??? success "انقر للكشف عن الإجابة"

    القيمة الافتراضية لـ WIS2BOX_STORAGE_DATA_RETENTION_DAYS هي 30 يومًا. يمكنك تغيير هذه القيمة إلى عدد مختلف من الأيام إذا كنت ترغب في ذلك.
    
    تقوم حاوية wis2box-management بتشغيل cronjob يوميًا لإزالة البيانات الأقدم من عدد الأيام المحدد بواسطة WIS2BOX_STORAGE_DATA_RETENTION_DAYS من دلو `wis2box-public` والواجهة الخلفية لـ API:
    
    ```{.copy}
    0 0 * * * su wis2box -c "wis2box data clean --days=$WIS2BOX_STORAGE_DATA_RETENTION_DAYS"
    ```

!!! note

    يحتوي ملف `wis2box.env` على متغيرات البيئة التي تحدد تكوين wis2box الخاص بك. لمزيد من المعلومات، راجع [wis2box-documentation](https://docs.wis2box.wis.wmo.int/en/latest/reference/configuration.html).

    لا تقم بتعديل ملف `wis2box.env` ما لم تكن متأكدًا من التغييرات التي تقوم بها. قد تؤدي التغييرات غير الصحيحة إلى توقف wis2box عن العمل.

    لا تشارك محتويات ملف `wis2box.env` الخاص بك مع أي شخص، حيث يحتوي على معلومات حساسة مثل كلمات المرور.

## بدء تشغيل wis2box

تأكد من أنك في الدليل الذي يحتوي على ملفات تعريف حزمة برامج wis2box:

```{.copy}
cd ~/wis2box-1.0.0rc1
```

ابدأ تشغيل wis2box بالأمر التالي:

```{.copy}
python3 wis2box-ctl.py start
```

عند تشغيل هذا الأمر لأول مرة، سترى الإخراج التالي:

```
لم يتم العثور على ملفات docker-compose.images-*.yml، يتم إنشاء واحد
الإصدار الحالي=غير محدد، أحدث إصدار=1.0.0rc1
هل ترغب في التحديث؟ (y/n/exit)
```

اختر ``y`` وسيقوم السكربت بإنشاء الملف ``docker-compose.images-1.0.0rc1.yml``، وتنزيل الصور Docker المطلوبة وبدء الخدمات.

قد يستغرق تنزيل الصور بعض الوقت اعتمادًا على سرعة اتصالك بالإنترنت. هذه الخطوة مطلوبة فقط في المرة الأولى التي تبدأ فيها تشغيل wis2box.

تفقد الحالة بالأمر التالي:

```{.copy}
python3 wis2box-ctl.py status
```

كرر هذا الأمر حتى تكون جميع الخدمات قيد التشغيل.

!!! note "wis2box و Docker"
    يعمل wis2box كمجموعة من حاويات Docker التي يديرها docker-compose.
    
    تتم تعريف الخدمات في ملفات `docker-compose*.yml` المختلفة التي يمكن العثور عليها في دليل `~/wis2box-1.0.0rc1/`.
    
    يتم استخدام السكربت البرمجي `wis2box-ctl.py` لتشغيل أوامر Docker Compose الأساسية التي تتحكم في خدمات wis2box.

    لا تحتاج إلى معرفة تفاصيل حاويات Docker لتشغيل حزمة برامج wis2box، ولكن يمكنك فحص ملفات `docker-compose*.yml` لمعرفة كيفية تعريف الخدمات. إذا كنت مهتمًا بمعرفة المزيد عن Docker، يمكنك العثور على مزيد من المعلومات في [وثائق Docker](https://docs.docker.com/).

لتسجيل الدخول إلى حاوية wis2box-management، استخدم الأمر التالي:

```{.copy}
python3 wis2box-ctl.py login
```

داخل حاوية wis2box-management، يمكنك تشغيل أوامر مختلفة لإدارة wis2box الخاص بك، مثل:

- `wis2box auth add-token --path processes/wis2box` : لإنشاء رمز تفويض لنقطة النهاية `processes/wis2box`
- `wis2box data clean --days=<number-of-days>` : لتنظيف البيانات الأقدم من عدد معين من الأيام من دلو `wis2box-public`

للخروج من الحاوية والعودة إلى الجهاز المضيف، استخدم الأمر التالي:

```{.copy}
exit
```

قم بتشغيل الأمر التالي لرؤية حاويات docker التي تعمل على جهازك المضيف:

```{.copy}
docker ps
```

يجب أن ترى الحاويات التالية قيد التشغيل:

- wis2box-management
- wis2box-api
- wis2box-minio
- wis2box-webapp
- wis2box-auth
- wis2box-ui
- wis2downloader
- elasticsearch
- elasticsearch-exporter
- nginx
- mosquitto
- prometheus
- grafana
- loki

تعتبر هذه الحاويات جزءًا من حزمة برامج wis2box وتوفر الخدمات المختلفة اللازمة لتشغيل wis2box.

قم بتشغيل الأمر التالي لرؤية أحجام docker التي تعمل على جهازك المضيف:

```{.copy}
docker volume ls
```

يجب أن ترى الأحجام التالية:

- wis2box_project_auth-data
- wis2box_project_es-data
- wis2box_project_htpasswd
- wis2box_project_minio-data
- wis2box_project_prometheus-data
- wis2box_project_loki-data

بالإضافة إلى بعض الأحجام المجهولة التي تستخدمها الحاويات المختلفة.

تُستخدم الأحجام التي تبدأ بـ `wis2box_project_` لتخزين البيانات الدائمة للخدمات المختلفة في حزمة برامج wis2box.

## واجهة برمجة تطبيقات wis2box

تحتوي wis2box على واجهة برمجة تطبيقات (API) توفر الوصول إلى البيانات والعمليات للتصور التفاعلي وتحويل البيانات والنشر.

افتح علامة تبويب جديدة وانتقل إلى الصفحة `http://<your-host>/oapi`.

<img alt="wis2box-api.png" src="../../assets/img/wis2box-api.png" width="800">

هذه هي صفحة البداية لواجهة برمجة تطبيقات wis2box (تعمل عبر حاوية **wis2box-api**).

!!! question
     
     ما هي المجموعات المتاحة حالي