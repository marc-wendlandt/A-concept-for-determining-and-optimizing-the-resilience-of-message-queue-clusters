import subprocess
import pika
import time

#rabbitmqctl: https://www.rabbitmq.com/rabbitmqctl.8.html
#perf-test: https://rabbitmq.github.io/rabbitmq-perf-test/stable/htmlsingle/
#cluster-setup: https://levelup.gitconnected.com/setting-up-rabbitmq-cluster-c247d61385ed

#create rabbitmq cluster with 2 nodes/brokers
subprocess.call(r'tests\\rabbitmq\startCluster_2Nodes.bat', shell=True)
#time.sleep(30)

#establish connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=8081))
channel = connection.channel()

channel.queue_declare(queue='meine_queue', durable=True)

connection.close()

#result = subprocess.run("java -jar perf-test.jar --help", shell=True, check=True, text=True, capture_output=True)
#print(result.stdout)   


#stop cluster
#subprocess.call(r'tests\\rabbitmq\stopCluster.bat', shell=True)