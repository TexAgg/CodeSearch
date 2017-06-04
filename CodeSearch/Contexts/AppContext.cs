using System;
using System.Data.Entity;
using CodeSearch.Models;

namespace CodeSearch.Contexts
{
	public class AppContext: DbContext
	{
		public DbSet<Code> Codes { get; set; }

		public AppContext(): base("name=db")
		{
		}
	}
}
