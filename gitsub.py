import os
import subprocess

# 设置你的项目目录路径
project_path = './'
submodules_dir = os.path.join(project_path, 'custom_nodes')

# 确保 .gitmodules 文件存在
gitmodules_path = os.path.join(project_path, '.gitmodules')
if not os.path.exists(gitmodules_path):
    open(gitmodules_path, 'w').close()

# 读取现有的 .gitmodules 文件内容，避免重复添加
with open(gitmodules_path, 'r') as file:
    existing_gitmodules = file.read()

# 用于存储 .gitmodules 文件的新内容
new_gitmodules_content = existing_gitmodules

# 检查每个子目录
for folder in os.listdir(submodules_dir):
    folder_path = os.path.join(submodules_dir, folder)
    if os.path.isdir(folder_path):
        # 检查子目录是否是 Git 仓库
        if os.path.isdir(os.path.join(folder_path, '.git')):
            try:
                # 获取子模块的远程仓库 URL
                remote_url = subprocess.check_output(
                    ['git', 'config', '--get', 'remote.origin.url'],
                    cwd=folder_path
                ).decode('utf-8').strip()

                # 创建 .gitmodules 文件内容
                submodule_config = (
                    f"\n[submodule \"{folder}\"]\n"
                    f"\tpath = {os.path.relpath(folder_path, project_path)}\n"
                    f"\turl = {remote_url}\n"
                )

                # 检查是否已经存在该子模块的配置
                if submodule_config not in existing_gitmodules:
                    new_gitmodules_content += submodule_config

            except subprocess.CalledProcessError as e:
                print(f"Error reading repository info for {folder}: {e}")

# 更新 .gitmodules 文件
with open(gitmodules_path, 'w') as file:
    file.write(new_gitmodules_content)
