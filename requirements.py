import ast
import os
import sys

# Untuk versi Python 3.8+, gunakan importlib.metadata
try:
    import importlib.metadata as importlib_metadata
except ImportError:
    # Untuk Python < 3.8
    import importlib_metadata

# Daftar file target yang ingin discan
files_to_scan = [
    'Day-1/main.py',
    'Day-1/main2.py',
    'Day-2/main.py',
]

# Set untuk menyimpan modul unik yang diimpor
modules = set()

# Mapping modul ke nama paket PyPI jika berbeda
module_aliases = {
    'cv2': 'opencv-python',
    'PIL': 'Pillow',
}

# Scan file dan ambil semua import
for filepath in files_to_scan:
    if not os.path.exists(filepath):
        print(f"[!] File tidak ditemukan: {filepath}")
        continue

    with open(filepath, 'r', encoding='utf-8') as file:
        node = ast.parse(file.read(), filename=filepath)
        for n in ast.walk(node):
            if isinstance(n, ast.Import):
                for alias in n.names:
                    modules.add(alias.name.split('.')[0])
            elif isinstance(n, ast.ImportFrom):
                if n.module:
                    modules.add(n.module.split('.')[0])

# Langsung simpan ke requirements.txt dengan versi
with open('requirements.txt', 'w') as f:
    for module in sorted(modules):
        package_name = module_aliases.get(module, module)
        try:
            version = importlib_metadata.version(package_name)
            f.write(f"{package_name}=={version}\n")
        except importlib_metadata.PackageNotFoundError:
            print(f"[!] Modul '{module}' tidak ditemukan di environment saat ini.")

print("✅ requirements.txt berhasil dibuat langsung dari file Python")