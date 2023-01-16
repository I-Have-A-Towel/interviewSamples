"""
These variables (dir_1, dir_1_gsurls, dir_2, dir_2_gsurls) would 
typically be filled automatically based on data in firestore/firebase.
They are filled in directly for purpose of a simple example.
"""

dir_1 = "descriptions"
dir_1_gsurls = [
    "gs://bucket/dir_1/file1.txt",
    "gs://bucket/dir_1/file2.txt",
    "gs://bucket/dir_1/file3.txt",
    "gs://bucket/dir_1/file4.txt",
]
dir_2 = "photos"
dir_2_gsurls = [
    "gs://bucket/dir_2/file1.png",
    "gs://bucket/dir_2/file2.png",
    "gs://bucket/dir_2/file3.png",
    "gs://bucket/dir_2/file4.png",
]


def get_files_list(tmp_dir):
    file_path1 = f"/{tmp_dir}/{dir_1}.txt"
    with open(file_path1, "w+") as f:
        f.write(" ".join(dir_1_gsurls))

    file_path2 = f"/{tmp_dir}/{dir_2}.txt"
    with open(file_path2, "w+") as f:
        f.write(" ".join(dir_2_gsurls))

    return f"{dir_1}\n{dir_2}"
