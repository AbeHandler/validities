# can speed up => export PYTHONDONTWRITEBYTECODE=1

.PHONY: test
test:

	cd gp && conda run -n causaldsr --no-capture-output pytest test --disable-warnings && cd ..

.PHONY: conda
conda:
	conda env update --file config/causaldsr.yml --prune -n causaldsr


# things to initialize spacy
wnut/wnut16/data/dev.products.conll:
	# make the config file
	python -m spacy init fill-config config/spacy/ner/base_config.cfg ./config/spacy/ner/config.cfg
	python -m src.preprocessor # make a product only version of the dev data this is needed to get a best model for products
	python -m spacy convert -n 10  ./wnut/wnut16/data/dev.conll ./wnut/wnut16/data/
	python -m spacy convert -n 10  ./wnut/wnut16/data/train.conll ./wnut/wnut16/data/
	python -m spacy convert -n 10  ./wnut/wnut16/data/test.conll ./wnut/wnut16/data/
	python -m spacy convert -n 10  ./wnut/wnut16/data/dev.products.conll ./wnut/wnut16/data/


.PHONY: train
train:
	python -m spacy train config/config.cfg --output ./output --paths.train ./wnut/wnut16/data/train.spacy --paths.dev  ./wnut/wnut16/data/dev.products.spacy