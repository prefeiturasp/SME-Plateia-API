using System;
using System.Collections.Generic;

namespace SME_API_Plateia.DataDB
{
    public partial class Event
    {
        public Event()
        {
            Inscriptions = new HashSet<Inscription>();
            ProdutorEventos = new HashSet<ProdutorEvento>();
        }

        public long Id { get; set; }
        public long ShowId { get; set; }
        public Guid CityId { get; set; }
        public string Local { get; set; } = null!;
        public string Address { get; set; } = null!;
        public string? PartnerCompany { get; set; }
        public DateTime PresentationDate { get; set; }
        public DateTime Schedule { get; set; }
        public DateTime EnrollStartAt { get; set; }
        public DateTime EnrollEndAt { get; set; }
        public int TicketQuantity { get; set; }
        public int TicketAvailable { get; set; }
        public int TicketByMember { get; set; }
        public int QueueSize { get; set; }
        public int QueueRemaining { get; set; }
        public byte State { get; set; }
        public DateTime CreateDate { get; set; }
        public DateTime UpdateDate { get; set; }
        public bool AllowPrint { get; set; }
        public string? Titulo { get; set; }

        public virtual City City { get; set; } = null!;
        public virtual Show Show { get; set; } = null!;
        public virtual ICollection<Inscription> Inscriptions { get; set; }
        public virtual ICollection<ProdutorEvento> ProdutorEventos { get; set; }
    }
}
