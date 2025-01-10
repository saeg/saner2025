# Quantum Testing in the Wild: A Case Study with Qiskit Algorithms

This repository contains the data and analysis scripts used in our Early Research Achievement (ERA) paper accepted at the IEEE International Conference on Software Analysis, Evolution and Reengineering (SANER 2025) in Montreal.

## Paper Abstract

Although classical computing has excelled in a wide range of applications, there remain problems that push the limits of its capabilities, especially in fields like cryptography, optimization, and materials science. Quantum computing introduces a new computational paradigm, based on principles of superposition and entanglement to explore solutions beyond the capabilities of classical computation. With the increasing interest in the field, there are challenges and opportunities for academics and practitioners in terms of software engineering practices, particularly in testing quantum programs. This paper presents an empirical study of testing patterns in quantum algorithms. We analyzed all the tests handling quantum aspects of the implementations in the Qiskit Algorithms library and identified seven distinct patterns that make use of (1) fixed seeds for algorithms based on random elements; (2) deterministic oracles; (3) precise and approximate assertions; (4) Data-Driven Testing (DDT); (5) functional testing; (6) testing for intermediate parts of the algorithms being tested; and (7) equivalence checking for quantum circuits. Our results show a prevalence of classical testing techniques to test the quantum-related elements of the library, while recent advances from the research community have yet to achieve wide adoption among practitioners.

## Repository Contents

### Data Files
- `assertions.csv`: Quantitative data on different types of assertions found in the Qiskit-Algorithms framework
- `dataset.csv`: Raw dataset with manual annotations from the authors
- `summary.csv`: Aggregated results and key columns

### Analysis Scripts
- `count_assertions.py`: Python script for analyzing and categorizing assertions in the codebase
- `count_tests.py`: Python script for:
  - Counting test methods in the framework
  - Generating a list of tests for further analysis

## Getting Started

### Prerequisites

- Python 3.10 or higher
- pandas library
- Anaconda (recommended) or Python installed in your operating system

While we recommend using Anaconda with a virtual environment for better dependency management, the scripts should work with any Python installation as long as pandas is available, since it's a common library.

### Environment Setup

#### Using Anaconda (Recommended)
```bash
# Create a new conda environment
conda create -n quantumtesting python=3.12

# Activate the environment
conda activate quantumtesting

# Install required package
conda install pandas
```

#### Using Pip (Alternative)
```bash
pip install pandas
```

#### Usage
```bash
# Example commands to run the analysis scripts
python count_assertions.py
python count_tests.py
```

## Authors

- **Neilson C. L. Ramalho** - School of Arts, Sciences, and Humanities, University of São Paulo - neilson@usp.br
- **Erico A. da Silva** - School of Arts, Sciences, and Humanities, University of São Paulo - augusto.ericosilva@usp.br
- **Higor A. de Souza** - Department of Computing, São Paulo State University - higor.amario@unesp.br
- **Marcos Lordello Chaim** - School of Arts, Sciences, and Humanities, University of São Paulo - chaim@usp.br

### Affiliations

1. School of Arts, Sciences, and Humanities -- University of São Paulo, São Paulo, SP, Brazil
2. Department of Computing -- São Paulo State University, Bauru, SP, Brazil
