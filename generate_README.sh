#!/bin/bash

# Generate the final Markdown table

echo "Below you can find the solution in the dropdown menu" > final_table.md
echo "<details>" >> final_table.md
echo "<summary>List of the Solutions by language</summary>" >> final_table.md
echo "<br>" >> final_table.md
echo " " >> final_table.md
echo "| ID | Problem Name | Python Solution Link |" >> final_table.md
echo "|----|--------------|----------------------|" >> final_table.md

while read -r line 
do 
	pn=$( echo "$line" | grep -E -o '\[\s*([0-9]+)\s*\]' | grep -E -o '[0-9]+' ) # problem number
	filename=$(ls ~/.leetcode/code/ | grep "^$pn\..*\.py$")
	if [ -n "$filename" ]; then
		# split the filename in 3 parts, dividing by the .
		title=$(echo "$filename" | cut -d '.' -f 2)
		# and now we substitute all '-' with empty spaces
		problem_name=$(echo "$title" | tr '-' ' ' )
		echo "| $pn | $problem_name | [Python solution](solutions/$filename) |" >> final_table.md
		cp ~/.leetcode/code/$pn*.py solutions/
	else
		echo "| $pn | | |" >> final_table.md
	fi
done < .out
echo "</details>" >> final_table.md

cat .header > README.md
cat final_table.md >> README.md
cat .footer >> README.md
