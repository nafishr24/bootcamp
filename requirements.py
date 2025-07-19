import ast
import os
import sys
from pathlib import Path

# Untuk versi Python 3.8+, gunakan importlib.metadata
try:
    import importlib.metadata as importlib_metadata
except ImportError:
    # Untuk Python < 3.8
    import importlib_metadata

# Set untuk menyimpan modul unik yang diimpor
modules = set()

# Mapping modul ke nama paket PyPI jika berbeda
module_aliases = {
    'cv2': 'opencv-python',
    'PIL': 'Pillow',
    'sklearn': 'scikit-learn',
    'bs4': 'beautifulsoup4',
}

def find_py_files(root_dir='.'):
    """Mencari semua file .py di direktori dan subdirektori"""
    py_files = []
    for dirpath, _, filenames in os.walk(root_dir):
        # Skip direktori yang tidak perlu (opsional)
        if 'venv' in dirpath or '.env' in dirpath or '__pycache__' in dirpath:
            continue
            
        for filename in filenames:
            if filename.endswith('.py'):
                full_path = os.path.join(dirpath, filename)
                py_files.append(full_path)
    return py_files

def extract_imports(filepath):
    """Ekstrak semua import dari sebuah file Python"""
    with open(filepath, 'r', encoding='utf-8') as file:
        try:
            node = ast.parse(file.read(), filename=filepath)
            for n in ast.walk(node):
                if isinstance(n, ast.Import):
                    for alias in n.names:
                        modules.add(alias.name.split('.')[0])
                elif isinstance(n, ast.ImportFrom):
                    if n.module and n.level == 0:  # Hanya import absolut
                        modules.add(n.module.split('.')[0])
        except SyntaxError as e:
            print(f"[!] Error parsing {filepath}: {e}")

def main():
    # Cari semua file Python
    py_files = find_py_files()
    
    if not py_files:
        print("Tidak ditemukan file .py di direktori ini dan subdirektori")
        return
    
    print(f"Memproses {len(py_files)} file Python...")
    
    # Proses setiap file
    for filepath in py_files:
        extract_imports(filepath)
    
    # Tulis ke requirements.txt
    with open('requirements.txt', 'w') as f:
        for module in sorted(modules):
            package_name = module_aliases.get(module, module)
            try:
                version = importlib_metadata.version(package_name)
                f.write(f"{package_name}=={version}\n")
            except importlib_metadata.PackageNotFoundError:
                print(f"[!] Modul '{module}' tidak ditemukan di environment saat ini (paket PyPI mungkin: {package_name})")

    print("✅ requirements.txt berhasil dibuat dari analisis semua file Python")

if __name__ == '__main__':
    main()