data = "Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n"
file1 = "file_start.txt"
file2 = "file_res.txt"


def file_change_line(my_data, f1, f2, p1, p2):
    with open(f1, "w+") as fr, open(f2, "w+") as fw:
        fr.write(my_data)
        fr.seek(0)
        lst = fr.readlines()
        fr.seek(0)
        if 0 <= p1 <= len(lst) - 1 and 0 <= p2 <= len(lst) - 1:
            if p1 != p2:
                lst[p1], lst[p2] = lst[p2], lst[p1]
                fw.writelines(lst)
                fw.seek(0)
                print("Изменение позиции строк произведено успешно\n")
            else:
                fw.writelines(lst)
                fw.seek(0)
                print("Изменение позиции строк не произведено\n")
        else:
            if (p1 < 0 or p1 > len(lst) - 1) and (p2 < 0 or p2 > len(lst) - 1):
                print(f"Строк с номерами: ({pos1},{pos2}) - нет в файле {file1}.\n")
            else:
                res = pos1 if (p1 < 0 or p1 > len(lst) - 1) else pos2
                print(f"Строки с номером: {res} - не существует в файле {file1}.\n")
        print(f"Содержимое файла {file1}:")
        print(fr.read(), end="\n")
        print(f"Содержимое файла {file2}:")
        print(fw.read())


pos1 = int(input("Номер первой строки: "))
pos2 = int(input("Номер второй строки: "))
file_change_line(data, file1, file2, pos1, pos2)

