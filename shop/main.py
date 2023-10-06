import logging
import os
from datetime import datetime

from util.shop_utils import write_shop_index
from apscheduler.schedulers.blocking import BlockingScheduler

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
os.environ['TZ'] = 'Europe/Madrid'

scheduler = BlockingScheduler()


@scheduler.scheduled_job(trigger='interval', id='create_shop_index', minutes=10)
def create_shop_index():
    logger.info(f'Indexing task running at {datetime.now()}')
    write_shop_index()


if __name__ == '__main__':
    logger.info('Starting index generation')
    write_shop_index()
    scheduler.start()
