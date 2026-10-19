# setup_env.py
import subprocess
import sys
from pathlib import Path

REPO_URL = "https://gl.susu.ru/zhuravleviv/baseml.git"

def run(cmd, cwd=None):
    """Выполняет команду и выводит результат."""
    print(f"🔄 {cmd}")
    result = subprocess.run(
        cmd, shell=True, capture_output=True, text=True, cwd=cwd
    )
    if result.returncode != 0:
        print(f"❌ Ошибка:\n{result.stderr}")
        sys.exit(1)
    if result.stdout.strip():
        print(result.stdout)

def main():
    project_root = Path(__file__).parent.resolve()
    baseml_path = project_root / "baseml"
    
    # Клонируем только если папки нет
    if not baseml_path.exists():
        print(f"📥 Клонирую baseml...")
        run(f"git clone {REPO_URL} {baseml_path}", cwd=project_root)
    else:
        print("✅ Папка baseml уже существует")
    
    print("\n🎉 Готово!")

if __name__ == "__main__":
    main()