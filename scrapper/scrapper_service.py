import scrapper.justjoinit_scrapper as justjoinit_scrapper
import db.db_service as db

def fetch_all_offers_and_save_to_db():
    offers = justjoinit_scrapper.get_offers_from_website()
    db.create_session_and_save_offers(offers)
