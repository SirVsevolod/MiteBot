токкен взять из ботфазера и вставить в файл "config.py"
------------------------------------------------------
Рекомендовано для удобства пользования
также у ботфазера надо поставить боту аватарку
написать ботфазеру
/setcommands
выбрать данного бота
subscribe - Подписаться на рассылку
unsubscribe - Отписаться от рассылки
help - Помощь
-------------------------------------------------------
ОБЯЗАТЕЛЬНО
зайти в 'text.py'
прописать ссылки
на бонус в url_bonus
на акции url_promotions
заполнить srart_text ЭТО ТО СООБЩЕНИЕ КОТОРОЕ БУДЕТ ПРИХОДИТЬ ПРИ /start
я бы мог сделать чтобы он еще и какую то фотку отправлял но фотку мне не скинули
это кароч чтобы в каком то тексте была ссылка
чтобы изменить текст измените в >тут<
я решил что так будет красивее чем кнопки непонятные
'<a href=\'' + url_promotions + '\'>Акции</a>\n' \
'<a href=\'' + url_bonus + '\'>Забрать бонус</a>\n\n' \

help_text заполнить каким нибудь ну я не знаю описывающим бота словами
и прописать туда команды

/subscribe - Подписаться на рассылку
/unsubscribe - Отписаться от рассылки

ну чтобы пользователь мог понять что он может делать
-------------------------------------------------------
Для рассылки фотографии с подписью прикрепить к сообщению фотографию
подпись начать с "Special"
ПРИМЕР:
прикрепить фотографию
(Подпись) Special это фотография
-------------------------------------------------------
Для отправки сообщений с HTML
"/specialHTTML текст***ссылка на картинку"
ПРИМЕР
/specialHTTML текст <a href="ССЫЛКА">текст к которому прикреплена ссылка</a> и еще текст***ССЫЛКА НА КАРТИНКУ

/testHTML - тоже самое что и написано выше НО отправляет только вам для просмотра
--------------------------------------------------------
SQL
я использовал sqlite3
базу назвать 'mitedb.db'

CREATE TABLE subs (
    id      INTEGER       PRIMARY KEY AUTOINCREMENT,
    user_id VARCHAR (255) NOT NULL,
    status  BOOLEAN       NOT NULL
                          DEFAULT (TRUE)
);

желаю удачи работы с этим прекрасным ботом

