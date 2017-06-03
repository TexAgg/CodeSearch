using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using System.Web.Mvc.Ajax;

namespace CodeSearch.Controllers
{
	public class HomeController : Controller
	{
		public ActionResult Index()
		{
			var mvcName = typeof(Controller).Assembly.GetName ();
			var isMono = Type.GetType ("Mono.Runtime") != null;

			ViewData ["Version"] = mvcName.Version.Major + "." + mvcName.Version.Minor;
			ViewData ["Runtime"] = isMono ? "Mono" : ".NET";

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
			return View();
		}
	}
}

