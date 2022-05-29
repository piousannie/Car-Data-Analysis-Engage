Use cars;
Select Make,Model,ARAI_Certified_Mileage
from cleanedagain7
Order by Cylinder_Tank_Capacity
;

Use cars;
Select Make,Model,ARAI_Certified_Mileage
from cleanedagain7
Order by Fuel_Type
;

Use cars;
Select Length,Width,Height
from cleanedagain7
Order by Cylinder_Configuration
;

Use cars;
Select Body_Type,avg(Cylinder_Tank_Capacity)
from cleanedagain7
Where Body_Type="Sedan" 
;