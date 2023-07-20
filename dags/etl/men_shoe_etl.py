import etl.viper.web_scraping as vws
import etl.viper.shoe_loader as loader

def run():
    category = 'men'
    shoes_info, stocks = vws.shoe_extraction_with_two_columns()
    loader.store_in_postgres(
            shoes_info, 
            stocks,
            table_name='men_shoes'
        )
    # loader.convert_into_csv('/home/gavincanete/Downloads/', category, shoes_info, stocks)

# LOGS
run()