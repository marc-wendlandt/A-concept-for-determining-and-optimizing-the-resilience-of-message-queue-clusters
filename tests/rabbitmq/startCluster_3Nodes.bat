@echo off
echo creating network rabbit
docker network create rabbit

echo Starting rabbitmq
docker run -d --rm --network rabbit ^
-v "G:\Meine Ablage\uni\Bachelorarbeit\A-concept-for-determining-and-optimizing-the-resilience-of-message-queue-clusters\tests\rabbitmq/config/3_Nodes/rabbit-1/:/config" ^
-e RABBITMQ_CONFIG_FILE=/config/rabbitmq ^
-e RABBITMQ_ERLANG_COOKIE=QMUGAWMCJIYNJHYZGCCP ^
--hostname rabbit-1 ^
--name rabbit-1 ^
-p 15672:15672 ^
rabbitmq:3.12-management

echo Starting rabbit-2
docker run -d --rm --network rabbit ^
-v "G:\Meine Ablage\uni\Bachelorarbeit\A-concept-for-determining-and-optimizing-the-resilience-of-message-queue-clusters\tests\rabbitmq/config/3_Nodes/rabbit-2/:/config" ^
-e RABBITMQ_CONFIG_FILE=/config/rabbitmq ^
-e RABBITMQ_ERLANG_COOKIE=QMUGAWMCJIYNJHYZGCCP ^
--hostname rabbit-2 ^
--name rabbit-2 ^
-p 15673:15672 ^
rabbitmq:3.12-management

echo Starting rabbit-3
docker run -d --rm --network rabbit ^
-v "G:\Meine Ablage\uni\Bachelorarbeit\A-concept-for-determining-and-optimizing-the-resilience-of-message-queue-clusters\tests\rabbitmq/config/3_Nodes/rabbit-3/:/config" ^
-e RABBITMQ_CONFIG_FILE=/config/rabbitmq ^
-e RABBITMQ_ERLANG_COOKIE=QMUGAWMCJIYNJHYZGCCP ^
--hostname rabbit-3 ^
--name rabbit-3 ^
-p 15674:15672 ^
rabbitmq:3.12-management