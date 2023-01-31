import os
import json
import subprocess
import re
import pdb


def create_cache_dir():
    if not os.path.exists("./cache/"):
        os.mkdir("./cache/")
        print("Created cache directory")


def config():
    path = "./pipelines_config.json"
    if os.path.exists(path):
        file = open(path)
        config_file = json.load(file)
        file.close()
        return config_file


def download_model(model_name):
    path = os.path.realpath("./cache/" + model_name.split("/")[-1])
    if os.path.exists(path):
        print("Model found in cache: " + path)
    else:
        print("Model not found in cache: " + path)
        previous = os.getcwd()
        os.chdir("./cache/")
        os.system("GIT_LFS_SKIP_SMUDGE=1 git clone https://huggingface.co/" + model_name)
        os.chdir(previous)


def size_to_bytes(size, unity):
    if unity == "GB":
        return float(size) * 1024 * 1024 * 1024
    elif unity == "MB":
        return float(size) * 1024 * 1024
    elif unity == "KB":
        return float(size) * 1024
    else:
        return float(size)


def get_lfs_size(path):
    previous = os.getcwd()
    os.chdir(path)
    lfs_sizes = []
    output = subprocess.run(["git", "lfs", "ls-files", "-s"], stdout=subprocess.PIPE).stdout.decode('utf-8')
    for size in output.split("\n"):
        if size != "":
            match = re.search(r'\((.*?)\)', size).group(1).split(" ")
            lfs_sizes.append(size_to_bytes(match[0], match[1]))
    os.chdir(previous)
    return sum(lfs_sizes)


def get_download_order():
    paths = os.listdir("cache")
    size_dict = {}
    for path in paths:
        size_dict[path] = get_lfs_size("cache/" + path)
    sorted_dict = sorted(size_dict, key=size_dict.get)
    print("Download order: " + str(sorted_dict))
    return sorted_dict


def download_assets():
    order = get_download_order()
    for path in order:
        previous = os.getcwd()
        os.chdir("./cache/" + path)
        os.system("git lfs pull")
        os.chdir(previous)


def download_models():
    config_file = config()
    for model_config in config_file:
        model_name = config_file.get(model_config).get("model_name")
        print("Performing install for " + model_name)
        download_model(model_name)


create_cache_dir()
download_models()
download_assets()
