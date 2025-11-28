import pandas as pd

csv_sheet=pd.read_csv("Virtual_Env\WebScrapping\sample.csv")
print(csv_sheet)
print(csv_sheet.head(1))
print(csv_sheet.tail(1))

high_rating=csv_sheet[csv_sheet["rating"]>=3.5]
print(high_rating)
print('-------after sorting---------')
sort_data=csv_sheet.sort_values('rating')
print(sort_data)
print('-----after sorting the price-------')
sort_price=csv_sheet.sort_values('price',ascending=False)
print(sort_price)

# Add a new column
csv_sheet["usd_price"]=(csv_sheet["price"] * 10)
print(csv_sheet)

new_shet=csv_sheet.to_csv('Virtual_Env\WebScrapping\\new_sheet.csv',index=False)

print(new_shet)

