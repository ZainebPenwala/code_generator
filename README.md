<p align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
</p>
<p align="center">
    <h1 align="center">CODE_GENERATOR</h1>
</p>
<p align="center">
    <em>Automate code generation with the code_generator!</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/ZainebPenwala/code_generator?style=default&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/ZainebPenwala/code_generator?style=default&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/ZainebPenwala/code_generator?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/ZainebPenwala/code_generator?style=default&color=0080ff" alt="repo-language-count">
<p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>
<hr>

##  Quick Links

> - [ Overview](#-overview)
> - [ Features](#-features)
> - [ Repository Structure](#-repository-structure)
> - [ Modules](#-modules)
> - [ Getting Started](#-getting-started)
>   - [ Installation](#-installation)
>   - [ Running code_generator](#-running-code_generator)
>   - [ Tests](#-tests)
> - [ Project Roadmap](#-project-roadmap)
> - [ Contributing](#-contributing)
> - [ License](#-license)
> - [ Acknowledgments](#-acknowledgments)

---

##  Overview

The code_generator project is a code generation chatbot that allows users to upload PDF or DOC documents and generate Python code based on the extracted text from the document. Users can upload a document, and the chatbot will extract the text from the document. The extracted text is then combined with a static prompt and sent to the OpenAI GPT model to generate Python code. The generated code is displayed in a code block. Users can also ask follow-up questions or provide additional input without uploading a document. The chatbot uses the OpenAI GPT-3.5-turbo model for code generation. The project provides an efficient and user-friendly way to generate Python code based on document content, making it a valuable tool for developers and programmers.

---

##  Features

|    |   Feature         | Description |
|----|-------------------|---------------------------------------------------------------|
| ⚙️  | **Architecture**  | The project follows a simple client-server architecture using Streamlit as the UI framework and OpenAI as the code generation API. It leverages external libraries like `fitz` for PDF extraction, `python-docx` for DOC extraction, and `streamlit` for UI development. |
| 🔩 | **Code Quality**  | The codebase appears to be well-structured and readable, with meaningful variable and function names. However, there are no code quality tools, such as linters or formatters, mentioned in the repository. |
| 📄 | **Documentation** | There is limited documentation in the form of comments within the code. However, a more comprehensive README file could greatly improve the project's documentation quality. |
| 🔌 | **Integrations**  | The project integrates with external dependencies such as OpenAI for code generation and several libraries like `fitz`, `python-docx`, and `streamlit` for PDF and DOC extraction and UI development, respectively. |
| 🧩 | **Modularity**    | The codebase seems to be modular, with separate Python modules for OpenAI integration, PDF extraction, and the Streamlit app. This allows for easier maintenance and potential reusability of components. |
| 🧪 | **Testing**       | There are no explicit mentions of testing frameworks or tools in the repository. The project would benefit from incorporating testing practices for ensuring code correctness and reducing regressions. |
| ⚡️  | **Performance**   | The efficiency and speed of the project are primarily influenced by the OpenAI API and the performance characteristics of the external library dependencies. Further performance evaluations can be done based on the response time and resource utilization. |
| 🛡️ | **Security**      | The project does not provide explicit details about data protection measures, such as encryption or authentication. Security considerations may depend on the external services used, like OpenAI. |
| 📦 | **Dependencies**  | The key external libraries and dependencies include `txt`, `python-docx`, `langchain`, `py`, `openai`, `PyMuPDF`, `python`, `streamlit`, and `text`. These dependencies are listed in the `requirements.txt` file. |


---

##  Repository Structure

```sh
└── code_generator/
    ├── requirements.txt
    ├── streamlit_app.py
    └── version1.py
```

---

##  Modules

<details closed><summary>.</summary>

| File                                                                                             | Summary                                                                                                                                                                                                                                                                                                                                                        |
| ---                                                                                              | ---                                                                                                                                                                                                                                                                                                                                                            |
| [requirements.txt](https://github.com/ZainebPenwala/code_generator/blob/master/requirements.txt) | This code snippet, located in the `requirements.txt` file, specifies the dependencies needed for the code generator application. It includes packages for streamlit, openai, langchain, PyMuPDF, and python-docx. These dependencies are crucial for the functioning of the code generator application in the repository.                                      |
| [version1.py](https://github.com/ZainebPenwala/code_generator/blob/master/version1.py)           | The code snippet in `version1.py` is part of a code generator chatbot. It allows users to upload PDF or DOC documents and generate Python code based on the extracted text from the document. Users can also provide additional input to generate code without document upload. The chatbot utilizes the OpenAI GPT-3.5-turbo model for code generation.       |
| [streamlit_app.py](https://github.com/ZainebPenwala/code_generator/blob/master/streamlit_app.py) | The `streamlit_app.py` file in the `code_generator` repository is responsible for creating a code generation chatbot. It allows users to upload a PDF or DOC document and generates Python code based on the extracted text from the document. The chatbot uses the OpenAI GPT-4 model for code completion and can also handle follow-up questions from users. |

</details>

---

##  Getting Started

***Requirements***

Ensure you have the following dependencies installed on your system:

* **Python**: `version x.y.z`

###  Installation

1. Clone the code_generator repository:

```sh
git clone https://github.com/ZainebPenwala/code_generator
```

2. Change to the project directory:

```sh
cd code_generator
```

3. Install the dependencies:

```sh
pip install -r requirements.txt
```

###  Running code_generator

Use the following command to run code_generator:

```sh
python main.py
```

###  Tests

To execute tests, run:

```sh
pytest
```

---

##  Project Roadmap

- [X] `► INSERT-TASK-1`
- [ ] `► INSERT-TASK-2`
- [ ] `► ...`

---

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github/ZainebPenwala/code_generator/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github/ZainebPenwala/code_generator/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github/ZainebPenwala/code_generator/issues)**: Submit bugs found or log feature requests for Code_generator.

<details closed>
    <summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
   ```sh
   git clone https://github.com/ZainebPenwala/code_generator
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.

Once your PR is reviewed and approved, it will be merged into the main branch.

</details>

---

##  License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

##  Acknowledgments

- List any resources, contributors, inspiration, etc. here.

[**Return**](#-quick-links)

---
