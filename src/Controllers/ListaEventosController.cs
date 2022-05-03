using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Newtonsoft.Json;
using SME_API_Plateia.DataDB;

// For more information on enabling Web API for empty projects, visit https://go.microsoft.com/fwlink/?LinkID=397860

namespace SME_API_Plateia.Controllers
{
    [Route("api/evento/listainscricoesabertas")]
    [ApiController]
    public class ListaEventosController : ControllerBase
    {
        // GET: api/<ListaEventosController>
        [HttpGet]
        public IEnumerable<Models.ListaEventos> Get()
        {
            //Data Atual
            DateTime currentDate = DateTime.Now.Date;

            //6 dias pra frente
            DateTime finalDate = currentDate.AddDays(6);


            using (var db = new PlateiaSMESPContext())
            {
                try
                {
                    IEnumerable<Event> lstEvent = null;
                    IEnumerable<Models.ListaEventos> lstEventShowResultSet = null;

                    lstEvent = db.Events.AsQueryable().Include(x => x.Show).Include(x => x.Show.Genre).Include(x => x.Show.ShowType).Include(x => x.Show.Files)
                                            .AsNoTracking()
                                            .Where(x => x.PresentationDate >= currentDate &&
                                                        x.PresentationDate <= finalDate &&
                                                        x.TicketAvailable > 0 && DateTime.Now >= x.EnrollStartAt && DateTime.Now <= x.EnrollEndAt
                                                ).ToList();


                    lstEvent = lstEvent.OrderBy(x => x.PresentationDate);
                    lstEvent = lstEvent.DistinctBy(x => x.ShowId).ToList();

                    lstEventShowResultSet = lstEvent.Select(e => new Models.ListaEventos
                    {
                        IdEvento = e.Show.Id,
                        TipoEspetaculo = e.Show.ShowType.Name,
                        Titulo = e.Show.Name,
                        Sintese = e.Show.Synopsis,
                        Data = Convert.ToString(e.PresentationDate.ToString("dd/MM/yyyy")).Substring(0,10),
                        StatusInscricao = "Inscrições abertas"
                    }).ToList();

                    return lstEventShowResultSet;

                }
                catch (Exception)
                {                    
                    throw;
                }

            }

        }

        // GET api/<ListaEventosController>/5
        [HttpGet("{id}")]
        public string Get(int id)
        {
            return "value";
        }

        // POST api/<ListaEventosController>
        [HttpPost]
        public void Post([FromBody] string value)
        {
        }

        // PUT api/<ListaEventosController>/5
        [HttpPut("{id}")]
        public void Put(int id, [FromBody] string value)
        {
        }

        // DELETE api/<ListaEventosController>/5
        [HttpDelete("{id}")]
        public void Delete(int id)
        {
        }
    }
}
