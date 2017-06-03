﻿using System;
using System.ComponentModel.DataAnnotations.Schema;

namespace CodeSearch.Models
{
	[Table("codes")]
	public class Code
	{
		[Column("id")]
		public int id { get; set; }

		[Column("url")]
		public string url { get; set; }

		[Column("content")]
		public string content { get; set; }

		[Column("payload_digest")]
		public string payloadDigest { get; set; }

		[Column("last_updated")]
		public string lastUpdated { get; set; }
	}
}