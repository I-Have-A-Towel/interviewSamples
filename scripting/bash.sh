#!/bin/bash

###
# Can you describe what this script is intended to do?
###

benchmark_ref=$1
tmp_dir="/tmp/gsurl_list_files"
save_dir="/tmp/sorted_files"

if [[ ! -d $tmp_dir ]]; then
  mkdir -p $tmp_dir
fi
rm $tmp_dir/*.txt


gsuri_files=$(python -c "from helpers import get_files_list; gsurlfiles = get_files_list(\"$tmp_dir\"); print(gsurlfiles);")
echo $gsuri_files

if [[ "$gsuri_files" = *"none" ]]; then
  echo "no files"
  exit 0
fi


if [[ "$save_dir" != "gs://"* ]]; then
  mkdir $save_dir
fi

for gsuri_file in ${gsuri_files[@]}
do
  echo copying $save_dir/$gsuri_file...
  if [[ "$save_dir" != "gs://"* ]]; then
    mkdir $save_dir/$gsuri_file
  fi
  gsutil -m cp $(cat "$tmp_dir/$gsuri_file.txt") $save_dir/$gsuri_file
done

ls $save_dir/*