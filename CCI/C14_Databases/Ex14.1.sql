select TenantName from Tenants
 where TenantID in (
  select T.TenantID from Tenants T
    inner join AptTenants AT
      on T.TenantID = AT.TenantID
    group by T.TenantID
    having count(*) > 1)
