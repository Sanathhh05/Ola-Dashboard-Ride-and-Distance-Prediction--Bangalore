SELECT * FROM ola.bookings_ola;

#q1 : retrieve all successful bookings

CREATE VIEW Successful_booking as
SELECT * FROM ola.bookings_ola
WHERE Booking_Status='success';

select * from Successful_booking;


#q2 : select avg ride dist of each vehicle type

create view avg_dist_per_vehicle as
select distinct vehicle_type , avg(Ride_Distance)
from ola.bookings_ola
group by Vehicle_Type;

select * from avg_dist_per_vehicle;



#find all areas of bangalore

select distinct Pickup_Location
from ola.bookings_ola;



#q3: totoal no of cancel rides by customer and driver 

create view cancelled as
select count(Canceled_Rides_by_Customer),count(Canceled_Rides_by_Driver) 
from ola.bookings_ola;

select * from cancelled;



#q4: list top 5 customer booked highest no of rides

create view highest_rides_booked as
select Customer_ID, count(Booking_ID) 
from ola.bookings_ola
group by Customer_ID
order by count(Booking_ID) desc limit 5;

select * from highest_rides_booked;


#q5:  Get the number of rides cancelled by drivers due to personal and car-related issues

create view car_prob as
select count(*) from ola.bookings_ola
where Canceled_Rides_by_Driver='personal & car related issue';

select * from car_prob;


#q6: Find the maximum and minimum driver ratings for Prime Sedan bookings:

create view sedan_ratings as
select Vehicle_Type, max(Driver_Ratings) as max_rate ,min(Driver_Ratings) as min_rate
from ola.bookings_ola
where Vehicle_Type='prime sedan';

select * from sedan_ratings;


#q7: Retrieve all rides where payment was made using UPI:

create view upi_payment as
select * from bookings_ola
where Payment_Method='upi';

select * from upi_payment;


#q8:Find the average customer rating per vehicle type:(any question having per uses group by funct)

create view avg_cust_rating_per_vehicletype as
select avg(Customer_Rating),Vehicle_Type 
from bookings_ola
group by Vehicle_Type;

select * from avg_cust_rating_per_vehicletype;


#q9: Calculate the total booking value of rides completed successfully

create view value_succesful_booking as
select sum(Booking_Value) from bookings_ola
where Booking_Status='success';

select * from value_succesful_booking;

#for not succesful
select sum(Booking_Value) from bookings_ola
where Booking_Status!='success';


#q10: List all incomplete rides along with the reason:

create view reason_for_incomplte_ride as
select Booking_ID,Incomplete_Rides_Reason 
from bookings_ola
where Incomplete_Rides='yes';

select * from reason_for_incomplte_ride;

#VTAT : Time taken for a driver/vehicle to complete a trip cycle (e.g., from pickup start to drop + returning to next available state).
#CTAT : Time taken from when a customer requests a ride until it is fulfilled (or completed).

#q11: avg turn around time and avg customer turn around

create view vtat_ctat as
SELECT AVG(V_TAT) AS Avg_Driver_Waiting_Time , AVG(C_TAT) AS Avg_Customer_Turnaround
FROM bookings_ola
WHERE V_TAT and C_TAT IS NOT NULL 
AND Booking_Status = 'Success';

select * from vtat_ctat;


#q12: Per Area avg turn around time and customer turnaround

create view per_area_tat_ctat as
SELECT Pickup_Location,AVG(V_TAT) AS Avg_Driver_Waiting_Time , AVG(C_TAT) AS Avg_Customer_Turnaround
FROM bookings_ola
WHERE V_TAT and C_TAT IS NOT NULL 
AND Booking_Status = 'Success'
GROUP BY Pickup_Location;

select * from per_area_tat_ctat;

#q13: Per area total amount generated 

create view Per_Area_Amount_generated as
select Pickup_Location ,sum(Booking_Value) from bookings_ola
where Booking_Status='Success'
group by Pickup_Location
order by 2 desc;

select * from Per_Area_Amount_generated;
