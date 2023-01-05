class Folders:
    def __init__(self, folder_name) -> None:
        self.folder_name = folder_name

    def __str__(self) -> str:
        return f'/{self.folder_name}'


class Files(Folders):
    def __init__(self, folder_name, file_name) -> None:
        super().__init__(folder_name)
        self.file_name = file_name

    def __str__(self) -> str:
        return f'{super().__str__()}/{self.file_name}'

class Shortcuts(Files):
    def __init__(self, folder_name, file_name, extension) -> None:
        super().__init__(folder_name, file_name)
        self.extension = extension

    def __str__(self) -> str:
        return f'{super().__str__()}/{self.file_name}.{self.extension}'


if __name__ == '__main__':
    folder = Folders('bam')
    file = Files('bim', 'bum')
    shortcut = Shortcuts('folder', 'file', 'bin')

    print(f"folder: {folder}")
    print(f"file: {file}")
    print(f"shortcut: {shortcut}")