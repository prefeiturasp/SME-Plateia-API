using System;
using System.Collections.Generic;

namespace SME_API_Plateia.DataDB
{
    public partial class EventHistory
    {
        public long? Id { get; set; }
        public long? ShowId { get; set; }
        public Guid? CityId { get; set; }
        public string? Local { get; set; }
        public string? Address { get; set; }
        public string? PartnerCompany { get; set; }
        public DateTime? PresentationDate { get; set; }
        public DateTime? Schedule { get; set; }
        public DateTime? EnrollStartAt { get; set; }
        public DateTime? EnrollEndAt { get; set; }
        public int? TicketQuantity { get; set; }
        public int? TicketAvailable { get; set; }
        public int? TicketByMember { get; set; }
        public int? QueueSize { get; set; }
        public int? QueueRemaining { get; set; }
        public byte? State { get; set; }
        public DateTime? CreateDate { get; set; }
        public DateTime? UpdateDate { get; set; }
    }
}
