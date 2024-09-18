import os
import re

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

def main():
    app_name = input("Enter the app name: ")
    main_dir = "/Users/ahmetyigitdayi/Desktop/" + input("Enter the main directory path: ")

    object_name = input("Enter the object name: ")
    repo_name = input("Enter the repository name: ")
    use_cases = input("Enter use case names (comma-separated): ").split(',')

    simple_screens = input("Enter simple screen names (comma-separated): ").split(',')
    complex_screens = input("Enter complex screen names (comma-separated): ").split(',')

    structure = [
        f"/data/repository/{repo_name}RepositoryImpl.kt",
        f"/data/retrofit/dto/{object_name}Dto.kt",
        f"/data/retrofit/{object_name}Api.kt",

        f"/data/room/dto/{object_name}Dto.kt",
        f"/data/room/{object_name}Dao.kt",
        "/data/room/ApplicationDatabase.kt",

        "/dependency_injection/AppModule.kt",
        "/dependency_injection/RepositoryModule.kt",
        "/dependency_injection/RetrofitModule.kt",
        "/dependency_injection/RoomModule.kt",

        f"/domain/model/{object_name}.kt",
        f"/domain/repository/{repo_name}Repository.kt",
    ]

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

    structure.extend([
        "/util/Constants.kt",
        "/util/Preferences.kt",
        "/util/Resource.kt",

        "/presentation/MainActivity.kt",

        "/presentation/ui/theme/Color.kt",
        "/presentation/ui/theme/Typography.kt",
        "/presentation/ui/theme/Theme.kt",

        f"/{app_name}Application.kt",
    ])

    create_file_structure(main_dir, structure)

if __name__ == "__main__":
    main()