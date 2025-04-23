import pickle
import re
from pathlib import Path
from time import localtime, strftime

import dotenv
import fitz  # PyMuPDF
import utils
from langchain_community.document_loaders.parsers import LLMImageBlobParser
from langchain_ollama import ChatOllama
from langchain_ollama.embeddings import OllamaEmbeddings
from langchain_pymupdf4llm import PyMuPDF4LLMLoader
from my_langchain_experimental.graph_transformers import LLMGraphTransformer
from my_langchain_experimental.text_splitter import SemanticChunker
from tqdm import tqdm

root_dir = utils.get_project_root()
f = root_dir / ".secrets" / ".env"
assert f.exists(), f"File not found: {f}"
dotenv.load_dotenv(f)



def update_filename_len(file_path: Path, page_delimiter=None) -> tuple[str, int]:
    """
    Update the filename length for the given file path.
    :param file_path: The file path to update.
    :return: A tuple containing the updated file name and its length.
    """
    file_name = file_path.stem.lower()
    with fitz.open(file_path) as pdf_doc:
        if page_delimiter is not None:
            # use regex to look for the number of page delimiter in the file contents
            file_len = len([page for page in pdf_doc if page_delimiter in page.get_text("text").lower()])
        else:
            file_len = len(pdf_doc)
    return file_name, file_len



file_path = Path() / ".." / "data" / "pdfs" / "biopython.pdf"

file_path = file_path.resolve()
file_path = utils.fuzzy_find(file_path)

file_name, file_len = update_filename_len(file_path)

# create directory for pkl files
pkl_dir = file_path.parent.parent / "pkls"
pkl_dir.mkdir(exist_ok=True, parents=True)

print(f"file_path = {file_path}")

pfile_path = file_path
extract_images = True

pfile_name, pfile_len = update_filename_len(pfile_path)

if extract_images:
    loader = PyMuPDF4LLMLoader(
        pfile_path,
        mode="page",  # page | single
        extract_images=True,
        images_parser=LLMImageBlobParser(model=ChatOllama(model="granite3.2-vision", max_tokens=1024)),
    )
else:
    loader = PyMuPDF4LLMLoader(pfile_path, mode="page")

print(f"{pfile_name=} -> {pfile_len} pages")


pkl_name = pkl_dir / f"docs_pages_{pfile_name}.pkl"

if pkl_name.exists():
    print("Loading docs from pickle")
    with open(pkl_name, "rb") as f:
        docs = pickle.load(f)
else:
    docs = []
    try:
        print(
            f"Loading docs from pdf. \nThis will take some time (~{int(pfile_len / 30)} min)"
        )  # on average 30 pages per minute

        for doc in tqdm(loader.lazy_load(), total=pfile_len):
            docs.append(doc)

        # pickle save the docs
        with open(pkl_name, "wb") as f:
            pickle.dump(docs, f)

    except Exception as e:
        print(f"{len(docs)=}")
        tname = pkl_name.with_suffix(f".{strftime('%m%d.%H%M%S', localtime())}.pkl")
        with open(tname, "wb") as f:
            pickle.dump(docs, f)
        raise e

print(f"Loaded {pfile_name}: {len(docs)} documents")

for doc in tqdm(docs, total=len(docs)):
    txt = doc.page_content

    # cleaning Content section
    if doc.metadata["page"] in range(0, 10):
        # we use ". ." so not to delete the end sentence dot
        txt = txt.replace(". .", "").strip()

        while txt.find("  ") > 0:
            txt = txt.replace("  ", " ")

        txt = txt.replace(" . ", " ")
        txt = re.sub(r" (\d+(?:\d+)*?)\n", r" page: \1\n", txt)

    txt = re.sub(r"(\n*)(\d*)(\n*)$", r"", txt)  # remove page numbers

    if txt in ["", ".", " "]:
        doc.metadata['empty'] = 1
    doc.page_content = txt

# delete empty docs
docs = [doc for doc in docs if "empty" not in doc.metadata]

print(f"New docs: {len(docs)}")


pkl_name = pkl_dir / f"docs_pages_semantic_split_bgem3_{pfile_name}.pkl"

text_splitter = SemanticChunker(
    embeddings=OllamaEmbeddings(model="bge-m3"), add_start_index=True, show_progress=True, save_temp=True
)

if pkl_name.exists():
    print("Loading split docs from pickle")
    with open(pkl_name, "rb") as f:
        docs_split = pickle.load(f)
else:
    docs_split = text_splitter.split_documents(docs)

    with open(pkl_name, "wb") as f:
        pickle.dump(docs_split, f)

print(f"Loaded {pfile_name}: {len(docs_split)} documents")


pkl_name = pkl_dir / f"docs_graph_bgem3_{pfile_name}.pkl"

if pkl_name.exists():
    print("Loading graph docs from pickle")
    with open(pkl_name, "rb") as f:
        gdocs = pickle.load(f)
else:
    llm = ChatOllama(model="gemma3:4b-it-qat", temperature=0, format="json")
    llm_transformer = LLMGraphTransformer(llm=llm, show_progress=True, pkl_path=pkl_name, force_finish=True)
    gdocs, sdocs = llm_transformer.convert_to_graph_documents(docs_split)

    with open(pkl_name, "wb") as f:
        pickle.dump(gdocs, f)
    
    if len(sdocs) > 0:
        with open(pkl_name.with_suffix(".skipped.id.pkl"), "wb") as f:
            pickle.dump(sdocs, f)

print(f"Loaded {pfile_name}: {len(gdocs)} documents")
