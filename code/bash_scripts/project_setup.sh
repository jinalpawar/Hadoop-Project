# Configure directory names
hadoop=~/mainhadoop
project=~/Hadoop-Project-main

cd "$hadoop"

# Restart all HDFS processes
bin/stop-all.sh
bin/start-all.sh

# Verify all processes are running
jps

# Remove directories from previous runs
bin/hadoop dfs -rmr hadoop-project T1-2 T1-3 T1-4 T1-5 
bin/hadoop dfs -rmr T2 T3-2 T4-travel T5-travel

# Add text file to directory
bin/hadoop dfs -mkdir hadoop-project
bin/hadoop dfs -put $project/text/text_processed.txt hadoop-project

# Run Task 1 with word composition lengths 2, 3, 4 and 5
bash $project/code/bash_scripts/T1.sh 2 T1-2
bash $project/code/bash_scripts/T1.sh 3 T1-3
bash $project/code/bash_scripts/T1.sh 4 T1-4
bash $project/code/bash_scripts/T1.sh 5 T1-5

# Run Task 2
bash $project/code/bash_scripts/T2.sh T2

# Run Task 3 with specified top n% 
bash $project/code/bash_scripts/T3.sh 2 T3-2

# Run Task 4
bash $project/code/bash_scripts/T4.sh travel T4-travel

# Run Task 5
bash $project/code/bash_scripts/T5.sh travel T5-travel