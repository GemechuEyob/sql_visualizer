query1 = '''SELECT
     COUNT(a.PostID)  AS AcceptedAnswers
    ,SUM(CASE WHEN a.PostScore = 0 THEN 0 ELSE 1 END) AS ScoredAnswers
    ,SUM(CASE WHEN a.PostScore = 0 THEN 1 ELSE 0 END) AS UnscoredAnswers
    ,UnscoredAnswers * 1000 / COUNT(a.PostID) / 10.0  AS PercentageUnscored
FROM dbo.Posts q
JOIN dbo.Posts a ON a.PostID = q.AcceptedAnswerId
WHERE 1 = 1
  AND a.PostCommunityOwnedDate is null
  AND a.PostOwnerUserId = 26837
  AND q.PostOwnerUserId != 26837
  AND a.PostTypeId = 2 -- answer
;'''

query2 = '''create table employees (employee_id integer, store_id integer, sales numeric(10,2), 
    sales_date date);
insert into stores (store_id, city) values 
    (1, 'Winnipeg'),
    (2, 'Toronto');
insert into employees (employee_id, store_id, sales, sales_date) values 
    (1001, 1, 9000.00, '2020-01-27'),
    (1002, 1, 2000.00, '2020-01-27'),
    (2001, 2, 6000.00, '2020-01-27'),
    (2002, 2, 4000.00, '2020-01-27'),
    (2002, 2, 5000.00, '2020-01-28')
    ;'''




