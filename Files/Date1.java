package day3practice1;
public class Date1 
{
	private int day;
	private int month;
	private int year;
	public void showDate()
	{
		System.out.println("Date: "+day+"/"+month+"/"+year);
	}
	public void assignDate(int d, int m, int y)
	{
		day=d;
		month=m;
		year=y;
	}
}
