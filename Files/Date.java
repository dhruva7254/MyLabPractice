package com.bank;
public class Date 
{
		private int day,month,year;
		public Date(int day, int month, int year) 
		{	 
			this.day = day;
			this.month = month;
			this.year = year;
		}
		public Date() 
		{
			this.day = 1;
			this.month = 2;
			this.year = 2000;
		}
		public String toString()
		{
			return "My Date :"+day+"/"+month+"/"+year;
		}	
}