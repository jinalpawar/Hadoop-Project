cd "$hadoop"

# Run Task 3 with specified mapper and reducer
bin/hadoop jar contrib/streaming/hadoop-streaming-1.2.1.jar \
-file $project/code/python_code/topn_mapper.py -mapper "python3 topn_mapper.py $1" \
-file $project/code/python_code/topn_reducer.py -combiner "python3 topn_reducer.py" \
-file $project/code/python_code/topn_reducer.py -reducer "python3 topn_reducer.py" \
-input hadoop-project-files \
-output "$2"