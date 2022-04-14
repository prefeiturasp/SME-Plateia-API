using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Web.Http;

using SME_API_DataAccess;

namespace SME_API_Plateia.Controllers
{
    public class DadosEventoController : ApiController
    {
        public IEnumerable<Event> Get() 
        {
            using (PlateiaSMESPEntities entities = new PlateiaSMESPEntities())
            {
                return entities.Events.ToList();
            }
        }
    }
}
