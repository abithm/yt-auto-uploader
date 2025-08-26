import os
import time
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

UPLOAD_DIR = "path_to_your_upload_folder"
CHECK_INTERVAL = 600  # seconds, e.g., check every 10 minutes
uploaded = set()  # store uploaded video filenames

def get_catchy_description(title):
    # Dummy function, replace with your real one or API call
    return f"Check out this video: {title}!"

def save_uploaded_video(video):
    uploaded.add(video)

def upload_video(file_path, title, description):
    """
    Replace this with your actual upload function.
    Return a dummy video_id for now.
    """
    logging.info(f"Uploading {file_path} with title: {title}")
    return "dummy_video_id"

def scheduler():
    while True:
        videos = [v for v in os.listdir(UPLOAD_DIR) if v.endswith(".mp4")]
        
        for video in videos:
            if video not in uploaded:
                file_path = os.path.join(UPLOAD_DIR, video)
                title = os.path.splitext(video)[0]
                description = get_catchy_description(title)

                try:
                    logging.info(f"🎬 Uploading new video: {video}")
                    video_id = upload_video(file_path, title, description)
                    save_uploaded_video(video)
                    logging.info(f"✅ Uploaded {video} (videoId={video_id})")
                except Exception as e:
                    logging.error(f"❌ Failed to upload {video}: {e}")

                # Wait 1 hour before next upload
                logging.info("⏳ Waiting 1 hour before next upload...")
                time.sleep(3600)

        logging.info("⏳ Scheduled upload check completed. Waiting for next check...")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    scheduler()
