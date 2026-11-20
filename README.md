# Hadoop Project : Text Processing and Analysis

### Team Members: [Jinal Pawar](github.com/jinalpawar), [Jeanne Ciz](github.com/jeanneciz)

****

In this project, we perform the alloted 5 tasks on the provided text "Notebooks of Leonardo Da Vinci" from Project Gutenberg. The tasks are as follows:

1. Count the frequency of compositions of 2 words, 3 words, 4 words, and 5 words
2. Output Wordlength count
3. Output the top 2% most used letters in words that are longer than 4 letters and shorter than 10 letters
4. List the expected following word, for a given word
5. List the sentences which includes, a given word

## Repository Structure

Within `code`:
- `python_code` holds our python map-reduce + preprocessing scripts
- `bash_script` holds bash scripts to execute each task + script to setup hadoop and run all tasks one by one with prespecified arguments
- `text` holds original text, cleaned text and preprocessing python script.

## Implementation

### Preprocessing
For the purposes of this project, we perform minimal preprocessing:

- lowercasing 
- removal of trailing white spaces and periods
- splitting of paragraphs at sentence breaks using ". " as the delimiter.

> The selected delimiter misses edge cases for abbreviations (e.g.: "etc. ", "ltd. "). We let these pass for the sake of brevity.

### Task 1: Phrase count
`T1.sh` runs shell commands to execute python mapper and reducer scripts:
- `compositon_mapper` takes phrase length as input and provides all available phrases of that length.
- `original_reducer` is restructured version of original provided reducer python script.

We are able to perform this task for any given provided phrase length. 

### Task 2: Word Length Count
`T2.sh` runs shell commands to execute python mapper and reducer scripts:
- `wordlengthcount_mapper` takes no arguments and provides word length as key with the count as value
- `original_reducer` is restructured version of original provided reducer python script. 

We are able to attain key-value pairs of word length and counts of words with corresponding word lengths.

### Task 3: Top n% of letters in words with length between 5 to 9
`T3.sh` runs shell commands to execute python mapper and reducer scripts:
-  `topn_mapper` takes n (2 for 2%, 20 for 20%, etc.) as input and provides key-value pairs of letters used in words with lengths between 5 to 9. For the purposes of this question, we strip symbols from abbreviations to get actual alphabetic length of the word. (example: N.A.S.A. will be considered as NASA)
- `topn_reducer` takes these key-value pairs and creates a dictionary of letters and lettercounts. We only consider top n% of the available letters. (example: top 30% of the 15 letters used in filtered words)

We are able to perform this task for any provided n.

### Task 4: Next Predicted word
`T4.sh` runs shell commands to execute python mapper and reducer scripts:
-`next_mapper` takes target word as input and provides all possible predictions as output
-`next_reducer` performs the same as `original_reducer` except the count is replaced with their weightages. 

We are able to run this for any provided word within the text.

### Task 5: Sentence
`T5.sh` runs shell commands to execute python mapper and reducer scripts:
- `sentence_mapper` takes target word as input and provides all sentences containing the word as output
- `original_reducer` provides counts of those sentences.

We are able to run this for any provided word within the text as well.

## Demonstration
The project can be run all at once via `project_setup.sh`. 

## Results

All tasks are completed successfully. PDFs with browser pages of each jobs should be available in repo for verification.

