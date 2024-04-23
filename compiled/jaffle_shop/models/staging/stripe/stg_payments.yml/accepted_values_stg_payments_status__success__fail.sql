
    
    

with all_values as (

    select
        status as value_field,
        count(*) as n_records

    from ANALYTICS_PROD.ANALYTICS.stg_payments
    group by status

)

select *
from all_values
where value_field not in (
    'success','fail'
)


