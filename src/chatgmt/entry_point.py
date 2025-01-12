""" Start the Uvicorn server with the Dash app """
import logging
import os

from chatgmt.chatgmt import app
from chatgmt.settings import settings


server = app.server


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def main():

    os.environ['REACT_VERSION'] = '18.2.0'

    logger.info('Starting server')

    app.run(
        host='0.0.0.0',
        port=settings.PORT,
        debug=settings.DEBUG_MODE,
    )


if __name__ == "__main__":
    main()
