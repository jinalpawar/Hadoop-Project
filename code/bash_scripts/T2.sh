cd "$hadoop"

# Run Wordlength count with original reducer
bin/hadoop jar contrib/streaming/hadoop-streaming-1.2.1.jar \
- file $project/code/python_code/wordlengthcount_mapper.py -mapper "python3 wordlengthcount_mapper.py"
- file $project/code/python_code/orig_reducer.py -combiner "python3 orig_reducer.py"
- file $project/code/python_code/orig_reducer.py -reducer "python3 orig_reducer.py"
- input hadoop-project-files \
- output "$1"