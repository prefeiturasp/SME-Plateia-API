using System;
using System.Collections.Generic;

namespace SME_API_Plateia.DataDB
{
    public partial class ShowType
    {
        public ShowType()
        {
            Shows = new HashSet<Show>();
            Genres = new HashSet<Genre>();
        }

        public long Id { get; set; }
        public string Name { get; set; } = null!;
        public byte State { get; set; }
        public DateTime CreateDate { get; set; }
        public DateTime UpdateDate { get; set; }

        public virtual ICollection<Show> Shows { get; set; }

        public virtual ICollection<Genre> Genres { get; set; }
    }
}
