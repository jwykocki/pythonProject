from apscheduler.schedulers.background import BackgroundScheduler
import scrapper.scrapper_service as scrapper_service
import logging
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
seconds = config.get('scheduler', 'seconds')

def start_scheduling():
    scheduler = BackgroundScheduler()
    scheduler.add_job(scrapper_service.delete_old_offers_and_fetch_new, trigger='interval', seconds=seconds)
    logging.info(f"Starting scheduled tasks")
    scheduler.start()