using System;
using System.Collections.Generic;

namespace SME_API_Plateia.DataDB
{
    public partial class Inscription
    {
        public long Id { get; set; }
        public Guid UserId { get; set; }
        public long EventId { get; set; }
        public bool Presence { get; set; }
        public int Priority { get; set; }
        public byte State { get; set; }
        public DateTime CreateDate { get; set; }
        public DateTime UpdateDate { get; set; }

        public virtual Event Event { get; set; } = null!;
        public virtual User User { get; set; } = null!;
    }
}
