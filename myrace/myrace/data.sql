INSERT INTO races_race (
    name,
    date,
    distance,
    deniv,
    time,
    date_added,
    category_id,
    runner_id
    )

SELECT 
   name,
   date,
   distance,
   deniv,
   time,
   DATE('now'),
   category_id,
   runner_id

FROM 
   races_data;