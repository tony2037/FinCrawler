PY = python3
cna: cna.py
	$(PY) $^
cna_corpus: cna.py
	$(PY) $^ > cna_corpus.txt
