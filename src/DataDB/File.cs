using System;
using System.Collections.Generic;

namespace SME_API_Plateia.DataDB
{
    public partial class File
    {
        public long Id { get; set; }
        public string Name { get; set; } = null!;
        public int Length { get; set; }
        public string Path { get; set; } = null!;
        public string? ThumbnailPath { get; set; }
        public string? Extension { get; set; }
        public long ShowId { get; set; }
        public byte State { get; set; }
        public DateTime CreateDate { get; set; }
        public DateTime UpdateDate { get; set; }

        public virtual Show Show { get; set; } = null!;
    }
}
