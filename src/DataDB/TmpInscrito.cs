using System;
using System.Collections.Generic;

namespace SME_API_Plateia.DataDB
{
    public partial class TmpInscrito
    {
        public long Id { get; set; }
        public long EventId { get; set; }
        public Guid UserId { get; set; }
        public int Priority { get; set; }
        public string Local { get; set; } = null!;
        public string? PartnerCompany { get; set; }
        public string Address { get; set; } = null!;
        public DateTime PresentationDate { get; set; }
        public DateTime Schedule { get; set; }
        public DateTime EnrollStartAt { get; set; }
        public DateTime EnrollEndAt { get; set; }
        public int TicketQuantity { get; set; }
        public int TicketAvailable { get; set; }
        public int TicketByMember { get; set; }
        public int QueueRemaining { get; set; }
        public DateTime CreateDate { get; set; }
        public string Name { get; set; } = null!;
        public string? Rf { get; set; }
        public string? UserName { get; set; }
        public string? UserEmail { get; set; }
        public string? UserPhone { get; set; }
        public bool UserPresence { get; set; }
        public int? InscriptionStatus { get; set; }
        public int? EventStatus { get; set; }
        public int? RowNumber { get; set; }
    }
}
