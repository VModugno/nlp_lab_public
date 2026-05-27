# SMM694: Applied Natural Language Processing
## Session 1: NLP Foundations & Practical Workspace Setup

Welcome to the repository for **SMM694: Applied Natural Language Processing**. This repository serves as your comprehensive guide and code workspace for our first practical session. Below, you will find instructions on how to understand virtual environments, install our lightweight package management stack, and complete your first set of core Python NLP exercises.

---

## 🧠 Part 1: Conceptual Background

Natural Language Processing (NLP) is a field of artificial intelligence focused on the interaction between computers and humans through natural language. Its primary goal is to enable computers to understand, interpret, and generate human language in a meaningful and useful way. 

### The NLP Timeline & Foundations
Modern NLP stands at the intersection of computational linguistics, computer science, and machine learning/deep learning ($ML/DL$). The field has evolved through distinct historical paradigms:
* **Early History (1950s–1960s)**: Roots began with early attempts to process human language computationally, kickstarted by Weaver's memorandum in 1949 and early grammar theories.
* **Rule-Based & Symbolic Systems (1970s–1980s)**: Dominated by handcrafted linguistic rules, patterns, and conceptual ontologies to analyze and generate text.
* **Statistical Methods (1990s–2000s)**: Shifted toward data-driven, robust probabilistic models like Hidden Markov Models (HMMs) and Maximum Entropy Models.
* **The Deep Learning Era (2003–Present)**: Marked by Neural Language Models (2003), Multi-task Learning (2008), Word Embeddings like Word2Vec (2013), Sequence-to-Sequence learning (2014), Attention Mechanisms (2015), and modern state-of-the-art Pretrained Transformers like BERT and GPT (2018).

### Why NLP Matters in Finance and Business
For business and financial analysts, NLP transforms massive volumes of unstructured text into actionable data insights. Key strategic applications include:
* **Market & News Sentiment Analysis**: Monitoring social media, customer feedback, and financial news to gauge market dynamics and assist in stock price prediction.
* **Information Extraction**: Automatically tracing entities, events, dates, and relationships within corporate filings and earnings call transcripts.
* **Operational Automation**: Deploying text summarization tools, question-answering virtual assistants, and conversational dialogue systems for customer relationship management.

---

## ⚙️ Part 2: Managing Your Workspace with Miniforge

Before writing code, you must establish an isolated development environment.

### What is a Virtual Environment and Why Do We Need It?
A virtual environment is an isolated, self-contained directory on your computer that houses a specific version of Python and a custom set of installed libraries. 
* **Preventing Package Conflicts**: Different projects often require different versions of the same library. Isolation ensures that upgrading a library for one project does not inadvertently break another project.
* **Avoiding System Pollution**: It protects your computer's built-in operating system Python from getting corrupted by experimental packages.
* **Ensuring Reproducibility**: It allows you to track and replicate the exact software environment your code needs to execute perfectly on a colleague or student's machine.

### Why Miniforge?
Instead of downloading the heavy, bloated Anaconda distribution, we will use **Miniforge**. Miniforge is a lightweight, clean, community-led alternative. It comes pre-configured to use **Conda-forge** (the most reliable open-source package channel) and includes **Mamba**, an ultra-fast package solver written in C++ that speeds up library downloads from minutes to seconds.

### 💾 Step 1: Download Miniforge
Navigate to the official GitHub repository to download the installer for your respective operating system:
🔗 **[Miniforge Download Link (Official GitHub Repository)](https://github.com/conda-forge/miniforge)**

---

### 💻 Step 2: Installation Instructions

#### For Windows Users
1. Download the **Miniforge3-Windows-x86_64.exe** installer from the link above.
2. Double-click the installer and progress through the setup wizard. We highly recommend selecting the installation type **"Just Me"**.
3. Once completed, do **not** use the standard Windows Command Prompt (CMD) or PowerShell. Instead, open your Start Menu, search for **Miniforge Prompt**, and launch it. This prompt automatically configures your paths to recognize conda and mamba commands.
4. Run `conda init` to initialize your shell, then close and reopen the Miniforge Prompt.

#### For macOS Users
1. Download the installer script. For Apple Silicon Macs (M1/M2/M3 chips), choose **Miniforge3-MacOSX-arm64.sh**. For older Intel Macs, choose **Miniforge3-MacOSX-x86_64.sh**.
2. Open your standard **Terminal** app and navigate to your downloads directory:
   ```bash
   cd ~/Downloads
   ```
3. Execute the installer script by running:
   ```bash
   bash Miniforge3-MacOSX-arm64.sh
   ```
4. Press Enter to review the license agreement, type `yes` to accept, and when asked "Do you wish the installer to initialize Miniforge3 by running conda init?", type `yes`.
5. Close your terminal and reopen it for the changes to take effect.

### 🏎️ Pro Workflow: Conda vs. Mamba Commands
Miniforge exposes two interface commands: `conda` and `mamba`. To optimize your workflow, follow this strict professional convention:

* 📦 **Use `mamba` exclusively for installing and updating packages.** (e.g., `mamba install spacy`). Mamba contains a high-performance solver engine that computes dependency trees instantly.
* 🔄 **Use `conda` for environment management, switching, and configuration.** (e.g., `conda activate nlp_course`). Tasks like environment activation are core configurations handled natively by the base conda manager.

### 🛠️ Step 3: Initializing the Project Workspace
Run the following sequential commands in your terminal or Miniforge prompt to assemble your project environment:

```bash
# 1. Create a clean, dedicated environment named 'nlp_course' using Python 3.10
conda create -n nlp_course python=3.10

# 2. Activate your newly built environment
conda activate nlp_course

# 3. Use Mamba to download the production-grade NLP libraries required for this module
mamba install spacy nltk textblob pandas notebook

# 4. Download spaCy's optimized English foundational processing pipeline model
python -m spacy download en_core_web_sm
```

Verify your environment is correctly configured by checking your package listing:

```bash
mamba list
```

---

## 📝 Part 3: Python NLP Exercises
Our exercises rely heavily on `spaCy` (a fast, production-oriented industrial NLP engine) and `TextBlob` (a high-level tool ideal for straightforward sentiment analytics).

### Exercise 1: The NLP Pipeline (Tokenization & Part-of-Speech Tagging)
**Background**: Standard NLP pipelines take raw string inputs, pass them through a structural tokenizer to break text into meaningful segments (tokens) , and sequentially run a part-of-speech tagger to determine grammatical roles.

**Task**: Process the sentence: "Apple is looking at buying U.K. startup for $1 billion". Extract and print each token's text, canonical dictionary base form (Lemma), detailed part-of-speech tag, syntactic dependency label, and stop-word boolean status.


### Exercise 2: Data Dimensionality Reduction (Text Cleaning)
**Background**: Financial data corpora contain significant noise. Pipelines allow us to drop data dimensionality and optimize performance by stripping out punctuation and stop-words that carry minimal contextual signal.

**Task**: Clean the provided financial headline sentence. Return a clean list consisting exclusively of lowercase, fully lemmatized tokens with all stop words and punctuation removed.



### Exercise 3: Named Entity Recognition (NER) for Corporate Intelligence
**Background**: Named Entity Recognition (NER) is a core pipeline module that identifies and classifies proper nouns inside text strings into pre-defined real-world categories.

**Task**: Process the financial news narrative snippet below. Extract all detected entities and display their corresponding classifications, keeping an eye out for organizations (ORG), geopolitical entities/locations (GPE), and explicitly declared monetary values (MONEY).


### Exercise 4: Feedback Sentiment Parsing via TextBlob
**Background**: TextBlob abstracts low-level algorithmic complexities to provide accessible sentiment scoring. It scores blocks of text along a Polarity spectrum ranging smoothly from -1.0 (highly negative) to +1.0 (highly positive), which is useful for analyzing market feedback.

**Task**: Construct a Python script that instantiates TextBlob metrics over the provided positive and negative consumer review texts to dynamically extract and report polarity index variables.



## 🚀 Running the Lab Code

Activate your workspace:
```bash
conda activate nlp_course
```

Launch a script directly from the directory:
```bash
python exercise_1.py
```
