import os
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi

# 配置Kaggle API客户端
api = KaggleApi()
api.authenticate()

# 下载数据集
dataset = '<dataset-id>'  # 替换为实际的数据集ID
download_path = 'D:/kaggle_datasets'  # 替换为你希望的数据集存储路径

if not os.path.exists(download_path):
    os.makedirs(download_path)

api.dataset_download_files(dataset, path=download_path, unzip=False)

# 解压下载的zip文件
zip_file_path = os.path.join(download_path, dataset + '.zip')
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(download_path)

# 删除zip文件
os.remove(zip_file_path)

print(f'Dataset {dataset} has been downloaded and extracted to {download_path}')
