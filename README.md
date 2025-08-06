# RAG-System
# update 2025.08.06

# install
1. install langchain and pdf reader

```
pip install openai

pip install pypdf

pip install pyyaml

pip install rich

pip install python-poppler

pip install pdf2image

pip install pdfminer

pip install pdfminer.six

sudo apt install poppler-utils
```

# process RAG pdf database
```
python update_database.py --add_file ./samples/
```


# process RAG json dictionary
```
python update_dictionary.py --add_file ./samples/
```

# run RAG
```
python main.py
```
