import scrapper.justjoinit_scrapper as justjoinit_scrapper
import scrapper.nofluffjobs_scrapper as no_fluff_jobs_scrapper
import db.db_service as db

def delete_old_offers_and_fetch_new():
    offers = []
    offers_from_just_join = justjoinit_scrapper.get_offers_from_website()
    offers_from_no_fluff = no_fluff_jobs_scrapper.get_offers_from_website()
    offers.extend(offers_from_just_join)
    offers.extend(offers_from_no_fluff)
    db.delete_old_offers_and_save_new_to_db(offers)

