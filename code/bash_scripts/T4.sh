cd "$hadoop"

# Run task 4 with specified mapper and reducer
bin/hadoop jar contrib/streaming/hadoop-streaming-1.2.1.jar \
-file $project/code/python_code/next_mapper.py -mapper "python3 next_mapper.py $1" \
-file $project/code/python_code/next_reducer.py -combiner "python3 next_reducer.py" \
-file $project/code/python_code/next_reducer.py -reducer "python3 next_reducer.py" \
-input hadoop-project-files \
-output "$2"