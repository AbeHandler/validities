from spacy.cli.train import train
import pathlib
import shutil
import json
import configparser


def training_hyperparams():
    for i in [1, 2, 10, 100, 300]:
        outputdir = f"output/{i}"
        path = pathlib.Path(outputdir)
        if path.is_dir():
            shutil.rmtree(path)
        path.mkdir(parents=True, exist_ok=True)
        
        train("./config/spacy/ner/config.cfg",
              output_path=f'output/{i}',
              overrides={"paths.train": "./wnut/wnut16/data/train.products.spacy",
                         "components.ner.model.hidden_width": i, #this only works on efficient model
                         "components.ner.model.maxout_pieces": 1,
                         "paths.dev": "./wnut/wnut16/data/dev.products.spacy"})


def read_results():
    all_scores = []

    for i in range(1, 4):
        with open(f"output/{i}/model-best/meta.json", 'r') as inf:
            dt = json.load(inf)
            config = configparser.RawConfigParser()
            config.read(f'output/{i}/model-best/config.cfg')
            hidden_width = dict(config.items('components.ner.model'))["hidden_width"]
            scores = dt['performance']["ents_per_type"]["product"]
            scores["hidden_width"] = hidden_width
            all_scores.append(scores)

    return all_scores


if __name__ == "__main__":
    training_hyperparams()
    all_scores = read_results()
    print(all_scores)



