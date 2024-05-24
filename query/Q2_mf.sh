select max(count) from (select part.P_PARTKEY,count(*) as count from part group by part.P_PARTKEY) as t;
select max(count) from (select partsupp.PS_SUPPKEY,count(*) as count from partsupp group by partsupp.PS_SUPPKEY) as t;
select max(count) from (select partsupp.PS_PARTKEY,count(*) as count from partsupp group by partsupp.PS_PARTKEY) as t;
select max(count) from (select partsupp.PS_SUPPKEY, partsupp.PS_PARTKEY, count(*) as count from partsupp group by partsupp.PS_SUPPKEY, partsupp.PS_PARTKEY) as t;
select max(count) from (select supplier.S_SUPPKEY,count(*) as count from supplier group by supplier.S_SUPPKEY) as t;
select max(count) from (select lineitem.L_SUPPKEY, lineitem.L_PARTKEY, count(*) as count from lineitem group by lineitem.L_SUPPKEY, lineitem.L_PARTKEY) as t;
select max(count) from (select lineitem.L_ORDERKEY,count(*) as count from lineitem group by lineitem.L_ORDERKEY) as t;
select max(count) from (select orders.O_ORDERKEY,count(*) as count from orders group by orders.O_ORDERKEY) as t;
