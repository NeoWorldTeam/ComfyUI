from importlib import import_module


module_list = [
    ".src.gen_input",
    ".src.style.select",
    ".src.style.EasyPromptSelecto",
    ".src.style.StyleSelecto",
    ".src.comfy_latent_interposer",
]

# 初始化字典
NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}

package_name = __package__ or '当前模块的包名'

for module_path in module_list:
    full_module_path = f"{package_name}{module_path}"
    try:
        imported_module = import_module(full_module_path, package_name)
        NODE_CLASS_MAPPINGS.update(getattr(imported_module, 'NODE_CLASS_MAPPINGS', {}))
        NODE_DISPLAY_NAME_MAPPINGS.update(getattr(imported_module, 'NODE_DISPLAY_NAME_MAPPINGS', {}))
    except ImportError as e:
        print(f"无法导入模块 {full_module_path}: {e}")

print("NODE_CLASS_MAPPINGS:", NODE_CLASS_MAPPINGS)
print("NODE_DISPLAY_NAME_MAPPINGS:", NODE_DISPLAY_NAME_MAPPINGS)

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']