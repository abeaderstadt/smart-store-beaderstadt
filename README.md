# smart-store-beaderstadt
# Project 6 - BI Insights and Storytelling

## Overview

Project 6 focuses on using OLAP techniques like slicing, dicing, and drilldown to uncover specific analytic insights for a particular business objective.

```
## **How to Install and Run the Project**
---
### **Step 1. Create a New Repo in GitHub**
 - Open your browser and log in to your GitHub account.
 - Select 'Create New Repository' from the dropdown menu, and name your repo.
 - Select the Public option so others can view your repository, and add a README.md file.
 - Click the 'Create repository' button to finalize the process.
 - Clone your repo to local using your new URL pasted into the following example command.
  - git clone https://github.com/youraccount/yourrepo
 - Create your .gitignore and requirements.txt files.
 - Run the following command from your project route directory to create your virtual environment.
  - py -m venv .venv
 - Use the following commands to add files to version control.
IMPORTANT: Replace the commit message with a clear and descriptive note about what you added or changed.
  - git add .    # stages changes, adds files to source control
  - git commit -m "Add .gitignore and requirements.txt files"    # creates a labeled snapshot of staged changes.
  - git push -u origin main    # updates the remote repository
 - Open the newly cloned folder to begin working in it by selecting 'file' 'open folder' navigate to the new repo and select 'open'.
---
### **Step 2. Activate Your .venv**
 - Before making any changes to a project, ALWAYS pull the latest changes from the remote repository on GitHub using the following command.
  - git pull origin main
 - Run the following command to activate your .venv # HINT- You MUST activate your .venv before editing a project.
  - .venv\Scripts\activate
---
### **Step 3. Install Packages Into Your Local Project Virtual Environment**
 - Ensure your .venv is active, update key packages, and install dependencies from your requirements.txt using the following commands.
  - .venv\Scripts\activate
  - py -m pip install --upgrade pip setuptools wheel
  - py -m pip install -r requirements.txt
---
## **Repeatable Project Workflow**
 Follow these steps when starting a new work session on a professional Python project.
### **1. Pull the Latest Changes from GitHub:**
  - git pull origin main
### **2. Activate the Project Virtual Environment:**
  - .venv\Scripts\activate
### **3. Install Dependencies As Needed:**
  - py -m pip install -r requirements.txt
### **4. Run Scripts as needed:**
  - select python interpreter for your local venv
  - py myfile.py   
### **5. Run Jupyter Notebooks as needed:**
 - click the kernel selector in the top-right corner of the notebook editor and choose the interpreter associated with your .venv.
 - Click on a cell and press Shift+Enter to execute it and move to the next cell.
 - Alternatively, use Ctrl+Enter to execute the current cell without moving.
 - Use 'Run ALL' to execute notebooks fully before running git add-commit-push to GitHub.
 - Save your notebook periodically to avoid losing progress. Or make sure the File / Autosave option is on.
### **6. Save your work with git add-commit-push to GitHub:**
  - git add .    
  - git commit -m "Add your unique message here." 
  - git push -u origin main  
```

---

 # P1: Specifications

  Project 1 is a hands-on project, that follows professional practices for starting a business intelligence data analytics project. Our project will evolve over time, so we want a place to keep it safe - backed up and ready for sharing or presenting our work. For that, we'll use GitHub, a popular place for storing code.
  - Link to starter repo: https://github.com/denisecase/smart-sales-starter-files/

## Task 1: Plan Your Project
- Before you start coding, spend some time planning your project. 
- We will start with a common business insight: https://github.com/denisecase/smart-sales-analysis-goals/blob/main/example_bi_goals/1-CUSTOMER_TOTAL_REVENUE.md


## Task 2: Complete/Verify Initialization
- Follow the above step-by-step instructions to initialize a new Python project.
- Hint: you should have both a GitHub repo (which you created with a default README.md) and have cloned it down to your machine, added useful files, done a git add-commit-push to GitHub and created a project virtual environment for Python. 

## Task 3: Organize Your Project Folder
- Open the project in VS Code or use your computer's file management program to organize your project professionally. For now, just organize the project this way. Files will be mostly empty - we'll add contents later.

smart-store-yourname/   
│
├── data/                
│   ├── raw/                          
│
├── scripts/                            
│
├── utils/                     
│   └── logger.py              
│
├── .gitignore                 
├── README.md                  
└── requirements.txt     

- First, create the folders. Follow capitalization (all lower case), spelling, and spacing, EXACTLY. 
- In your project repository, create the data folder first as show above. In the data folder, create a folder named raw (if it doesn't exist yet). 

## Task 4: Add Sample Data
- Use the sample data files provided in this repository: https://github.com/denisecase/smart-sales-raw-dataLinks to an external site. to your data/raw folder.
- Either download these files and put them in your data/raw folder, or create new empty files and copy and paste the contents into each. 
- For best results, be sure the file names are exactly the same.
- When finished, in your data/raw folder, you should have with some raw sample data in each:

    - customers_data.csv
    - products_data.csv
    - sales_data.csv

## Task 5: Explore the Data
- Before using tools, examine the data manually. Open the CSV files and make a few observations:

---

  # P2 Specifications

  In Project 2 we continue to initialize a business intelligence data analytics project. Our goal is to get acquainted with these powerful tools and key files so we'll feel a bit more comfortable joining a Git-based team.

## Task 6: Add Utility & Script Files
- In VS Code, use File / New Folder to create a new folder named utils to hold your utility scripts.
- create a file named logger.py (exactly). Copy and paste the content from the starter repo linked above. 
- In VS Code, use File / New Folder to create a new folder named scripts to hold your scripts.
- create a file named data_prep.py (exactly).  Copy and paste the content from the starter repo linked above. 

---

   # P3 Specifications

   In Project 3, we'll focus on using raw data and cleaning methods. The data we'll be working with has already been partially cleaned in previous projects. The aim is to get the data into a clean, consistent format, laying the groundwork for the more complex analytics tasks ahead. This ensures that the insights we generate are built on accurate and trustworthy data.
 ## Task 7: Practice Reusable Cleaning with a DataScrubber Class
 - Create the following file in your project: scripts/data_scrubber.py 
 - Copy and paste the content from the module 3 repo (https://github.com/denisecase/smart-sales-docs/)
 - Complete the remaining TODO items in this script.
  
 ## Task 8: Test the DataScrubber Class
 - Create the following folder and file for this in your project:tests/test_data_scrubber.py
 - Copy and paste the content from the module 3 repo linked above.
 - Use the terminal to run the test_data_scrubber.py script.
 - py tests\test_data_scrubber.py
  
## Task 9: Use Your Data Scrubber
- Now that we've verified these methods, we can run the data_prep.py script that cleans and prepares the data.
- Use the terminal to run the data_prep.py script.
- py scripts\data_prep.py

---

   # P4 Specifications

   In Project 4, we design and implement a data warehouse  structure that optimizes data retrieval and scalability. 
   We will build the schema, load the cleaned data, and validate the structure. This prepares us for advanced business intelligence tasks and data-driven decision-making.
## Task 10:  Plan Your Data Warehouse
- Design Your Data Warehouse Schema
- Determine the most suitable schema for your data warehouse (Hint: We use Star Warehouse in this example)
- Sketch out the tables

## Task 11: Define, Create, and Populate Your DW Schema
- Create a 'scripts' subfolder named 'dw_scripts'
- Create a file inside named etl_to_dw.py (it can do all steps together).
- Create a file inside named create_tables.sql (for debugging I chose to build and test my SQL first and keep them separate, but either way works.)
- Contents of both files was copy and pasted from course website.
- Adjused this to reflect my tables, columns, and their appropriate data types. 

## Task 12:  Validate the Data Warehouse
- Use the terminal to run the etl_to_dw.py file.
- py scripts/dw_scripts/etl_to_dw.py
- Ensure the schema is correctly implemented and that the structure meets your design expectations. 

---

   # P5 Specifications

   In Project 5, we will use Power BI Desktop to apply core BI techniques (slicing, dicing, and drilldown) and generate interactive visualizations to explore business performance. This project reinforces key data analysis and reporting skills used across industries.

   ### SQL Queries & Reports

- **Top Customers Query**: Used a JOIN between `sales` and `customers`, grouped by customer name, and summed total spent.
- **Sales by Product & Region**: Created a Matrix visual to dice data by category (Rows) and supplier (Columns), with the values representing the count of unit_price.
- **Sales Trends Drilldown**: Used hierarchy (Year > Quarter > Month) to explore sales over time using a column chart.

### Dashboard Design Choices

- Used **slicer** to filter by sale date, providing flexible time-based analysis.
- Added **bar chart** to display top customers by total spending.
- Created **matrix visualization** for clear cross-section of product category and region.
- Added **column chart** to explore sales over time using a hierarchy (Year > Quarter > Month).
- Used a **line chart** with drilldown to explore sales trends across time.
- Used **slicer** to focus on specific product categories across all visuals
- Added color-coded visuals to improve interactivity and clarity.

### Power BI Model View
![Model View](screenshots/model_view.png)

### Query Results
![Query Results](screenshots/query_results.png)

### Final Dashboard
![Final Dashboard](screenshots/dashboard.png)

---

   # P6 Specifications
   
   In Project 6, we explored OLAP (Online Analytical Processing) techniques to better understand customer purchasing behavior. This notebook based project focused on querying a data warehouse and analyzing spending patterns by customer and product.

## Section 1: The Business Goal
- CUSTOMER_TOTAL_PURCHASES_BY_PRODUCT
- How much does each customer spend on individual products?
- This question helps identify high value customers and the specific products they purchase. 
- These insights are valuable for personalized promotions, customer retention, and inventory planning.

## Section 2: Data Source
- Prepared data from my SQLite3 data warehouse, which was designed and loaded in Project 4 was used.
The primary table used was:
sales_df : includes sale_id, customer_id, product_id, store_id, campaign, sale_amount, sale_date, discount_percentage, and state.
- focused on:
  - customer_id
  - product_id
  - sale_amount (used as the total dollar amount for each purchase)
- joined with:
  - customers_df: to retrieve customer names
  - products_df: to retrieve product names

## Section 3: Tools
- Jupyter Notebook: Used for querying, analyzing, and visualizing data in Python. Chosen for its flexibility and because I'm comfortable working in it.
- Pandas: For grouping, joining, and aggregating data.
- Matplotlib & Seaborn: For visualizing purchase patterns.

## Section 4: Workflow & Logic
- Connect to the Data Warehouse using sqlite3.
- Load and join tables: customers, products, and sales data.
- Group by customer and product.
- Sum the sale_amount to calculate total purchases.
- Sort the results to highlight high-spending customers.
- Visualize the data with tables and bar charts.
- Key dimensions:
  - Customer
  - Product
- Key aggregation:
  - SUM of sale_amount

## Section 5: Results
- Customers 1001 and 1010 spent the most across multiple products.
- The 'laptop' product stands out as the highest total spend among customers.

##  Visualizations

### 1. Total Spend by Customers on Each Product  
![Total Spend by Customer on Each Product](screenshots/bar_total_spend_by_customer_and_product.png)  
_This bar chart displays the total purchase amount of all customers, broken down by product._

---

### 2. Heatmap of Customer Spend by Product  
![Heatmap of Customer Spend by Product](screenshots/heatmap_customer_product_spend.png)  
_This heatmap provides a visual overview of how much each customer has spent across all product types._

---

### 3. Daily Sales Trend for Products  
![Daily Sales Trend for a Specific Product](screenshots/line_daily_sales_by_product.png)  
_This line graph shows daily sales trends for all products within a specific month._

---

### 4. Customer Spend on Laptops  
![Customer Spend on Laptops](screenshots/bar_customer_spend_on_laptops.png)  
_This bar chart shows the total spend of customer specifically for laptop purchases._

---

### 5. Grouped Laptop Purchase Analysis  
![Grouped Laptop Purchase Analysis](screenshots/grouped_laptop_purchase_analysis.png)  
_This screenshot shows the grouped and aggregated data used to analyze laptop purchases by customer._

---

### 6. Pivot Table Script (OLAP Logic)  
![Pivot Table Script](screenshots/pivot_table_script.png)  
_This shows the pivot table code that powers the OLAP query to analyze total spend per customer and product._


## Section 6: Suggested Business Action
- Target high-spending customers with loyalty rewards or personalized offers.
- Bundle frequently purchased products or recommend similar items to increase average order size.
- Use purchase trends to improve inventory and campaign planning.

## Section 7: Challenges
- I initially considered using Power BI, but opted for Jupyter due to familiarity and control over data manipulation.
- Took extra care to ensure join logic and aggregations were correct.
- Making the visualS easy to read required a few formatting tweaks with pivot tables and bar charts.

---

   # P7 Specifications
   
   In Project 7, we explored OLAP (Online Analytical Processing) techniques to identify the most profitable day of the week for sales.

# Project README

## Section 1. The Business Goal
The primary goal of this analysis is to determine **which product categories drive the most weekly revenue** and **identify key trends in sales patterns**. By analyzing weekly sales data, the project aims to provide actionable insights into sales performance by category, which can help in optimizing inventory management and promotional strategies.

## Section 2. Data Source
- Prepared data from my SQLite3 data warehouse, which was designed and loaded in Project 4 was used.
The primary table used was:
sales_df : includes sale_id, customer_id, product_id, store_id, campaign, sale_amount, sale_date, discount_percentage, and state.
- focused on:
  - customer_id
  - product_id
  - sale_amount (used as the total dollar amount for each purchase)
  - sale_date
- joined with:
  - customers_df: to retrieve customer information
  - products_df: to retrieve product information
- The data is covering a period from January 2024 to October 2024. The specific fields used include:
    - `year_week`: Date range for the week
    - `category`: Product category (Electronics, Clothing, Sports)
    - `sale_amount`: Total sales amount for each category in a given week

## Section 3. Tools Used
- Jupyter Notebook: Used for querying, analyzing, and visualizing data in Python. Chosen for its flexibility and because I'm comfortable working in it.
- Pandas: For grouping, joining, and aggregating data.
- Matplotlib & Seaborn: For visualizing purchase patterns.

## Section 4. Workflow & Logic

1. **Data Import & Preprocessing**:
- Connect to the Data Warehouse using sqlite3.
- Load and join tables: customers, products, and sales data.
- `category` and `sale_amount` were extracted for analysis.

2. **Analysis**:
   - The data was aggregated by product category and week to calculate the total sales per category.
   - The analysis focused on identifying patterns and trends, such as which categories had the highest sales during specific weeks.
   
3. **Visualization**:
   - A bar plot was created to visually represent total sales by category across different weeks.
   - Additional visualizations were made to highlight trends over time, focusing on weekly sales data.

4. **Interpretation**:
   - Weekly sales trends were analyzed to determine which categories consistently performed well, and where opportunities for improvement or targeted actions lie.

## Section 5. Results (Narrative + Visualizations)
### Narrative:
- Thursday stands out as the top performing sales day, especially in the Electronics category with laptops driving the majority of revenue.High value customers like 1001 and 1010 contribute significantly to Thursday’s sales, making them strong candidates for personalized promotions or loyalty efforts.The weekly sales trends clearly indicate that Electronics is the dominant category, consistently driving the most revenue. This aligns with the earlier analysis of product performance on Thursdays.

### Visualizations:
![Total Sales by Day of Week](screenshots/total_sales_by_day_of_week.png)
*Figure: Total sales by day of week.*

![Sales by Day of Week and Product Category](screenshots/day_of_week_sales_by_category.png)
*Figure: Sales by Day of Week and Category.*

![Customer Contributions by Day of Week and Category](screenshots/customer_sales_category_day.png)
*Figure: Total sales per customer by day and product category.*

![Top Thursday Products](screenshots/top_products_thursday.png)
*Figure: Top Products Sold on Thursdays.*

![Top Thursday Categories](screenshots/top_categories_thursday.png)
*Figure: Top Selling Categories on Thursdays.*

![Top Thursday Customers](screenshots/top_customers_thursday.png)
*Figure: Top Purchasing Customers on Thursdays.*

![Weekly Sales by Category](screenshots/weekly_sales_by_category.png)
*Figure: Total weekly sales per product category.*

## Section 6. Suggested Business Action
- Top Sales Day: Thursday consistently delivers the highest sales volume, especially in Electronics. Consider making this a focus for future product drops or campaigns.

- Customer Behavior: Customers 1001 and 1010 show consistent high spending. Target these repeat buyers with exclusive deals, loyalty perks, or early access to new releases.

- Product Performance: Laptops are the top product by far, followed by clothing items like jackets and hoodies. These should be considered in future bundles or promotional offers.

Actionable Next Steps:

  - Launch Thursday focused promotions that align with high customer traffic.

  - Personalize offers to high value customers using past purchase data.

  - Monitor seasonal dips and spikes to time sales more effectively and optimize stock.

  - Increase exclusive deals on electronics to boost sales since Electronics consistently performs well, especially during high revenue weeks.

## Section 7. Challenges
- **Time Constraints**: Due to time limitations, the analysis focused on a broad overview rather than in depth category level breakdowns, which could have provided more insights.

## Section 8. Ethical Considerations
- The business can use the insights from this analysis to target high value customers and optimize product offerings. However, these actions should be taken with consideration of fairness and transparency. For example, personalized marketing campaigns should avoid being overly intrusive, and discounts should not disadvantage certain customer groups. Additionally, the business should be mindful of the ethical implications of automated decisions such as targeting, price optimization, and promotional offers.

