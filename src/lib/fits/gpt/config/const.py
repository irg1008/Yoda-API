from .types import Config, FineTuneConfig


def parse_model_name(base: str, org: str, name: str, version: str, time: str):
    return f"{base}:ft-{org}:{name.lower()}-v{version.replace('.', '-')}-{time}"


org_name = "lighthouse-feed"

fine_tune_config: FineTuneConfig = {
    "model_base": "curie",
    "batch_size": 4,
    "epochs": 10,
    "model_name": "shortener",
    "version": "0.2",
}


time_mark = "2022-07-27-10-54-50"  # Change this when tunning new model.
trained_model = parse_model_name(
    base=fine_tune_config["model_base"],
    org=org_name,
    name=fine_tune_config["model_name"],
    version=fine_tune_config["version"],
    time=time_mark,
)

config: Config = {
    "model_name": trained_model,
    "max_prompt_length": 150,
    "min_tokens": 15,
    "max_tokens": 22,
    "max_token_downsample": 0.7,
    "prompt_start": "Long: ",
    "prompt_end": "",
    "completion_start": "Short: ",
    "completion_end": ".",
}
