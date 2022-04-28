using System;
using System.Collections.Generic;

namespace SME_API_Plateia.DataDB
{
    public partial class Produtor
    {
        public Produtor()
        {
            ProdutorEventos = new HashSet<ProdutorEvento>();
        }

        public long Id { get; set; }
        public string? Nome { get; set; }
        public string? Email { get; set; }
        public string? Telefone { get; set; }
        public byte State { get; set; }
        public DateTime CreateDate { get; set; }
        public DateTime UpdateDate { get; set; }
        public string? Email2 { get; set; }
        public string? Email3 { get; set; }
        public string? Celular { get; set; }

        public virtual ICollection<ProdutorEvento> ProdutorEventos { get; set; }
    }
}
