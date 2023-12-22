import logging
from controller.server_service import start_http_server
import scheduler.scheduler as sched

logging.basicConfig(level=logging.INFO)
port = 8090

sched.start_scheduling()
start_http_server(port)



