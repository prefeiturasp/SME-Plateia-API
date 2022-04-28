using System;
using System.Collections.Generic;

namespace SME_API_Plateia.DataDB
{
    public partial class Parameter
    {
        public int Id { get; set; }
        public string Key { get; set; } = null!;
        public string? Value { get; set; }
        public string Description { get; set; } = null!;
        public byte State { get; set; }
        public DateTime CreateDate { get; set; }
        public DateTime UpdateDate { get; set; }
    }
}
