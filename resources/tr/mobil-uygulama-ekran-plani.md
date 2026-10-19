# Mobil uygulama ekran planı ve kabul kontrolü

Brainbaby tarafından hazırlanmış özgün, düzenlenebilir Türkçe planlama kaynağı.

Bu dosya bir uygulama, APK, kaynak kod veya tamamlanmış test raporu değildir. Alışveriş listesi hayali bir örnektir. İndirmek ve planı doldurmak ücretsizdir; Brainbaby oluşturucusunda üretim ve değişiklikler uygulama oluşturma kredilerini kullanır. Güncel maliyeti işlemden önce kontrol edin.

## Kendi projeniz

- Kullanıcı: [kim?]
- Tamamlayacağı tek temel iş: [sonuç?]
- İlk sürümün dışında tutulacaklar: [hesap, ödeme, ortak kullanım vb.]
- Tutulacak veriler: [alanlar?]
- Saklama yeri: [yalnızca cihaz / ayrıca tanımlanacak hizmet]
- Veriyi silme ve iptal davranışı: [kapsam?]
- Hedef cihazlar: [iOS / Android; denenmeyenleri belirtin]

## Hayali örneğin ekran haritası

| Ekran | Kullanıcı hedefi | Ana eylem | İkincil eylem | Veri | Boş ve hata durumları |
| --- | --- | --- | --- | --- | --- |
| Listeler | Liste seçmek veya oluşturmak | Yeni liste | Yeniden adlandır; onaylı sil | Liste kimliği ve adı | Henüz liste yok; kayıt başarısız |
| Liste ayrıntısı | Ürün eklemek ve alınanı işaretlemek | Ürün ekle | Düzenle; sil | Ürün adı; isteğe bağlı miktar; alınma durumu | Boş ad; uzun metin; klavye açık; kayıt hatası |
| Ayarlar | Görünümü ve yerel veriyi yönetmek | Görünümü değiştir | Onaylı veri temizleme | Görünüm tercihi | İptal; temizlik sonrası boş durum |

## Bir ekranı tarif etmek için kopyalayın

### [Ekran adı]

- Açılış yolu: [hangi ekran veya eylemden geliyor?]
- Görünen başlık: [metin]
- Görünen alan etiketleri: [metinler; yalnızca placeholder kullanmayın]
- Ana eylem: [etiket ve sonuç]
- Kaydedilecek veri: [alanlar]
- Kaydetme başarısızsa: [giriş korunuyor mu; hata ve tekrar deneme?]
- Boş durumda: [açıklama ve başlangıç eylemi]
- Klavye açıkken: [ana eyleme ulaşma; kapatma; geri gitme]
- Silme varsa: [kapsam; onay; iptal; işlem sonrası ekran]
- Erişilebilirlik: [metin boyutu; dokunma alanı; ekran okuyucu adı; renk dışı durum işareti]
- Kabul koşulu: [gözlemlenebilir sonuç]

## Örnek üretim talimatı

Türkçe bir alışveriş listesi uygulamasının ilk mobil prototipini oluştur. Listeler, Liste ayrıntısı ve Ayarlar ekranları olsun. Liste oluşturma, yeniden adlandırma ve onaylı silme ekle. Ayrıntıda ürün adı ve isteğe bağlı miktar girilsin; boş ad kaydedilmesin. Alınan ürünün durumu metin ve işaretle anlaşılsın. Veriyi bu cihazda sakla; kayıt başarısızsa başarı gösterme ve kullanıcının girişini koru. Klavye açıkken ekleme düğmesine ulaşılabilsin. Türkçe karakterleri ve büyütülmüş yazıyı kontrol et. İlk sürüme hesap, ödeme, bulut eşitleme veya bildirim ekleme.

Bu talimat istenen davranışı tanımlar; üretilen projenin bunları doğru yaptığına dair kanıt değildir.

## Gerçek testlerden sonra doldurun

| Kontrol | Beklenen | Görülen | Cihaz ve sürüm | Sonuç |
| --- | --- | --- | --- | --- |
| Liste ve ürün ekle; uygulamayı yeniden aç | Kayıt korunur | [doldurun] | [doldurun] | [denenmedi / geçti / kaldı] |
| Boş ürün adı gönder | Kaydedilmez; hata açıklanır | [doldurun] | [doldurun] | [denenmedi / geçti / kaldı] |
| Uzun ad ve Türkçe karakterler | Okunur; taşmaz | [doldurun] | [doldurun] | [denenmedi / geçti / kaldı] |
| Klavye açıkken ana eyleme ulaş | Ekleme düğmesi erişilebilir | [doldurun] | [doldurun] | [denenmedi / geçti / kaldı] |
| Alınan ürünü işaretle | Durum renksiz de anlaşılır | [doldurun] | [doldurun] | [denenmedi / geçti / kaldı] |
| Silmeyi iptal et | Veri korunur | [doldurun] | [doldurun] | [denenmedi / geçti / kaldı] |
| Silmeyi onayla | Yalnızca açıklanan kapsam silinir | [doldurun] | [doldurun] | [denenmedi / geçti / kaldı] |
| Yazıyı büyüt ve görünümü değiştir | Metin ve kontroller kullanılabilir | [doldurun] | [doldurun] | [denenmedi / geçti / kaldı] |

Bir platform denenmediyse test sütununa başarı yazmayın. Çizim veya önizleme, kayıt ve cihaz testinin yerine geçmez. Hata raporlarında gerçek müşteri verisi yerine hayali veri kullanın.

## Kaynaklar ve devam

- Rehber ve özgün ekran çizimi: https://brainbaby.ai/tr/blog/mobil-uygulama-tasarimi
- Mobil oluşturma akışı: https://brainbaby.ai/tr/mobile-apps
- Güncel planlar: https://brainbaby.ai/tr/fiyatlandirma
- Apple gezinme ilkeleri: https://developer.apple.com/design/human-interface-guidelines/tab-bars
- Android erişilebilirlik rehberi: https://developer.android.com/guide/topics/ui/accessibility/apps

Mağaza hesapları, imzalı derleme, izinler, gizlilik açıklamaları ve mağaza incelemesi ayrıca hazırlanır. Bu dosya mağaza onayı veya otomatik yayın vadetmez.

Lisans: CC BY 4.0. Kaynak belirtin: Brainbaby — https://brainbaby.ai/tr/blog/mobil-uygulama-tasarimi
