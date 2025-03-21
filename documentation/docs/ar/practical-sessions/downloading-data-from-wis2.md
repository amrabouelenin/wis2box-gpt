---
title: تنزيل وفك تشفير البيانات من WIS2
---

# تنزيل وفك تشفير البيانات من WIS2

!!! abstract "نتائج التعلم!"

    بنهاية هذه الجلسة العملية، ستكون قادرًا على:

    - استخدام "wis2downloader" للاشتراك في إشعارات بيانات WIS2 وتنزيل البيانات إلى نظامك المحلي
    - عرض حالة التنزيلات في لوحة تحكم Grafana
    - فك تشفير بعض البيانات المُنزلة باستخدام حاوية "decode-bufr-jupyter"

## مقدمة

في هذه الجلسة ستتعلم كيفية إعداد اشتراك في وسيط WIS2 وتنزيل البيانات تلقائيًا إلى نظامك المحلي باستخدام خدمة "wis2downloader" المضمنة في wis2box.

!!! note "حول wis2downloader"
     
     يتوفر wis2downloader أيضًا كخدمة مستقلة يمكن تشغيلها على نظام مختلف عن النظام الذي ينشر إشعارات WIS2. راجع [wis2downloader](https://pypi.org/project/wis2downloader/) لمزيد من المعلومات حول استخدام wis2downloader كخدمة مستقلة.

     إذا كنت ترغب في تطوير خدمتك الخاصة للاشتراك في إشعارات WIS2 وتنزيل البيانات، يمكنك استخدام [شيفرة المصدر wis2downloader](https://github.com/wmo-im/wis2downloader) كمرجع.

!!! Other tools for accessing WIS2 data

    يمكن أيضًا استخدام الأدوات التالية لاكتشاف والوصول إلى بيانات من WIS2:

    - [pywiscat](https://github.com/wmo-im/pywiscat) يوفر قدرة البحث فوق كتالوج الاكتشاف العالمي WIS2 لدعم التقارير وتحليل كتالوج WIS2 وبيانات الاكتشاف المرتبطة به
    - [pywis-pubsub](https://github.com/wmo-im/pywis-pubsub) يوفر قدرة الاشتراك وتنزيل بيانات WMO من خدمات البنية التحتية WIS2

## التحضير

قبل البدء، يرجى تسجيل الدخول إلى جهاز الطالب الافتراضي VM وتأكد من أن نسخة wis2box الخاصة بك تعمل.

## التمرين 1: عرض لوحة تحكم wis2download في Grafana

افتح متصفح ويب وانتقل إلى لوحة تحكم Grafana لنسخة wis2box الخاصة بك بالانتقال إلى `http://<your-host>:3000`.

انقر على لوحات التحكم في القائمة اليسرى، ثم حدد **لوحة تحكم wis2downloader**.

يجب أن ترى اللوحة التالية:

![لوحة تحكم wis2downloader](../assets/img/wis2downloader-dashboard.png)

تعتمد هذه اللوحة على المقاييس التي نشرتها خدمة wis2downloader وستعرض لك حالة التنزيلات الجارية.

في الزاوية العلوية اليسرى، يمكنك رؤية الاشتراكات النشطة حاليًا.

احتفظ بفتح هذه اللوحة حيث ستستخدمها لمراقبة تقدم التنزيل في التمرين التالي.

## التمرين 2: مراجعة تكوين wis2downloader

يمكن تكوين خدمة wis2downloader التي بدأتها مجموعة wis2box-stack باستخدام المتغيرات البيئية المحددة في ملف wis2box.env الخاص بك.

تستخدم المتغيرات البيئية التالية بواسطة wis2downloader:

    - DOWNLOAD_BROKER_HOST: اسم المضيف لوسيط MQTT الذي سيتم الاتصال به. الافتراضي هو globalbroker.meteo.fr
    - DOWNLOAD_BROKER_PORT: منفذ وسيط MQTT الذي سيتم الاتصال به. الافتراضي هو 443 (HTTPS لواجهات الويب)
    - DOWNLOAD_BROKER_USERNAME: اسم المستخدم للاتصال بوسيط MQTT. الافتراضي هو everyone
    - DOWNLOAD_BROKER_PASSWORD: كلمة المرور للاتصال بوسيط MQTT. الافتراضي هو everyone
    - DOWNLOAD_BROKER_TRANSPORT: واجهات الويب أو tcp، آلية النقل المستخدمة للاتصال بوسيط MQTT. الافتراضي هو واجهات الويب،
    - DOWNLOAD_RETENTION_PERIOD_HOURS: فترة الاحتفاظ بالبيانات المنزلة بالساعات. الافتراضي هو 24
    - DOWNLOAD_WORKERS: عدد عمال التنزيل المستخدمين. الافتراضي هو 8. يحدد عدد التنزيلات المتوازية.
    - DOWNLOAD_MIN_FREE_SPACE_GB: الحد الأدنى للمساحة الحرة بالجيجابايت للحفاظ عليها في المجلد الذي يستضيف التنزيلات. الافتراضي هو 1.

لمراجعة التكوين الحالي لـ wis2downloader، يمكنك استخدام الأمر التالي:

```bash
cat ~/wis2box-1.0.0rc1/wis2box.env | grep DOWNLOAD
```

!!! question "راجع تكوين wis2downloader"
    
    ما هو وسيط MQTT الافتراضي الذي يتصل به wis2downloader؟

    ما هي فترة الاحتفاظ الافتراضية للبيانات المنزلة؟

??? success "انقر للكشف عن الإجابة"

    وسيط MQTT الافتراضي الذي يتصل به wis2downloader هو `globalbroker.meteo.fr`.

    فترة الاحتفاظ الافتراضية للبيانات المنزلة هي 24 ساعة.

!!! note "تحديث تكوين wis2downloader"

    لتحديث تكوين wis2downloader، يمكنك تعديل ملف wis2box.env. لتطبيق التغييرات يمكنك إعادة تشغيل أمر بدء تشغيل مجموعة wis2box-stack:

    ```bash
    python3 wis2box-ctl.py start
    ```

    وسترى خدمة wis2downloader تعيد التشغيل بالتكوين الجديد.

يمكنك الاحتفاظ بالتكوين الافتراضي لغرض هذا التمرين.

## التمرين 3: إضافة اشتراكات إلى wis2downloader

داخل حاوية **wis2downloader**، يمكنك استخدام سطر الأوامر لسرد الاشتراكات النشطة وإضافتها وحذفها.

لتسجيل الدخول إلى حاوية **wis2downloader**، استخدم الأمر التالي:

```bash
python3 wis2box-ctl.py login wis2downloader
```

ثم استخدم الأمر التالي لسرد الاشتراكات النشطة حاليًا:

```bash
wis2downloader list-subscriptions
```

يعيد هذا الأمر قائمة فارغة نظرًا لعدم وجود اشتراكات نشطة حاليًا.

لغرض هذا التمرين، سنشترك في الموضوع التالي `cache/a/wis2/de-dwd-gts-to-wis2/#`، للاشتراك في البيانات التي نشرها بوابة GTS-to-WIS2 المستضافة من DWD وإشعارات التنزيل من الذاكرة العالمية.

لإضافة هذا الاشتراك، استخدم الأمر التالي:

```bash
wis2downloader add-subscription --topic cache/a/wis2/de-dwd-gts-to-wis2/#
```

ثم اخرج من حاوية **wis2downloader** بكتابة `exit`:

```bash
exit
```

تحقق من لوحة تحكم wis2downloader في Grafana لرؤية الاشتراك الجديد المضاف. انتظر بضع دقائق ويجب أن ترى التنزيلات الأولى تبدأ. انتقل إلى التمرين التالي بمجرد تأكيد بدء التنزيلات.

## التمرين 4: عرض البيانات المنزلة

تقوم خدمة wis2downloader في مجموعة wis2box-stack بتنزيل البيانات في دليل 'downloads' في الدليل الذي حددته كـ WIS2BOX_HOST_DATADIR في ملف wis2box.env الخاص بك. لعرض محتويات دليل التنزيلات، يمكنك استخدام الأمر التالي:

```bash
ls -R ~/wis2box-data/downloads
```

لاحظ أن البيانات المنزلة مخزنة في دلائل مسماة بعد الموضوع الذي نُشرت عليه إشعارات WIS2.

## التمرين 5: إزالة الاشتراكات من wis2downloader

بعد ذلك، سجل الدخول مرة أخرى إلى حاوية wis2downloader:

```bash
python3 wis2box-ctl.py login wis2downloader
```

وأزل الاشتراك الذي قمت به من wis2downloader، باستخدام الأمر التالي:

```bash
wis2downloader remove-subscription --topic cache/a/wis2/de-dwd-gts-to-wis2/#
```

واخرج من حاوية wis2downloader بكتابة `exit`:
    
```bash
exit
```

تحقق من لوحة تحكم wis2downloader في Grafana لرؤية إزالة الاشتراك. يجب أن ترى التنزيلات تتوقف.

## التمرين 6: الاشتراك في wis2training-broker وإعداد اشتراك جديد

للتمرين التالي سنشترك في wis2training-broker.

هذا يوضح كيفية الاشتراك في وسيط ليس الوسيط الافتراضي وسيتيح لك تنزيل بعض البيانات التي نشرت من وسيط تدريب WIS2.

عدل ملف wis2box.env وغير DOWNLOAD_BROKER_HOST إلى `wis2training-broker.wis2dev.io`، غير DOWNLOAD_BROKER_PORT إلى `1883` وغير DOWNLOAD_BROKER_TRANSPORT إلى `tcp`:

```copy
# إعدادات التنزيل
DOWNLOAD_BROKER_HOST=wis2training-broker.wis2dev.io
DOWNLOAD_BROKER_PORT=1883
DOWNLOAD_BROKER_USERNAME=everyone
DOWNLOAD_BROKER_PASSWORD=everyone
# آلية نقل التنزيل (tcp أو واجهات الويب)
DOWNLOAD_BROKER_TRANSPORT=tcp
```

ثم أعد تشغيل مجموعة wis2box-stack لتطبيق التغييرات:

```bash
python3 wis2box-ctl.py start
```

تحقق من سجلات wis2downloader لمعرفة ما إذا كان الاتصال بالوسيط الجديد ناجحًا:

```bash
docker logs wis2downloader
```

يجب أن ترى رسالة السجل التالية:

```copy
...
INFO - Connecting...
INFO - Host: wis2training-broker.wis2dev.io, port: 1883
INFO - Connected successfully
```

الآن سنقوم بإعداد اشتراك جديد للموضوع لتنزيل بيانات مسار الإعصار من وسيط تدريب WIS2.

سجل الدخول إلى حاوية **wis2downloader**:

```bash
python3 wis2box-ctl.py login wis2downloader
```

ونفذ الأمر التالي (انسخ والصق هذا لتجنب الأخطاء):

```bash
wis2downloader add-subscription --topic origin/a/wis2/int-wis2-training/data/core/weather/prediction/forecast/medium-range/probabilistic/trajectory
```

اخرج من حاوية **wis2downloader** بكتابة `exit`.

انتظر حتى ترى التنزيلات تبدأ في لوحة تحكم wis2downloader في Grafana.

!!! note "تنزيل البيانات من وسيط تدريب WIS2"

    وسيط تدريب WIS2 هو وسيط اختبار يُستخدم لأغراض التدريب وقد لا ينشر البيانات طوال الوقت.

    خلال جلسات التدريب الشخصية، سيضمن المدرب المحلي أن وسيط تدريب WIS2 سينشر البيانات لك لتنزيلها.

    إذا كنت تقوم بهذا التمرين خارج جلسة تدريب، فقد لا ترى أي بيانات يتم تنزيلها.

تحقق من تنزيل البيانات بفحص سجلات wis2downloader مرة أخرى باستخدام:

```bash
docker logs wis2