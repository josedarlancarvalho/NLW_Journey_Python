import pytest
import uuid
from src.models.settings.db_connection_handler import db_connection_handler
from src.models.repositories.links_repository import LinksRepository

db_connection_handler.connect()

link_id = str(uuid.uuid4())
trip_id = str(uuid.uuid4())

def test_registry_link():
    conn = db_connection_handler.get_connection()
    link_repository = LinksRepository(conn)

    link_infos = {
        "id": link_id,
        "trip_id": trip_id,
        "link": "somelink.com",
        "title": "Hotel"
    }

    link_repository.registry_link(link_infos)
