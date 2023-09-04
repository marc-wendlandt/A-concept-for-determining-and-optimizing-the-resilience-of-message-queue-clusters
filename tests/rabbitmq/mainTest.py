import subprocess
import time
from subprocess import Popen

def runTest(brokers, consumer, producer, messageSize, queues, duration):

    resultNode_1 = subprocess.run(
        "docker run -it --rm --network rabbit pivotalrabbitmq/perf-test:latest --uri amqp://rabbit-1" +
        " -x " + str(producer) +
        " -y " + str(consumer) +
        " -s " + str(messageSize) +
        " -u " + str(queues) +
        " -z " + str(duration),
        shell=True, text=True, capture_output=True, check=True)

    

    resultNode_2 = subprocess.run(
        "docker run -it --rm --network rabbit pivotalrabbitmq/perf-test:latest --uri amqp://rabbit-2" +
        " -x " + str(producer) +
        " -y " + str(consumer) +
        " -s " + str(messageSize) +
        " -u " + str(queues) +
        " -z " + str(duration),
        shell=True, text=True, capture_output=True, check=True)


    if brokers >= 3:
        resultNode_3= subprocess.run("docker run -d --rm pivotalrabbitmq/perf-test:latest --network rabbit --uri amqp://rabbit-3" +
                                  " -x " + str(producer) + 
                                  " -y " + str(consumer) +
                                  " -s " + str(messageSize) +
                                  " -u " + str(queues) +
                                  " -st " + str(duration)
                                  , shell=True, check=True, text=True, capture_output=True)

    if brokers >= 4:
        resultNode_4= subprocess.run("docker run -d --rm pivotalrabbitmq/perf-test:latest --network rabbit --uri amqp://rabbit-4" +
                                  " -x " + str(producer) + 
                                  " -y " + str(consumer) +
                                  " -s " + str(messageSize) +
                                  " -u " + str(queues) +
                                  " -st " + str(duration)
                                  , shell=True, check=True, text=True, capture_output=True)
        
    return resultNode_1, resultNode_2   

#rabbitmqctl: https://www.rabbitmq.com/rabbitmqctl.8.html
#perf-test: https://rabbitmq.github.io/rabbitmq-perf-test/stable/htmlsingle/
#cluster-setup: https://levelup.gitconnected.com/setting-up-rabbitmq-cluster-c247d61385ed

#create rabbitmq cluster with 2 nodes/brokers
#subprocess.call(r'tests\\rabbitmq\startCluster_2Nodes.bat', shell=True)
#time.sleep(30)

#run test
print(runTest(2, 1, 1, 1000, 1, 5))