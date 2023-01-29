import os
import json


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


def download_assets():
    os.system("ls -d cache/* | xargs -I {} bash -c \"cd '{}' && git lfs pull\"")


def download_models():
    config_file = config()
    for model_config in config_file:
        print("Performing install for " + config_file.get(model_config))
        download_model(config_file.get(model_config))


create_cache_dir()
download_models()
download_assets()
