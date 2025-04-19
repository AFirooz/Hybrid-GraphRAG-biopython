from typing import List, Optional, Sequence

from langchain_community.graphs.graph_document import GraphDocument
from langchain_core.documents import Document
from langchain_core.runnables import RunnableConfig

from langchain_experimental.graph_transformers import LLMGraphTransformer as LangchainLLMGraphTransformer
from my_langchain_experimental.text_splitter import in_jupyter

from tqdm.notebook import tqdm as tqdm_ipy
from tqdm import tqdm as tqdm_py
import tempfile
import pickle
from pathlib import Path
from time import strftime, localtime
import warnings


class LLMGraphTransformer(LangchainLLMGraphTransformer):
    def __init__(
        self,
        show_progress: bool = False,
        save_temp: bool = False,
        pkl_path: Path = None,
        force_finish: bool = False,
        **kwargs,
    ):
        super().__init__(**kwargs)
        
        self.show_progress = show_progress

        self.force_finish = True if force_finish else False

        if pkl_path is not None:
            warnings.warn('Since "pkl_path" is provided, "save_temp" is ignored')
            pkl_path = Path(pkl_path)
            assert isinstance(pkl_path, Path) and str(pkl_path).endswith('.pkl'), "pkl_path must be a string or Path object that point to a .pkl file"
            self.pkl_path = pkl_path
        elif save_temp:
            self.pkl_path = Path(tempfile.TemporaryDirectory()) / "LLMGraphTransformer.pkl"
            print(f"temp pkl path: {str(self.pkl_path)}")
        else:
            self.pkl_path = False

    def convert_to_graph_documents(
        self, documents: Sequence[Document], config: Optional[RunnableConfig] = None,
        subset: Optional[Sequence[int]] = None
    ) -> List[GraphDocument]:
        """Same as the original, but with more options.
        - a progress bar
        - saving intermediate results to a .pkl file
        - resuming from a state
        - skip problematic documents
        """
        # using a single name.pkl to save any temporary results instead of multiple files each time.
        tname_base = self.pkl_path.with_suffix(f".run.{strftime('%m%d%H%M%S', localtime())}.pkl") if self.pkl_path else None

        if subset is not None:
            documents = [documents[i] for i in subset]

        if self.show_progress:
            if in_jupyter():
                iterator = tqdm_ipy(enumerate(documents), total=len(documents))
            else:
                iterator = tqdm_py(enumerate(documents), total=len(documents))
        else:
            iterator = documents

        skip_documents = []
        graph_documents = []
        try:
            for i, doc in iterator:
                try:
                    # first round of processing
                    gdoc = self.process_response(doc, config)
                    graph_documents.append(gdoc)
                except Exception as e:
                    # Don't handle KeyboardInterrupt or SystemExit, let them propagate
                    if isinstance(e, (KeyboardInterrupt, SystemExit)):
                        raise e

                    # saving the intermediate results
                    if self.pkl_path:
                        with open(tname_base.with_suffix(f".t.{strftime('%m%d%H%M%S', localtime())}.pkl"), "wb") as f:
                            pickle.dump([graph_documents, skip_documents], f)
                    if not self.force_finish:
                        print(f"{len(graph_documents)=}")
                        print(f"{skip_documents=}")
                        raise e
                    else:
                        # try to process the document again
                        print(f"\nError processing document: {i} at {strftime('%m/%d - %H:%M:%S', localtime())}\nRetrying...")
                        try:
                            gdoc = self.process_response(doc, config)
                            graph_documents.append(gdoc)
                        except Exception as e:
                            # if the problem persists, save the skipped document index
                            skip_documents.append(i)
        finally:
            # if the process is interrupted, save the results
            if self.pkl_path:
                with open(tname_base.with_suffix(".last.pkl"), "wb") as f:
                    pickle.dump([graph_documents, skip_documents], f)
        return graph_documents, skip_documents

    
    if __name__ == "__main__":
        pass
    