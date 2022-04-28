using System.ComponentModel.DataAnnotations;

namespace SME_API_Plateia.Models
{
    public class ListaEventos
    {
        public long IdEvento { get; set; }
        public string TipoEspetaculo { get; set; }
        public string Titulo { get; set; }
        public string Sintese { get; set; }

        public string Data { get; set; }

        public string StatusInscricao { get; set; }
    }
}
