def askValue():
  money = raw_input("Masukkan total uang yang dapat dipergunakan: ")
  validationMoney(money)

def validationMoney(money):
  if money != "":
    money = int(money)
    count(money)
  else:
    print "Nilai kosong"
    restart = raw_input("Apakah ingin masukkan lagi (y/n): ")
    if restart == "y":
      askValue()  
    else:
      quit()

def count(money):
  investasi = (money * 25)/100 
  liburan = (money * 10)/100
  selfImprovement = (money * 15)/100
  bersosialisasi = (money * 20)/100
  days = (money * 30)/100
  print "total cash yang dapat dipergunakan: ", '{:,}'.format(money) 
  print "----------===-----------"
  print "investasi: ", '{:,}'.format(investasi) 
  print "Dibagi menjadi: \n*Nikah\n*Ke Israel\n*DP Tenjo City J6-35\n*Administrasi Cicilan Sentra Finance\n"
  print "----------===-----------"
  print "liburan: ", '{:,}'.format(liburan) 
  print "Dibagi menjadi: \n*Pacaran\n"
  print "----------===-----------"
  print "Pengembangan diri: ", '{:,}'.format(selfImprovement) 
  print "Dibagi menjadi: \n*Kuliah\n*Pelatihan Online\n*Kartu Kredit\n"
  print "----------===-----------"
  print "bersosialisasi: ", '{:,}'.format(bersosialisasi) 
  print "Dibagi menjadi: \n*Perpuluhan\n*Sedekah\n"
  print "----------===-----------"
  print "Sehari hari: ", '{:,}'.format(days) 
  print "Dibagi menjadi: \n*Makan\n*Wifi\n*Minyak Motor\n*Cuci Motor + Helm\n*Servis Motor\n*Oli Motor\n*Tabungan 500ribu\n*Kos\n*Kuota Internet"


askValue()

