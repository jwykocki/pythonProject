from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker
import logging
from offer.offer import Base, Offer
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
host = config.get('database', 'host')
port = int(config.get('database', 'port'))
user = config.get('database', 'user')
password = config.get('database', 'password')
database = config.get('database', 'database')


def delete_old_offers_and_save_new_to_db(offers):
    session = create_session()
    delete_all_offers_from_database(session)
    save_offers_to_database(session, offers)
    return session

def create_session_and_get_offers():
    session = create_session()
    offers = get_offers_from_database(session, limit=50)
    return offers


def create_session():

    engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}")
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    logging.info(f"Created session with database")
    return session()

def save_offers_to_database(session, offers):
    logging.info(f"Saving {len(offers)} offers to database")
    added = 0
    for offer in offers:
        try:
            session.add(offer)
            session.commit()
            added += 1
        except IntegrityError:
            session.rollback()
            logging.info(f"Offer with URL: {offer.offerUrl} already exists in database")
    logging.info(f"Added {added} offers to database")
    return added

def get_offers_from_database(session, limit=None):
    logging.info(f"Getting offers from database")
    query = session.query(Offer)
    if limit is not None:
        query = query.limit(limit)
    offers = query.all()
    logging.info(f"Got {len(offers)} offers from database")
    return offers

def delete_all_offers_from_database(session):
    logging.info(f"Deleting all offers from database")
    session.query(Offer).delete()
    session.commit()
    logging.info(f"Deleted all offers from database")
