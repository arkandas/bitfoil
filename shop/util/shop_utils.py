import json
import logging
import os

from model.ShopIndex import IndexFile, ShopIndex

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_games_list() -> list[dict]:
    root_dir = os.getenv('SHOP_PATH')
    file_list: list[dict] = []
    for directory, _, files in os.walk(root_dir):
        for file_name in files:
            if file_name.lower().endswith(('.nsp', '.nsz', '.xci', '.xcz')):
                rel_dir = os.path.relpath(directory, root_dir)
                if rel_dir != '.':
                    rel_file = os.path.join(rel_dir, file_name)
                else:
                    rel_file = file_name
                file_list.append(IndexFile('../' + rel_file,
                                           os.path.getsize(os.path.join(root_dir, rel_file))).to_json_dict())
    logger.info(f'Found {len(file_list)} game(s) and DLC(s) in monitored folder')
    return file_list


def write_shop_index() -> None:
    shop_index = ShopIndex(os.getenv('SHOP_MOTD'))
    shop_index.files = create_games_list()
    shop_files = ['shop.json', 'shop.tfl']
    for shop in shop_files:
        try:
            with open(os.getenv('SHOP_PATH') + '/' + shop, 'w') as file:
                file.write(json.dumps(shop_index.to_json_dict(), indent=4))
                logger.info(f'{shop} created successfully')
        except Exception as e:
            logger.error(f'Error creating {shop}:\n{e}')


