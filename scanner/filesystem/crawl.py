import os
import re

def crawl_filesystem(top: str = "/", regex_patterns: str):

    """    
    :param patterns: 
    :param top: 
    :param excludes: 
    :return: 
    """
    files_matching_pattern = []
    for root, dirs, files in os.walk(top):
        for file in files:
            file_path = os.path.join(root, file)
            if re.match(regex_patterns, file_path):
                files_matching_pattern.append(file_path)
    return files_matching_pattern


if __name__ == "__main__":
    crawl_filesystem(regex_patterns="kevin")