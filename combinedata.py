import pandas as pd
portions_data1={'order_id':[2,1,3],
                'item_name':['Burger','Pizza','Salad'],
                'quantity':[2,1,3]}

portions_data2={'order_id':[4,6,5],
                'item_name':['Soup','Burger','Wok'],
                'quantity':[1,3,4]}

df1=pd.DataFrame(portions_data1)
df2=pd.DataFrame(portions_data2)

combined = pd.concat([df1,df2])

orders_data={
    'order_id':[1,2,3],
    'customer_name':['Alice','Bob','Charlie'],
    'total_amount':[25.5,30.2,15.75]
}

portions_data={
    'order_id':[1,2,3],
    'item_name':['Burger','Pizza','Salad'],
    'quantity':[2,1,3]
    }

orders_df=pd.DataFrame(orders_data)
portions_df=pd.DataFrame(portions_data) 

merged_df=pd.merge(orders_df,portions_df,on='order_id')
