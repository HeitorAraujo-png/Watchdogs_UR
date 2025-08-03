from settings import *
from services import Geral, Financeiro
from datetime import datetime
from watchdog.events import FileSystemEventHandler

timestamp = datetime.now().strftime('%d-%m-%y | %H:%M:%S |')

class MyHandler(FileSystemEventHandler):

    def on_modified(self, event):
        if not event.is_directory:
            path = event.src_path
            name = os.path.basename(path)
            try:
                if name.endswith(('.xlsx', '.csv')):
                    auto = Geral(path)
                    auto.MakeArq()
                    auto.Tratamento()
                    auto.Espaco()
                else:
                    with open(ERROR_LOG, 'a') as log:
                        log.write(f"{timestamp} Arquivo incompativel! {event.src_path} \n")
            except Exception as error:
                with open(ERROR_LOG, 'a') as log:
                    log.write(f"{timestamp} ERROR: {error}! {event.src_path} \n")    
        else:
            with open(ERROR_LOG, 'a') as log:
                log.write(f"{timestamp} Novo diretorio detectado! {event.src_path} \n")