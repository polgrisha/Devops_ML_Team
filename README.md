# ml-team-repo

## Задание по миникурсу devops для ml репозитория проекта HobbyTaste

Выполнены задания 1), 2), 4)

Для использования DevBox необходимо выполнить следующие шаги:
1. Установить [VirtualBox](https://www.virtualbox.org/wiki/Downloads).
2. Установить vagrant
3. Образ ОС для `vagrant`:
```shell script
vagrant box add ubuntu/bionic64
```
4. Запустить виртуальную машину:
```shell script
vagrant up
```
5. Установить необходимые зависимости с помощью salt:
```shell script
vagrant provision
```
6. Войти в консольный интерфейс виртуальной машины:
```shell script
vagrant ssh
```

Папка локального репозитория синхронизирована с папкой `~/vagrant/`.
Проброшены порты 8888, 8889, 8890 на хосте `0.0.0.0`
Для запуска `jupyter notebook` необходимо выполнтить в нужной папке на виртуальной машине
```shell script
jupyter notebook --ip=0.0.0.0
```

Для остановки виртуальной машины необходимо выполнить
```shell script
vagrant halt
```