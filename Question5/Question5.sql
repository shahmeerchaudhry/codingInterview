-- using mySQL
SELECT 

CONCAT(Person.FamilyName,' ',Person.GivenName) AS PersonName, 
TIMESTAMPDIFF(YEAR, Person.DateOfBirth, CURRENT_DATE) AS AGE,

-- COALESCE Used to return UNKNOWN on NULL
COALESCE(CONCAT(Father.FamilyName,' ',Father.GivenName),'UNKNOWN') AS FatherName,
COALESCE(CONCAT(Mother.FamilyName,' ',Mother.GivenName),'UNKNOWN') AS MotherName

FROM Person

LEFT JOIN PersonParent ON Person.PersonID = PersonParent.PersonID
LEFT JOIN Person AS Father ON Person.PersonID = Father.PersonID AND Father.Gender ='M'
LEFT JOIN Person AS Mother ON Person.PersonID = Mother.PersonID AND Mother.Gender ='F';