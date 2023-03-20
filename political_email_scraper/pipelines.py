from itemadapter import ItemAdapter
import sqlite3
from sqlite3 import Error


class PoliticalEmailScraperPipeline:

    def __init__(self):
        self.con = sqlite3.connect('pol_email.db')

        self.cur = self.con.cursor()

        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS organizations(
            name TEXT,
            url TEXT
            )
            """)

    def process_item(self, item, spider):

        # self.cur.execute(" SELECT * FROM organzations where name = ?", (item['name'],))
        # result = self.cur.fetchone()
        #
        # if result:
        #     spider.logger.warn(f"Org already in database: {item['text']}")
        #
        # else:

        self.cur.execute("""
        INSERT INTO organizations (name, url) VALUES (?, ?)
        """, (
            item['name'],
            item['url']
                         ))
        self.con.commit()

        return item
