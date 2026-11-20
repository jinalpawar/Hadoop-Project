cd "$hadoop"

# Run task 5 with specified mapper and original reducer
bin/hadoop jar contrib/streaming/hadoop-streaming-1.2.1.jar \
-file $project/code/python_code/sentence_mapper.py -mapper "python3 sentence_mapper.py $1" \
-file $project/code/python_code/orig_reducer.py -combiner "python3 orig_reducer.py" \
-file $project/code/python_code/orig_reducer.py -reducer "python3 orig_reducer.py" \
-input hadoop-project \
-output "$2"