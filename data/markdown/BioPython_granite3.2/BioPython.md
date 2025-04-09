![](_page_0_Picture_0.jpeg)

Biopython Tutorial and Cookbook

Jeff Chang, Brad Chapman, Iddo Friedberg, Thomas Hamelryck, Michiel de Hoon, Peter Cock, Tiago Antao, Eric Talevich, Bartek Wilczy´nski

Last Update – January 10, 2024 (Biopython 1.83)

## Contents

| 1 |          | Introduction                                                       | 10                                                                                       |     |
|---|----------|--------------------------------------------------------------------|------------------------------------------------------------------------------------------|-----|
|   | 1.1      | What is Biopython?<br>.                                            | 10                                                                                       |     |
|   | 1.2      | What can I find in the Biopython package                           | 10                                                                                       |     |
|   | 1.3      | Installing Biopython<br>.                                          | 11                                                                                       |     |
|   | 1.4      | Frequently Asked Questions (FAQ)                                   | 11                                                                                       |     |
| 2 |          | Quick Start – What can you do with Biopython?                      | 15                                                                                       |     |
|   | 2.1      | General overview of what Biopython provides                        | 15                                                                                       |     |
|   | 2.2      | Working with sequences<br>.                                        | 15                                                                                       |     |
|   | 2.3      | A usage example<br>.                                               | 16                                                                                       |     |
|   | 2.4      | Parsing sequence file formats<br>.                                 | 16                                                                                       |     |
|   |          | 2.4.1<br>Simple FASTA parsing example                              | 17                                                                                       |     |
|   |          | 2.4.2<br>Simple GenBank parsing example<br>.                       | 17                                                                                       |     |
|   |          | 2.4.3<br>I love parsing – please don't stop talking about it!<br>. | 18                                                                                       |     |
|   | 2.5      | Connecting with biological databases                               | 18                                                                                       |     |
|   | 2.6      | What to do next<br>.                                               | 19                                                                                       |     |
|   |          |                                                                    |                                                                                          |     |
| 3 |          | Sequence objects                                                   | 20                                                                                       |     |
|   | 3.1      | Sequences act like strings<br>.                                    | 20                                                                                       |     |
|   | 3.2      | Slicing a sequence<br>.                                            | 21                                                                                       |     |
|   | 3.3      | Turning Seq objects into strings                                   | 22                                                                                       |     |
|   | 3.4      | Concatenating or adding sequences                                  | 22                                                                                       |     |
|   | 3.5      | Changing case                                                      | 23                                                                                       |     |
|   | 3.6      | Nucleotide sequences and (reverse) complements<br>.                | 23                                                                                       |     |
|   | 3.7      | Transcription<br>.                                                 | 24                                                                                       |     |
|   | 3.8      | Translation<br>.                                                   | 25                                                                                       |     |
|   | 3.9      | Translation Tables<br>.                                            | 27                                                                                       |     |
|   |          | 3.10 Comparing Seq objects                                         | 29                                                                                       |     |
|   |          | 3.11 Sequences with unknown sequence contents<br>.                 | 29                                                                                       |     |
|   |          | 3.12 Sequences with partially defined sequence contents<br>.       | 29                                                                                       |     |
|   |          | 3.13 MutableSeq objects                                            | 30                                                                                       |     |
|   |          | 3.14 Finding subsequences                                          | 31                                                                                       |     |
|   |          | 3.15 Working with strings directly<br>.                            | 32                                                                                       |     |
|   |          |                                                                    |                                                                                          |     |
| 4 |          | Sequence annotation objects                                        | 34                                                                                       |     |
|   | 4.1      | The SeqRecord object<br>.                                          | 34                                                                                       |     |
|   | 4.2      | Creating a SeqRecord<br>.                                          | 35                                                                                       |     |
|   |          | 4.2.1<br>SeqRecord objects from scratch                            | 35                                                                                       |     |
|   |          | 4.2.2<br>SeqRecord objects from FASTA files<br>.                   | 36                                                                                       |     |
|   |          | 4.2.3<br>SeqRecord objects from GenBank files                      | 37                                                                                       |     |
|   | 4.3      |                                                                    | Feature, location and position objects<br>.                                              | 38  |
|   |          | 4.3.1                                                              | SeqFeature objects                                                                       | 38  |
|   |          | 4.3.2                                                              | Positions and locations                                                                  | 39  |
|   |          | 4.3.3                                                              | Sequence described by a feature or location<br>.                                         | 41  |
|   | 4.4      |                                                                    | Comparison                                                                               | 42  |
|   | 4.5      |                                                                    | References                                                                               | 43  |
|   | 4.6      |                                                                    | The format method                                                                        | 43  |
|   | 4.7      |                                                                    | Slicing a SeqRecord<br>.                                                                 | 44  |
|   | 4.8      |                                                                    | Adding SeqRecord objects                                                                 | 46  |
|   | 4.9      |                                                                    | Reverse-complementing SeqRecord objects                                                  | 48  |
|   |          |                                                                    |                                                                                          |     |
| 5 |          |                                                                    | Sequence Input/Output                                                                    | 50  |
|   | 5.1      |                                                                    | Parsing or Reading Sequences                                                             | 50  |
|   |          | 5.1.1                                                              | Reading Sequence Files<br>.                                                              | 50  |
|   |          | 5.1.2                                                              | Iterating over the records in a sequence file<br>.                                       | 51  |
|   |          | 5.1.3                                                              | Getting a list of the records in a sequence file                                         | 52  |
|   |          | 5.1.4                                                              | Extracting data                                                                          | 53  |
|   |          | 5.1.5                                                              | Modifying data                                                                           | 55  |
|   | 5.2      |                                                                    | Parsing sequences from compressed files<br>.                                             | 55  |
|   | 5.3      |                                                                    | Parsing sequences from the net<br>.                                                      | 56  |
|   |          | 5.3.1                                                              | Parsing GenBank records from the net                                                     | 57  |
|   |          | 5.3.2                                                              | Parsing SwissProt sequences from the net<br>.                                            | 58  |
|   | 5.4      |                                                                    | Sequence files as Dictionaries<br>.                                                      | 58  |
|   |          | 5.4.1                                                              | Sequence files as Dictionaries – In memory<br>.                                          | 59  |
|   |          | 5.4.2                                                              | Sequence files as Dictionaries – Indexed files                                           | 62  |
|   |          | 5.4.3                                                              | Sequence files as Dictionaries – Database indexed files<br>.                             | 63  |
|   |          | 5.4.4                                                              | Indexing compressed files<br>.                                                           | 64  |
|   |          | 5.4.5                                                              | Discussion                                                                               | 65  |
|   | 5.5      |                                                                    | Writing Sequence Files                                                                   | 66  |
|   |          | 5.5.1                                                              | Round trips                                                                              | 67  |
|   |          | 5.5.2                                                              | Converting between sequence file formats<br>.                                            | 68  |
|   |          | 5.5.3                                                              | Converting a file of sequences to their reverse complements<br>.                         | 69  |
|   |          | 5.5.4                                                              | Getting your SeqRecord objects as formatted strings                                      | 70  |
|   | 5.6      |                                                                    | Low level FASTA and FASTQ parsers<br>.                                                   | 70  |
|   |          |                                                                    |                                                                                          |     |
| 6 |          |                                                                    | Sequence alignments                                                                      | 72  |
|   | 6.1      |                                                                    | Alignment objects<br>.                                                                   | 72  |
|   |          | 6.1.1                                                              | Creating an Alignment object from sequences and coordinates<br>.                         | 72  |
|   |          | 6.1.2                                                              | Creating an Alignment object from aligned sequences<br>.                                 | 73  |
|   |          | 6.1.3                                                              | Common alignment attributes                                                              | 74  |
|   | 6.2      |                                                                    | Slicing and indexing an alignment<br>.                                                   | 75  |
|   | 6.3      |                                                                    | Getting information about the alignment<br>.                                             | 77  |
|   |          | 6.3.1                                                              | Alignment shape<br>.                                                                     | 77  |
|   |          | 6.3.2                                                              | Comparing alignments                                                                     | 77  |
|   |          | 6.3.3                                                              | Finding the indices of aligned sequences<br>.                                            | 77  |
|   |          | 6.3.4                                                              | Counting identities, mismatches, and gaps                                                | 79  |
|   |          | 6.3.5                                                              | Letter frequencies<br>.                                                                  | 79  |
|   |          | 6.3.6                                                              | Substitutions<br>.                                                                       | 79  |
|   |          | 6.3.7                                                              | Alignments as arrays                                                                     | 80  |
|   | 6.4      |                                                                    | Operations on an alignment                                                               | 81  |
|   |          | 6.4.1                                                              | Sorting an alignment                                                                     | 81  |
|   |          | 6.4.2                                                              | Reverse-complementing the alignment<br>.                                                 | 81  |
|   |          |                                                                    |                                                                                          |     |
|   |          | 6.4.3                                                              | Adding alignments                                                                        | 82  |
|   |          | 6.4.4                                                              | Mapping a pairwise sequence alignment<br>.                                               | 83  |
|   |          | 6.4.5                                                              | Mapping a multiple sequence alignment<br>.                                               | 86  |
|   | 6.5      |                                                                    | The Alignments class                                                                     | 88  |
|   | 6.6      |                                                                    | Reading and writing alignments                                                           | 89  |
|   |          | 6.6.1                                                              | Reading alignments<br>.                                                                  | 90  |
|   |          | 6.6.2                                                              | Writing alignments                                                                       | 90  |
|   |          | 6.6.3                                                              | Printing alignments<br>.                                                                 | 90  |
|   | 6.7      |                                                                    | Alignment file formats<br>.                                                              | 92  |
|   |          | 6.7.1                                                              | Aligned FASTA                                                                            | 92  |
|   |          | 6.7.2                                                              | ClustalW<br>.                                                                            | 94  |
|   |          | 6.7.3                                                              | Stockholm                                                                                | 96  |
|   |          | 6.7.4                                                              | PHYLIP output files                                                                      | 99  |
|   |          | 6.7.5                                                              | EMBOSS<br>.                                                                              | 102 |
|   |          | 6.7.6                                                              | GCG Multiple Sequence Format (MSF)<br>.                                                  | 104 |
|   |          | 6.7.7                                                              | Exonerate                                                                                | 106 |
|   |          | 6.7.8                                                              | NEXUS<br>.                                                                               | 109 |
|   |          | 6.7.9                                                              | Tabular output from BLAST or FASTA                                                       | 110 |
|   |          | 6.7.10                                                             | HH-suite output files                                                                    | 112 |
|   |          | 6.7.11                                                             | A2M                                                                                      | 116 |
|   |          | 6.7.12                                                             | Mauve eXtended Multi-FastA (xmfa) format<br>.                                            | 117 |
|   |          | 6.7.13                                                             | Sequence Alignment/Map (SAM)                                                             | 122 |
|   |          | 6.7.14                                                             | Browser Extensible Data (BED)<br>.                                                       | 126 |
|   |          | 6.7.15                                                             | bigBed                                                                                   | 128 |
|   |          | 6.7.16                                                             | Pattern Space Layout (PSL)<br>.                                                          | 131 |
|   |          | 6.7.17                                                             | bigPsl<br>.                                                                              | 133 |
|   |          | 6.7.18                                                             | Multiple Alignment Format (MAF)                                                          | 136 |
|   |          | 6.7.19                                                             | bigMaf                                                                                   | 139 |
|   |          | 6.7.20                                                             | UCSC chain file format<br>.                                                              | 142 |
|   |          |                                                                    |                                                                                          |     |
| 7 |          |                                                                    | Pairwise sequence alignment                                                              | 145 |
|   | 7.1      | Basic usage                                                        | .                                                                                        | 145 |
|   | 7.2      |                                                                    | The pairwise aligner object<br>.                                                         | 149 |
|   | 7.3      |                                                                    | Substitution scores                                                                      | 150 |
|   | 7.4      |                                                                    | Affine gap scores<br>.                                                                   | 151 |
|   | 7.5      |                                                                    | General gap scores<br>.                                                                  | 152 |
|   | 7.6      |                                                                    | Using a pre-defined substitution matrix and gap scores                                   | 154 |
|   | 7.7      |                                                                    | Iterating over alignments<br>.                                                           | 155 |
|   | 7.8      |                                                                    | Aligning to the reverse strand                                                           | 157 |
|   | 7.9      |                                                                    | Substitution matrices                                                                    | 158 |
|   |          | 7.9.1                                                              | Array objects                                                                            | 158 |
|   |          | 7.9.2                                                              | Calculating a substitution matrix from a pairwise sequence alignment<br>.                | 161 |
|   |          | 7.9.3                                                              | Calculating a substitution matrix from a multiple sequence alignment<br>.                | 163 |
|   |          | 7.9.4                                                              | Reading Array objects from file                                                          | 165 |
|   |          | 7.9.5                                                              | Loading predefined substitution matrices<br>.                                            | 167 |
|   |          | 7.10 Examples                                                      | .                                                                                        | 168 |
|   |          |                                                                    | 7.11 Generalized pairwise alignments                                                     | 170 |
|   |          | 7.11.1                                                             | Generalized pairwise alignments using a substitution matrix and alphabet                 | 170 |
|   |          | 7.11.2                                                             | Generalized pairwise alignments using match/mismatch scores and an alphabet              | 171 |
|   |          | 7.11.3                                                             | Generalized pairwise alignments using match/mismatch scores and integer sequences .      | 172 |
|   |          | 7.11.4                                                             | Generalized pairwise alignments using a substitution matrix and integer sequences<br>. . | 173 |
|   |          |                                                                    | 7.12 Codon alignments<br>.                                                               | 174 |
|   |          | 7.12.1                                                             | Aligning a nucleotide sequence to an amino acid sequence<br>.                            | 174 |
|   |          | 7.12.2                                                             | Generating a multiple sequence alignment of codon sequences                              | 176 |
|   |          | 7.12.3                                                             | Analyzing a codon alignment<br>.                                                         | 177 |
|   |          |                                                                    |                                                                                          |     |
| 8 |          |                                                                    | Multiple Sequence Alignment objects                                                      | 182 |
|   | 8.1      |                                                                    | Parsing or Reading Sequence Alignments<br>.                                              | 182 |
|   |          | 8.1.1                                                              | Single Alignments<br>.                                                                   | 183 |
|   |          | 8.1.2                                                              | Multiple Alignments                                                                      | 185 |
|   |          | 8.1.3                                                              | Ambiguous Alignments<br>.                                                                | 187 |
|   | 8.2      |                                                                    | Writing Alignments                                                                       | 189 |
|   |          | 8.2.1                                                              | Converting between sequence alignment file formats<br>.                                  | 190 |
|   |          | 8.2.2                                                              | Getting your alignment objects as formatted strings<br>.                                 | 193 |
|   | 8.3      |                                                                    | Manipulating Alignments<br>.                                                             | 194 |
|   |          | 8.3.1                                                              | Slicing alignments<br>.                                                                  | 194 |
|   |          | 8.3.2                                                              | Alignments as arrays                                                                     | 196 |
|   |          | 8.3.3                                                              | Counting substitutions                                                                   | 197 |
|   |          | 8.3.4                                                              | Calculating summary information<br>.                                                     | 197 |
|   |          | 8.3.5                                                              | Calculating a quick consensus sequence<br>.                                              | 198 |
|   |          |                                                                    |                                                                                          |     |
|   |          | 8.3.6                                                              | Position Specific Score Matrices                                                         | 199 |
|   |          | 8.3.7                                                              | Information Content                                                                      | 200 |
|   | 8.4      |                                                                    | Getting a new-style Alignment object<br>.                                                | 202 |
|   | 8.5      |                                                                    | Calculating a substitution matrix from a multiple sequence alignment<br>.                | 202 |
|   | 8.6      |                                                                    | Alignment Tools<br>.                                                                     | 204 |
|   |          | 8.6.1                                                              | ClustalW<br>.                                                                            | 204 |
|   |          | 8.6.2                                                              | MUSCLE<br>.                                                                              | 206 |
|   |          | 8.6.3                                                              | EMBOSS needle and water<br>.                                                             | 206 |
|   |          |                                                                    |                                                                                          | 209 |
| 9 |          |                                                                    | Pairwise alignments using pairwise2                                                      |     |
|   |          |                                                                    |                                                                                          |     |
|   |          |                                                                    |                                                                                          |     |
|   | 10 BLAST |                                                                    |                                                                                          | 212 |
|   |          |                                                                    | 10.1 Running BLAST over the Internet<br>.                                                | 212 |
|   |          |                                                                    | 10.2 Running BLAST locally<br>.                                                          | 214 |
|   |          | 10.2.1                                                             | Introduction<br>.                                                                        | 214 |
|   |          | 10.2.2                                                             | Standalone NCBI BLAST+                                                                   | 215 |
|   |          | 10.2.3                                                             | Other versions of BLAST<br>.                                                             | 215 |
|   |          |                                                                    | 10.3 Parsing BLAST output<br>.                                                           | 215 |
|   |          |                                                                    | 10.4 The BLAST record class                                                              | 217 |
|   |          |                                                                    | 10.5 Dealing with PSI-BLAST<br>.                                                         | 218 |
|   |          |                                                                    | 10.6 Dealing with RPS-BLAST                                                              | 218 |
|   |          |                                                                    |                                                                                          |     |
|   |          |                                                                    | 11 BLAST and other sequence search tools                                                 | 221 |
|   |          |                                                                    | 11.1 The SearchIO object model<br>.                                                      | 221 |
|   |          | 11.1.1                                                             | QueryResult<br>.                                                                         | 222 |
|   |          | 11.1.2                                                             | Hit                                                                                      | 227 |
|   |          | 11.1.3                                                             | HSP                                                                                      | 230 |
|   |          | 11.1.4                                                             | HSPFragment                                                                              | 233 |
|   |          |                                                                    | 11.2 A note about standards and conventions                                              | 234 |
|   |          |                                                                    | 11.3 Reading search output files<br>.                                                    | 235 |
|   |          |                                                                    | 11.4 Dealing with large search output files with indexing<br>.                           | 236 |

| 12 Accessing NCBI's Entrez databases                                   | 238 |
|------------------------------------------------------------------------|-----|
| 12.1 Entrez Guidelines                                                 | 239 |
| 12.2 EInfo: Obtaining information about the Entrez databases<br>.      | 240 |
| 12.3 ESearch: Searching the Entrez databases                           | 242 |
| 12.4 EPost: Uploading a list of identifiers<br>.                       | 243 |
| 12.5 ESummary: Retrieving summaries from primary IDs                   | 244 |
| 12.6 EFetch: Downloading full records from Entrez                      | 244 |
| 12.7 ELink: Searching for related items in NCBI Entrez                 | 247 |
| 12.8 EGQuery: Global Query - counts for search terms<br>.              | 248 |
| 12.9 ESpell: Obtaining spelling suggestions<br>.                       | 249 |
| 12.10Parsing huge Entrez XML files<br>.                                | 249 |
| 12.11HTML escape characters                                            | 250 |
| 12.12Handling errors                                                   | 251 |
| 12.13Specialized parsers<br>.                                          | 253 |
| 12.13.1 Parsing Medline records                                        | 253 |
| 12.13.2 Parsing GEO records                                            | 255 |
| 12.13.3 Parsing UniGene records                                        | 256 |
| 12.14Using a proxy                                                     | 258 |
| 12.15Examples<br>.                                                     | 258 |
| 12.15.1 PubMed and Medline<br>.                                        | 258 |
| 12.15.2 Searching, downloading, and parsing Entrez Nucleotide records  | 260 |
| 12.15.3 Searching, downloading, and parsing GenBank records            | 261 |
| 12.15.4 Finding the lineage of an organism                             | 263 |
| 12.16Using the history and WebEnv<br>.                                 | 264 |
| 12.16.1 Searching for and downloading sequences using the history<br>. | 264 |
| 12.16.2 Searching for and downloading abstracts using the history      | 265 |
| 12.16.3 Searching for citations                                        | 266 |
|                                                                        |     |
| 13 Swiss-Prot and ExPASy                                               | 267 |
| 13.1 Parsing Swiss-Prot files<br>.                                     | 267 |
| 13.1.1<br>Parsing Swiss-Prot records<br>.                              | 267 |
| 13.1.2<br>Parsing the Swiss-Prot keyword and category list             | 269 |
| 13.2 Parsing Prosite records                                           | 270 |
| 13.3 Parsing Prosite documentation records                             | 271 |
| 13.4 Parsing Enzyme records<br>.                                       | 272 |
| 13.5 Accessing the ExPASy server<br>.                                  | 273 |
| 13.5.1<br>Retrieving a Swiss-Prot record<br>.                          | 273 |
| 13.5.2<br>Searching Swiss-Prot                                         | 274 |
| 13.5.3<br>Retrieving Prosite and Prosite documentation records<br>.    | 274 |
| 13.6 Scanning the Prosite database                                     | 275 |
|                                                                        |     |
| 14 Going 3D: The PDB module                                            | 277 |
| 14.1 Reading and writing crystal structure files                       | 277 |
| 14.1.1<br>Reading an mmCIF file<br>.                                   | 277 |
| 14.1.2<br>Reading files in the MMTF format                             | 278 |
| 14.1.3<br>Reading a PDB file                                           | 278 |
| 14.1.4<br>Reading a PQR file                                           | 279 |
| 14.1.5<br>Reading files in the PDB XML format                          | 279 |
| 14.1.6<br>Writing mmCIF files                                          | 279 |
| 14.1.7<br>Writing PDB files<br>.                                       | 279 |
| 14.1.8<br>Writing PQR files<br>.                                       | 280 |
| 14.1.9<br>Writing MMTF files<br>.                                      | 280 |