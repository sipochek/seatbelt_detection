# test.py
import sys
from pathlib import Path

# Динамическое определение пути к baseml относительно текущего файла
BASML_PATH = Path(__file__).parent.resolve() / "baseml"
sys.path.insert(0, str(BASML_PATH))

from baseml import FolderDataset

def print_dataset_summary(dataset):
    """Локальная реализация сводки."""
    print(f"Groups: {dataset.groups}")
    print(f"Total samples: {len(dataset)}")
    for group in dataset.groups:
        count = len(dataset >> group)
        print(f"  - {group}: {count} samples")

# Путь к датасету тоже лучше делать относительным
DATASET_PATH = Path(__file__).parent.resolve() / "data"

if not DATASET_PATH.exists():
    raise FileNotFoundError(f"Датасет не найден: {DATASET_PATH}")

dataset = FolderDataset(DATASET_PATH)
print_dataset_summary(dataset)

# Проверка сэмпла
sample = dataset[0]
print(f"\nKeys: {list(sample.keys())}")
print(f"Image shape: {sample['image'].shape}")