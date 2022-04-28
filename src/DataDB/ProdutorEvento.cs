using System;
using System.Collections.Generic;

namespace SME_API_Plateia.DataDB
{
    public partial class ProdutorEvento
    {
        public long Id { get; set; }
        public long EventId { get; set; }
        public long ProdutorId { get; set; }
        public bool EnviarLista { get; set; }
        public byte State { get; set; }
        public DateTime CreateDate { get; set; }
        public DateTime UpdateDate { get; set; }

        public virtual Event Event { get; set; } = null!;
        public virtual Produtor Produtor { get; set; } = null!;
    }
}
