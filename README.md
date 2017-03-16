Stream Check

Программулина на Python 3.4 которая проверяет через GoodGame API статус стрима.
Опрос каналов производится каждую минуту.

Статус Dead значит что стрим мёртв.
Статус Live значит что стрим жив.
Ваш Кэп.

streamers.cfg содержит список каналов на гудгейме, так как мы видим их в ссылке на их канал
https://goodgame.ru/channel/Artistthe/#autoplay
https://goodgame.ru/channel/DiceMaster/#autoplay
записываются как:
Artistthe
DiceMaster

Так же если программа находит .wav файл в папке созвучной с названием канала 
(записи в streamers.cfg), проигрывает его вместо стандартного default.wav

Любителям поковыряться предлагаю посмотреть:
https://goodgame.ru/api/getchannelstatus?id=Miker

Исходный код прилагается