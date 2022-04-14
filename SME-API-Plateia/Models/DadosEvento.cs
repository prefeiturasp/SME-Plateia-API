using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace SME_API_Plateia.Models
{
    public class DadosEvento
    {
        public string TipoEspetaculo { get; set; }
        public string Titulo { get; set; }
        public string Sintese { get; set; }
        public DateTime Data { get; set; }
        public long IdEvento { get; set; }
        public string StatusInscricao { get; set; }

    }
}