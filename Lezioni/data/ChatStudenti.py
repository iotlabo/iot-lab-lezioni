import paho.mqtt.client as mqtt    #Necessario installare paho con il comando "pip install paho-mqtt"
import time
import socket


# Come broker viene utilizzato un Broker Python, hbmqtt, installabile con "pip install hbmqtt"
# Per eseguire il broker usare il comando "hbmqtt -c hbmqtt_config.yaml"
# Dove è stato creato il relativo file di configurazione nella directory da dove si lancia il broker
# Il contenuto del file di configurazione è il seguente:
# listeners:
#   default:
#     type: tcp
#     bind: 0.0.0.0:1883
# sys_interval: 20
# auth:
#   allow-anonymous: true
# plugins:
#   - auth_file
#   - auth_anonymous
# topic-check:
#   enabled': True
#   plugins': 
#     - topic_taboo


    
# Descrive un oggetto che permette di creare una chat tra studenti usando il protocollo MQTT
class ChatStudente():
    nickname = ""            # nome utente
    target_nickname = ""     # nome del destinatario
    porta_broker = 1883
    ip_broker = ""           # ip del PC docente (broker)
    # Funzione realizzata dall'utente per gestire i messaggi ricevuti
    # Deve ricevere i seguenti parametri: nickname_mittente, messaggio
    funzione_utente_gestione_messaggi = None    
    
    # Costruttore
    def __init__(self, broker_ip, nickname):
        self.ip_broker = broker_ip.strip()
        self.nickname = nickname.strip().lower().replace(" ", "_").replace("/", "_")
        
    # Funzione per uso interno alla classe: callback evento on_connect di Paho MQTT, usato solo in modalità avviaRicevitore()
    def __paho_on_connect(self, client, userdata, flags, rc):
        print("Connesso al Broker MQTT su " + self.ip_broker)
        print("Avvio Subscriber MQTT: Per terminare la chat premere due volte I in Jupyter (Kernel -> Interrupt Kernel) oppure CTRL+C se nel terminale\n")
        client.subscribe("chat/" + self.nickname + "/#")
     
    # Funzione per uso interno alla classe: callback evento on_publish (conferma) di Paho MQTT
    def __paho_on_publish(self, client, userdata, mid):
        print("Messaggio inviato!")
        client.disconnect()
    
    # Funzione per uso interno alla classe: callback on_message di Paho MQTT
    def __paho_on_message(self, client, userdata, msg):
        topic_split = msg.topic.split("/")
        nickname_mittente = topic_split[2]
        messaggio = msg.payload.decode("utf-8")
        print(">>>> [{}] Ricevuto messaggio da: {}".format(time.strftime("%Y/%m/%d %H:%M:%S"), nickname_mittente))
        self.funzione_utente_gestione_messaggi(nickname_mittente, messaggio)
    
    # Funzione per inviare un messaggio ad un nickname destinatario
    def inviaMessaggio(self, destinatario, messaggio):
        self.target_nickname = destinatario.strip().lower().replace(" ", "_").replace("/", "_")
        client = mqtt.Client()
        client.on_publish = self.__paho_on_publish 
        client.connect(self.ip_broker, self.porta_broker, 60)
        print("Connesso al Broker MQTT su " + self.ip_broker + " - Invio messaggio a: {} .....".format(self.target_nickname), end=" ")
        client.publish("chat/" + self.target_nickname + "/"+ self.nickname, messaggio)
    
    # Funzione per avviare il ricevitore dei messaggi (loop infinito)
    def avviaRicevitore(self, funzione_callback_gestione_messaggi_ricevuti):
        self.funzione_utente_gestione_messaggi = funzione_callback_gestione_messaggi_ricevuti
        client = mqtt.Client()
        client.on_connect = self.__paho_on_connect
        client.on_message = self.__paho_on_message
        client.connect(self.ip_broker, self.porta_broker, 60)
        client.loop_forever()

        
def get_lan_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP
    
    