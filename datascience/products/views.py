from datetime import date
from django.shortcuts import render
from .models import Product, Purchase
import pandas as pd
# Create your views here.

def Chartselectview(request):
    error_message = None
    merge_df = None
    product_df = pd.DataFrame(Product.objects.all().values())
    purchase_df = pd.DataFrame(Purchase.objects.all().values())
    print('purchase position:::',purchase_df.shape)
    product_df['id'] = product_df['id']

    if purchase_df.shape[0] > 0:
        merge_df = pd.merge(purchase_df, product_df, on='id').drop(['created_date_y'],axis=1).rename({'created_date_x':'created_at'}, axis=1)
        print('date:::',merge_df['created_at'][0])
        print('type date:::', type(merge_df['created_at'][0]))
        if request.method ==  "POST":
            chart_type = request.POST.get('sales')
            date_from = request.POST['date_from']
            date_to = request.POST['date_to']

            merge_df['created_at'] = merge_df['created_at'].apply(lambda x:x.strftime('%y-%m-%d'))
            print('merge df date:::', merge_df['created_at'])
            merge_df2 = merge_df.groupby('created_at', as_index=False)['total_price'].agg(sum)
            print(merge_df2)

            if chart_type != "":
                if date_from != "" and date_to != "":
                    df = merge_df[merge_df(['created_at']>date_from) & (merge_df['created_at']>date_to)]
                    merge_df2 = merge_df.groupby('created_at', as_index=False)['total_price'].agg(sum)
                #function to get graph
                
            else:
                error_message = "Please select a chart type to continue!"

    else:
        error_message = 'No data available'
       
    context = {
        'error_message':error_message,
        'title': 'Product',
        'product': product_df.to_html(),
        'purchase':purchase_df.to_html(),
        'df': merge_df.to_html(),
    }
    return render(request, 'products/main.html', context)
