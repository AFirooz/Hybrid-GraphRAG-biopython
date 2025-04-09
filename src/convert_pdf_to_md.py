# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.7
#   kernelspec:
#     display_name: .venv
#     language: python
#     name: python3
# ---

# %%
from pathlib import Path

from marker.config.parser import ConfigParser
from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict
from marker.output import text_from_rendered
from glob import glob


# %%
pdf_path = Path(".").cwd().parent / "data" / "pdfs"
md_path = Path(".").cwd().parent / "data" / "markdown"

pdf_files = glob(str(pdf_path / "*.pdf"))
pdf_files.sort()
print(f"Found {len(pdf_files)} PDF files")

md_path.mkdir(parents=True, exist_ok=True)

# %% [markdown]
# Even though we did not pass `workers` or `num_devices`, it's using 100% of my Macbook Pro M4 GPU.
#
# ## LLM Config
#
# You can find what LLMs are available from [here.](https://github.com/VikParuchuri/marker?tab=readme-ov-file#llm-services) Just note that the service must be passed as string, and not the actual object (eg.`"marker.services.ollama.OllamaService"`).
#

# %%
# Same as the CLI configs
# run `$ marker --help` to see all the config options
config = {
    # "num_devices": 5,  # min 2. Number of GPUs to use
    "workers": 2,  # 5 by default. Number of conversion workers to run simultaneously
    # "output_dir": md_path,  # todo: test if it will save it automatically
    "output_format": "markdown",  # options: markdown, json, html
    "force_ocr": False,  # avoid OCR if not needed
    "languages": "en",  # support English for OCR
    "paginate_output": False,  # add page numbers to the output [Markdown]
    "disable_links": True,  # removes hyperlinks in text
    # --- LLM Config
    "use_llm": False,  # too big and slow for local
    # --- OLLAMA
    "llm_service": "marker.services.ollama.OllamaService",
    "ollama_base_url": "http://localhost:11434",
    # "ollama_model": "gemma3:4b",
    "ollama_model": "smollm2:135m",
    # --- GEMINI
    # "gemini_api_key": "API KEY",
    # "llm_service": "services.gemini.GoogleGeminiService", # default
    # "model_name": "gemini-2.0-flash" # default
}

config_parser = ConfigParser(config)

# %%
converter = PdfConverter(
    config=config_parser.generate_config_dict(),
    artifact_dict=create_model_dict(),
    processor_list=config_parser.get_processors(),
    renderer=config_parser.get_renderer(),
    llm_service=config_parser.get_llm_service(),
)

# %%
# Convert the document
for file in pdf_files:
    rendered = converter(file)

    # Save the output to a file
    output_file = md_path / Path(file).name.replace(".pdf", ".md")

    with open(output_file, "w") as f:
        # markdown_text, metadata, images = text_from_rendered(rendered)
        f.write(text_from_rendered(rendered))
