using System;
using System.Collections.Generic;

namespace SME_API_Plateia.DataDB
{
    public partial class City
    {
        public City()
        {
            Events = new HashSet<Event>();
        }

        public Guid Id { get; set; }
        public string Name { get; set; } = null!;
        public byte State { get; set; }
        public DateTime CreateDate { get; set; }
        public DateTime UpdateDate { get; set; }

        public virtual ICollection<Event> Events { get; set; }
    }
}
