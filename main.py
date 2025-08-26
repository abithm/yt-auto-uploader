import logging
from scheduler import schedule_uploads

if __name__ == "__main__":
    logging.basicConfig(
        filename="uploader.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    logging.info("🚀 YouTube Shorts Auto Uploader started.")
    schedule_uploads()
