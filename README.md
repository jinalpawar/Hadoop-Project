# Hadoop Project : Text Processing and Analysis

In this project, we perform the alloted 5 tasks on the provided text "Notebooks of Leonardo Da Vinci" from Project Gutenberg. The tasks are as follows:

1. Count the frequency of compositions of 2 words, 3 words, 4 words, and 5 words
2. Output Wordlength count
3. Output the top 2% most used letters in words that are longer than 4 letters and shorter than 10 letters
4. List the expected following word, for a given word
5. List the sentences which includes, a given word

## Repository Structure

Within `code`:
- `python_code` holds our python map-reduce + preprocessing scripts
- `bash_script` holds bash scripts to execute each task

## Implementation

### Preprocessing
For the purposes of this project, we perform minimal preprocessing to ensure each task is executed correctly. To maintain pythonic code organization, the preprocessing script is separate and called in every bash script. It performs:

- lowercasing 
- removal of trailing white spaces and periods
- splitting of paragraphs at sentence breaks using ". " as the delimiter.

> The selected delimiter misses edge cases for abbreviations (e.g.: "etc. ", "ltd. "). We let these pass for the sake of brevity.

### Task 1: Phrase count
