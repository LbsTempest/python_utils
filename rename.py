import os


def rename_files(folder_path: str, file_extension: str) -> None:
    # 获取文件夹中指定类型的文件
    files: list[str] = [file for file in os.listdir(folder_path) if file.endswith(file_extension)]

    # 重命名文件
    for j, file in enumerate(files):
        print(file)
        # 构建新的文件名
        new_name: str = f"{j + 1}.{file_extension}"

        # 旧文件的完整路径
        old_path: str = os.path.join(folder_path, file)

        # 新文件的完整路径
        new_path: str = os.path.join(folder_path, new_name)

        # 重命名文件
        os.rename(old_path, new_path)
        print(f"重命名文件: {file} -> {new_name}")

