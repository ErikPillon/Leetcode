#!/bin/bash

# Get the directory containing the Python files
dir=$1

# Create a new file called "statistics.csv"
touch statistics.csv

# Iterate over all of the Python files in the directory
for file in $dir/*.py; do

  # Get the date the file was created
  date=$(stat -c %y $file)

  # Get the name of the LeetCode problem
  problem=$(basename $file | sed 's/\.py//g')

  # Get the number of lines of code in the solution
  number_of_lines=$(wc -l $file | awk '{print $1}')

  # Get the number of test cases in the solution
  # number_of_tests=$(grep -c "def test" $file)

  # Get the percentage of test cases that the solution passes
  # passing_percentage=$(python -m unittest $file | grep -c "ok") / $number_of_tests * 100

  # Append a row to the "statistics.csv" file
  echo "$date,$problem,$number_of_lines" >> statistics.csv
done
