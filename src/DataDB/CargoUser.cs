using System;
using System.Collections.Generic;

namespace SME_API_Plateia.DataDB
{
    public partial class CargoUser
    {
        public Guid Id { get; set; }
        public long CodigoCargo { get; set; }
        public string? NomeCargo { get; set; }
        public Guid IdUser { get; set; }
        public byte State { get; set; }
        public DateTime CreateDate { get; set; }
        public DateTime UpdateDate { get; set; }
    }
}
