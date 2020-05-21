# ml-team-repo

## Задание по миникурсу devops для ml репозитория проекта HobbyTaste

Выполнены задания 1), 2), 4)

### 1) Requrements:
Все необходимые зависимости описаны в файлe [requirements.txt](./vm/salt/requirements.txt)

После установки новых пакетов необходимо выполнить:
```shell script
pip3 freeze > /path/to/requirements.txt
```

### 2) DevBox (vagrant + salt)
Для использования DevBox необходимо выполнить следующие шаги:
1. Установить [VirtualBox](https://www.virtualbox.org/wiki/Downloads).
2. Установить [vagrant](https://www.vagrantup.com)
3. Образ ОС для `vagrant`:
```shell script
vagrant box add ubuntu/bionic64
```
4. Запустить виртуальную машину:
```shell script
vagrant up
```
5. Установить необходимые зависимости:
```shell script
vagrant provision
```
6. Войти в консольный интерфейс виртуальной машины:
```shell script
vagrant ssh
```

Папка локального репозитория синхронизирована с папкой `~/vagrant/`.
Проброшены порты 8888->18888, 8889->18889, 8890->18889 на хосте `0.0.0.0`
Для запуска `jupyter notebook` необходимо выполнтить в нужной папке на виртуальной машине
```shell script
jupyter notebook --ip=0.0.0.0
```

Для остановки виртуальной машины необходимо выполнить
```shell script
vagrant halt
```

### 4) GitLab CI
Запуск пайплайна с тестированием основных компонент проекта с помощью pytest.