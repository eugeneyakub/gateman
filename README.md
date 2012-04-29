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

Понадобится доустановить пакеты, которых будет не хавать
<pre>
sudo apt-get install texlive
sudo apt-get install texlive-lang-cyrillic
sudo apt-get install texlive-latex-extra
sudo apt-get install python-pypdf
</pre>

команда для компиляции:
<pre>
  /sudo/bin/pdflatex some_file.tex
</pre> 
Для создания макета использовался Kile из репозитория.  Он поставит часть пакетов латекса автоматически.

Пример макета чека (latex_test.tex)
<pre>
\documentclass[12pt ]{extarticle}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage[english,russian]{babel}
\usepackage[width=7cm]{geometry}
\usepackage{dashrule}
\usepackage{ulem}
\usepackage[active,tightpage]{preview}
\renewcommand{\PreviewBorder}{0.5cm}
\newcommand{\Newpage}{\end{preview}\begin{preview}}
\renewcommand{\arraystretch}{1.5}
\hyphenpenalty=10000 
\usepackage{sans}
\renewcommand{\bfdefault}{sbc}
\begin{document}
\begin{preview}
\begin{flushleft}
  \textbf{{\huge Взаботе} \\ 
    \vspace{0.5cm}
    {\large Список покупок}} \\
  \vspace{0.5cm}
  \hdashrule{6.5cm}{1pt}{}\\
  \vspace{0.5cm}
  \begin{trivlist} 
  \item
    \textbf{{\large Кактус} \\
      супермаркет}\\
    Свердловсикй проспект $-$, 71 /\\
    Карла Либхнета, 24\\
    \vspace{0.2cm}
    \hdashrule{6.5cm}{1pt}{1pt}\\
    \vspace{0.5cm}
    \begin{tabular}{p{3cm}p{1.2cm}r}
       Мука пшеничная. Первая мыльница  & 2 кг & 410 \sout{Р} \\
       Гречка  & 1 кг & 105 \sout{Р} \\
      Хлеб ржаной  & 1 б & 15.5 \sout{Р} \\
       Итого  &   & 651 \sout{Р} \\
    \end{tabular}\\
    \vspace{0.22cm}
    \hdashrule{6.5cm}{1pt}{1pt}\\
    \vspace{0.5cm}
    \textbf{Cпособы оплаты} \\
    Наличными, картой \\
    \vspace{0.5cm}
    \textbf{Часы работы} \\
    \begin{tabular}{p{3.2cm}p{3.2cm}}
       \textbf{Пн$-$Пт}  & \textbf{Сб$-$Вс} \\
       9:00$-$19:00 & 9:00$-$16:00 \\
    \end{tabular}\\
    \vspace{0.4cm}
    \hdashrule{6.5cm}{1pt}{}\\
    \vspace{0.5cm}
  \item
    \textbf{{\large Молния} \\
      супермаркет}\\
    Свердловсикй проспект, 71 /\\
    Карла Либхнета, 24\\
    \vspace{0.2cm}
    \hdashrule{6.5cm}{1pt}{1pt}\\
    \vspace{0.5cm}
    \begin{tabular}{p{3cm}p{1.2cm}r}
       Мука пшеничная. Первая мыльница  & 2 кг & 410 \sout{Р} \\
       Гречка  & 1 кг & 105 \sout{Р} \\
      Хлеб ржаной  & 1 б & 15.5 \sout{Р} \\
       Итого  &   & 651 \sout{Р} \\
    \end{tabular}\\
    \vspace{0.22cm}
    \hdashrule{6.5cm}{1pt}{1pt}\\
    \vspace{0.5cm}
    \textbf{Cпособы оплаты} \\
    Наличными, картой \\
    \vspace{0.5cm}
    \textbf{Часы работы} \\
    \begin{tabular}{p{3.2cm}p{3.2cm}}
       \textbf{Пн$-$Пт}  & \textbf{Сб$-$Вс} \\
       9:00$-$19:00 & 9:00$-$16:00 \\
    \end{tabular}\\
    \vspace{0.4cm}
    \hdashrule{6.5cm}{1pt}{}\\
    \vspace{0.5cm}
  \end{trivlist}
\end{flushleft}
\end{preview}
\end{document}
</pre>