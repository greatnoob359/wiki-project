from queue import Queue
import wikipediaapi
import time

user_agent = "wiki-project (pohidt@outlook.com)"
wiki = wikipediaapi.Wikipedia(user_agent, "en")

def fetch_links(page):
    links_list = []
    links = page.links

    for title in links.keys():
        links_list.append(title)
    return links_list


def wikipedia_solver(start_page, target_page):
    print("loading, pease wait")
    start_time = time.time()

    queue = Queue()
    visited = set()
    parent = {}

    queue.put(start_page.title)
    visited.add(start_page.title)

    while not queue.empty():
        current_page_title = queue.get()
        if current_page_title == target_page.title:
            break

        current_page = wiki.page(current_page_title)
        links = fetch_links(current_page)

        for link in links:
            if link not in visited:
                queue.put(link)
                parent[link] = current_page_title

    path = []
    page_title = target_page.title
    while page_title != start_page.title:
        path.append(page_title)
        page_title = parent[page_title]

    path.append(start_page.title)
    path.reverse()

    end_time = time.time()
    print("time it took", end_time - start_time, "seconds to run")
    return path

#creating start and target pages
start_page = wiki.page("chicken nugget")
target_page = wiki.page("responsibility")
path = wikipedia_solver(start_page, target_page)
print(fetch_links(start_page))