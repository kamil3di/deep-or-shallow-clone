import os

folder_path = "/path/to/folder"  # ana klasör yolunu belirleyin
delta_logs_file = "delta_logs.txt"  # delta_log klasörleri dosyasının adını belirleyin
parquets_file = "parquets.txt"  # parquet klasörleri dosyasının adını belirleyin

delta_logs = []  # tüm delta_log klasörlerinin tam yolunu tutacak bir liste oluşturun
parquets = []  # tüm parquet klasörlerinin tam yolunu tutacak bir liste oluşturun

for root, dirs, files in os.walk(folder_path):
    if "delta_log" in dirs:
        delta_logs.append(os.path.join(root))
    else:
        if not "delta_log" in root:
            parquets.append(root)

# delta_log ve parquet klasörlerinin tam yolunu ilgili dosyalara kaydedin
with open(delta_logs_file, "w") as f:
    f.write("\n".join(delta_logs))

with open(parquets_file, "w") as f:
    f.write("\n".join(parquets))
