using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Web.Http;
using System.Data.Entity;
using SME_API_DataAccess;
using System.Data.SqlClient;
using System.Configuration;
using System.Data;



namespace SME_API_Plateia.Controllers
{
    public class DadosEventoController : ApiController
    {

        [Route("api/evento/listaeventos")]
        public IEnumerable<Models.DadosEvento> Get()
        {

            List<Models.DadosEvento> retDados = new List<Models.DadosEvento>();
            SqlConnection cn = new SqlConnection(ConfigurationManager.ConnectionStrings["PlateiaSMESPEntities"].ConnectionString);

            try
            {
                string command = "SELECT "
                                    + "ST.Name as [Tipo do Espetáculo], "
                                    + "S.Name as [Título], "
                                    + "S.Synopsis as [Síntese], "
                                    + "E.PresentationDate as [Data], "
                                    + "E.Id as [Id do evento], "
                                    + "'Inscrições abertas' as [Status das inscrições] "
                                + "FROM[PlateiaSMESP].[dbo].[Event] as E (nolock) "
                                + "inner join[PlateiaSMESP].[dbo].[Show] S(nolock) "
                                + "on E.ShowId = S.Id "
                                + "inner join[PlateiaSMESP].[dbo].[ShowType] ST(nolock) "
                                + "on S.ShowTypeId = ST.Id "
                                + "where E.PresentationDate between getdate() and DATEADD(day, 10, Getdate())"
                                + "and E.TicketAvailable > 0 and GETDATE() >= E.EnrollStartAt and GETDATE() <= E.EnrollEndAt";

                cn.Open();

                SqlDataAdapter adapter = new SqlDataAdapter(command, cn);
                DataSet ds = new DataSet();
                adapter.Fill(ds);

                foreach (DataRow dr in ds.Tables[0].Rows)
                {
                    retDados.Add(new Models.DadosEvento
                    {
                        TipoEspetaculo = (string)dr["Tipo do Espetáculo"],
                        Titulo = (string)dr["Título"],
                        Sintese = (string)dr["Síntese"],
                        Data = (DateTime)dr["Data"],
                        IdEvento = (long)dr["Id do evento"],
                        StatusInscricao = "Inscrições abertas"
                    });

                }

            }
            catch (Exception)
            {
                cn.Close();
                throw;
            }
            
            return retDados;

        }


        public Event Get(int id)
        {
            using (PlateiaSMESPEntities dados = new PlateiaSMESPEntities())
            {
                return dados.Events.FirstOrDefault(x => x.Id == id);
            }
        }
    }
}
