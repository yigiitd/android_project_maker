import os
import re

def create_file_from_template(main_dir, file_name, templates_dir):
    template_path = os.path.join(templates_dir, file_name)
    output_path = os.path.join(main_dir, file_name)
    
    try:
        with open(template_path, 'r') as template_file, open(output_path, 'w') as output_file:
            output_file.write(template_file.read())
        print(f"Created: {output_path}")
    except IOError as e:
        print(f"Error reading or writing file {file_name}: {e}")

def create_file_structure(main_dir, structure, app_owner: str):
    for path in structure:
        full_path = os.path.join(main_dir, path.lstrip('/'))
        dir_path = os.path.dirname(full_path)
        
        os.makedirs(dir_path, exist_ok=True)

        relative_path = os.path.relpath(dir_path, main_dir)
        package = relative_path.replace(os.path.sep, ".").lower()
        
        with open(full_path, 'w') as f:
            if package != ".":
                f.write(f"package com.{app_owner}.{package}\n\n")
        
        print(f"Created: {full_path}")
    
    templates_dir = os.path.join(os.path.dirname(__file__), "code_templates")
    template_files = ["M_build.gradle.kts", "P_build.gradle.kts", "libs.versions.toml"]

    for file_name in template_files:
        create_file_from_template(main_dir, file_name, templates_dir)

def main():
    app_name = input("Enter the app name: ")
    app_owner = input("Enter the app owner: ")
    main_dir = input("Enter the main directory path: ")

    objects = input("Enter the object names: ").split(",")
    repos = input("Enter the repository names: ").split(",")
    use_cases = input("Enter use case names: ").split(',')

    simple_screens = input("Enter simple screen names: ").split(',')
    complex_screens = input("Enter complex screen names: ").split(',')

    structure = [
        f"/{app_name}Application.kt",

        "/util/Constants.kt",
        "/util/Preferences.kt",
        "/util/Resource.kt",

        "/presentation/MainActivity.kt",
        "/presentation/UiUtils.kt"
        "/presentation/ui/theme/Color.kt",
        "/presentation/ui/theme/Typography.kt",
        "/presentation/ui/theme/Theme.kt",

        "/data/room/ApplicationDatabase.kt",

        "/dependency_injection/AppModule.kt",
        "/dependency_injection/RepositoryModule.kt",
        "/dependency_injection/RetrofitModule.kt",
        "/dependency_injection/RoomModule.kt", 
    ]

    for object in objects:
        structure.extend([
            f"/data/retrofit/{object}/{object}Dto.kt",
            f"/data/retrofit/{object}/{object}Api.kt",

            f"/data/room/{object}/{object}Dto.kt",
            f"/data/room/{object}/{object}Dao.kt",

            f"/domain/model/{object}.kt",
        ])

    for repo in repos:
        structure.extend([
            f"/domain/repository/{repo}Repository.kt",
            f"/data/repository/{repo}RepositoryImpl.kt",
        ])

    for use_case in use_cases:
        structure.append(f"/domain/use_case/{re.sub(r'(?<!^)(?=[A-Z])', '_', use_case.strip()).lower()}/{use_case}UseCase.kt")

    for screen in simple_screens:
        structure.append(f"/presentation/ui/screens/{screen.lower()}_screen/{screen}Screen.kt")

    for screen in complex_screens:
        screen_lower = screen.lower()
        structure.extend([
            f"/presentation/ui/screens/{screen_lower}_screen/view/{screen}Screen.kt",
            f"/presentation/ui/screens/{screen_lower}_screen/{screen}Event.kt",
            f"/presentation/ui/screens/{screen_lower}_screen/{screen}State.kt",
            f"/presentation/ui/screens/{screen_lower}_screen/{screen}ViewModel.kt",
        ])

    create_file_structure(main_dir, structure, app_owner)

if __name__ == "__main__":
    main()