money = input("Masukkan total uang yang dapat dipergunakan: ")
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