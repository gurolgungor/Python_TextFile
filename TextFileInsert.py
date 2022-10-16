#-------------------------------------------------------------------------------
# Name:        TextFileInsert.py
# Purpose:
#
# Author:      Gürol Güngör
#
# Created:     16.10.2022
# Copyright:   (c) Gürol Güngör 2022
# Licence:     GNU - General Public Licence
#-------------------------------------------------------------------------------

#Text dosyası yeri ve adi tanımlanır
TextDosyasi = r"C:\Database\TextFile.txt"

#Text dosya olusturuluyor.
f = open(TextDosyasi,"w")

#Text dosyaya kayit yaziliyor
f.write("Merhaba Dünya")

#islem detayi yazilir.
print(f)

#Text dosyayı kapatıyoruz
f.close()

