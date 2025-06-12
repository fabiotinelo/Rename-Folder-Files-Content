import os

root_dir = r"C:\Projects\Globant.GCode"
old_word = "Globant"
new_word = "FTI"

# 1. Renomeia pastas
for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
    for dirname in dirnames:
        if old_word in dirname:
            old_dir = os.path.join(dirpath, dirname)
            new_dir = os.path.join(dirpath, dirname.replace(old_word, new_word))
            print(f'Renomeando pasta: "{old_dir}" -> "{new_dir}"')
            os.rename(old_dir, new_dir)

# 2. Renomeia arquivos
for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        if old_word in filename:
            old_file = os.path.join(dirpath, filename)
            new_file = os.path.join(dirpath, filename.replace(old_word, new_word))
            print(f'Renomeando arquivo: "{old_file}" -> "{new_file}"')
            os.rename(old_file, new_file)

# 3. Altera conteúdo dos arquivos .cs, .csproj e .sln
for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.endswith(('.cs', '.csproj', '.sln')):
            file_path = os.path.join(dirpath, filename)
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                if old_word in content:
                    new_content = content.replace(old_word, new_word)
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f'Alterado conteúdo em: "{file_path}"')
            except Exception as e:
                print(f'Erro ao processar "{file_path}": {e}')
