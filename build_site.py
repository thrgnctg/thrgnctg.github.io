#!/usr/bin/env python3
"""Build the dependency-free, bilingual GitHub Pages site for ShiftLife."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BASE = "https://thrgnctg.github.io"
GOOGLE_SITE_VERIFICATION = "ZOvy3cL8KDfEu2qvsGk_tlrdckcJPJMAosgKHQQffbM"
DATE_TR = "26 Eylül 2026"
DATE_EN = "September 26, 2026"

PAGES = {
    "home": {
        "tr": {
            "path": "/", "title": "ShiftLife · Vardiya Ritmi",
            "description": "Vardiya döngüne göre gününü, hedeflerini ve dinlenmeni planla.",
            "eyebrow": "VARDİYA DÖNGÜSÜNE GÖRE YAŞAM PLANI",
            "heading": "Vardiyan değişir.<br>Ritmin sana ait kalır.",
            "lead": "ShiftLife, haftaya sığmayan vardiya düzenini bir döngü olarak kurmana; iş, dinlenme, rutin ve hedeflerine ayırdığın zamanı aynı planda görmene yardımcı olan iPhone uygulamasıdır.",
            "body": """
<section class="card-grid" aria-label="Özellikler">
  <article class="card"><span class="card-index">01</span><h2>Döngünü kur</h2><p>Vardiya pencerelerini ve gün şablonlarını tanımla. Bugün ve gelecek günlerin planı döngünden hesaplanır.</p></article>
  <article class="card"><span class="card-index">02</span><h2>Hayatına yer aç</h2><p>Rutinlerini, projelerini ve hedeflerini planına bağla. Gerçekleşen çalışmanı ve ritmini Analiz’de izle.</p></article>
  <article class="card"><span class="card-index">03</span><h2>İstersen bağla</h2><p>İzin verirsen vardiya ve devir saatlerini Apple Takvim veya Google Calendar’a yaz; son yedi günün uyku, adım ve aktif enerji özetini Apple Sağlık’tan gör.</p></article>
</section>
<section class="notice"><h2>Kontrol sende</h2><p>Hesap açmadan kullanabilirsin. Planların bu sürümde cihazında saklanır; otomatik cihazlar arası ShiftLife eşitlemesi yoktur. Takvim ve Sağlık bağlantıları isteğe bağlıdır. Veri kullanımını <a href="/privacy/">Gizlilik Politikası</a> sayfasında açıkça anlatıyoruz.</p></section>
""",
        },
        "en": {
            "path": "/en/", "title": "ShiftLife · Shift Rhythm",
            "description": "Plan your days, goals, and rest around your shift cycle.",
            "eyebrow": "LIFE PLANNING AROUND SHIFT CYCLES",
            "heading": "Your shifts change.<br>Keep your own rhythm.",
            "lead": "ShiftLife is an iPhone app that helps you build a repeating shift cycle and see work, rest, routines, and goals in one plan, even when your schedule does not fit a seven day week.",
            "body": """
<section class="card-grid" aria-label="Features">
  <article class="card"><span class="card-index">01</span><h2>Build your cycle</h2><p>Set shift windows and day templates. Your plan for today and upcoming days is calculated from that cycle.</p></article>
  <article class="card"><span class="card-index">02</span><h2>Make room for life</h2><p>Connect routines, projects, and goals to your plan. Review completed work and your rhythm in Analytics.</p></article>
  <article class="card"><span class="card-index">03</span><h2>Connect if you choose</h2><p>With permission, write shift and handover times to Apple Calendar or Google Calendar, and view seven day sleep, step, and active energy summaries from Apple Health.</p></article>
</section>
<section class="notice"><h2>You stay in control</h2><p>You can use ShiftLife without an account. Plans are stored on your device in this release; automatic ShiftLife sync across devices is not available. Calendar and Health connections are optional. Read our <a href="/en/privacy/">Privacy Policy</a> for details.</p></section>
""",
        },
    },
    "privacy": {
        "tr": {
            "path": "/privacy/", "title": "Gizlilik Politikası · ShiftLife",
            "description": "ShiftLife uygulamasının verileri nasıl kullandığını öğrenin.",
            "eyebrow": "GİZLİLİK POLİTİKASI", "heading": "Verilerin nasıl kullanılır?",
            "lead": f"Son güncelleme: {DATE_TR}. ShiftLife, LIFEDEVLABS adı altında TAHIR GENCTOG tarafından sunulur. Soruların için <a href=\"mailto:tahirgenctog@icloud.com\">tahirgenctog@icloud.com</a> adresine yazabilirsin.",
            "body": """
<div class="legal">
<section><h2>1. Cihazında tuttuğumuz veriler</h2><p>Vardiya döngülerin, gün şablonların, hedeflerin, projelerin, rutinlerin, oturum notların, gerçekleşen kayıtların, profil adın ve seçtiğin fotoğraf ile uygulama ayarların cihazında saklanır. Bunları çalıştırmak için bize ait bir sunucuya yüklemeyiz. Bu sürümde ShiftLife planları için otomatik cihazlar arası iCloud eşitlemesi yoktur. iOS cihaz yedekleme ayarların ayrıca geçerli olabilir.</p><p>Uygulama içinden JSON yedeği veya CSV dosyası dışa aktarırsan paylaşacağın konumu sen seçersin. Dışa aktarılan dosyalar uygulamadaki verileri içerebilir; onları sakladığın hizmetin kuralları geçerlidir.</p></section>
<section><h2>2. İsteğe bağlı hesap girişi</h2><p>Hesap açmadan devam edebilirsin. Apple ile girişte Apple’ın verdiği hesap kimliğini ve varsa adı, Google ile girişte Google hesap kimliğini ve varsa adı veya e posta adresini yalnız cihazındaki profil bağı için kullanırız. Google profil girişinde alınan kimlik belirtecini saklamayız. Giriş sağlayıcıları kendi gizlilik kurallarına göre işlem yapar.</p></section>
<section><h2>3. İsteğe bağlı takvim bağlantıları</h2><p>Apple Takvim’i bağlarsan iOS takvim izniyle seçtiğin hesapta ayrı bir ShiftLife takvimi oluştururuz. Vardiya ve devir saatlerinin başlık, başlangıç, bitiş ve saat dilimi bilgilerini bu takvime yazarız. Senkron tek yönlüdür: ShiftLife’tan takvime. Seçtiğin takvim hesabı iCloud veya başka bir sağlayıcıyla eşitleniyorsa bu olayları o sağlayıcı işler.</p><p>Google Calendar’ı bağlarsan Google hesabının kimlik ve e posta bilgisini bağlantıyı tanımak için alırız; takvim listesini okur, yalnız uygulamanın oluşturduğu ayrı ShiftLife takvimindeki olayları yönetiriz. Uygulama, yaklaşık 90 günlük vardiya ve devir olaylarının başlık, zaman, saat dilimi ve yönetim işaretlerini doğrudan Google’a gönderir. Diğer takvimlerindeki etkinlikleri ShiftLife planına almayız. Google yenileme anahtarı cihazının anahtar zincirinde, erişim anahtarı yalnız bellekte tutulur. Bu verileri reklam, satış veya başka amaç için kullanmayız.</p><p>Bağlantıyı normal yoldan kapatırken gelecekteki yönetilen olayları silmeyi deneriz. Geçmiş olaylar ve oluşturulan takvim kalır. Ağ veya izin sorunu nedeniyle temizlik tamamlanamazsa uzaktaki gelecekteki olaylar da kalabilir; bunları takvim sağlayıcında yönetebilirsin.</p></section>
<section><h2>4. İsteğe bağlı Apple Sağlık</h2><p>İzin verirsen son yedi günün uyku, adım ve aktif enerji verilerini Analiz’de özetlemek için Apple Sağlık’tan okuruz. Bu okunan sağlık verilerini sunucumuza göndermeyiz. Yalnız senin onaylayıp saatlerini seçtiğin tamamlanmış bir uyku aralığını Apple Sağlık’a yazarız. Tekrar yazmayı önleyen zaman ve işlem kayıtları cihazında korumalı bir dosyada tutulur. Uygulama verilerini silmen, Apple Sağlık’ta daha önce oluşturulan kayıtları silmez; onları Sağlık uygulamasından yönetebilirsin.</p></section>
<section><h2>5. Bildirimler, widget’lar ve satın alımlar</h2><p>İzin verirsen hatırlatıcılar cihazında planlanır. Widget verisi aynı cihazdaki uygulama ile paylaşılır. Kilit ekranında kişisel adların görünmesini uygulama ayarından kapatabilirsin.</p><p>Pro satın alımları Apple’ın StoreKit sistemiyle işlenir. Ödeme bilgilerini biz almayız; uygulama doğrulanmış satın alma hakkını kontrol eder ve cihazda bir durum kaydı tutar. Aboneliğini Apple hesabından yönetirsin.</p></section>
<section><h2>6. Paylaşım, destek ve web sitesi</h2><p>Uygulamada reklam, üçüncü taraf analiz SDK’sı veya takip amaçlı veri paylaşımı yoktur. Verileri yalnız seçtiğin Apple/Google bağlantısının çalışması için ilgili sağlayıcıya iletiriz. Bize e posta gönderirsen adresini ve mesaj içeriğini destek isteğini yanıtlamak için kullanırız. Bu web sitesi GitHub Pages üzerinde barındırılır; sitede analiz veya takip betiği kullanmıyoruz. GitHub erişim kayıtlarını kendi <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement">gizlilik bildirimi</a> kapsamında işleyebilir.</p></section>
<section><h2>7. Silme ve başvuru</h2><p>Uygulamadaki <strong>Ayarlar → Veri &amp; yedekleme → Tüm verileri sil</strong> veya <strong>Ayarlar → Hesap → Hesabı ve verileri sil</strong> akışlarını kullanabilirsin. Google Takvim bağlantısını Ayarlar’dan ayırabilir; Google hesabındaki erişim izinlerini ayrıca kaldırabilirsin. Apple Sağlık ve takvim sağlayıcındaki kayıtlar için ilgili uygulamayı kullan. Daha önce dışa aktardığın dosyaları seçtiğin konumdan ayrıca silmen gerekir.</p><p>Gizlilik sorusu, erişim veya silme talebi için <a href="mailto:tahirgenctog@icloud.com">tahirgenctog@icloud.com</a> adresine yaz. Destek yazışmalarını talebi çözmek ve yasal yükümlülükleri yerine getirmek için gerekli olduğu sürece tutarız.</p></section>
<section><h2>8. Değişiklikler</h2><p>Uygulamanın veri uygulamaları değişirse bu politikayı güncelleriz. Güncel tarihi bu sayfanın başında gösteririz.</p></section>
</div>
""",
        },
        "en": {
            "path": "/en/privacy/", "title": "Privacy Policy · ShiftLife",
            "description": "Learn how the ShiftLife app uses data.",
            "eyebrow": "PRIVACY POLICY", "heading": "How your data is used",
            "lead": f"Last updated: {DATE_EN}. ShiftLife is provided by TAHIR GENCTOG under the LIFEDEVLABS name. For questions, email <a href=\"mailto:tahirgenctog@icloud.com\">tahirgenctog@icloud.com</a>.",
            "body": """
<div class="legal">
<section><h2>1. Data stored on your device</h2><p>Your shift cycles, day templates, goals, projects, routines, session notes, activity records, profile name and selected photo, and app settings are stored on your device. We do not upload them to a server that we operate. Automatic iCloud sync of ShiftLife plans across devices is not available in this release. Your iOS device backup settings may still apply.</p><p>If you export a JSON backup or CSV file in the app, you choose where to share it. Exported files may contain your app data and are subject to the rules of the service where you store them.</p></section>
<section><h2>2. Optional sign in</h2><p>You can continue without an account. With Apple sign in, we use the account identifier and, if provided, your name only for the profile link stored on your device. With Google sign in, we use the Google account identifier and, if provided, your name or email address for that local profile link. We do not retain the Google ID token used for profile sign in. The sign in providers process requests under their own privacy policies.</p></section>
<section><h2>3. Optional calendar connections</h2><p>If you connect Apple Calendar, we use iOS calendar permission to create a separate ShiftLife calendar in the account you select. We write shift and handover event titles, start and end times, and time zones to that calendar. Sync runs one way, from ShiftLife to your calendar. If your selected calendar account syncs with iCloud or another provider, that provider processes those events.</p><p>If you connect Google Calendar, we receive your Google account identifier and email to identify the connection, read your calendar list, and manage events only in a separate calendar created by the app. The app sends titles, times, time zones, and management markers for about 90 days of shift and handover events directly to Google. We do not import events from your other calendars into your ShiftLife plan. The Google refresh token is held in your device Keychain; the access token is held only in memory. We do not use this data for advertising, sale, or other purposes.</p><p>When you disconnect normally, we try to remove future events managed by the app. Past events and the created calendar remain. If cleanup cannot finish because of a network or permission issue, future events may remain remotely too; you can manage them in your calendar provider.</p></section>
<section><h2>4. Optional Apple Health</h2><p>With your permission, we read sleep, step, and active energy data from Apple Health to display a summary of the past seven days in Analytics. We do not send the Health data we read to our server. We write a completed sleep interval to Apple Health only after you confirm it and select its times. Time and operation records that prevent duplicate writes are kept in a protected file on your device. Deleting app data does not delete records already written to Apple Health; you can manage those in the Health app.</p></section>
<section><h2>5. Notifications, widgets, and purchases</h2><p>With your permission, reminders are scheduled on your device. Widget data is shared with the app on that same device. You can turn off personal names on the lock screen in app settings.</p><p>Pro purchases are processed by Apple's StoreKit system. We do not receive your payment details. The app checks verified purchase entitlements and keeps a local status record. You manage subscriptions through your Apple account.</p></section>
<section><h2>6. Sharing, support, and this website</h2><p>The app has no ads, third party analytics SDK, or tracking data sharing. We send data to Apple or Google only to run the connections you choose. If you email us, we use your address and message to respond to your support request. This website is hosted on GitHub Pages and uses no analytics or tracking scripts. GitHub may process access logs under its own <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement">privacy statement</a>.</p></section>
<section><h2>7. Deletion and requests</h2><p>Use <strong>Settings → Data &amp; Backup → Delete all data</strong> or <strong>Settings → Account → Delete account and data</strong> in the app. You can disconnect Google Calendar in Settings and separately remove access in your Google account. Use the relevant app to manage records held by Apple Health or your calendar provider. Files that you exported earlier must be deleted separately from wherever you saved them.</p><p>For privacy questions, access, or deletion requests, email <a href="mailto:tahirgenctog@icloud.com">tahirgenctog@icloud.com</a>. We keep support correspondence as needed to resolve requests and meet legal obligations.</p></section>
<section><h2>8. Changes</h2><p>We will update this policy if the app's data practices change. The current date appears at the top of this page.</p></section>
</div>
""",
        },
    },
    "support": {
        "tr": {
            "path": "/support/", "title": "Destek · ShiftLife",
            "description": "ShiftLife destek ve iletişim bilgileri.",
            "eyebrow": "DESTEK", "heading": "Yardım için buradayız.",
            "lead": "Uygulama, satın alma, bağlantı veya gizlilik soruların için doğrudan geliştiriciye yaz.",
            "body": """
<div class="legal">
<section class="contact"><h2>E posta</h2><p><a class="email" href="mailto:tahirgenctog@icloud.com?subject=ShiftLife%20Destek">tahirgenctog@icloud.com</a></p><p>Mesajına mümkünse uygulama sürümünü, iOS sürümünü ve sorunu yeniden oluşturan adımları ekle. Sağlık verisi veya hesap şifresi göndermene gerek yok.</p></section>
<section><h2>Satın alım ve abonelik</h2><p>Uygulamada <strong>Ayarlar → Hesap → Satın alımı geri yükle</strong> yolunu deneyebilirsin. Abonelik iptali ve yönetimi Apple hesabındaki abonelik ekranından yapılır. Ödeme ve geri ödeme taleplerini Apple yönetir.</p></section>
<section><h2>Takvim ve Sağlık bağlantıları</h2><p>Bağlantı durumunu uygulamadaki <strong>Ayarlar → Takvim senkronu</strong> ve <strong>Ayarlar → Apple Health</strong> sayfalarından görebilirsin. İzinleri iOS Ayarlar’dan da değiştirebilirsin. Google bağlantısını kapatırken ağ bağlantısı ve Google hesabına erişim gerekebilir.</p></section>
<section><h2>Verilerini yönet</h2><p>JSON yedeği alma, içe aktarma ve tüm uygulama verilerini silme seçenekleri <strong>Ayarlar → Veri &amp; yedekleme</strong> altında bulunur. Veri kullanımı ve sağlayıcılardaki kayıtların nasıl yönetileceği <a href="/privacy/">Gizlilik Politikası</a> sayfasında anlatılır.</p></section>
</div>
""",
        },
        "en": {
            "path": "/en/support/", "title": "Support · ShiftLife",
            "description": "ShiftLife support and contact information.",
            "eyebrow": "SUPPORT", "heading": "We're here to help.",
            "lead": "Email the developer with questions about the app, purchases, connections, or privacy.",
            "body": """
<div class="legal">
<section class="contact"><h2>Email</h2><p><a class="email" href="mailto:tahirgenctog@icloud.com?subject=ShiftLife%20Support">tahirgenctog@icloud.com</a></p><p>If possible, include the app version, iOS version, and steps to reproduce the problem. You do not need to send Health data or your account password.</p></section>
<section><h2>Purchases and subscriptions</h2><p>Try <strong>Settings → Account → Restore purchases</strong> in the app. Manage or cancel a subscription in your Apple account's subscriptions screen. Apple handles billing and refund requests.</p></section>
<section><h2>Calendar and Health connections</h2><p>Check connection status in <strong>Settings → Calendar sync</strong> and <strong>Settings → Apple Health</strong> in the app. You can also change permissions in iOS Settings. Disconnecting Google may require network access and access to your Google account.</p></section>
<section><h2>Manage your data</h2><p>JSON backup, import, and deletion options are under <strong>Settings → Data &amp; Backup</strong>. Our <a href="/en/privacy/">Privacy Policy</a> explains data use and how to manage records with other providers.</p></section>
</div>
""",
        },
    },
    "terms": {
        "tr": {
            "path": "/terms/", "title": "Kullanım Koşulları · ShiftLife",
            "description": "ShiftLife için geçerli Apple Standart Son Kullanıcı Lisans Sözleşmesi.",
            "eyebrow": "KULLANIM KOŞULLARI", "heading": "Uygulama lisansı",
            "lead": "ShiftLife, Apple App Store üzerinden sunulur. Uygulamanın kullanımına Apple’ın Standart Son Kullanıcı Lisans Sözleşmesi uygulanır.",
            "body": """
<div class="legal"><section class="contact"><h2>Geçerli sözleşme</h2><p><a class="button" href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">Apple Standart Lisans Sözleşmesi ↗</a></p><p>Bu bağlantı Apple’ın yayımladığı güncel sözleşmeye gider. Bu sayfa ayrı bir özel lisans sözleşmesi oluşturmaz.</p></section><section><h2>Pro satın alımları</h2><p>Abonelik ve uygulama içi satın alma koşulları, fiyat, süre ve varsa deneme teklifi satın alma ekranında gösterilir. Abonelik yönetimi ve iptali Apple hesabından yapılır. Satın alma soruları için <a href="/support/">Destek</a> sayfasını kullanabilirsin.</p></section><section><h2>Gizlilik</h2><p>Uygulamanın veri kullanımını <a href="/privacy/">Gizlilik Politikası</a> açıklar.</p></section></div>
""",
        },
        "en": {
            "path": "/en/terms/", "title": "Terms · ShiftLife",
            "description": "Apple's Standard End User License Agreement applies to ShiftLife.",
            "eyebrow": "TERMS", "heading": "App license",
            "lead": "ShiftLife is distributed through the Apple App Store. Apple's Standard End User License Agreement applies to use of the app.",
            "body": """
<div class="legal"><section class="contact"><h2>Applicable agreement</h2><p><a class="button" href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">Apple Standard EULA ↗</a></p><p>This link opens Apple's current published agreement. This page does not create a separate custom license agreement.</p></section><section><h2>Pro purchases</h2><p>Subscription and in app purchase terms, prices, duration, and any trial offer are shown before purchase. Manage or cancel subscriptions through your Apple account. For purchase questions, see <a href="/en/support/">Support</a>.</p></section><section><h2>Privacy</h2><p>Our <a href="/en/privacy/">Privacy Policy</a> explains the app's data practices.</p></section></div>
""",
        },
    },
}

NAV = {
    "tr": [("/", "Ana sayfa"), ("/privacy/", "Gizlilik"), ("/support/", "Destek"), ("/terms/", "Koşullar")],
    "en": [("/en/", "Home"), ("/en/privacy/", "Privacy"), ("/en/support/", "Support"), ("/en/terms/", "Terms")],
}

def render(kind: str, lang: str) -> str:
    item = PAGES[kind][lang]
    other = "en" if lang == "tr" else "tr"
    other_item = PAGES[kind][other]
    nav = "".join(
        f'<a href="{path}"{" aria-current=\"page\"" if path == item["path"] else ""}>{label}</a>'
        for path, label in NAV[lang]
    )
    switch_label = "English" if lang == "tr" else "Türkçe"
    footer = "TAHIR GENCTOG · LIFEDEVLABS" if lang == "tr" else "TAHIR GENCTOG · LIFEDEVLABS"
    verification_meta = (
        f'  <meta name="google-site-verification" content="{GOOGLE_SITE_VERIFICATION}" />\n'
        if kind == "home" and lang == "tr" else ""
    )
    return f'''<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
{verification_meta}  <meta name="color-scheme" content="light dark">
  <meta name="description" content="{item['description']}">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{item['title']}">
  <meta property="og:description" content="{item['description']}">
  <meta property="og:url" content="{BASE}{item['path']}">
  <link rel="canonical" href="{BASE}{item['path']}">
  <link rel="alternate" hreflang="tr" href="{BASE}{PAGES[kind]['tr']['path']}">
  <link rel="alternate" hreflang="en" href="{BASE}{PAGES[kind]['en']['path']}">
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  <link rel="stylesheet" href="/style.css">
  <title>{item['title']}</title>
</head>
<body>
<a class="skip" href="#content">{"İçeriğe geç" if lang == "tr" else "Skip to content"}</a>
<header class="site-header"><div class="shell header-inner">
  <a class="brand" href="{'/' if lang == 'tr' else '/en/'}" aria-label="ShiftLife"><img src="/favicon.svg" alt="" width="32" height="32"><span>ShiftLife</span></a>
  <nav aria-label="{'Ana menü' if lang == 'tr' else 'Main menu'}">{nav}</nav>
  <a class="lang" href="{other_item['path']}" lang="{other}" hreflang="{other}">{switch_label}</a>
</div></header>
<main id="content" class="shell">
  <div class="hero"><p class="eyebrow">{item['eyebrow']}</p><h1>{item['heading']}</h1><p class="lead">{item['lead']}</p></div>
{item['body']}
</main>
<footer class="site-footer"><div class="shell footer-inner"><p>© 2026 {footer}</p><p><a href="{'/privacy/' if lang == 'tr' else '/en/privacy/'}">{'Gizlilik' if lang == 'tr' else 'Privacy'}</a> · <a href="{'/support/' if lang == 'tr' else '/en/support/'}">{'Destek' if lang == 'tr' else 'Support'}</a> · <a href="{'/terms/' if lang == 'tr' else '/en/terms/'}">{'Koşullar' if lang == 'tr' else 'Terms'}</a></p></div></footer>
</body>
</html>
'''

for kind, localized in PAGES.items():
    for lang, item in localized.items():
        path = ROOT / item["path"].lstrip("/") / "index.html"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(render(kind, lang), encoding="utf-8")

urls = "\n".join(f"  <url><loc>{BASE}{item['path']}</loc></url>" for page in PAGES.values() for item in page.values())
(ROOT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n', encoding="utf-8")
