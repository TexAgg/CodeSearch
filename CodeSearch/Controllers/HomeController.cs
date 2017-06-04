using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using System.Web.Mvc.Ajax;
using CodeSearch.Contexts;
using MySql.Data.MySqlClient;

namespace CodeSearch.Controllers
{
	public class HomeController : Controller
	{
		private AppContext _context = null;

		public HomeController()
		{
			_context = new AppContext();	
		}

		public ActionResult Index()
		{
			var mvcName = typeof(Controller).Assembly.GetName ();
			var isMono = Type.GetType ("Mono.Runtime") != null;

			ViewData["Version"] = mvcName.Version.Major + "." + mvcName.Version.Minor;
			ViewData["Runtime"] = isMono ? "Mono" : ".NET";

			return View();
		}

		[HttpGet]
		/// <summary>
		/// Search for the code.
		/// </summary>
		/// <param name="q">Q.</param>
		public ActionResult Search(string q)
		{
			// http://bit.ly/2qtWF2h
			ViewData["q"] = q;

			// Run stored procedure on query.
			// https://stackoverflow.com/a/14264829/5415895
			// https://stackoverflow.com/a/39063015/5415895
			//SqlParameter parameter1 = new SqlParameter ("@Parameter1", q);
			//MySqlParameter parameter1 = ;
			List<Models.Code> results = _context.Database.SqlQuery<Models.Code>("CALL codesearch(@q)", new MySqlParameter("@q", q)).ToList();

			return View(results);
		}
	}
}

