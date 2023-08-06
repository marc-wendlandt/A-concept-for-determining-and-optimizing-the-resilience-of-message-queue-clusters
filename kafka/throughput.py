import random
import csv
import pprint 
pp = pprint.PrettyPrinter(indent=1, width=80, compact=True)
from tkinter import *
from PIL import ImageTk, Image
import matplotlib.pyplot as plt


def calculate_throughput(B, p_values, Sm, Nb, batchHeaderSize, packetHeaderSize, compressionRatio):
    # User inputs
    if B == None or p_values == None or Sm == None or Nb == None or batchHeaderSize == None or packetHeaderSize == None or compressionRatio == None:
        B = int(input("Enter the value of B (number of brokers): "))
        Nb = int(input("Enter the value of Nb (number of messages per batch): "))
        p_values = {}
        for i in range(1, B + 1):
            p_values[f"p{i}"] = int(input(f"Enter the amount of leader partitions for Broker {i}: "))
        Sm = float(input("Enter the value of Sm (message size in bytes): "))
        batchHeaderSize = float(input("Enter the value of batchHeaderSize (in bytes): "))
        packetHeaderSize = float(input("Enter the value of packetHeaderSize (in bytes): "))
        compressionRatio = float(input("Enter the value of compressionRatio: ")) 

    # Calculate S_b
    S_b = (Sm * Nb + batchHeaderSize) / compressionRatio

    # Calculate S_r for each broker
    S_r = {}
    for i in range(1, B + 1):
        S_r[f"S_r{i}"] = S_b * p_values[f"p{i}"] + packetHeaderSize



    # Calculate G_s for each

    def getDelay(packetSize, paritions):
        return packetSize * 0.00003566191301 + 0.115461799 + 0.01121152*paritions

    # Calculate G_s for each broker based on the provided formulas
    G_s = {}
    
    for i in range(1, B + 1):
        G_s[f"G_s{i}"] = getDelay(S_r[f"S_r{i}"], p_values[f"p{i}"])

    # Calculate R_s for each broker
    R_s = {}
    for i in range(1, B + 1):
        R_s[f"R_s{i}"] = 1 / G_s[f"G_s{i}"] * 1000


    # Calculate throughput of packets in bytes per second for each broker
    X_sp = {}
    for i in range(1, B + 1):
        X_sp[f"X_sp{i}"] = S_r[f"S_r{i}"] * R_s[f"R_s{i}"]

    # Calculate throughput of messages per second for each broker
    X_sm = {}
    for i in range(1, B + 1):
        X_sm[f"X_sm{i}"] = R_s[f"R_s{i}"] * Nb * p_values[f"p{i}"]

    # Output results

    #print total throughput in bytes per second
    total_throughput_in_B = 0
    for i in range(1, B + 1):
        total_throughput_in_B += X_sp[f"X_sp{i}"]

    #print total throughput in messages per second
    total_throughput_in_Messages = 0
    for i in range(1, B + 1):
        total_throughput_in_Messages += X_sm[f"X_sm{i}"]


    #print(f"S_r for each broker: {S_r}")    
    #print(f"G_s for each broker: {G_s}")
    #print(f"R_s for each broker: {R_s}")
    #print(f"X_sp for each broker: {X_sp}")
    #print(f"X_sm for each broker: {X_sm}")
    #print(f"Throughput of packets in bytes per second for each broker: {X_sp}")
    #print(f"Throughput of messages per second for each broker: {X_sm}")
    #print(f"Total throughput in bytes per second: {total_throughput_in_B}")
    #print(f"Total throughput in messages per second: {total_throughput_in_Messages}")

    return S_r, G_s, R_s, X_sp, X_sm, total_throughput_in_B, total_throughput_in_Messages    

def graph(x, y, xLabel, yLabel):

    plt.plot(x, y, label = i)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.show()




if __name__ == "__main__":

    with open('kafka/kafka_throughput.csv', 'w') as csvfile:
        writer = csv.writer(csvfile , quotechar='"', quoting=csv.QUOTE_MINIMAL, dialect='excel')
    
        #calculate the throughput for one broker with different p values from 1 to 15
        writer.writerow(["calculate the throughput for one broker with different p values from 1 to 15"])
        resultDifferentPValuesOneBroker = {}
        for i in range (1, 16):
            messages_per_sec = round(calculate_throughput(1, {"p1": i}, 1024, 5, 128, 64, 2)[-1],1)
            writer.writerow(["brokers: 1   p1: ", i, "   |   ", messages_per_sec, "messages/sec"])
            resultDifferentPValuesOneBroker[i] = messages_per_sec
        graph(resultDifferentPValuesOneBroker.keys(), resultDifferentPValuesOneBroker.values(), "p values", "messages/sec")

        #calculate the throughput for 3 brokers with different p values from 1 to 15 randomly distributed between the brokers
        writer.writerow(["calculate the throughput for 3 brokers with different p values from 1 to 15 randomly distributed between the brokers"])
        resultDifferentPValuesThreeBrokers = {}
        for i in range (1, 16):
            #create a dictionary p_values with the keys p1 to p3 and a random value up to i
            p_values = {}
            for j in range(1, 4):
                p_values[f"p{j}"] = random.randint(1, i)    
            messages_per_sec = round(calculate_throughput(3, p_values, 1024, 5, 128, 64, 2)[-1],1)
            writer.writerow(["brokers: 3   p: ", p_values, "   |   ", messages_per_sec, "messages/sec"])
            resultDifferentPValuesThreeBrokers[i] = messages_per_sec
        graph(resultDifferentPValuesThreeBrokers.keys(), resultDifferentPValuesThreeBrokers.values(), "p values", "messages/sec")

        #calculate the throughput for different brokers with different p values from 1 to
        writer.writerow(["calculate the throughput for different brokers with different p values from 1 to 15"])
        resultDifferentBrokers = {}
        for i in range (1, 16):
            #create a dictionary p_values with the keys p1 to pi and a random value up to i
            resultSingleBroker = {}
            p_values = {}
            for k in range (15):
                for j in range(1, i + 1):
                    p_values[f"p{j}"] = random.randint(1, i)
                messages_per_sec = round(calculate_throughput(i, p_values, 1024, 5, 128, 64, 2)[-1],1)
                resultSingleBroker[f"run {k}"] = messages_per_sec
                writer.writerow(["brokers: ",i,"    p: ", p_values, "|   ",messages_per_sec , "messages/sec"])
            resultDifferentBrokers[f"{i}"] = resultSingleBroker

        #prepare the data for the graph
        for i in resultDifferentBrokers.keys():
            run = {}
            run = resultDifferentBrokers[i]
            average = 0
            index = 0
            for run in resultDifferentBrokers[i].keys():
                average += resultDifferentBrokers[i][run]
                index += 1
            average = average / index
            resultDifferentBrokers[i] = average    
    
    graph(resultDifferentBrokers.keys(), resultDifferentBrokers.values(),"amount of brokers", "messages/sec")


    
