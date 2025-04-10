import os
import subprocess
import shutil


def list_all_files_and_folders(directory):
    """
    Lista todos los archivos y carpetas del directorio dado con paths completos.
    """
    print("\nLista de todos los archivos y carpetas del proyecto generado:")
    for root, dirs, files in os.walk(directory):
        for name in dirs:
            print(os.path.join(root, name))
        for name in files:
            print(os.path.join(root, name))


def main():
    # Variables
    project_slug = "{{ cookiecutter.project_slug }}"
    print(f"Proyecto NestJS generado correctamente en {project_slug}")
    list_all_files_and_folders(dest_path)


if __name__ == "__main__":
    main()