import os

folder_path = "path/to/folder"  # ana klasör
delta_logs_file = "delta_logs.txt"  # delta_log klasörleri dosyasının adı
parquets_file = "parquets.txt"  # parquet klasörleri dosyasının adı

delta_logs = []  # tüm delta_log klasörlerinin tam yolunu tutacak bir liste
parquets = []  # tüm parquet klasörlerinin tam yolunu tutacak bir liste
delta_path = "_delta_log"

for root, dirs, files in os.walk(folder_path):
    if delta_path in dirs:
        delta_logs.append(os.path.join(root))
    else:
        if not "delta_log" in root:
            parquets.append(root)

# delta_log ve parquet klasörlerinin tam yolunu ilgili dosyalara kaydetme işlemi
with open(delta_logs_file, "w") as f:
    f.write("\n".join(delta_logs))

with open(parquets_file, "w") as f:
    f.write("\n".join(parquets))

# SQL sorgularını hazırlayın ve ilgili dosyaya kaydetme işlemi
with open(delta_logs_file, "r") as f:
    delta_logs = f.readlines()

with open("delta_logs.sql", "w") as f:
    for delta_log in delta_logs:
        table_name = os.path.basename(delta_log)
        f.write(f"CREATE TABLE SHALLOW CLONE {table_name}\n")
