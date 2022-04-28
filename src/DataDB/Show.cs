using System;
using System.Collections.Generic;

namespace SME_API_Plateia.DataDB
{
    public partial class Show
    {
        public Show()
        {
            Comments = new HashSet<Comment>();
            Events = new HashSet<Event>();
            Files = new HashSet<File>();
        }

        public long Id { get; set; }
        public string Name { get; set; } = null!;
        public string Synopsis { get; set; } = null!;
        public string? Classification { get; set; }
        public int Duration { get; set; }
        public string? PostScript { get; set; }
        public string? Video { get; set; }
        public long ShowTypeId { get; set; }
        public long GenreId { get; set; }
        public byte? HighLight { get; set; }
        public byte State { get; set; }
        public DateTime CreateDate { get; set; }
        public DateTime UpdateDate { get; set; }
        public string? Site { get; set; }

        public virtual Genre Genre { get; set; } = null!;
        public virtual ShowType ShowType { get; set; } = null!;
        public virtual ICollection<Comment> Comments { get; set; }
        public virtual ICollection<Event> Events { get; set; }
        public virtual ICollection<File> Files { get; set; }
    }
}
