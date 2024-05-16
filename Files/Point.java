package day3practice1;
public class Point 
{
	private int x;
	private int y;
	public Point()
	{
		x=2;
		y=5;
	}
	public Point(int a, int b)
	{
		x=a;
		y=b;
	}
	public void assignPoint(int c, int d)
	{
		x=c;
		y=d;
	}
	public void showPoint()
	{
		System.out.println("X = "+x+" Y = "+y);	
	}
}