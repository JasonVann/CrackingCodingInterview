Update Requests R
  Set Status = 'close'
  inner join Apartments A
     on R.AptID = A.AptID
     and R.Status = 'Open'
   inner join Buildings B
   on B.BuildingID = A.BuildingID
   where B.BuildingName = '11'
