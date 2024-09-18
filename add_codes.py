import os
import re
from typing import List, Tuple, NamedTuple

class Config(NamedTuple):
    path: str
    templates_dir: str

def read_template(template_path: str) -> str:
    try:
        with open(template_path, 'r') as file:
            return file.read()
    except IOError as e:
        print(f"Error reading template file {template_path}: {e}")
        return ""

def process_files(config: Config, file_configs: List[Tuple[str, str]]) -> None:
    for root, _, files in os.walk(config.path):
        for file in files:
            for condition_regex, template_path in file_configs:
                if re.search(condition_regex, file):
                    file_path = os.path.join(root, file)
                    template_content = read_template(template_path)
                    if template_content:
                        try:
                            with open(file_path, 'a') as f:
                                f.write(template_content)
                            print(f"Appended code to:{file_path}")
                        except IOError as e:
                            print(f"Error writing to {file_path}: {e}")
                    break

def get_file_configs(templates_dir: str) -> List[Tuple[str, str]]:
    return [
        (r"Api.kt",               os.path.join(templates_dir, "Api.kt")),
        (r"Application.kt",       os.path.join(templates_dir, "Application.kt")),
        (r"AppModule.kt",         os.path.join(templates_dir, "AppModule.kt")),
        (r"Constants.kt",         os.path.join(templates_dir, "Constants.kt")),
        (r"Dao.kt",               os.path.join(templates_dir, "Dao.kt")),
        (r"Database.kt",          os.path.join(templates_dir, "Database.kt")),
        (r"Event.kt",             os.path.join(templates_dir, "Event.kt")),
        (r"MainActivity.kt",      os.path.join(templates_dir, "MainActivity.kt")),
        (r"RepositoryModule.kt",  os.path.join(templates_dir, "RepositoryModule.kt")),
        (r"Resource.kt",          os.path.join(templates_dir, "Resource.kt")),
        (r"RetrofitModule.kt",    os.path.join(templates_dir, "RetrofitModule.kt")),
        (r"RoomModule.kt",        os.path.join(templates_dir, "RoomModule.kt")),
        (r"Screen.kt",            os.path.join(templates_dir, "Screen.kt")),
        (r"ScreenUtils.kt",       os.path.join(templates_dir, "ScreenUtils.kt")),
        (r"State.kt",             os.path.join(templates_dir, "State.kt")),
        (r"ViewModel.kt",         os.path.join(templates_dir, "ViewModel.kt")),
    ]

def get_config() -> Config:
    path = os.path.join("/Users/ahmetyigitdayi/Desktop/", input("Enter the application path: "))
    templates_dir = os.path.join(os.path.dirname(__file__), "code_templates")

    if not os.path.exists(path):
        raise ValueError(f"Error: The path {path} does not exist.")

    if not os.path.exists(templates_dir):
        raise ValueError(f"Error: Templates directory {templates_dir} does not exist.")

    return Config(path, templates_dir)

def main():
    try:
        config = get_config()
        file_configs = get_file_configs(config.templates_dir)
        process_files(config, file_configs)
    except ValueError as e:
        print(e)
        return

if __name__ == "__main__":
    main()