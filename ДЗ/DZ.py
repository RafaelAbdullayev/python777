# Решение через функции
import os

my_dirs = [r"work\f1", r"work\f1\f11", r"work\f2", r"work\f2\f21"]
files = {
    "work": ["w.txt", "w_empty.txt"],
    r"work\f1": ["f10.txt", "f11.txt", "f12.txt"],
    r"work\f1\f11": ["run.txt", "default.txt"],
    r"work\f2": ["hello.txt"],
    r"work\f2\f21": ["f210.txt", "f211.txt", "f212.txt"]
}
texted_files = [r"work\w.txt", r"work\F1\f12.txt", r"work\F2\F21\f211.txt", r"work\F2\F21\f212.txt"]
root_dir = "work"
empty_files_dir = r"work\empty_files"


def creator(lst_dirs, dict_files):
    """

    :param
    :param
    """
    for d in lst_dirs:
        if not os.path.exists(d):
            os.makedirs(d)
    for dir_w, f_w in dict_files.items():
        for file_create in f_w:
            file_path = os.path.join(dir_w, file_create)
            open(file_path, "w").close()
    print("Вложенные директории созданы, пустые файлы созданы.", end="\n\n")


def file_writer(lst_files):
    """

    :param
    """
    for file_wr in lst_files:
        with open(file_wr, "w") as fw:
            fw.write(input("Скопируйте из test_text какой-то текст и сделайте вставку-->>"))
    print("\nВыбранные файлы записаны.", end="\n\n")


def stage1(m_dir):
    """

    :param
    """
    print("Записанные файлы и их размер:")
    for root_func, dirs_func, files_func in os.walk(m_dir):
        for file_check in files_func:
            path = os.path.join(root_func, file_check)
            size_file = os.path.getsize(path)
            if size_file > 0:
                print(f"\t{path} - {size_file} bytes")


def stage2(m_dir, m_dir2):
    """

    :param
    :param
    """
    print("\nПеремещенные файлы и их пути:")
    for root_func2, dirs_func2, files_func2 in os.walk(m_dir):
        for file_check in files_func2:
            old_path = os.path.join(root_func2, file_check)
            new_path = os.path.join(m_dir2, file_check)
            size_file = os.path.getsize(old_path)
            if size_file == 0:
                print(f"\tФайл: {file_check}; старый путь:{old_path}; новый путь:{new_path}")
                if not os.path.exists(new_path):
                    os.renames(old_path, new_path)


def cleaner(m_dir2):
    """

    :param m
    """
    dir_empty_lst = os.listdir(m_dir2)
    print(f"\nДиректория {m_dir2}\nСписок пустых файлов: \n\t{dir_empty_lst}", end="\n\n")
    for del_file in dir_empty_lst:
        path_empty = os.path.join(empty_files_dir, del_file)
        os.remove(path_empty)
    print(f"Директория {m_dir2} очищена")


def deleter(m_dir):
    """

    :param m_dir:
    """
    if os.path.exists(m_dir):
        for root_n, dirs_n, files_n in os.walk(m_dir):
            for file_del1 in files_n:
                to_del_file = os.path.join(root_n, file_del1)
                os.remove(to_del_file)
        print(f"Все файлы корневой директории {m_dir} удалены")
        for root_n, dirs_n, files_n in os.walk(m_dir, topdown=False):
            if not os.listdir(root_n):
                os.rmdir(root_n)
        print(f"Вложенные директории {m_dir} удалены. Корневая директория удалена")


test_text = "меня зовут Рафаэль я Студент  топ Академи "

creator(my_dirs, files)
file_writer(texted_files)
stage1(root_dir)
stage2(root_dir, empty_files_dir)
