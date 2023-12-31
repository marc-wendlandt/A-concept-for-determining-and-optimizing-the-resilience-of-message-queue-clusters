@echo off
echo creating network rabbit
docker network create rabbit

echo Starting rabbit-1
docker run -d --rm --net rabbit ^
-v "G:\Meine Ablage\uni\Bachelorarbeit\A-concept-for-determining-and-optimizing-the-resilience-of-message-queue-clusters\tests\rabbitmq/config/4_Nodes/rabbit-1/:/config" ^
-e RABBITMQ_CONFIG_FILE=/config/rabbitmq ^
-e RABBITMQ_ERLANG_COOKIE=IEWLRKYWOKIHEOZHXFMN ^
--hostname rabbit-1 ^
--name rabbit-1 ^
-p 15672:15672 ^
rabbitmq:management

echo Starting rabbit-2
docker run -d --rm --net rabbit ^
-v "G:\Meine Ablage\uni\Bachelorarbeit\A-concept-for-determining-and-optimizing-the-resilience-of-message-queue-clusters\tests\rabbitmq/config/4_Nodes/rabbit-2/:/config" ^
-e RABBITMQ_CONFIG_FILE=/config/rabbitmq ^
-e RABBITMQ_ERLANG_COOKIE=QMUGAWMCJIYNJHYZGCCP ^
--hostname rabbit-2 ^
--name rabbit-2 ^
-p 15673:15672 ^
rabbitmq:management

echo Starting rabbit-3
docker run -d --rm --net rabbit ^
-v "G:\Meine Ablage\uni\Bachelorarbeit\A-concept-for-determining-and-optimizing-the-resilience-of-message-queue-clusters\tests\rabbitmq/config/4_Nodes/rabbit-3/:/config" ^
-e RABBITMQ_CONFIG_FILE=/config/rabbitmq ^
-e RABBITMQ_ERLANG_COOKIE=QMUGAWMCJIYNJHYZGCCP ^
--hostname rabbit-3 ^
--name rabbit-3 ^
-p 15674:15672 ^
rabbitmq:management

echo Starting rabbit-4
docker run -d --rm --net rabbit ^
-v "G:\Meine Ablage\uni\Bachelorarbeit\A-concept-for-determining-and-optimizing-the-resilience-of-message-queue-clusters\tests\rabbitmq/config/4_Nodes/rabbit-4/:/config" ^
-e RABBITMQ_CONFIG_FILE=/config/rabbitmq ^
-e RABBITMQ_ERLANG_COOKIE=QMUGAWMCJIYNJHYZGCCP ^
--hostname rabbit-4 ^
--name rabbit-4 ^
-p 15675:15672 ^
rabbitmq:management