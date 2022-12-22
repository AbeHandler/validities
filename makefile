# can speed up => export PYTHONDONTWRITEBYTECODE=1

.PHONY: test
test:

	cd gp && conda run -n causaldsr --no-capture-output pytest test --disable-warnings && cd ..

.PHONY: conda
conda:
	conda env update --file config/causaldsr.yml --prune -n causaldsr


.PHONY: spacy_init
spacy_init:
	cd config &&  python -m spacy init fill-config base_config.cfg config.cfg && cd ../
	python -m spacy convert -n 10  ./wnut/wnut16/data/dev.conll ./wnut/wnut16/data/
	python -m spacy convert -n 10  ./wnut/wnut16/data/train.conll ./wnut/wnut16/data/
	python -m spacy convert -n 10  ./wnut/wnut16/data/test.conll ./wnut/wnut16/data/


.PHONY: train
train:
	python -m spacy train config/config.cfg --output ./output --paths.train ./wnut/wnut16/data/train.spacy --paths.dev  ./wnut/wnut16/data/dev.spacy