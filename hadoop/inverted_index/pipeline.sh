#!/bin/bash
#
# Example of how to chain MapReduce jobs together.  The output of one
# job is the input to the next.
#
# Hadoop (or Madoop) options
# jar index/hadoop/hadoop-streaming-2.7.2.jar   # Hadoop configuration
# -input <directory>                            # Input directory
# -output <directory>                           # Output directory
# -mapper <exec_name>                           # Mapper executable
# -reducer <exec_name>                          # Reducer executable
# -numReduceTasks 3                             # Number of reducers

# Stop on errors
# See https://vaneyckt.io/posts/safer_bash_scripts_with_set_euxo_pipefail/
set -Eeuo pipefail

# Optional input directory argument
PIPELINE_INPUT=input
if [ -n "${1-}" ]; then
  PIPELINE_INPUT="$1"
fi

# Print commands
set -x

# Remove output directories
rm -rf output output[0-9]
rm -rf ../../index/index/inverted_index

# Job 0: Document Count (this job is not part of the pipeline)
madoop \
  -input ${PIPELINE_INPUT} \
  -output output0 \
  -mapper ./map0.py \
  -reducer ./reduce0.py

# Copy document count to a separate file
cp output0/part-00000 total_document_count.txt

# Job 1
madoop \
  -input ${PIPELINE_INPUT} \
  -output output1 \
  -mapper ./map1.py \
  -reducer ./reduce1.py

# Job 2
madoop \
  -input output1 \
  -output ../../index/index/inverted_index \
  -mapper ./map2.py \
  -reducer ./reduce2.py \
  -numReduceTasks 3

  # Job 3
# madoop \
#   -input output2 \
#   -output output3 \
#   -mapper ./map3.py \
#   -reducer ./reduce3.py


# Take the original filename
ORIGINAL="../../index/index/inverted_index/part-00000"
# Take the renamed filename
RENAME="../../index/index/inverted_index/inverted_index_0.txt"

# Check the original file exists or not
if [ -f $ORIGINAL ]; then
     # Rename the file
     $(mv $ORIGINAL $RENAME)
     echo "The file is renamed."
fi
# Take the original filename
ORIGINAL="../../index/index/inverted_index/part-00001"
# Take the renamed filename
RENAME="../../index/index/inverted_index/inverted_index_1.txt"

# Check the original file exists or not
if [ -f $ORIGINAL ]; then
     # Rename the file
     $(mv $ORIGINAL $RENAME)
     echo "The file is renamed."
fi
# Take the original filename
ORIGINAL="../../index/index/inverted_index/part-00002"
# Take the renamed filename
RENAME="../../index/index/inverted_index/inverted_index_2.txt"

# Check the original file exists or not
if [ -f $ORIGINAL ]; then
     # Rename the file
     $(mv $ORIGINAL $RENAME)
     echo "The file is renamed."
fi
# REMINDER: don't forget to set -numReduceTasks in your last stage.  You'll
# need this to generate the correct number of inverted index segments.
