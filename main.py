import  threading
from queue import Queue
from spider import Spider
from domain import *
from demo import *

PROJECT_NAME = 'the site'
HOME_PAGE = 'https://en.wikipedia.org/wiki/King%27s_Dock,_Port_of_Liverpool'
DOMAIN_NAME = get_domain_name(HOME_PAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 4
queue = Queue()
Spider(PROJECT_NAME, HOME_PAGE, DOMAIN_NAME)

def crawl():
    queued_links = file_to_set(QUEUE_FILE)  # load links from file
    if len(queued_links) > 0:
        print('links in the que are:' + str(len(queued_links)))
        create_jobs() # put the link in the queue

def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
        queue.join()
        crawl()

def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work) # crate a thred for work function
        t.daemon = True
        t.start()

def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.currentThread().name, url)
        queue.task_done() # terminate thread


create_workers()
crawl()