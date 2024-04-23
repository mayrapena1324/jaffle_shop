with payments as (
    select * from ANALYTICS_PROD.ANALYTICS.stg_payments 
)

select
    order_id,
    SUM(amount) as total_amount
from payments 

group by 1
having total_amount < 0