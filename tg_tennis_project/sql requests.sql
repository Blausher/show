CREATE TABLE schedule ( 
training_id INT not null AUTO_INCREMENT primary key, 
weekday1 VARCHAR(20),
date1 DATE,
time1 TIME NOT NULL,
lasts_hours INT,
location VARCHAR(250) NOT NULL,
column group_lvl INT
);

INSERT INTO schedule (weekday1, date1, time1, lasts_hours, location, group_lvl)
VALUES ('Вторник','2023-09-25', '21:00:00', 1, 'Зорге', 1);

INSERT INTO schedule (weekday1, date1, time1, lasts_hours, location, group_lvl)
VALUES ('Среда','2023-09-26', '19:00:00', 1, 'Спартак Сокольники', 2);


CREATE TABLE clients ( 
client_id INT not null AUTO_INCREMENT primary key,
name VARCHAR(250),
tgnick VARCHAR(250),
phone VARCHAR(250),
group_lvl INT,
payment INT,
payment_date DATE,
trainings_left INT
);

INSERT INTO clients (name, tgnick, phone, group_lvl, payment, payment_date, trainings_left)
VALUES ('Иван', '@ivan', '+79035521799', 1, 20000, '2023-09-10', 4),
('Петр', '@petr', '+79225521799', 2, 12000, '2023-09-05', 2)



CREATE TABLE clid_trid (
match_id INT not null AUTO_INCREMENT primary key
clid INT,
trid INT,
FOREIGN KEY (clid) REFERENCES clients(client_id),
FOREIGN KEY (trid) REFERENCES schedule(training_id)
);


INSERT into clid_trid (clid, trid)
values (1, 1),
(2, 1)



-- Запрос - кто к нам придет во вторник на id тренировки 1
SELECT *
FROM 
(SELECT ct.clid  
FROM schedule s 
LEFT JOIN clid_trid as ct 
ON s.training_id = ct.trid
WHERE s.training_id = 1) df1
left join clients c 
ON c.client_id = df1.clid


INSERT INTO schedule (weekday1, date1, time1, lasts_hours, location, group_lvl)
VALUES ('Четверг','2023-09-27', '18:00:00', 1, 'Спартак Сокольники', 2),
('Четверг','2023-09-27', '19:00:00', 1, 'Спартак Сокольники', 3),
('Пятница','2023-09-28', '8:00:00', 1, 'НТЦ', 1),
('Суббота','2023-08-26', '18:00:00', 1, 'Спартак Сокольники', 2),
('Четверг','2023-09-16', '19:00:00', 1, 'Зорге', 3)


CREATE TABLE T
(
S DATETIME 
)

INSERT INTO T 
VALUES('2013-08-30 19:05:00')

SELECT *
FROM T

-- Запрос - кто к нам придет во вторник на id тренировки 1
SELECT *
FROM 
(SELECT ct.clid  
FROM schedule s 
LEFT JOIN clid_trid as ct 
ON s.training_id = ct.trid
WHERE s.training_id = 1) df1
left join clients c 
ON c.client_id = df1.clid

SELECT * from schedule s 
where date1 > '2023-09-17'




create view df1 as
SELECT ct.trid, ct.clid
FROM schedule s 
LEFT JOIN clid_trid as ct 
ON s.training_id = ct.trid
left join clients c 
ON c.client_id = ct.clid
WHERE s.training_id = 1 



select *
from schedule s 
left join clid_trid ct 
on s.training_id = ct.trid 
left join clients c 
on c.client_id = ct.clid 

