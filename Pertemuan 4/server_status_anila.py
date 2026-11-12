print("===================================")
print("        SERVER STATUS CHECKER")
print("===================================")

nama_server = input("Nama Server : ")
suhu_cpu = int(input("Suhu CPU    : "))

if suhu_cpu < 40:
    status = "Suhu terlalu rendah"
elif suhu_cpu <= 59:
    status = "Suhu normal"
elif suhu_cpu <= 79:
    status = "Suhu cukup tinggi"
else:
    status = "WARNING! Suhu terlalu tinggi"

print("-----------------------------------")
print("Nama Server :", nama_server)
print("Suhu CPU    :", suhu_cpu, "°C")
print("Status      :", status)
print("===================================")
