import requests
import time
import logging
from typing import Dict

logger = logging.getLogger(__name__)

def notify_evaluation(evaluation_url: str, payload: Dict) -> None:
    """
    POST payload to evaluation_url with exponential backoff on transient errors.
    Logs a warning instead of crashing if all retries fail.
    """
    delays = [1, 2, 4, 8]
    headers = {"Content-Type": "application/json"}
    for attempt, delay in enumerate(delays, start=1):
        try:
            r = requests.post(evaluation_url, json=payload, headers=headers, timeout=15)
            if 200 <= r.status_code < 300:
                logger.info(f"✅ Notified evaluation server successfully on attempt {attempt}")
                return
            else:
                logger.warning(f"⚠️ Attempt {attempt}: got status {r.status_code} from evaluation server")
        except requests.RequestException as e:
            logger.warning(f"⚠️ Attempt {attempt}: exception while notifying evaluation server: {e}")
        time.sleep(delay)
    
    # Instead of crashing, just warn
    logger.error("❌ Failed to notify evaluation URL after retries — continuing anyway")
