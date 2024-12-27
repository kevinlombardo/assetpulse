import os
import re

def crawl_filesystem(top: str = "/", regex_patterns: str = ""):

    """    
    :param patterns: 
    :param top: 
    :param excludes: 
    :return: 
    """
    files_matching_pattern = {}
    for root, dirs, files in os.walk(top):
        for file in files:
            file_path = os.path.join(root, file)
            match = re.match(regex_patterns, file)
            if match:
                for k, v in match.groupdict().items():
                    if v is not None:
                        print(f"{k}")
                        files_matching_pattern[k] = file_path
    return files_matching_pattern


if __name__ == "__main__":
    print(crawl_filesystem(regex_patterns="(?P<TEST1>)^kevin$|(?P<TEST2>)^kevin2$"))