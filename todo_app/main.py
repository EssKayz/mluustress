#!/usr/bin/env python3
import logging


logger = logging.getLogger(__name__)
_app_port = 9999

if __name__ == "__main__":
    logger.info("Server started in port %d", _app_port)
