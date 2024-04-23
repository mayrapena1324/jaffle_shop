select 
    order_id,
    sum(amount) as total_amount
from ANALYTICS_PROD.ANALYTICS.stg_payments

group by 1
having not(total_amount >= 0)