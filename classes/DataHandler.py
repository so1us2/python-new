from MysqlConnector import MysqlConnector
from TextCleaner import TextCleaner
import io


class DataHandler:

    mysqlc= MysqlConnector()

    def get_data(self,table,columns):
        query=self.mysqlc.select_query(columns=columns,table=table)
        data=self.mysqlc.execute_query(query, returns=True)
        return data

    def clean_text(self,txt):
        txtc = TextCleaner(txt=txt)

        #Cleaning everything but dont lower text
        txtc.clear_binded_words()
        txtc.clear_links()
        txtc.find_special_chars()
        txtc.clear_dates()
        txtc.clear_special_char()
        txtc.clear_digits()
        txtc.clear_multispace()
        raw_text=txtc.get_text()
        return raw_text

    def process_json(self,json_value):
        pass

    def send_data(self,table,data,dictionary):
        self.mysqlc.insert_to_table(table=table,values=data,dictionary=dictionary)

    def write_to_file(self,data,f_name=None,loc=None,iterator=None):
        #TODO check for / at the end of loc
        if f_name is None:
            f_name = "txt-" + str(iterator) + ".txt"
            if loc is not None:
             f_name=loc+f_name



        with io.open(f_name, 'w', encoding="utf-8") as f:
            f.write(data)

def main():
    pass

if __name__ == '__main__':
    main()