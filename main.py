import logging
from controller.server_service import start_http_server
import scheduler.scheduler as sched

logging.basicConfig(level=logging.INFO)

sched.start_scheduling()
start_http_server()



