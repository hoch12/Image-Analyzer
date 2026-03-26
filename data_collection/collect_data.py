import os
import sys
import time
from icrawler.builtin import BingImageCrawler

"""
Data collection utility for the Image Analyzer project.
Uses icrawler (Bing) to automate image harvesting for model training.
"""

# Add the project root to the path so we can import from `src`
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src import config

def crawl_images(keyword, save_dir, max_num):
    """
    Downloads images for a specific keyword into the target directory.
    Uses an offset to prevent overwriting existing data.

    Args:
        keyword (str): The search term for Bing.
        save_dir (str): Directory where images will be stored.
        max_num (int): Maximum number of images to attempt to download.
    """
    print(f"[*] Starting crawl for: '{keyword}' into {save_dir}")
    os.makedirs(save_dir, exist_ok=True)
    
    # Calculate offset so we don't overwrite existing images (000001.jpg, 000002.jpg...)
    existing_files = len([f for f in os.listdir(save_dir) if os.path.isfile(os.path.join(save_dir, f))])
    print(f"    Current files in dir: {existing_files}. Offset set to {existing_files}.")
    
    crawler = BingImageCrawler(storage={'root_dir': save_dir})
    
    # Filters to ensure we get photographic color data
    filters = dict(type='photo', color='color')
    
    crawler.crawl(keyword=keyword, filters=filters, max_num=max_num, file_idx_offset=existing_files)
    print(f"[+] Finished crawling for: '{keyword}'. Total requested: {max_num}\n")

def main():
    """Main execution loop for full dataset harvesting."""
    print("===============================================")
    print(" Image Analyzer - Web Crawling Data Collection ")
    print("===============================================")
    
    # Queries and targets are now loaded centrally from config
    middle_finger_queries = config.CRAWLER_MIDDLE_FINGER_QUERIES
    other_queries = config.CRAWLER_OTHER_QUERIES
    
    imgs_per_mf_query = config.CRAWLER_IMGS_PER_MF_QUERY
    imgs_per_other_query = config.CRAWLER_IMGS_PER_OTHER_QUERY

    print("\n--- Harvesting 'Middle Finger' Class ---")
    for q in middle_finger_queries:
        crawl_images(q, config.SAVE_DIR_MIDDLE, imgs_per_mf_query)
        time.sleep(2) # Prevent rate-limiting

    print("\n--- Harvesting 'Other' Class ---")
    for q in other_queries:
        crawl_images(q, config.SAVE_DIR_OTHER, imgs_per_other_query)
        time.sleep(2)

    print("===============================================")
    print(" Data collection finished. Please verify the `data/raw` contents.")

if __name__ == "__main__":
    main()
