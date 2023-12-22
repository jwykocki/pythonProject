from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker
import logging
from offer.offer import Base, Offer


def create_session_and_save_offers(offers):
    session = create_session()
    save_offers_to_database(session, offers)
    return session

def create_session_and_get_offers():
    session = create_session()
    offers = get_offers_from_database(session)
    return offers


def create_session():
    engine = create_engine("mysql+mysqlconnector://root:Bdpsfirstjjoobb.cpp0002@127.0.0.1/job_offers")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    logging.info(f"Created session with database")
    return Session()

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
            logging.info(f"Offer {offer} already exists in database")
    logging.info(f"Added {added} offers to database")
    return added

def get_offers_from_database(session):
    logging.info(f"Getting offers from database")
    offers = session.query(Offer).all()
    logging.info(f"Got {len(offers)} offers from database")
    return offers

