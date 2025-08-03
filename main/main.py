from watch import *
import logging
from time import sleep
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler


if __name__ == "__main__":
    logging.basicConfig(
        filename=DEV_LOG,
        filemode="a",
        level=logging.INFO,
        format="%(asctime)s | %(process)d | %(message)s",
        datefmt="%d-%m-%y %H:%M:%S",
    )
    path = ARQUIVO_MONITORADO
    log = LoggingEventHandler()
    event_handler = MyHandler()
    obs = Observer()
    obs.schedule(log, path, recursive=False)
    obs.schedule(
        event_handler, path, recursive=False
    )  # recursive=True == Ler subpastas
    obs.start()
    try:
        while True:
            sleep(1)
    except KeyboardInterrupt:
        obs.stop()
        obs.join()
