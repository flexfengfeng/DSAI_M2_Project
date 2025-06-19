import pandas as pd

# Remove line breaks from review_comment_message field
df_cleaned = pd.read_csv("/Users/fengfeng/Downloads/olist_dataset/olist_order_reviews_dataset.csv", encoding='utf-8')

df_cleaned["review_comment_message"] = df_cleaned["review_comment_message"].astype(str).str.replace(r'[\n\r]+', ' ', regex=True)

output_no_newlines = "/Users/fengfeng/Downloads/olist_dataset/olist_order_reviews_dataset_no_linebreaks2.csv"
df_cleaned.to_csv(output_no_newlines, index=False)

output_no_newlines