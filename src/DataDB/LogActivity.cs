using System;
using System.Collections.Generic;

namespace SME_API_Plateia.DataDB
{
    public partial class LogActivity
    {
        public int Id { get; set; }
        public DateTime Date { get; set; }
        public string? Message { get; set; }
        public string? Action { get; set; }
        public string? Browser { get; set; }
        public string? HostName { get; set; }
        public string? UserHostAddress { get; set; }
        public string? QueryString { get; set; }
        public string? FilePath { get; set; }
        public string? Identity { get; set; }
        public string? Plataform { get; set; }
        public string? MobileDeviceModel { get; set; }
    }
}
