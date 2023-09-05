import subprocess
import time
from subprocess import Popen

#rabbitmqctl: https://www.rabbitmq.com/rabbitmqctl.8.html
#perf-test: https://rabbitmq.github.io/rabbitmq-perf-test/stable/htmlsingle/
#cluster-setup: https://levelup.gitconnected.com/setting-up-rabbitmq-cluster-c247d61385ed


import concurrent.futures
import subprocess

def run_command(command, output_file):
    try:
        with open(output_file, 'w', buffering=2) as file:
            result = subprocess.run(command, shell=True, text=True, stdout=file, stderr=subprocess.PIPE, check=True)
        return result
    except subprocess.CalledProcessError as e:
        print(f"Fehler bei Befehl: {command}")
        print(e)

def runTest(testID, brokers, messageSize, consumer, producer, queues, duration):
    commands = []
    output_files = []

    for i in range(1, brokers + 1):
        uri = f"amqp://rabbit-{i}"
        command = f"docker run -it --rm --network rabbit pivotalrabbitmq/perf-test:latest -mf compact --use-millis --uri {uri}" \
                  f" -x {producer} -y {consumer} -s {messageSize} -u {queues} -z {duration}"
        commands.append(command)
        output_files.append(f"test_{testID}_broker_{i}_of_{brokers}_messageSize_{messageSize}_clients_{producer}.txt")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(run_command, commands, output_files))

    return results



run = 1
for i in range(2,5):

    #Stop running cluster
    subprocess.call(r'tests\\rabbitmq\stopCluster.bat', shell=False)
    time.sleep(10)
    #start broker cluster
    print("starting cluster")
    if i == 2:
        subprocess.call(r'tests\\rabbitmq\startCluster_2Nodes.bat', shell=False)
    if i == 3:
        subprocess.call(r'tests\\rabbitmq\startCluster_3Nodes.bat', shell=False)
    if i == 4:
        subprocess.call(r'tests\\rabbitmq\startCluster_4Nodes.bat', shell=False)
    time.sleep(60)
    print("cluster started")


    #run tests
    print("Runing tests")

    #number of brokers
    for j in range(1, 4):

        #message size
        for k in [1, 1000, 8000]:

            #client pairs
            for l in [1, 4, 16]:
                print(f"Run {run} with {i} brokers, {j} client pairs, {k} message size and {l} client pairs...")
                runTest(run, i, k, l, l, 1, 10)
                print("Test finished")
                time.sleep(5)
                run += 1 
