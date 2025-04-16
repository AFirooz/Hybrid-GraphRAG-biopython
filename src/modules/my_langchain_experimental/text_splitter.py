import copy
from typing import List, Optional
from langchain_core.documents import Document
from langchain_experimental.text_splitter import SemanticChunker as LangchainSemanticChunker
from IPython import get_ipython
import os
import tempfile
import pickle
from tqdm.notebook import tqdm as tqdm_ipy
from tqdm import tqdm as tqdm_py


def in_jupyter() -> bool:
    """
    Check if the code is being executed in a Jupyter Notebook.

    Returns:
        bool: True if running in a Jupyter Notebook, False otherwise.
    """
    try:
        return get_ipython() is not None
    except ImportError:
        return False


class SemanticChunker(LangchainSemanticChunker):
    def __init__(self, show_progress: bool = False, save_temp: bool = False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.show_progress = show_progress

        if save_temp:
            self.temp_dir = tempfile.TemporaryDirectory()
            print(f"Temporary directory: {self.temp_dir.name}")
        else:
            self.temp_dir = False

    def create_documents(self, texts: List[str], metadatas: Optional[List[dict]] = None) -> List[Document]:
        """Same as the original, but with a progress bar."""
        _metadatas = metadatas or [{}] * len(texts)
        documents = []

        if self.show_progress:
            if in_jupyter():
                iterator = tqdm_ipy(enumerate(texts), total=len(texts))
            else:
                iterator = tqdm_py(enumerate(texts), total=len(texts))
        else:
            iterator = enumerate(texts)

        for i, text in iterator:
            start_index = 0
            for chunk in self.split_text(text):
                metadata = copy.deepcopy(_metadatas[i])
                if self._add_start_index:
                    metadata["start_index"] = start_index
                new_doc = Document(page_content=chunk, metadata=metadata)
                documents.append(new_doc)
                start_index += len(chunk)
            if self.temp_dir:
                with open(os.path.join(self.temp_dir.name, "i_documents.pkl"), "wb") as f:
                    pickle.dump((i, documents), f)
        return documents


if __name__ == "__main__":
    pass