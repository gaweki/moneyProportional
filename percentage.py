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
  print "----------===-----------"
  print "liburan: ", '{:,}'.format(liburan) 
  print "----------===-----------"
  print "Pengembangan diri: ", '{:,}'.format(selfImprovement) 
  print "----------===-----------"
  print "bersosialisasi: ", '{:,}'.format(bersosialisasi) 
  print "----------===-----------"
  print "Sehari hari: ", '{:,}'.format(days) 


askValue()

