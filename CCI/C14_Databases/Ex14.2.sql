select BuildingName, IFNULL(OpenCount, 0)
  from Buildings B
  inner join
(select BuildingID, count(RequestID) as OpenCount from Requests R
  inner join Apartments A
     on R.AptID = A.AptID
     and R.Status = 'Open'
   group by A.BuildingID) C
   on B.BuildingID = C.BuildingID
