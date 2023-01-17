#!/bin/bash

###
# Q1: Can you describe what this script is intended to do?
#
# Q2: When the script runs, it gives error: `InvalidUrlError: Invalid destination path: /tmp/sorted_files/descriptions` why might this be?
###

tmp_dir="/tmp/gsurl_list_files"
save_dir="/tmp/sorted_files"

if [[ ! -d $tmp_dir ]]; then
  mkdir -p $tmp_dir
fi
rm $tmp_dir/*.txt


gsuri_files_dirs=$(python -c "from helpers import get_files_list; gsurlfiles = get_files_list(\"$tmp_dir\"); print(gsurlfiles);")
echo $gsuri_files_dirs

if [[ "$gsuri_files_dirs" = *"none" ]]; then
  echo "no files"
  exit 0
fi


if [[ "$save_dir" != "gs://"* ]]; then
  mkdir $save_dir
fi

for gsuri_file_dir in ${gsuri_files_dirs[@]}
done
  gsutil -m cp $(cat "$tmp_dir/$gsuri_file_dir.txt") $save_dir/$gsuri_file_dir
done

ls $save_dir/*