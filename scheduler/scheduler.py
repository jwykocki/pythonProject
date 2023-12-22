from apscheduler.schedulers.background import BackgroundScheduler
import scrapper.scrapper_service as scrapper_service
import logging

def start_scheduling():
    scheduler = BackgroundScheduler()
    scheduler.add_job(scrapper_service.fetch_all_offers_and_save_to_db, trigger='interval', seconds=3000)
    logging.info(f"Starting scheduled tasks")
    scheduler.start()