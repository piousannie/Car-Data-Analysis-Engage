Use cars;
Select Make,Model,Cylinder_Configuration
from cleanedagain7
where Model='WagonR' OR Model='Swift' OR Model='Dzire' OR Model='Nexon' OR Model='Alto' OR Model='Ertiga' OR Model='Seltos' OR Model='Venue'OR Model='Eeco'or Model='Punch' OR Model='Creta' OR Model='Brezza' OR Model='Celerio' OR Model='Sonet' OR Model='i10' OR Model='i20' OR Model='Baleno'OR Model='S-Presso' or Model='Amaze' or Model='Tiago'
;
Select avg(Height),avg(Width),avg(Length)
from cleanedagain7
where Model='WagonR' OR Model='Swift' OR Model='Dzire' OR Model='Nexon' OR Model='Alto' OR Model='Ertiga' OR Model='Seltos' OR Model='Venue'OR Model='Eeco'or Model='Punch' OR Model='Creta' OR Model='Brezza' OR Model='Celerio' OR Model='Sonet' OR Model='i10' OR Model='i20' OR Model='Baleno'OR Model='S-Presso' or Model='Amaze' or Model='Tiago'
;
Select avg(Power),avg(Torque)
from cleanedagain7
where Model='WagonR' OR Model='Swift' OR Model='Dzire' OR Model='Nexon' OR Model='Alto' OR Model='Ertiga' OR Model='Seltos' OR Model='Venue'OR Model='Eeco'or Model='Punch' OR Model='Creta' OR Model='Brezza' OR Model='Celerio' OR Model='Sonet' OR Model='i10' OR Model='i20' OR Model='Baleno'OR Model='S-Presso' or Model='Amaze' or Model='Tiago'
;
Select max(Seating_Capacity)
from cleanedagain7
where Model='WagonR' OR Model='Swift' OR Model='Dzire' OR Model='Nexon' OR Model='Alto' OR Model='Ertiga' OR Model='Seltos' OR Model='Venue'OR Model='Eeco'or Model='Punch' OR Model='Creta' OR Model='Brezza' OR Model='Celerio' OR Model='Sonet' OR Model='i10' OR Model='i20' OR Model='Baleno'OR Model='S-Presso' or Model='Amaze' or Model='Tiago'
;
Select max(Length),max(Width)
from cleanedagain7
where Model='WagonR' OR Model='Swift' OR Model='Dzire' OR Model='Nexon' OR Model='Alto' OR Model='Ertiga' OR Model='Seltos' OR Model='Venue'OR Model='Eeco'or Model='Punch' OR Model='Creta' OR Model='Brezza' OR Model='Celerio' OR Model='Sonet' OR Model='i10' OR Model='i20' OR Model='Baleno'OR Model='S-Presso' or Model='Amaze' or Model='Tiago'
and
where Body_Type="Sedan";
;
Select min(Kerb_Weight)
from cleanedagain7
where Model='WagonR' OR Model='Swift' OR Model='Dzire' OR Model='Nexon' OR Model='Alto' OR Model='Ertiga' OR Model='Seltos' OR Model='Venue'OR Model='Eeco'or Model='Punch' OR Model='Creta' OR Model='Brezza' OR Model='Celerio' OR Model='Sonet' OR Model='i10' OR Model='i20' OR Model='Baleno'OR Model='S-Presso' or Model='Amaze' or Model='Tiago'
and
where ARAI_Certified_Mileage>=20;


