using System;
using System.Collections.Generic;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata;
using System.Configuration;

namespace SME_API_Plateia.DataDB
{
    public partial class PlateiaSMESPContext : DbContext
    {
        public PlateiaSMESPContext()
        {
        }

        public PlateiaSMESPContext(DbContextOptions<PlateiaSMESPContext> options)
            : base(options)
        {
        }

        public virtual DbSet<Alertum> Alerta { get; set; } = null!;
        public virtual DbSet<CargoEol> CargoEols { get; set; } = null!;
        public virtual DbSet<CargoUser> CargoUsers { get; set; } = null!;
        public virtual DbSet<City> Cities { get; set; } = null!;
        public virtual DbSet<Comment> Comments { get; set; } = null!;
        public virtual DbSet<Event> Events { get; set; } = null!;
        public virtual DbSet<EventHistory> EventHistories { get; set; } = null!;
        public virtual DbSet<File> Files { get; set; } = null!;
        public virtual DbSet<Genre> Genres { get; set; } = null!;
        public virtual DbSet<Inscription> Inscriptions { get; set; } = null!;
        public virtual DbSet<LogActivity> LogActivities { get; set; } = null!;
        public virtual DbSet<LogError> LogErrors { get; set; } = null!;
        public virtual DbSet<MigrationHistory> MigrationHistories { get; set; } = null!;
        public virtual DbSet<Parameter> Parameters { get; set; } = null!;
        public virtual DbSet<Produtor> Produtors { get; set; } = null!;
        public virtual DbSet<ProdutorEvento> ProdutorEventos { get; set; } = null!;
        public virtual DbSet<Show> Shows { get; set; } = null!;
        public virtual DbSet<ShowType> ShowTypes { get; set; } = null!;
        public virtual DbSet<TmpInscrito> TmpInscritos { get; set; } = null!;
        public virtual DbSet<User> Users { get; set; } = null!;

        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            if (!optionsBuilder.IsConfigured)
            {

                var cs = Environment.GetEnvironmentVariable("PlateiaSMESPEntities");

                optionsBuilder.UseSqlServer(cs);
            }
        }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            modelBuilder.Entity<Alertum>(entity =>
            {
                entity.Property(e => e.CreateDate).HasColumnType("datetime");

                entity.Property(e => e.EnicioExibe).HasColumnType("datetime");

                entity.Property(e => e.FimExibe).HasColumnType("datetime");

                entity.Property(e => e.UpdateDate).HasColumnType("datetime");
            });

            modelBuilder.Entity<CargoEol>(entity =>
            {
                entity.HasKey(e => e.CdCargo)
                    .HasName("PK_cargo");

                entity.ToTable("CargoEol");

                entity.Property(e => e.CdCargo)
                    .ValueGeneratedNever()
                    .HasColumnName("cd_cargo");

                entity.Property(e => e.DcCargo)
                    .HasMaxLength(50)
                    .IsUnicode(false)
                    .HasColumnName("dc_cargo");

                entity.Property(e => e.DtAtualizacaoTabela)
                    .HasColumnType("datetime")
                    .HasColumnName("dt_atualizacao_tabela");
            });

            modelBuilder.Entity<CargoUser>(entity =>
            {
                entity.ToTable("CargoUser");

                entity.Property(e => e.Id).ValueGeneratedNever();

                entity.Property(e => e.CreateDate).HasColumnType("datetime");

                entity.Property(e => e.UpdateDate).HasColumnType("datetime");
            });

            modelBuilder.Entity<City>(entity =>
            {
                entity.ToTable("City");

                entity.Property(e => e.Id).ValueGeneratedNever();

                entity.Property(e => e.CreateDate).HasColumnType("datetime");

                entity.Property(e => e.Name).HasMaxLength(200);

                entity.Property(e => e.UpdateDate).HasColumnType("datetime");
            });

            modelBuilder.Entity<Comment>(entity =>
            {
                entity.ToTable("Comment");

                entity.HasIndex(e => e.ShowId, "IX_ShowId");

                entity.HasIndex(e => e.UserId, "IX_UserId");

                entity.Property(e => e.Content).HasMaxLength(500);

                entity.Property(e => e.CreateDate).HasColumnType("datetime");

                entity.Property(e => e.UpdateDate).HasColumnType("datetime");

                entity.HasOne(d => d.Show)
                    .WithMany(p => p.Comments)
                    .HasForeignKey(d => d.ShowId)
                    .OnDelete(DeleteBehavior.ClientSetNull)
                    .HasConstraintName("FK_dbo.Comment_dbo.Show_ShowId");

                entity.HasOne(d => d.User)
                    .WithMany(p => p.Comments)
                    .HasForeignKey(d => d.UserId)
                    .OnDelete(DeleteBehavior.ClientSetNull)
                    .HasConstraintName("FK_dbo.Comment_dbo.User_UserId");
            });

            modelBuilder.Entity<Event>(entity =>
            {
                entity.ToTable("Event");

                entity.HasIndex(e => e.CityId, "IX_CityId");

                entity.HasIndex(e => e.PresentationDate, "IX_Event_PresentationDate");

                entity.HasIndex(e => e.ShowId, "IX_ShowId");

                entity.Property(e => e.Address).HasMaxLength(400);

                entity.Property(e => e.CreateDate).HasColumnType("datetime");

                entity.Property(e => e.EnrollEndAt).HasColumnType("datetime");

                entity.Property(e => e.EnrollStartAt).HasColumnType("datetime");

                entity.Property(e => e.Local).HasMaxLength(300);

                entity.Property(e => e.PartnerCompany).HasMaxLength(150);

                entity.Property(e => e.PresentationDate).HasColumnType("datetime");

                entity.Property(e => e.Schedule).HasColumnType("datetime");

                entity.Property(e => e.UpdateDate).HasColumnType("datetime");

                entity.HasOne(d => d.City)
                    .WithMany(p => p.Events)
                    .HasForeignKey(d => d.CityId)
                    .OnDelete(DeleteBehavior.ClientSetNull)
                    .HasConstraintName("FK_dbo.Event_dbo.City_CityId");

                entity.HasOne(d => d.Show)
                    .WithMany(p => p.Events)
                    .HasForeignKey(d => d.ShowId)
                    .OnDelete(DeleteBehavior.ClientSetNull)
                    .HasConstraintName("FK_dbo.Event_dbo.Show_ShowId");
            });

            modelBuilder.Entity<EventHistory>(entity =>
            {
                entity.HasNoKey();

                entity.ToTable("_EventHistory");

                entity.Property(e => e.Address).HasMaxLength(400);

                entity.Property(e => e.CreateDate).HasColumnType("datetime");

                entity.Property(e => e.EnrollEndAt).HasColumnType("datetime");

                entity.Property(e => e.EnrollStartAt).HasColumnType("datetime");

                entity.Property(e => e.Local).HasMaxLength(300);

                entity.Property(e => e.PartnerCompany).HasMaxLength(150);

                entity.Property(e => e.PresentationDate).HasColumnType("datetime");

                entity.Property(e => e.Schedule).HasColumnType("datetime");

                entity.Property(e => e.UpdateDate).HasColumnType("datetime");
            });

            modelBuilder.Entity<File>(entity =>
            {
                entity.ToTable("File");

                entity.HasIndex(e => e.ShowId, "IX_ShowId");

                entity.Property(e => e.CreateDate).HasColumnType("datetime");

                entity.Property(e => e.Name).HasMaxLength(300);

                entity.Property(e => e.UpdateDate).HasColumnType("datetime");

                entity.HasOne(d => d.Show)
                    .WithMany(p => p.Files)
                    .HasForeignKey(d => d.ShowId)
                    .OnDelete(DeleteBehavior.ClientSetNull)
                    .HasConstraintName("FK_dbo.File_dbo.Show_ShowId");
            });

            modelBuilder.Entity<Genre>(entity =>
            {
                entity.ToTable("Genre");

                entity.Property(e => e.CreateDate).HasColumnType("datetime");

                entity.Property(e => e.Name).HasMaxLength(150);

                entity.Property(e => e.UpdateDate).HasColumnType("datetime");

                entity.HasMany(d => d.ShowTypes)
                    .WithMany(p => p.Genres)
                    .UsingEntity<Dictionary<string, object>>(
                        "GenreShowType",
                        l => l.HasOne<ShowType>().WithMany().HasForeignKey("ShowTypeId").OnDelete(DeleteBehavior.ClientSetNull).HasConstraintName("FK_dbo.GenreShowType_dbo.ShowType_ShowTypeId"),
                        r => r.HasOne<Genre>().WithMany().HasForeignKey("GenreId").OnDelete(DeleteBehavior.ClientSetNull).HasConstraintName("FK_dbo.GenreShowType_dbo.Genre_GenreId"),
                        j =>
                        {
                            j.HasKey("GenreId", "ShowTypeId").HasName("PK_dbo.GenreShowType");

                            j.ToTable("GenreShowType");

                            j.HasIndex(new[] { "GenreId" }, "IX_GenreId");

                            j.HasIndex(new[] { "ShowTypeId" }, "IX_ShowTypeId");
                        });
            });

            modelBuilder.Entity<Inscription>(entity =>
            {
                entity.ToTable("Inscription");

                entity.HasIndex(e => e.EventId, "IX_EventId");

                entity.HasIndex(e => e.Priority, "IX_Inscription_Priority");

                entity.HasIndex(e => e.UserId, "IX_UserId");

                entity.Property(e => e.CreateDate).HasColumnType("datetime");

                entity.Property(e => e.UpdateDate).HasColumnType("datetime");

                entity.HasOne(d => d.Event)
                    .WithMany(p => p.Inscriptions)
                    .HasForeignKey(d => d.EventId)
                    .OnDelete(DeleteBehavior.ClientSetNull)
                    .HasConstraintName("FK_dbo.Inscription_dbo.Event_EventId");

                entity.HasOne(d => d.User)
                    .WithMany(p => p.Inscriptions)
                    .HasForeignKey(d => d.UserId)
                    .OnDelete(DeleteBehavior.ClientSetNull)
                    .HasConstraintName("FK_dbo.Inscription_dbo.User_UserId");
            });

            modelBuilder.Entity<LogActivity>(entity =>
            {
                entity.ToTable("LogActivity");

                entity.HasIndex(e => e.Date, "IX_LogActivity_Date");

                entity.HasIndex(e => e.Identity, "IX_LogActivity_Identity");

                entity.Property(e => e.Action)
                    .HasMaxLength(30)
                    .IsUnicode(false);

                entity.Property(e => e.Browser)
                    .HasMaxLength(250)
                    .IsUnicode(false);

                entity.Property(e => e.Date).HasColumnType("datetime");

                entity.Property(e => e.FilePath)
                    .HasMaxLength(250)
                    .IsUnicode(false);

                entity.Property(e => e.HostName)
                    .HasMaxLength(500)
                    .IsUnicode(false);

                entity.Property(e => e.Identity)
                    .HasMaxLength(250)
                    .IsUnicode(false);

                entity.Property(e => e.Message)
                    .HasMaxLength(4000)
                    .IsUnicode(false);

                entity.Property(e => e.MobileDeviceModel)
                    .HasMaxLength(250)
                    .IsUnicode(false);

                entity.Property(e => e.Plataform)
                    .HasMaxLength(250)
                    .IsUnicode(false);

                entity.Property(e => e.QueryString)
                    .HasMaxLength(500)
                    .IsUnicode(false);

                entity.Property(e => e.UserHostAddress)
                    .HasMaxLength(500)
                    .IsUnicode(false);
            });

            modelBuilder.Entity<LogError>(entity =>
            {
                entity.ToTable("LogError");

                entity.HasIndex(e => e.Date, "IX_LogActivity_Date");

                entity.HasIndex(e => e.Identity, "IX_LogActivity_Identity");

                entity.Property(e => e.Browser)
                    .HasMaxLength(250)
                    .IsUnicode(false);

                entity.Property(e => e.Date).HasColumnType("datetime");

                entity.Property(e => e.Exception)
                    .HasMaxLength(8000)
                    .IsUnicode(false);

                entity.Property(e => e.FilePath)
                    .HasMaxLength(250)
                    .IsUnicode(false);

                entity.Property(e => e.HostName)
                    .HasMaxLength(500)
                    .IsUnicode(false);

                entity.Property(e => e.Identity)
                    .HasMaxLength(250)
                    .IsUnicode(false);

                entity.Property(e => e.Level)
                    .HasMaxLength(50)
                    .IsUnicode(false);

                entity.Property(e => e.Logger)
                    .HasMaxLength(255)
                    .IsUnicode(false);

                entity.Property(e => e.Message)
                    .HasMaxLength(4000)
                    .IsUnicode(false);

                entity.Property(e => e.MobileDeviceModel)
                    .HasMaxLength(250)
                    .IsUnicode(false);

                entity.Property(e => e.Plataform)
                    .HasMaxLength(250)
                    .IsUnicode(false);

                entity.Property(e => e.QueryString)
                    .HasMaxLength(500)
                    .IsUnicode(false);

                entity.Property(e => e.UserHostAddress)
                    .HasMaxLength(500)
                    .IsUnicode(false);
            });

            modelBuilder.Entity<MigrationHistory>(entity =>
            {
                entity.HasKey(e => new { e.MigrationId, e.ContextKey })
                    .HasName("PK_dbo.__MigrationHistory");

                entity.ToTable("__MigrationHistory");

                entity.Property(e => e.MigrationId).HasMaxLength(150);

                entity.Property(e => e.ContextKey).HasMaxLength(300);

                entity.Property(e => e.ProductVersion).HasMaxLength(32);
            });

            modelBuilder.Entity<Parameter>(entity =>
            {
                entity.ToTable("Parameter");

                entity.Property(e => e.CreateDate).HasColumnType("datetime");

                entity.Property(e => e.Description).HasMaxLength(250);

                entity.Property(e => e.Key).HasMaxLength(100);

                entity.Property(e => e.UpdateDate).HasColumnType("datetime");

                entity.Property(e => e.Value).HasColumnType("text");
            });

            modelBuilder.Entity<Produtor>(entity =>
            {
                entity.ToTable("Produtor");

                entity.Property(e => e.CreateDate).HasColumnType("datetime");

                entity.Property(e => e.UpdateDate).HasColumnType("datetime");
            });

            modelBuilder.Entity<ProdutorEvento>(entity =>
            {
                entity.ToTable("ProdutorEvento");

                entity.HasIndex(e => e.EventId, "IX_EventId")
                    .HasFillFactor(90);

                entity.HasIndex(e => e.ProdutorId, "IX_ProdutorId")
                    .HasFillFactor(90);

                entity.Property(e => e.CreateDate).HasColumnType("datetime");

                entity.Property(e => e.UpdateDate).HasColumnType("datetime");

                entity.HasOne(d => d.Event)
                    .WithMany(p => p.ProdutorEventos)
                    .HasForeignKey(d => d.EventId)
                    .OnDelete(DeleteBehavior.ClientSetNull)
                    .HasConstraintName("FK_dbo.ProdutorEvento_dbo.Event_EventId");

                entity.HasOne(d => d.Produtor)
                    .WithMany(p => p.ProdutorEventos)
                    .HasForeignKey(d => d.ProdutorId)
                    .OnDelete(DeleteBehavior.ClientSetNull)
                    .HasConstraintName("FK_dbo.ProdutorEvento_dbo.Produtor_ProdutorId");
            });

            modelBuilder.Entity<Show>(entity =>
            {
                entity.ToTable("Show");

                entity.HasIndex(e => e.GenreId, "IX_GenreId");

                entity.HasIndex(e => e.ShowTypeId, "IX_ShowTypeId");

                entity.Property(e => e.Classification).HasMaxLength(150);

                entity.Property(e => e.CreateDate).HasColumnType("datetime");

                entity.Property(e => e.Name).HasMaxLength(150);

                entity.Property(e => e.PostScript).HasMaxLength(250);

                entity.Property(e => e.Synopsis).HasMaxLength(1500);

                entity.Property(e => e.UpdateDate).HasColumnType("datetime");

                entity.Property(e => e.Video).HasMaxLength(150);

                entity.HasOne(d => d.Genre)
                    .WithMany(p => p.Shows)
                    .HasForeignKey(d => d.GenreId)
                    .OnDelete(DeleteBehavior.ClientSetNull)
                    .HasConstraintName("FK_dbo.Show_dbo.Genre_GenreId");

                entity.HasOne(d => d.ShowType)
                    .WithMany(p => p.Shows)
                    .HasForeignKey(d => d.ShowTypeId)
                    .OnDelete(DeleteBehavior.ClientSetNull)
                    .HasConstraintName("FK_dbo.Show_dbo.ShowType_ShowTypeId");
            });

            modelBuilder.Entity<ShowType>(entity =>
            {
                entity.ToTable("ShowType");

                entity.Property(e => e.CreateDate).HasColumnType("datetime");

                entity.Property(e => e.Name).HasMaxLength(150);

                entity.Property(e => e.UpdateDate).HasColumnType("datetime");
            });

            modelBuilder.Entity<TmpInscrito>(entity =>
            {
                entity.HasNoKey();

                entity.ToTable("_tmp_Inscritos");

                entity.Property(e => e.Address).HasMaxLength(400);

                entity.Property(e => e.CreateDate).HasColumnType("datetime");

                entity.Property(e => e.EnrollEndAt).HasColumnType("datetime");

                entity.Property(e => e.EnrollStartAt).HasColumnType("datetime");

                entity.Property(e => e.Local).HasMaxLength(300);

                entity.Property(e => e.Name).HasMaxLength(150);

                entity.Property(e => e.PartnerCompany).HasMaxLength(150);

                entity.Property(e => e.PresentationDate).HasColumnType("datetime");

                entity.Property(e => e.Rf)
                    .HasMaxLength(25)
                    .HasColumnName("RF");

                entity.Property(e => e.Schedule).HasColumnType("datetime");

                entity.Property(e => e.UserName).HasMaxLength(200);
            });

            modelBuilder.Entity<User>(entity =>
            {
                entity.ToTable("User");

                entity.HasIndex(e => e.Rf, "IX_User_RF");

                entity.Property(e => e.Id).ValueGeneratedNever();

                entity.Property(e => e.CreateDate).HasColumnType("datetime");

                entity.Property(e => e.DataNascimento)
                    .HasColumnType("datetime")
                    .HasDefaultValueSql("('1900-01-01T00:00:00.000')");

                entity.Property(e => e.EventDueDate).HasColumnType("datetime");

                entity.Property(e => e.Login).HasMaxLength(500);

                entity.Property(e => e.Name).HasMaxLength(200);

                entity.Property(e => e.PunishmentDueDate).HasColumnType("datetime");

                entity.Property(e => e.Rf)
                    .HasMaxLength(25)
                    .HasColumnName("RF");

                entity.Property(e => e.UpdateDate).HasColumnType("datetime");
            });

            OnModelCreatingPartial(modelBuilder);
        }

        partial void OnModelCreatingPartial(ModelBuilder modelBuilder);
    }
}
