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

Установка в системе для Латекса
<pre>
sudo cp ./http_latex /etc/xinetd.d
sudo stop xinetd; start xinetd
</pre>

В /etc/xinet.d/http_latex прописать путь к скрипту http_latex.py и имя запускающего 
пользователя в соответсвии с конфигурацие системы.

Понадобится доустановить пакеты, котррые будет не хватать
<pre>
sudo apt-cache search texlive
точно нужно: 
texlive                                         install
texlive-base                                    install
texlive-binaries                                install
texlive-common                                  install
texlive-doc-base                                install
texlive-extra-utils                             install
texlive-font-utils                              install
texlive-fonts-extra                             install
texlive-fonts-extra-doc                         install
texlive-fonts-recommended                       install
texlive-fonts-recommended-doc                   install
texlive-generic-extra                           install
texlive-generic-recommended                     install
texlive-lang-cyrillic                           install
texlive-latex-base                              install
texlive-latex-base-doc                          install
texlive-latex-extra                             install
texlive-latex-extra-doc                         install
texlive-latex-recommended                       install
texlive-latex-recommended-doc                   install
texlive-luatex                                  install
texlive-pictures                                install
texlive-pictures-doc                            install
texlive-pstricks                                install
texlive-pstricks-doc                            install

Установить обработчик pdf:
<pre>
  sudo pip install pypdf
</pre>

bash команда для компиляции:
<pre>
  /sudo/bin/pdflatex some_file.tex
</pre> 

Для создания макета использовался Kile из репозитория.  Он поставит часть пакетов латекса автоматически