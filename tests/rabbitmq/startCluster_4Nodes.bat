@echo off
echo creating network rabbit
docker network create rabbit

echo Starting rabbit-1
docker run -d --rm --net rabbit ^
-v "%cd%/config/rabbit-1/:/config" ^
-e RABBITMQ_CONFIG_FILE=/config/rabbitmq ^
-e RABBITMQ_ERLANG_COOKIE=IEWLRKYWOKIHEOZHXFMN ^
--hostname rabbit-1 ^
--name rabbit-1 ^
-p 8081:15672 ^
rabbitmq:management

echo Starting rabbit-2
docker run -d --rm --net rabbit ^
-v "%cd%/config/rabbit-2/:/config" ^
-e RABBITMQ_CONFIG_FILE=/config/rabbitmq ^
-e RABBITMQ_ERLANG_COOKIE=IEWLRKYWOKIHEOZHXFMN ^
--hostname rabbit-2 ^
--name rabbit-2 ^
-p 8082:15672 ^
rabbitmq:management

echo Starting rabbit-3
docker run -d --rm --net rabbit ^
-v "%cd%/config/rabbit-3/:/config" ^
-e RABBITMQ_CONFIG_FILE=/config/rabbitmq ^
-e RABBITMQ_ERLANG_COOKIE=IEWLRKYWOKIHEOZHXFMN ^
--hostname rabbit-3 ^
--name rabbit-3 ^
-p 8083:15672 ^
rabbitmq:management

echo Starting rabbit-4
docker run -d --rm --net rabbit ^
-v "%cd%/config/rabbit-3/:/config" ^
-e RABBITMQ_CONFIG_FILE=/config/rabbitmq ^
-e RABBITMQ_ERLANG_COOKIE=IEWLRKYWOKIHEOZHXFMN ^
--hostname rabbit-4 ^
--name rabbit-4 ^
-p 8084:15672 ^
rabbitmq:management