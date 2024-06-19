import subprocess
import time
import argparse
import sys


def run_shell_script(script_path):
    """
    运行指定的shell脚本，并持续检测其运行状态。
    如果脚本停止运行，则重新启动它。
    同时，将脚本的输出实时打印到终端。

    参数:
    script_path: 要运行的shell脚本的路径
    """
    while True:
        # 使用Popen运行脚本，并设置stdout和stderr为subprocess.PIPE，以便捕获输出
        process = subprocess.Popen(
            ["bash", script_path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT
        )

        # 实时输出脚本运行结果
        for line in iter(process.stdout.readline, b""):
            sys.stdout.write(line.decode(sys.stdout.encoding))
            sys.stdout.flush()

        # 检查脚本是否已停止
        poll = process.poll()
        if poll is None:
            print("comfy脚本正在运行...")
        else:
            print("comfy脚本停止运行，正在重启...")

        # 短暂休眠，避免无限快速重启
        time.sleep(3)


def parse_arguments():
    """
    解析命令行参数。

    返回:
    包含所有命令行参数值的Namespace对象。
    """
    parser = argparse.ArgumentParser(description="运行并监视shell脚本。如果脚本停止，将重新启动它。")
    parser.add_argument("--path", type=str, required=True, help="要运行的shell脚本的路径")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    run_shell_script(args.path)
