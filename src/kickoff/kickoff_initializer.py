import os


class KickOffInitializer:
    def __init__(self, root_folder):
        self.__root_folder = root_folder

    @property
    def root_folder(self):
        return self.__root_folder

    @root_folder.setter
    def root_folder(self, value):
        self.__root_folder = value

    def initialize(self):
        os.makedirs(self.__root_folder, exist_ok=True)
        os.chdir(self.__root_folder)

        folders = ["Images", "Notes", "Others"]
        for folder_name in folders:
            folder = Folder(folder_name)
            folder.create()

        gitignore_file = File(".gitignore", "*.vscode")
        gitignore_file.create()

        license_file = File("LICENSE", "")
        license_file.create()

        root_readme_file = File("README.md", "Description of your learning journey.")
        root_readme_file.create()

        for folder_name in folders:
            subfolder_readme_file = File(os.path.join(folder_name, "README.md"), "")
            subfolder_readme_file.create()


class Folder:
    def __init__(self, folder_name):
        self.__folder_name = folder_name

    def create(self):
        os.makedirs(self.__folder_name)


class File:
    def __init__(self, file_name, file_content):
        self.__file_name = file_name
        self.__file_content = file_content

    def create(self):
        with open(self.__file_name, "w") as file:
            file.write(self.__file_content)


if __name__ == "__main__":
    root_folder = input("Enter the root folder path: ")
    initializer = KickOffInitializer(root_folder)
    initializer.initialize()
