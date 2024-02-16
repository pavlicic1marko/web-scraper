import os


def create_proj_dir(directory):
    if not os.path.exists(directory):
        print('creating dir' + directory)
        os.makedirs(directory)
    else:
        print('directory exists: ' + directory)


def create_data_files(project_name, base_url):
    queue = os.path.join(project_name, "queue.txt")
    crawled = os.path.join(project_name, "crawled.txt")
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')


def write_file(path, data):
    with open(path,'w') as f:
        f.write(data)


def append_to_file(file_path, data):
    with open(file_path,'a') as f:
        f.write(data+'\n') # or ,


def delete_file_contents(path):
    open(path,'w').close()


def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:  # rt mode is read and write
        for line in f:
            results.add(line.replace('\n',''))
    return  results


def set_to_file(links,file_name):
    with open(file_name, 'w') as f:
        for line in sorted(links):
            f.write(line+'\n')


