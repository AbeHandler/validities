from spacy.cli.train import train
import pathlib
import shutil
import json
import configparser


if __name__ == "__main__":
    for i in range(1, 4):
        outputdir = f"output/{i}"
        path = pathlib.Path(outputdir)
        if path.is_dir():
            shutil.rmtree(path)
        path.mkdir(parents=True, exist_ok=True)
        
        train("./config/spacy/ner/config.cfg",
              output_path=f'output/{i}',
              overrides={"paths.train": "./wnut/wnut16/data/train.spacy",
                         "components.ner.model.hidden_width": i * 100,
                         "paths.dev": "./wnut/wnut16/data/dev.spacy"})




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