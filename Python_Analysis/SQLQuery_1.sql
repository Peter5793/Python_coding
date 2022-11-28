SELECT 
    BriefTitle,
    a.Id,
    b.Country
FROM Study AS a 
    INNER JOIN StudyCountry AS b 
    ON a.Id = b.Id;

SELECT 
    b.Country as Country,
    count(b.Country) AS StudyNumbers
FROM Study AS a 
    INNER JOIN StudyCountry AS b 
    ON a.Id = b.Id
GROUP BY b.Country
ORDER BY StudyNumbers DESC;

-- total number of tables in the database with the importstudyNumber Columns

WITH data AS(
    SELECT TABLE_NAME, COLUMN_NAME, DATA_TYPE, IS_NULLABLE, COLUMN_DEFAULT
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE COLUMN_NAME LIKE '%importNumber%' OR COLUMN_NAME LIKE '%importStudyNumber%' 
)
SELECT  * FROM data

SELECT 
    Id,
    ProductType,
    Code,
    OfficialTitle,
    importNumber
FROM Study
WHERE Code <> ''
-- Finding the toal number of tables in the database without View
SELECT
    TABLE_NAME, COLUMN_NAME
FROM INFORMATION_SCHEMA.COLUMNS
WHERE COLUMN_NAME LIKE '%RecruitmentStatus%'

-- find the view tables in the database
SELECT
    TABLE_NAME
FROM INFORMATION_SCHEMA.VIEWS

SELECT * FROM ProductBatch
SELECT * FROM StudyGroup

SELECT 
    ModifiedOn,
    ExpiryDate,
    DATEDIFF(day, ModifiedOn, ExpiryDate) AS time_difference
FROM ProductBatch

SELECT 
    *
FROM StudyPlanning
ORDER BY StartDatePlanning DESC

SELECT 
     *
FROM Study
WHERE BriefTitle <> 'NULL' AND BriefTitle <>''

SELECT
    
    a.InterventionName AS Product,
    b.DateFirstPatientIn,
    b.DateLastPatientOut,
    a.InterventionDescription
    --DATEDIFF(Month,b.DateFirstPatientIn, b.DateLastPatientOut) AS CountInMonth
FROM StudyGroup AS a  LEFT JOIN Site AS b 
ON a.Id = b.Id

SELECT TOP 10 * FROM Site 
SELECT id FROM StudyGroup ORDER BY id DESC


SELECT
    main.Id,
    secondary.Id AS SiteId ,
    main.InterventionName,
    main.InterventionDescription,
    secondary.DateFirstPatientIn,
    secondary.DateLastPatientOut
FROM StudyGroup AS main INNER JOIN Site AS secondary 
ON main.StudyId = secondary.StudyId
--INNER JOIN Study AS tertiary SELECT TOP 10 * FROM Study
--ON main.Id = tertiary.Id
WHERE secondary.DateFirstPatientIn IS NOT NULL
