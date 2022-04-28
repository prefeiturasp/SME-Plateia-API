using System;
using System.Collections.Generic;

namespace SME_API_Plateia.DataDB
{
    public partial class Alertum
    {
        public long Id { get; set; }
        public string? Titulo { get; set; }
        public string? Msg { get; set; }
        public DateTime? EnicioExibe { get; set; }
        public DateTime? FimExibe { get; set; }
        public byte State { get; set; }
        public DateTime CreateDate { get; set; }
        public DateTime UpdateDate { get; set; }
    }
}
