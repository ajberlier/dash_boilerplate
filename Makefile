build: 
	docker-compose build

up:
	docker-compose up -d

up-non-daemon:
	docker-compose up

start: 
	docker-compose start

stop:
	docker-compose stop

stop-all:
	docker stop $$(docker ps -a -q)

remove-all:
	docker rm $$(docker ps -a -q)

kill-all:
	docker stop $$(docker ps -a -q)
	docker rm $$(docker ps -a -q)

restart:
	docker-compose stop && docker-compose start

clean: 
	docker-compose down

list:
	docker-compose ps