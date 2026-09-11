# ============================================================
# WEEK 6 FINAL DATA ANALYTICS PROJECT
# Synthetic E-Commerce Sales Dataset Generator
# ============================================================

import os
import numpy as np
import pandas as pd

# ------------------------------------------------------------
# 1. SETTINGS
# ------------------------------------------------------------

np.random.seed(42)

N_ORDERS = 2500

# Create required folders automatically
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DATA_DIR = os.path.join(BASE_DIR, "data", "raw")

os.makedirs(RAW_DATA_DIR, exist_ok=True)

# ------------------------------------------------------------
# 2. MASTER DATA
# ------------------------------------------------------------

products = [
    ("P001", "Wireless Headphones", "Electronics", 1800, 1050),
    ("P002", "Smart Watch", "Electronics", 3200, 1900),
    ("P003", "Bluetooth Speaker", "Electronics", 2200, 1300),
    ("P004", "Laptop Stand", "Electronics", 1500, 850),
    ("P005", "Mechanical Keyboard", "Electronics", 2800, 1650),
    ("P006", "Running Shoes", "Sports", 3500, 2100),
    ("P007", "Yoga Mat", "Sports", 1200, 650),
    ("P008", "Fitness Band", "Sports", 2100, 1200),
    ("P009", "Office Backpack", "Accessories", 1800, 1000),
    ("P010", "Travel Bag", "Accessories", 2600, 1450),
    ("P011", "Leather Wallet", "Accessories", 1100, 550),
    ("P012", "Sunglasses", "Accessories", 1600, 850),
    ("P013", "Coffee Maker", "Home & Kitchen", 4200, 2550),
    ("P014", "Air Fryer", "Home & Kitchen", 5800, 3500),
    ("P015", "Electric Kettle", "Home & Kitchen", 1800, 1050),
    ("P016", "Desk Lamp", "Home & Kitchen", 1400, 750),
    ("P017", "Notebook Set", "Stationery", 600, 260),
    ("P018", "Premium Pen Set", "Stationery", 900, 400),
    ("P019", "Planner", "Stationery", 750, 320),
    ("P020", "Study Table Organizer", "Stationery", 1000, 450),
]

product_df = pd.DataFrame(
    products,
    columns=[
        "Product_ID",
        "Product_Name",
        "Category",
        "Unit_Price_Base",
        "Unit_Cost"
    ]
)

# ------------------------------------------------------------
# 3. CUSTOMER MASTER DATA
# ------------------------------------------------------------

regions = {
    "West": ["Mumbai", "Pune", "Ahmedabad", "Surat"],
    "North": ["Delhi", "Jaipur", "Lucknow", "Chandigarh"],
    "South": ["Bengaluru", "Chennai", "Hyderabad", "Kochi"],
    "East": ["Kolkata", "Bhubaneswar", "Patna", "Ranchi"],
}

region_names = list(regions.keys())

customer_ids = [f"C{str(i).zfill(4)}" for i in range(1, 601)]

customer_segments = np.random.choice(
    ["Consumer", "Corporate", "Home Office"],
    size=len(customer_ids),
    p=[0.62, 0.23, 0.15]
)

customer_df = pd.DataFrame({
    "Customer_ID": customer_ids,
    "Customer_Segment": customer_segments
})

# ------------------------------------------------------------
# 4. GENERATE ORDERS
# ------------------------------------------------------------

order_dates = pd.date_range(
    start="2024-01-01",
    end="2025-12-31",
    freq="D"
)

orders = []

for i in range(1, N_ORDERS + 1):

    order_id = f"ORD{str(i).zfill(5)}"

    order_date = np.random.choice(order_dates)

    customer_id = np.random.choice(customer_ids)

    customer_segment = customer_df.loc[
        customer_df["Customer_ID"] == customer_id,
        "Customer_Segment"
    ].iloc[0]

    region = np.random.choice(
        region_names,
        p=[0.35, 0.25, 0.23, 0.17]
    )

    city = np.random.choice(regions[region])

    sales_channel = np.random.choice(
        ["Website", "Mobile App", "Marketplace"],
        p=[0.42, 0.35, 0.23]
    )

    product = product_df.sample(1).iloc[0]

    product_id = product["Product_ID"]
    product_name = product["Product_Name"]
    category = product["Category"]

    base_price = product["Unit_Price_Base"]
    unit_cost = product["Unit_Cost"]

    # Slight natural variation in selling price
    unit_price = round(
        base_price * np.random.uniform(0.92, 1.08),
        2
    )

    # Quantity distribution
    quantity = np.random.choice(
        [1, 2, 3, 4, 5, 6],
        p=[0.48, 0.25, 0.13, 0.07, 0.04, 0.03]
    )

    # Discount depends slightly on sales channel
    if sales_channel == "Marketplace":
        discount = np.random.choice(
            [0, 5, 10, 15, 20],
            p=[0.10, 0.20, 0.30, 0.25, 0.15]
        )
    elif sales_channel == "Mobile App":
        discount = np.random.choice(
            [0, 5, 10, 15],
            p=[0.20, 0.30, 0.35, 0.15]
        )
    else:
        discount = np.random.choice(
            [0, 5, 10, 15],
            p=[0.30, 0.35, 0.25, 0.10]
        )

    gross_sales = round(
        quantity * unit_price,
        2
    )

    discount_amount = round(
        gross_sales * discount / 100,
        2
    )

    net_sales_before_return = round(
        gross_sales - discount_amount,
        2
    )

    shipping_cost = round(
        np.random.uniform(40, 250),
        2
    )

    payment_fee = round(
        net_sales_before_return * np.random.uniform(0.015, 0.035),
        2
    )

    cost_of_goods = round(
        quantity * unit_cost,
        2
    )

    # Return probability
    return_probability = {
        "Electronics": 0.09,
        "Sports": 0.07,
        "Accessories": 0.06,
        "Home & Kitchen": 0.08,
        "Stationery": 0.04,
    }[category]

    return_flag = (
        np.random.random() < return_probability
    )

    if return_flag:
        return_quantity = np.random.choice(
            range(1, quantity + 1)
        )

        return_amount = round(
            (return_quantity * unit_price)
            * (1 - discount / 100),
            2
        )
    else:
        return_quantity = 0
        return_amount = 0.0

    net_revenue = round(
        net_sales_before_return - return_amount,
        2
    )

    profit = round(
        net_revenue
        - cost_of_goods
        - shipping_cost
        - payment_fee,
        2
    )

    profit_margin = round(
        (profit / net_revenue * 100)
        if net_revenue != 0
        else 0,
        2
    )

    payment_method = np.random.choice(
        ["UPI", "Credit Card", "Debit Card", "Net Banking", "COD"],
        p=[0.38, 0.24, 0.18, 0.10, 0.10]
    )

    order_status = (
        "Returned"
        if return_flag
        else np.random.choice(
            ["Delivered", "Delivered", "Delivered", "Cancelled"],
            p=[0.65, 0.20, 0.10, 0.05]
        )
    )

    orders.append([
        order_id,
        order_date,
        customer_id,
        customer_segment,
        region,
        city,
        sales_channel,
        product_id,
        product_name,
        category,
        quantity,
        unit_price,
        discount,
        gross_sales,
        discount_amount,
        shipping_cost,
        payment_fee,
        cost_of_goods,
        return_flag,
        return_quantity,
        return_amount,
        net_revenue,
        profit,
        profit_margin,
        payment_method,
        order_status
    ])

# ------------------------------------------------------------
# 5. CREATE DATAFRAME
# ------------------------------------------------------------

columns = [
    "Order_ID",
    "Order_Date",
    "Customer_ID",
    "Customer_Segment",
    "Region",
    "City",
    "Sales_Channel",
    "Product_ID",
    "Product_Name",
    "Category",
    "Quantity",
    "Unit_Price",
    "Discount_Percent",
    "Gross_Sales",
    "Discount_Amount",
    "Shipping_Cost",
    "Payment_Fee",
    "Cost_of_Goods",
    "Return_Flag",
    "Return_Quantity",
    "Return_Amount",
    "Net_Revenue",
    "Profit",
    "Profit_Margin",
    "Payment_Method",
    "Order_Status"
]

df = pd.DataFrame(orders, columns=columns)

# ------------------------------------------------------------
# 6. INTENTIONAL DATA QUALITY ISSUES
# ------------------------------------------------------------
# These are deliberately introduced so the cleaning stage
# can demonstrate missing-value handling and error correction.

# 6.1 Missing values
missing_indices = np.random.choice(
    df.index,
    size=25,
    replace=False
)

df.loc[missing_indices[:8], "Customer_Segment"] = np.nan
df.loc[missing_indices[8:15], "City"] = np.nan
df.loc[missing_indices[15:20], "Payment_Method"] = np.nan
df.loc[missing_indices[20:], "Discount_Percent"] = np.nan

# 6.2 Invalid quantity
invalid_quantity_indices = np.random.choice(
    df.index,
    size=5,
    replace=False
)

df.loc[invalid_quantity_indices, "Quantity"] = -2

# 6.3 Invalid unit price
invalid_price_indices = np.random.choice(
    df.index,
    size=5,
    replace=False
)

df.loc[invalid_price_indices, "Unit_Price"] = -500

# 6.4 Invalid discount
invalid_discount_indices = np.random.choice(
    df.index,
    size=5,
    replace=False
)

df.loc[invalid_discount_indices, "Discount_Percent"] = 150

# 6.5 Incorrect future dates
future_date_indices = np.random.choice(
    df.index,
    size=3,
    replace=False
)

df.loc[future_date_indices, "Order_Date"] = pd.Timestamp(
    "2027-06-15"
)

# 6.6 Duplicate records
duplicate_rows = df.sample(
    10,
    random_state=42
)

df = pd.concat(
    [df, duplicate_rows],
    ignore_index=True
)

# ------------------------------------------------------------
# 7. DATA TYPES
# ------------------------------------------------------------

df["Order_Date"] = pd.to_datetime(
    df["Order_Date"]
)

# ------------------------------------------------------------
# 8. SAVE RAW DATASET
# ------------------------------------------------------------

raw_file = os.path.join(
    RAW_DATA_DIR,
    "ecommerce_sales_raw.csv"
)

df.to_csv(
    raw_file,
    index=False
)

# ------------------------------------------------------------
# 9. CREATE DATA DICTIONARY
# ------------------------------------------------------------

data_dictionary = pd.DataFrame({
    "Column": columns,
    "Description": [
        "Unique order identifier",
        "Date on which the order was placed",
        "Unique customer identifier",
        "Customer classification",
        "Customer geographic region",
        "Customer city",
        "Sales channel used for purchase",
        "Unique product identifier",
        "Product name",
        "Product category",
        "Number of units purchased",
        "Selling price per unit",
        "Discount percentage applied",
        "Sales value before discount",
        "Discount amount",
        "Shipping cost for the order",
        "Payment processing fee",
        "Cost incurred for goods sold",
        "Whether the order was returned",
        "Number of returned units",
        "Value of returned products",
        "Revenue after discounts and returns",
        "Profit after major order-level costs",
        "Profit as a percentage of net revenue",
        "Customer payment method",
        "Final order status"
    ]
})

dictionary_file = os.path.join(
    RAW_DATA_DIR,
    "data_dictionary.csv"
)

data_dictionary.to_csv(
    dictionary_file,
    index=False
)

# ------------------------------------------------------------
# 10. DISPLAY SUMMARY
# ------------------------------------------------------------

print("=" * 60)
print("DATASET GENERATION COMPLETED")
print("=" * 60)

print(f"\nRows generated: {len(df):,}")
print(f"Columns generated: {len(df.columns)}")

print("\nDataset shape:")
print(df.shape)

print("\nDate range:")
print(df["Order_Date"].min(), "to", df["Order_Date"].max())

print("\nCategories:")
print(df["Category"].value_counts())

print("\nRegions:")
print(df["Region"].value_counts())

print("\nSales channels:")
print(df["Sales_Channel"].value_counts())

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nRaw dataset saved to:")
print(raw_file)

print("\nData dictionary saved to:")
print(dictionary_file)

print("\nFirst 5 records:")
print(df.head())

print("\n" + "=" * 60)
print("READY FOR DATA INSPECTION AND CLEANING")
print("=" * 60)