import os
import subprocess
import json


def main():
    # Variables
    target_dir = os.path.join(os.getcwd())
    package_json_path = os.path.join(target_dir, "package.json")

    # Paso 1: Asegurarse de que el archivo package.json existe
    if os.path.exists(os.path.join(target_dir, "package.json.jinja2")):
        os.rename("package.json.jinja2", "package.json")

    # Paso 2: Instalar las dependencias del proyecto
    print("Instalando dependencias iniciales del proyecto...")
    subprocess.run(["yarn", "install"], cwd=target_dir, check=True)

    # Paso 3: Instalar las dependencias necesarias para pre-commit y commitlint
    print("Instalando dependencias necesarias para pre-commit, husky y commitlint...")
    subprocess.run([
        "yarn", "add", "--dev",
        "husky",
        "@commitlint/config-conventional",
        "@commitlint/cli",
        "pre-commit"
    ], cwd=target_dir, check=True)

    # Paso 4: Actualizar package.json con las configuraciones de pre-commit y commitlint
    print("Actualizando package.json con la configuración de pre-commit y commitlint...")
    with open(package_json_path, "r+") as package_file:
        try:
            # Leer el contenido existente del package.json
            package_data = json.load(package_file)

            # Agregar scripts si no existen
            package_data.setdefault("scripts", {})
            package_data["scripts"]["lint"] = "eslint ."
            package_data["scripts"]["prepare"] = "husky install"
            package_data["scripts"]["commitlint"] = "commitlint --edit"
            package_data["scripts"]["pre-commit"] = "re-commit run --all-files"

            # Configuración de commitlint
            package_data["commitlint"] = {
                "extends": ["@commitlint/config-conventional"],
                "rules": {
                    "type-enum": [
                        2,
                        "always",
                        ["feat", "fix", "docs", "style", "refactor", "perf", "test", "build", "ci", "chore", "revert"]
                    ],
                    "subject-case": [
                        2,
                        "never",
                        ["sentence-case", "start-case", "pascal-case", "upper-case"]
                    ]
                }
            }
            package_data["pre-commit-config"] = "./pre-commit-config.yaml"

            # Sobrescribir el package.json con los cambios realizados
            package_file.seek(0)
            json.dump(package_data, package_file, indent=2)
            package_file.truncate()

            print("Configuración de package.json actualizada correctamente.")

        except json.JSONDecodeError as e:
            print(f"Error al leer o actualizar el archivo package.json: {e}")
            return

    # Paso 5: Configuración de Husky manual
    print("Configurando Husky para habilitar los hooks...")
    # Inicializar Husky
    subprocess.run(["yarn", "husky", "install"], cwd=target_dir, check=True)

    # Crear archivo de hook pre-commit
    pre_commit_path = os.path.join(target_dir, ".husky", "pre-commit")
    with open(pre_commit_path, "w") as pre_commit_hook:
        pre_commit_hook.write("#!/bin/sh\n. \"$(dirname \"$0\")/_/husky.sh\"\nyarn lint\n")
    os.chmod(pre_commit_path, 0o755)

    # Crear archivo de hook commit-msg
    commit_msg_path = os.path.join(target_dir, ".husky", "commit-msg")
    with open(commit_msg_path, "w") as commit_msg_hook:
        commit_msg_hook.write("#!/bin/sh\n. \"$(dirname \"$0\")/_/husky.sh\"\nnpx commitlint --edit \"$1\"\n")
    os.chmod(commit_msg_path, 0o755)

    print("Configuración completa: pre-commit y commit-msg habilitados exitosamente.")


if __name__ == "__main__":
    main()