import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "customer online purchase analysis.xlsx"
xls = pd.ExcelFile(file_path)
print("Available sheets:", xls.sheet_names)
df = xls.parse(xls.sheet_names[0])
print("\nFirst 5 rows of data:")
print(df.head())
print("\nDataset Info:")
print(df.info())
print("\nSummary Statistics:")
print(df.describe(include='all'))

df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

if 'customer_id' in df.columns and 'order_value' in df.columns:
    total_sales = df['order_value'].sum()
    avg_order_value = df['order_value'].mean()
    num_customers = df['customer_id'].nunique()
    print(f"\n📈 Total Sales: ₹{total_sales:,.2f}")
    print(f"📊 Average Order Value: ₹{avg_order_value:,.2f}")
    print(f"👤 Unique Customers: {num_customers}")

if 'order_date' in df.columns and 'order_value' in df.columns:
    df['order_date'] = pd.to_datetime(df['order_date'])
    df.groupby(df['order_date'].dt.to_period("M"))['order_value'].sum().plot(kind='bar', figsize=(10,5))
    plt.title("Monthly Order Value")
    plt.ylabel("Total Order Value")
    plt.tight_layout()
    plt.show()

df.to_csv("cleaned_customer_data.csv", index=False)
