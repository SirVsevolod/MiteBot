import sqlite3

class SQLighter:

    def __init__(self, database_file):
        """Подключаемся к БД и сохраняем курсор соединения"""
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()

    def get_subscriptions(self, status=True):
        """получаем всех активных подписчиков бота"""
        with self.connection:
            return self.cursor.execute("SELECT * FROM subs WHERE status = ?", (status,)).fetchall()

    def subscriber_exist(self, user_id):
        """проверяем есть ли юзер в базе"""
        with self.connection:
            result = self.cursor.execute("SELECT * FROM subs WHERE user_id = ?", (user_id,)).fetchall()
            return bool(len(result))

    def add_subscriber(self, user_id, status=True):
        """Добавляем нового подписчика"""
        with self.connection:
            return self.cursor.execute("INSERT INTO subs (user_id,status) VALUES (?,?)", (user_id, status))

    def update_subscription(self, user_id, status):
        """Обновляем статус подписки"""
        with self.connection:
            return self.cursor.execute("UPDATE subs SET status = ? WHERE user_id = ?", (status, user_id))

    def close(self):
        self.connection.close()