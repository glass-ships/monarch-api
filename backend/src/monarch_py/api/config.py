import os
from functools import lru_cache

from pydantic import BaseSettings

from monarch_py.implementations.oak.oak_implementation import OakImplementation
from monarch_py.implementations.solr.solr_implementation import SolrImplementation


class Settings(BaseSettings):
    solr_host = os.getenv("SOLR_HOST") if os.getenv("SOLR_HOST") else "127.0.0.1"
    solr_port = os.getenv("SOLR_PORT") if os.getenv("SOLR_PORT") else 8983
    solr_url = os.getenv("SOLR_URL") if os.getenv("SOLR_URL") else f"http://{solr_host}:{solr_port}/solr"
    phenio_db_path = os.getenv("PHENIO_DB_PATH") if os.getenv("PHENIO_DB_PATH") else "/data/phenio.db"


settings = Settings()


@lru_cache(maxsize=1)
def solr():
    return SolrImplementation(settings.solr_url)


@lru_cache(maxsize=1)
def oak():
    phenio_db_path = settings.phenio_db_path if os.path.exists(settings.phenio_db_path) else None
    return OakImplementation().init_semsim(phenio_path=phenio_db_path)
