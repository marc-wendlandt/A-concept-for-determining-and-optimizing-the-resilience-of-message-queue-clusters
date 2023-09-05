@echo off
echo creating network rabbit
docker network create rabbit

echo Starting rabbit-1
docker run -d --rm --net rabbit ^
-v "G:\Meine Ablage\uni\Bachelorarbeit\A-concept-for-determining-and-optimizing-the-resilience-of-message-queue-clusters\tests\rabbitmq/config/2_Nodes/rabbit-1/:/config" ^
-e RABBITMQ_CONFIG_FILE=/config/rabbitmq ^
-e RABBITMQ_ERLANG_COOKIE=QMUGAWMCJIYNJHYZGCCP ^
--hostname rabbit-1 ^
--name rabbit-1 ^
-p 15672:15672 ^
rabbitmq:3.12-management

echo Starting rabbit-2
docker run -d --rm --net rabbit ^
-v "G:\Meine Ablage\uni\Bachelorarbeit\A-concept-for-determining-and-optimizing-the-resilience-of-message-queue-clusters\tests\rabbitmq/config/2_Nodes/rabbit-1/:/config" ^
-e RABBITMQ_CONFIG_FILE=/config/rabbitmq ^
-e RABBITMQ_ERLANG_COOKIE=QMUGAWMCJIYNJHYZGCCP ^
--hostname rabbit-2 ^
--name rabbit-2 ^
-p 15673:15672 ^
rabbitmq:3.12-management