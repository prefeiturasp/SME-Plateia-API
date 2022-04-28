using System;
using System.Collections.Generic;

namespace SME_API_Plateia.DataDB
{
    public partial class Comment
    {
        public long Id { get; set; }
        public Guid UserId { get; set; }
        public long ShowId { get; set; }
        public string Content { get; set; } = null!;
        public byte State { get; set; }
        public DateTime CreateDate { get; set; }
        public DateTime UpdateDate { get; set; }

        public virtual Show Show { get; set; } = null!;
        public virtual User User { get; set; } = null!;
    }
}
