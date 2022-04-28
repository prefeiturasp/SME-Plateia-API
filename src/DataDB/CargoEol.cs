using System;
using System.Collections.Generic;

namespace SME_API_Plateia.DataDB
{
    public partial class CargoEol
    {
        public int CdCargo { get; set; }
        public string? DcCargo { get; set; }
        public DateTime DtAtualizacaoTabela { get; set; }
    }
}
