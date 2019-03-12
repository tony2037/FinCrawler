PY = python3

clean:
	$(RM) *.txt
cna: cna.py
	$(PY) $^
cna_corpus: cna.py
	$(PY) $^ > cna_corpus.txt
