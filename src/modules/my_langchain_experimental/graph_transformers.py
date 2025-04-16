from typing import List, Optional, Sequence

from langchain_community.graphs.graph_document import GraphDocument
from langchain_core.documents import Document
from langchain_core.runnables import RunnableConfig

from langchain_experimental.graph_transformers import LLMGraphTransformer as LangchainLLMGraphTransformer
from my_langchain_experimental.text_splitter import in_jupyter

from tqdm.notebook import tqdm as tqdm_ipy
from tqdm import tqdm as tqdm_py


class LLMGraphTransformer(LangchainLLMGraphTransformer):
    def __init__(self, show_progress: bool = False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.show_progress = show_progress

    def convert_to_graph_documents(
        self, documents: Sequence[Document], config: Optional[RunnableConfig] = None
    ) -> List[GraphDocument]:
        """Same as the original, but with a progress bar."""
        
        if self.show_progress:
            if in_jupyter():
                iterator = tqdm_ipy(documents, total=len(documents))
            else:
                iterator = tqdm_py(documents, total=len(documents))
        else:
            iterator = documents

        return [self.process_response(document, config) for document in iterator]