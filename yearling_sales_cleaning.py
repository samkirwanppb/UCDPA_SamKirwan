#file will be used to merge and clean the yearling sales data locally.
import pandas as pd
import glob as glob



##first 22 csvs come from tattersalls           
tatts_sales = pd.DataFrame()
for i in glob.glob(f'C:/Users/kirwans/OneDrive - Paddy Power Betfair/ucd/yearling_sales/*')[0:22]:       
    df = pd.read_excel(i)     

    price_column = df.columns[-2]

    df_con = df[['Year Foaled', 'Sire', 'Dam', 'Sex', 'Consignor', price_column, 'Purchaser']]
    tatts_sales = tatts_sales.append(df_con)

tatts_sales = tatts_sales.drop_duplicates()


#rest of the csvs come from goffs
goffs_sales = pd.DataFrame()
for i in glob.glob(f'C:/Users/kirwans/OneDrive - Paddy Power Betfair/ucd/yearling_sales/*')[22:]:       
    if i[-3:] == 'xls':
        year = i[-8:-4]
    else:
        year = i[-9:-5]
        
    if 'premier' in i:        
        price_column = 'Price (£)'
    else:
        price_column = 'Price (€)'
        
    df = pd.read_excel(i)   
    df['Year'] = int(year)
    df['Year Foaled'] = df['Year'] - 1
    
    df_con = df[['Year Foaled', 'Sire', 'Dam', 'Sex', 'Consignor', 'Price', 'Purchaser']]
    df_con = df_con.rename(columns = {'Price': price_column})
                
    goffs_sales = goffs_sales.append(df_con)


all_sales = goffs_sales.append(tatts_sales)

all_sales.to_csv('C:/Users/kirwans/OneDrive - Paddy Power Betfair/ucd/yearling_sales/yearling_sales.csv', index = False)
