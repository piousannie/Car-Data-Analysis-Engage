Use cars;
Select Make,Model,Power
from cleanedagain7
where ARAI_Certified_Mileage>=20
;

Use cars;
Select Make,Model,Cylinder_Configuration,Cylinder_Tank_Capacity
from cleanedagain7
Order by ARAI_Certified_Mileage
;

Use cars;
Select Make,Model,Gears
from cleanedagain7
where ARAI_Certified_Mileage>=20
Order by Make
;

