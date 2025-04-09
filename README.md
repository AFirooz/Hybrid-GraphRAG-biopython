# GraphRAG using Neo4j graph database

## Overview
This repository is part of Google's 5-Day Intensive GenAI Course. It implements a Hybrid GraphRAG Agent using Gemini as the LLM orchestration layer, combining the power of Retrieval Augmented Generation with graph-based knowledge representation.

## Project Purpose
The AI Agent is designed to be grounded in documentation from:
- [Visual Molecular Dynamics (VMD)](https://www.ks.uiuc.edu/Research/vmd/) - A molecular visualization program for displaying, animating, and analyzing large biomolecular systems.
- [Nanoscale Molecular Dynamics (NAMD)](https://www.ks.uiuc.edu/Research/namd/) - A parallel molecular dynamics code designed for high-performance simulation of large biomolecular systems.
- BioPython - A set of tools for biological computation.
- Google Search - Real-time information retrieval for latest molecular dynamics research and techniques.

By integrating these resources into a graph database, the system aims to provide intelligent responses to complex queries about molecular dynamics simulations and protein visualization.

## Features

- PDF document ingestion and processing using Marker-PDF
- Knowledge graph representation in Neo4j
- RAG-enhanced responses using Gemini LLMs
- Interactive query interface via Streamlit (or Gradio)

## Getting Started

...

## Project Structure

- `/data/pdfs/` - Source documentation in PDF format
- `/src/` - Source code for the GraphRAG implementation

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.
