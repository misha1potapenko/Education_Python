import os
from pathlib import Path
# os.mkdir('new_os_dir')
# Path('new_path_dir').mkdir()
# os.makedirs('dir/other_dir/new_os_dir') # создать путь
# os.rmdir('new_os_dir')
# os.rmdir('dir/other_dir/new_os_dir')

# Если необходимо удалить каталог со всем его содержимым (вложенные каталоги и
# файлы), подойдёт функция из модуля shutil
import shutil
shutil.rmtree('dir/other_dir')
shutil.rmtree('some_dir')
