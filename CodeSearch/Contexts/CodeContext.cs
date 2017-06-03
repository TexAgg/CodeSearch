using System;
using System.Data.Entity;
using CodeSearch.Models;

namespace CodeSearch.Contexts
{
	public class CodeContext: DbContext
	{
		public DbSet<Code> Codes { get; set; }

		public CodeContext(): base("name=db")
		{
		}
	}
}
