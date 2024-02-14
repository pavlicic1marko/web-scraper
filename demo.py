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




create_proj_dir('this_wasite')
