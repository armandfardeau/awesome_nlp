from transformers import pipeline
from utils.config import cache
import os
import json

@cache.memoize()
def pipeline_file():
    path = "/app/pipelines_config.json"
    if os.path.exists(path):
        file = open(path)
        config = json.load(file)
        file.close()
        print(config)
        return config

@cache.memoize()
def cached_model_name(model_name):
    return model_name.split("/")[-1]

@cache.memoize()
def get_model(model_name):
    path = os.path.realpath("/app/cache/" + cached_model_name(model_name))
    if os.path.exists(path):
        print("Model found in cache: " + path)
        return path
    else:
        print("Model not found in cache: " + path)
        return model_name

@cache.memoize()
def pipeline_config():
    pipeline_config_dict = pipeline_file()
    configs = {}
    for config in pipeline_config_dict:
        print("Loading pipeline config: " + pipeline_config_dict.get(config))
        configs[config] = get_model(pipeline_config_dict.get(config))
    return configs


@cache.memoize()
def from_pipeline(pipeline_name):
    pipeline_config_dict = pipeline_config()
    return create_pipeline(pipeline_name, pipeline_config_dict.get(pipeline_name))

@cache.memoize()
def create_pipeline(pipeline_name, model_name):
    return pipeline(pipeline_name, model=model_name)
