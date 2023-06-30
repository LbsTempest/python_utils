import os


def sort_and_rename_files(folder_path, file_extension):
    # 获取文件夹中指定类型的文件
    files = [file for file in os.listdir(folder_path) if file.endswith(file_extension)]

    # 根据文件名进行排序
    files.sort()

    # 重命名文件
    for i, file in enumerate(files):
        # 构建新的文件名
        new_name = f"{i + 1}.{file_extension}"

        # 旧文件的完整路径
        old_path = os.path.join(folder_path, file)

        # 新文件的完整路径
        new_path = os.path.join(folder_path, new_name)

        # 重命名文件
        os.rename(old_path, new_path)
        print(f"重命名文件: {file} -> {new_name}")


# 指定文件夹路径和文件扩展名
folder_path = "您的文件夹路径"
file_extension = ".您的文件扩展名"

# 调用函数进行排序和批量重命名
sort_and_rename_files(folder_path, file_extension)
