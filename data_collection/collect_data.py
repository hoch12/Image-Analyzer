import os
import sys
import time
from icrawler.builtin import BingImageCrawler

# Add the project root to the path so we can import from `src`
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src import config

def crawl_images(keyword, save_dir, max_num):
    print(f"[*] Starting crawl for: '{keyword}' into {save_dir}")
    os.makedirs(save_dir, exist_ok=True)
    
    # Calculate offset so we don't overwrite existing images (000001.jpg, 000002.jpg...)
    existing_files = len([f for f in os.listdir(save_dir) if os.path.isfile(os.path.join(save_dir, f))])
    print(f"    Current files in dir: {existing_files}. Offset set to {existing_files}.")
    
    crawler = BingImageCrawler(storage={'root_dir': save_dir})
    
    # Optional filters to get better data
    filters = dict(type='photo', color='color')
    
    crawler.crawl(keyword=keyword, filters=filters, max_num=max_num, file_idx_offset=existing_files)
    print(f"[+] Finished crawling for: '{keyword}'. Total requested: {max_num}\n")

def main():
    print("===============================================")
    print(" Image Analyzer - Web Crawling Data Collection ")
    print("===============================================")
    
    # Queries and targets are now loaded centrally from config
    middle_finger_queries = config.CRAWLER_MIDDLE_FINGER_QUERIES
    other_queries = config.CRAWLER_OTHER_QUERIES
    
    imgs_per_mf_query = config.CRAWLER_IMGS_PER_MF_QUERY
    imgs_per_other_query = config.CRAWLER_IMGS_PER_OTHER_QUERY

    print("\n--- Crawling 'Middle Finger' Class ---")
    for q in middle_finger_queries:
        crawl_images(q, config.SAVE_DIR_MIDDLE, imgs_per_mf_query)
        time.sleep(2) # Be polite to the server

    print("\n--- Crawling 'Other' Class ---")
    for q in other_queries:
        crawl_images(q, config.SAVE_DIR_OTHER, imgs_per_other_query)
        time.sleep(2)

    print("===============================================")
    print(" Data collection finished. Please verify the `data/raw` contents.")
    print(" Note: Bing may not find the exact max_num, so check the final count.")

if __name__ == "__main__":
    main()
