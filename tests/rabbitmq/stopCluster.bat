@echo off

echo Stopping rabbit-1
docker stop rabbit-1

echo Stopping rabbit-2
docker stop rabbit-2

echo Stopping rabbit-3
docker stop rabbit-3

echo Stopping rabbit-4
docker stop rabbit-4

echo Removing network rabbit
docker network rm rabbit
