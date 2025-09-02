select 
    DISTINCT customer_id,
    customer_age,
    customer_gender,
    customer_income,
    customer_loyalty_level 
    from {{ ref("Consolidated_Table") }}

    
    