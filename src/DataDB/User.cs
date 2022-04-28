using System;
using System.Collections.Generic;

namespace SME_API_Plateia.DataDB
{
    public partial class User
    {
        public User()
        {
            Comments = new HashSet<Comment>();
            Inscriptions = new HashSet<Inscription>();
        }

        public Guid Id { get; set; }
        public Guid EntityId { get; set; }
        public string? Login { get; set; }
        public string? Password { get; set; }
        public int Crypt { get; set; }
        public string? Name { get; set; }
        public string? Rf { get; set; }
        public string? Email { get; set; }
        public string? Tel { get; set; }
        public bool IsAdmin { get; set; }
        public DateTime? EventDueDate { get; set; }
        public DateTime? PunishmentDueDate { get; set; }
        public byte State { get; set; }
        public DateTime CreateDate { get; set; }
        public DateTime UpdateDate { get; set; }
        public string? Email2 { get; set; }
        public string? Celular { get; set; }
        public DateTime? DataNascimento { get; set; }

        public virtual ICollection<Comment> Comments { get; set; }
        public virtual ICollection<Inscription> Inscriptions { get; set; }
    }
}
