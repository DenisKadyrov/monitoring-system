Дополнение которое позволяет запускать плагины на удаленных хостах Unix/Linux.
[GitHub repository](https://github.com/NagiosEnterprises/nrpe)
## Принцип работы
![|700](https://exchange.nagios.org/components/com_mtree/img/listings/m/93.png)
**Дополнение NRPE состоит из двух частей**:
- плагин check_nrpe, который запускается хосте Nagios и используется для связи с процессом NRPE на удаленном хосте.
- Программа NRPE запускается на удаленном хосте в фоновом режиме и обрабатывает запросы на выполнение команд от плагина check_nrpe на хосте Nagios

**Когда Nagios необходимо мониторить какую-нибудь службу на удаленном хосте:**
- Nagios запускает плагин check_nrpe и сообщает ему какую службу нужно мониторить
- check_nrpe связывается c демоном NRPE на удаленном хосте через защищенное соединение
- Демон NRPE запускает соответствующие плагины для мониторинга на удаленном хосте
- Результаты проверки демон NRPE отправляет обратно в плагин check_nrpe
- Плагин check_nrpe предоставляет их процессу nagios

## Настройка