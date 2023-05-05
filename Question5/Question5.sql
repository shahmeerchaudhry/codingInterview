--USING MYSQL

SELECT 
CONCAT(Person.FamilyName,' ',Person.GivenName) AS PersonName, 
TIMESTAMPDIFF(YEAR, Person.DateOfBirth, CURRENT_DATE) AS AGE,
CONCAT(Father.FamilyName,' ',Father.GivenName) AS FatherName,
CONCAT(Mother.FamilyName,' ',Mother.GivenName) AS MotherName

FROM Person
--Using LEFT JOIN Returns NULL IF it is EMPTY (ie - NO PARENT)
LEFT JOIN PersonParent ON Person.PersonID = PersonParent.PersonID
LEFT JOIN Person AS Father ON Person.PersonID = Father.PersonID AND Father.Gender ='M'
LEFT JOIN Person AS Mother ON Person.PersonID = Mother.PersonID AND Mother.Gender ='F';

