import os
import time
from icrawler.builtin import BingImageCrawler

# Define save directories
SAVE_DIR_MIDDLE = "data/raw/middle_finger"
SAVE_DIR_OTHER = "data/raw/other"

def crawl_images(keyword, save_dir, max_num):
    print(f"[*] Starting crawl for: '{keyword}' into {save_dir}")
    os.makedirs(save_dir, exist_ok=True)
    
    crawler = BingImageCrawler(storage={'root_dir': save_dir})
    
    # Optional filters to get better data
    filters = dict(type='photo', color='color')
    
    crawler.crawl(keyword=keyword, filters=filters, max_num=max_num, file_idx_offset=0)
    print(f"[+] Finished crawling for: '{keyword}'. Total requested: {max_num}\n")

def main():
    print("===============================================")
    print(" Image Analyzer - Web Crawling Data Collection ")
    print("===============================================")
    
    # Middle Finger Queries
    # Bing handles multiple overlapping queries well if we put them in the same root_dir
    # icrawler will automatically iterate file names starting from 000001.jpg
    middle_finger_queries = [
        "person showing middle finger",
        "middle finger gesture",
        "flipping the bird gesture",
        "hand pointing middle finger",
        "middle finger sign",
        "angry person middle finger",
        "showing the finger gesture",
        "middle finger isolated clear",
        "person face with middle finger gesture",
        "celebrity showing middle finger",
        "selfie showing middle finger",
        "crowd person pointing middle finger",
        "woman showing middle finger to camera",
        "man flipping bird portrait",
        "kid showing middle finger"
    ]
    
    # Other Gestures Queries (Negative dataset)
    other_queries = [
        "thumbs up hand gesture",
        "waving hand person",
        "open palm hand",
        "fist bump gesture",
        "peace sign hand fingers",
        "pointing index finger",
        "holding pen hand",
        "ok hand gesture sign",
        "clapping hands",
        "crossed fingers luck",
        "shaking hands gesture",
        "thumbs down gesture",
        "empty room interior",
        "nature landscape background",
        "person walking away",
        "person smiling face portrait",
        "group of people taking selfie",
        "man hands in pockets",
        "woman holding smartphone",
        "crowd of people cheering",
        "person eating food close up",
        "dog playing in park",
        "car driving on street"
    ]

    # Target images per query
    # 15 queries * 150 = 2250 max theoretical for middle finger
    # 23 queries * 100 = 2300 max theoretical for other
    imgs_per_mf_query = 150
    imgs_per_other_query = 100

    print("\n--- Crawling 'Middle Finger' Class ---")
    for q in middle_finger_queries:
        crawl_images(q, SAVE_DIR_MIDDLE, imgs_per_mf_query)
        time.sleep(2) # Be polite to the server

    print("\n--- Crawling 'Other' Class ---")
    for q in other_queries:
        crawl_images(q, SAVE_DIR_OTHER, imgs_per_other_query)
        time.sleep(2)

    print("===============================================")
    print(" Data collection finished. Please verify the `data/raw` contents.")
    print(" Note: Bing may not find the exact max_num, so check the final count.")

if __name__ == "__main__":
    main()
