# Tapşırıq 1: Sıralı Siyahı
def siyahi_duzelt():
   istifadeci_siyahisi = []
   for i in range(1, 6):
       istifadeci_daxili = int(input(f"{i}. ədədi daxil edin: "))
       istifadeci_siyahisi.append(istifadeci_daxili)
   siralanmis_siyahi = sorted(istifadeci_siyahisi)
   print(f"Sıralanmış siyahı: {siralanmis_siyahi}")

# Tapşırıq 2: Sözləri Əlifba Sırasına Düzmə
def sozleri_sirala():
   cumle = input("Cümləni daxil edin: ").strip()
   siralanmis_sozler = " ".join(["".join(sorted(soz)) for soz in cumle.split()])
   print(f"Əlifba sırasına görə sözlər: {siralanmis_sozler}")

# Tapşırıq 3: Ədəd Tapmaq Oyunu
def ededi_tap():
   hedefe_eded = 13
   cehdler = []
   while True:
       tehmin = int(input("Ədədi təxmin edin: "))
       cehdler.append(tehmin)
       if tehmin == hedefe_eded:
           cehd_sayi = len(cehdler)
           print(f"\nTəbriklər! {cehd_sayi} cəhddə ədədi tapdınız.")
           for i, cehd in enumerate(cehdler, start=1):
               print(f"{i}. cəhd: {cehd}")
           break

# Tapşırıq 4: Sadə Ədədlər
def sade_ededleri_cixart():
   sade_ededler = []
   for eded in range(1, 101):
       if all(eded % i != 0 for i in range(2, int(eded ** 0.5) + 1)):
           sade_ededler.append(eded)
   print(f"Sadə ədədlər: {sade_ededler}")

# Ana Proqram
while True:
   tapsirig_secimi = input("Tapşırıq nömrəsini daxil edin (1-4) və ya çıxmaq üçün 'q' düyməsini basın: ")
   if tapsirig_secimi == '1':
       siyahi_duzelt()
   elif tapsirig_secimi == '2':
       sozleri_sirala()
   elif tapsirig_secimi == '3':
       ededi_tap()
   elif tapsirig_secimi == '4':
       sade_ededleri_cixart()
   elif tapsirig_secimi.lower() == 'q':
       break
   else:
       print("Yanlış bir seçim etdiniz. Zəhmət olmasa yenidən cəhd edin.")
