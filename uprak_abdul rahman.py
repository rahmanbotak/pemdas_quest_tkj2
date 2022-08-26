print("1.balokk")

p = int(input("masukan nilai panjang"))
l = int(input("masukan nilai lebar"))
t = int(input("masukan niali tinggi"))
volume_plt = p * l * t
print("volume balok adalah", volume_plt)

print("2.limas")
la = int(input("masukan nilai luas alas: "))
t = int(input("masukan nilai tinggi: "))
volume_la = 1/3 * la * t
print("volume limas adalah",volume_la)

print("3.tabung")
la = int(input("masukan niali luas alas: "))
t = int(input("masukan niali tinggi: "))
volume_t = la * t
print("volume tabung adalah", volume_t)

kursDolar = 14800
rupiah = float(input("masukan uang rupiah= "))
rupToDol = rupiah/ kursDolar
