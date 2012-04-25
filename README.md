gateman
=======

Установка в системе
<pre>
sudo cp ./http_watchdog /etc/xinetd.d
sudo stop xinetd; start xinetd
</pre>

В /etc/xinet.d/http_watchdog прописать путь к скрипту http_watchdog.py и имя запускающего 
пользователя в соответсвии с конфигурацие системы.
 
Добавить в crontab запускающего пользователя периодическую задачу для проверки на 
превышение периода бездействия контролируемого приложения:

<pre>
crontab -u user -e
</pre>

Код пункта в crontab:
<pre>
*/1 * * * * ~/http_watchdog/check_timeout.py
</pre>

Для оповещения сторожевого таймера необходимо не реже заданного 
периода (1мин) отправлять любой HTTP запрос по адресу http://localhost:10000

Пример:
<pre>
<script type='text/javascript' charset='utf-8'>
function test(){
    $.get('http://localhost:10000', function(data){});
}
setInterval(test, 5000);
</script>
</pre>